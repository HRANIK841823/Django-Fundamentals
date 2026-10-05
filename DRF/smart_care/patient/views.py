from django.shortcuts import render,redirect
from .serializers import PatientSerializer,RegistrationSerializer,UserLoginSerializer
from .models import Patient
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.http import HttpResponse
#userlogin,logout
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,AllowAny
from .models import Patient

#For Sending Email
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
# Create your views here.
class PatientViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=Patient.objects.all()
    serializer_class=PatientSerializer

class UserRegistration(APIView):
    serializer_class=RegistrationSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        # if serializer.is_valid():
        #    user = serializer.save()
        #    return Response("User Registration SuccessFull Done !!!")
        # else:
        #     print("Validation errors:", serializer.errors)  # Debug output in console
        #     return Response(serializer.errors, status=400)

        
        if serializer.is_valid():
            user=serializer.save()
            token=default_token_generator.make_token(user)
            print("token",token)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            print("uid",uid)
            confirm_link=f"http://127.0.0.1:8000/user/active/{uid}/{token}"
            email_subject="Confirm Your Email"
            email_body=render_to_string('confirm_email.html',{'confirm_link':confirm_link})
            email=EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
            return Response("User Registration SuccessFull Done !!!")
        return Response(serializer.errors)

from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator

def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        print("Decoded UID:", uid)
        user = User._default_manager.get(pk=uid)
        print("User found:", user)
    except (User.DoesNotExist, ValueError, TypeError, OverflowError) as e:
        print("Exception while decoding UID or fetching user:", e)
        user = None

    if user is not None:
        is_valid_token = default_token_generator.check_token(user, token)
        print("Is token valid?", is_valid_token)

        if is_valid_token:
            user.is_active = True
            user.save()
            print("User activated")
            return redirect('http://localhost:3000/login.html?activated=1')
        else:
            print("Invalid token")
    else:
        print("User is None")

    return redirect('http://localhost:3000/login.html?activated=1')


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from .serializers import UserLoginSerializer
from .models import Patient

class UserLoginApiView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data = self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username= username, password=password)
            
            if user:
                token, _ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                print(user.id)
                return Response({'token' : token.key, 'user_id' : user.id})
            else:
                return Response({'error': "Invalid Credential"}, status=400)
        return Response(serializer.errors, status=400)



class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Delete user's token (for token auth)
        if hasattr(request.user, 'auth_token'):
            request.user.auth_token.delete()

        # Clear session
        logout(request)

        return Response({'message': 'Logout successful'}, status=200)
            
class CheckLoginStatusAPIView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            print(f"🔒 Authenticated as: {request.user.username}")
            return Response({'logged_in': True, 'username': request.user.username})
        else:
            print("🔓 Not authenticated")
            return Response({'logged_in': False})
