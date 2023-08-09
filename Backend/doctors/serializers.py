from rest_framework import serializers
from .models import Doctor,Speciality,TimeSlot
from accounts.models import CustomUser
from accounts.serializers import UserRegistrationSerializer


class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = ['email','password']

class SpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Speciality
        fields = 'specialty_description'

class DoctorSignupSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    # email = serializers.Email
    user = UserSerializer()
    
    class Meta:
        model = Doctor
        fields = ['user', 'is_surgeon', 'is_available_online', 'cnic', 'consultation_fee', 'about', 'speciality']


    def create(self,validated_data):
        # print(f'Validated Data inside doctor serializer{validated_data}')
        email = validated_data['user'].pop('email')
        password = validated_data['user'].pop('password')
        
        #When recieves users data, afterpopping email and password, empty user dict is pass
        #which causes error while passing datat to doctor. Hence empty user dict is popped
        validated_data.pop('user')
        # print(validated_data)

        # Creating a user instance
        user=CustomUser.objects.create_user(email=email,password=password)
        # print(user)
    
        #Creating Doctor instance
        doctor= Doctor.objects.create(user=user,**validated_data)

        return doctor


    