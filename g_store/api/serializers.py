from rest_framework.serializers import ModelSerializer
from inventory.models import Product, Purchase
from base.models import CustomUser


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        
        
class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
        
        
class BuySerializer(ModelSerializer):
    class Meta:
        model = Purchase
        exclude = ['user', 'total_amount']