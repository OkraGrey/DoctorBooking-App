from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import DoctorSignupSerializer
from .models import Doctor

@action(detail=True,methods=['post'])
class DoctorSignupView(ModelViewSet):
    serializer_class = DoctorSignupSerializer
    queryset=Doctor.objects.all()
    def create(self,request,*args, **kwargs):
        print(args,kwargs)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            doctor=serializer.save()
            return Response({'message':'Doctor SignUp Successfully'})
        return Response(serializer.errors,status=400)
    
    