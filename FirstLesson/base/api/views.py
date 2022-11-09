from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from . serializers import RoomSelializer



@api_view(['GET'])
def getRoutes(request):
    routes = [
        'Get /api',
        'Get /api/rooms',
        'Get /api/rooms/:id'
    ]
    return Response(routes)

@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSelializer(rooms, many=True)
    return Response(serializer.data)