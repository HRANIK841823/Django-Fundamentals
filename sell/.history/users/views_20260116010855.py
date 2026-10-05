from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
class UserRegistrationApiView(APIView):
    serializer_class=RegisterSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_vaild():
            user=serializer.save()
            return Response({"message":"From Submission Done"})
        return Response(serializer.erros)