import os
from blog_project.settings import BASE_DIR

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"my_static")
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static_local_cdn","static")

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static_local_cdn','media')
MEDIA_URL = '/media/'

