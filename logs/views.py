from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import UserActivityLog
from .serializers import UserActivityLogSerializer
from datetime import timedelta

class ActivityLogCreateView(generics.CreateAPIView):
    queryset = UserActivityLog.objects.all()
    serializer_class = UserActivityLogSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save(user=self.request.user)
        cache.delete(f"user_logs_{self.request.user.id}")  # Invalidate cache


class UserActivityLogListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        cache_key = f"user_logs_{user_id}_{request.GET.get('action', '')}_{request.GET.get('start', '')}_{request.GET.get('end', '')}"
        data = cache.get(cache_key)

        if not data:
            logs = UserActivityLog.objects.filter(user__id=user_id)
            if 'action' in request.GET:
                logs = logs.filter(action=request.GET['action'])
            if 'start' in request.GET and 'end' in request.GET:
                logs = logs.filter(timestamp__range=[request.GET['start'], request.GET['end']])
            serializer = UserActivityLogSerializer(logs, many=True)
            data = serializer.data
            cache.set(cache_key, data, timeout=60)  # cache for 1 min

        return Response(data)


class UpdateLogStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, pk):
        try:
            log = UserActivityLog.objects.get(pk=pk, user=request.user)
        except UserActivityLog.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        status_value = request.data.get("status")
        if status_value not in dict(UserActivityLog.STATUS_CHOICES):
            return Response({"error": "Invalid status"}, status=status.HTTP_400_BAD_REQUEST)

        log.status = status_value
        log.save()
        return Response(UserActivityLogSerializer(log).data)
