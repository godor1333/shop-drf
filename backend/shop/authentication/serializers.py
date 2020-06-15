from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        # description = models.TextField(blank=True, null=True)
        # location = models.CharField(max_length=30, blank=True)
        # date_joined = models.DateTimeField(auto_now_add=True)
        # updated_on = models.DateTimeField(auto_now=True)
        # is_organizer = models.BooleanField(default=False)
        # Add custom claims
        token['description'] = user.description
        token['location'] = user.location
        #token['date_joined'] = user.date_joined
       # token['updated_on'] = user.updated_on
        token['is_organizer'] = user.is_organizer
        return token

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Currently unused in preference of the below.
    """
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField()
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance