from rest_framework import serializers
from userAccounts.models import User
from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from .validators import PhoneNumberValidator
from twilio.rest import Client
import random




class UserSerializer(CountryFieldMixin,serializers.ModelSerializer):
    mobileNumber = serializers.CharField(validators = [PhoneNumberValidator(queryset=User.objects.all())] , required = True)
    country = CountryField(country_dict=True)
    success = serializers.CharField(max_length= 10 , required=False)
    message = serializers.CharField(max_length= 30 ,required = False)
    otp = serializers.CharField(max_length = 10,write_only=True,allow_blank=True)
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name','mobileNumber','country','avatar','description','otp','success','message')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type': 'password'},
            },
        }

    def create(self,validated_data):
        request = self.context.get('request')
        list_of_keys = validated_data.keys()
        try:
            otp = validated_data['otp']
        except Exception as e:
            otp = ''
        if otp=='':
            auth_token = '1729bdc3c04616dbc8ca2a1fde8b5a46'
            account_sid = 'ACf5adb3a8c7f5bfbffb575a2837e707f4'
            otp = random.randint(100000,999999)
            request.session['otp']=otp
            twilio_number = "+16304746450"
            to_number = str(validated_data['mobileNumber'])
            body = "Welcome To Chhattisgarh Tourism App. Your verification code is :" + str(otp)
            client = Client(account_sid , auth_token)
            message = client.api.messages.create(to_number,from_=twilio_number,body = body)
            if message.sid: 
                validated_data['success']=True
                validated_data['message']='OTP sent successfully'
            else:
                validated_data['success']=False
                validated_data['message']='OTP delivery failed'
            return validated_data
        else:
            if int(otp) == request.session['otp']:
                user = User(
                        username = validated_data.pop('username'),
                        mobileNumber = validated_data.pop('mobileNumber'), 
                    )
                user.set_password(validated_data.pop('password'))
                if ('email' in list_of_keys):
                    user.email = validated_data.pop('email')
                if ('first_name' in list_of_keys):
                    user.first_name = validated_data.pop('first_name')
                if ('last_name' in list_of_keys):
                    user.last_name = validated_data.pop('last_name')
                if ('avatar' in list_of_keys):
                    user.avatar = validated_data.pop('avatar')
                if ('country' in list_of_keys):
                    user.country = validated_data.pop('country')
                if('description' in list_of_keys):
                    user.descripton = validated_data.pop('description')
                user.save()
                return user
            else:
                validated_data['success']=False
                validated_data['message']='OTP verification failed'
                return validated_data
