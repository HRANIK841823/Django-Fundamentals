from rest_framework import serializers
from django.contrib.auth.models import User
class RegisterSerializer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','confirm_password']

        def save(self):
            username=self.vali