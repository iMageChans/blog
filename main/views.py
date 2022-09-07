from rest_framework.viewsets import mixins, GenericViewSet
from main.models import Main, Simple
from main.serializers import MainSerializers, SimpleSerializers


class MainViewSet(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  GenericViewSet
                  ):

    queryset = Main.objects.all().order_by('-id')
    serializer_class = MainSerializers


class SimpleViewSet(mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet
                    ):

    queryset = Simple.objects.all().order_by('-id')
    serializer_class = SimpleSerializers

