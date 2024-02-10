from rest_framework.serializers import ModelSerializer

from users.models import ShoppingCart


class ShoppingCartSerializer(ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = "__all__"
