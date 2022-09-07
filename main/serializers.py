from rest_framework import serializers
from main.models import Main, Simple


class SimpleSerializers(serializers.ModelSerializer):

    class Meta:
        model = Simple
        fields = '__all__'


class MainSerializers(serializers.ModelSerializer):

    class Meta:
        model = Main
        fields = '__all__'
