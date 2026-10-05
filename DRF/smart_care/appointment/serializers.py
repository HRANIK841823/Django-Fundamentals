from .models import Appiontment
from rest_framework import serializers
class AppiontmentSerializer(serializers.ModelSerializer):
    time=serializers.StringRelatedField(many=False)
    patient=serializers.StringRelatedField(many=False)
    doctor=serializers.StringRelatedField(many=False)
    class Meta:
        model=Appiontment
        fields='__all__'