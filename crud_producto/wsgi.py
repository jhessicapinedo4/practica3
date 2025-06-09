import sys
import os

# Añadir la ruta de tu proyecto
path = '/home/pierocruzado/crud_producto'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud_producto.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
