from rest_framework import viewsets, routers, serializers
from rest_framework.decorators import detail_route
from rest_framework.response import Response

...
class EntryViewSet(viewsets.ModelViewSet):
    model = Entry
    serializer_class=EntrySerializer

hours_router = routers.DefaultRouter()
hours_router.register('entry', EntryViewSet)
