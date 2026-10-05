from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer,UserLoginSerializer
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
class UserRegistrationApiView(APIView):
    serializer_class=RegisterSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            user=serializer.save()
            return Response({"message":"From Submission Done"})
        return Response(serializer.errors)

class UserLoginView(APIView):
    serializer_class=UserLoginSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            username=serializer.validated_data['username']
            password=serializer.validated_data["password"]

            user=authenticate(username,password)
            if user:
                token,_=Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request,user)
                return Response ({"token":token.key,'user_id':user.id})
            else:
                return Response({"error":"Invalid Credential"})
        return Response(serializer.errors)
    
class UserLogoutApiView(APIView):
    def get(self,request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')