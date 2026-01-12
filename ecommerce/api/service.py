from ecommerce.models import Cart, CartItem, Product
from django.shortcuts import get_object_or_404

def get_or_create_cart(user):
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart

def add_to_cart(cart, product, quantity):
    # 🔴 STOCK CHECK
    if product.quantity < quantity:
        raise ValueError("Not enough stock available")

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}
    )

    if not created:
        new_quantity = cart_item.quantity + quantity

        # 🔴 CHECK AGAIN when increasing
        if product.quantity < new_quantity:
            raise ValueError("Not enough stock available")

        cart_item.quantity = new_quantity
        cart_item.save()

    return cart_item

