from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Defino los endpoints de la API escribiendo @api_view
@api_view(['POST'])
def login(request):
    # Buscar el usuario a traves de su nombre de usuario y comprobar si existe
    # Si el usuario no existe retorna un error 404
    user = get_object_or_404(User, username=request.data['username'])
    # Comprobar si la contraseña escrita es correcta
    if not user.check_password(request.data['password']):
        # Si la contraseña no es correcta retorna un error 404
        return Response({"detail": "clave incorrecta"}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
def signup(request):
    # Inicializar una instancia del serializer basado en la data
    # que viene en nuestro request.data (api)
    serializer = UserSerializer(data=request.data)
    # Para que el serializer sea valido debe haber un: username, password y email
    if serializer.is_valid():
        # Guardar el nuevo usuario en nuestra base de datos
        serializer.save()
        # Buscar el usuario a traves de su nombre de usuario
        user = User.objects.get(username=request.data['username'])
        # Tomamos la contraseña del usuario y la convertimos en una 
        # cadena de caracteres alfanumerica
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
