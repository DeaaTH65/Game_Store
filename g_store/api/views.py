from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/products',
        'GET /api/products/:id',
        'GET /api/users',
        'GET /api/users/:id',
        'GET /api/profiles',
        'GET /api/profiles/:id',
        'GET /api/purchases',
        'GET /api/purchases/:id',
    ]
    return Response(routes)