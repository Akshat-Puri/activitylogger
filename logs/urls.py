from django.urls import path
from .views import ActivityLogCreateView, UserActivityLogListView, UpdateLogStatusView

urlpatterns = [
    path('activity-log/', ActivityLogCreateView.as_view(), name='create-log'),
    path('activity-log/user/<int:user_id>/', UserActivityLogListView.as_view(), name='user-logs'),
    path('activity-log/<int:pk>/status/', UpdateLogStatusView.as_view(), name='update-status'),
]
