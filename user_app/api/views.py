from rest_framework.decorators import api_view, permission_classes
from user_app.api.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    request.auth.delete()
    return Response(
        {"detail": "Logged out successfully"},
        status=status.HTTP_200_OK
    )
@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    serializer = RegistrationSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    account = serializer.save()

    token, _ = Token.objects.get_or_create(user=account)

    return Response({
        "message": "Registration successful",
        "username": account.username,
        "email": account.email,
        "token": token.key
    }, status=status.HTTP_201_CREATED)
    
    
