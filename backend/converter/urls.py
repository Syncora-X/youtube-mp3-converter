from django.urls import path
from .views import DownloadAudioView

urlpatterns = [
    path('download/', DownloadAudioView.as_view(), name='download'),
]
