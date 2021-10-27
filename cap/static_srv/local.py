import os

from cap.settings.base import BASE_DIR


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'my_static'),
]

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'cdn_local', 'static')
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'cdn_local', 'media')
print(f"STATIC ROOT PATH -> {STATIC_ROOT}")