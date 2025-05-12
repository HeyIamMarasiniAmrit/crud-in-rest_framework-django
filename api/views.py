from rest_framework.decorators import  api_view
from rest_framework.response import Response
from rest_framework import status
from .models import user
from .serializer import userSerializer


@api_view(['GET'])
def get_users(request):
    users = user.objects.all()
    serializer = userSerializer(users, many = True)
    return Response(userSerializer({'name':"pedro","age":30}).data)

@api_view(['POST'])
def create_user(request):
   serializer = userSerializer(data=request.data)
   if serializer.is_valid():
       serializer.save()
       return Response(serializer.data,status=status.HTTP_201_CREATED)
   else:
       Response(serializer.errors,status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request,pk):
    try:
        user = user.objects.get(pk=pk)
    except user.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = userSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = userSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user.data()
        return Response(status=status.HTTP_204_NO_CONTENT)