from .models import *
from rest_framework import serializers


class UserSer(serializers.ModelSerializer):
    class Meta:
        model=Myuser
        fields='__all__'