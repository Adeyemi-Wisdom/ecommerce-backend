from ecommerce.api.serializer import CategorySerializer, CartItemSerializer, ProductSerializer 
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ecommerce.api import service 
from rest_framework import generics
from ecommerce.models import Product, CartItem, Category
from rest_framework import permissions
from ecommerce.api import permission


class CategoryCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permission.IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['Name']
    
class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permission.IsAdminOrReadOnly]
    

class ProductCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permission.IsAdminOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['Name', 'Category__Name']
    
class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permission.IsAdminOrReadOnly]
    

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart = service.get_or_create_cart(request.user)

        data = request.data
        if isinstance(data, dict):
            data = [data]

        for item_data in data:
            serializer = CartItemSerializer(data=item_data)
            serializer.is_valid(raise_exception=True)

            product = serializer.validated_data['product']
            quantity = serializer.validated_data['quantity']

            # 🔴 STOCK CHECK
            if product.quantity < quantity:
                return Response(
                    {"error": f"Only {product.quantity} items available"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                product=product,
                defaults={'quantity': quantity}
            )

            if not created:
                new_quantity = cart_item.quantity + quantity

                # 🔴 CHECK AGAIN when increasing quantity
                if product.quantity < new_quantity:
                    return Response(
                        {"error": f"Only {product.quantity} items available"},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                cart_item.quantity = new_quantity
                cart_item.save()

        return Response(
            {"message": "Products added to cart"},
            status=status.HTTP_200_OK
        )


    
class RemoveCartView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        cart = service.get_or_create_cart(request.user)
        product_id = request.data.get('product')
        
        try:
            item = CartItem.objects.get(cart=cart, product_id = product_id)
            item.delete()
            return Response({"Message": "Product removed from cart"}, status=200)
        except CartItem.DoesNotExist:
            return Response({"error": "Item not in cart"}, status=404)
        
class ReduceCartItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        cart = service.get_or_create_cart(request.user)
        product_id = request.data.get('product')
        quantity_to_reduce = request.data.get('quantity')

        try:
            cart_item = CartItem.objects.get(
                cart=cart,
                product_id=product_id
            )
        except CartItem.DoesNotExist:
            return Response(
                {"error": "Product not in cart"},
                status=404
            )

        if quantity_to_reduce >= cart_item.quantity:
            cart_item.delete()
        else:
            cart_item.quantity -= quantity_to_reduce
            cart_item.save()

        return Response(
            {"message": "Cart updated successfully"},
            status=200
        )

        
            
        
        
        
    

    
    

    
    