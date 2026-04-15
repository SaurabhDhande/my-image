from django.http import JsonResponse, FileResponse, HttpResponse
import os

def home(request):
    html = (
        '<h1>Service 2</h1>'
        '<p>Use <a href="/health/">/health/</a> or <a href="/image/">/image/</a>.</p>'
    )
    return HttpResponse(html)

def health_check(request):
    return JsonResponse({'status': 'healthy'})

def image_view(request):
    image_path = os.path.join(os.path.dirname(__file__), 'me.jpg')
    if os.path.exists(image_path):
        return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')
    else:
        return JsonResponse({'error': 'Image not found'}, status=404)