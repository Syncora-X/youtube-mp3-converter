from rest_framework.views import APIView
from rest_framework.response import Response
from .tasks import download_audio_task
import os

class DownloadAudioView(APIView):
    def post(self, request):
        url = request.data.get('url')
        output_dir = os.path.join(os.getcwd(), 'downloads')
        os.makedirs(output_dir, exist_ok=True)

        # Trigger Celery background task
        result = download_audio_task.delay(url, output_dir)
        return Response({
            'status': 'Download started',
            'task_id': result.id,
            'url': url
        })
