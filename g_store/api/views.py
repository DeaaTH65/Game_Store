from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer, UserSerializer, PurchaseSerializer
from inventory.models import Product, Purchase
from base.models import CustomUser



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


@api_view(['GET'])
def getProducts(request):
    rooms = Product.objects.all()
    serializer = ProductSerializer(rooms, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    room = Product.objects.get(id=pk)
    serializer = ProductSerializer(room, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getUsers(request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getUser(request, pk):
    user = CustomUser.objects.get(id=pk)
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getPurchases(request):
    purchases = Purchase.objects.all()
    serializer = PurchaseSerializer(purchases, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPurchase(request, pk):
    purchase = Purchase.objects.get(id=pk)
    serializer = PurchaseSerializer(purchase, many=False)
    return Response(serializer.data)