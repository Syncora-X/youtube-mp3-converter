from celery import shared_task
import yt_dlp
import os

@shared_task
def download_audio_task(url, output_dir):
    try:
        # Make sure output folder exists
        os.makedirs(output_dir, exist_ok=True)

        # Setup YT-DLP options
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,  # 👈 prevents full playlist downloads
            'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        # Download the file
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'Unknown Title')
            filename = ydl.prepare_filename(info).replace('.webm', '.mp3').replace('.m4a', '.mp3')

        print(f"[✅] Download complete: {filename}")
        return {'status': 'completed', 'title': title, 'file': filename}

    except Exception as e:
        print(f"[❌] Error: {e}")
        return {'status': 'failed', 'error': str(e)}
