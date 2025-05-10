from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game, Robot, Rubbish
from .serializers import StartSerializer, RobotSerializer, RubbishSerializer, GameSerializer
from .utils import generate_random_robots, generate_random_rubbish

def GenericResponse(status, message, data=None):
    response = {
        'message': message,
        'data': data,
    }
    return Response(response, status=status)

def MapResponse(message):
    data = {
            'robots': RobotSerializer(Robot.objects.all(), many=True).data,
            'rubbishs': RubbishSerializer(Rubbish.objects.all(), many=True).data,
            'game': GameSerializer(Game.objects.all()[0]).data,
    }
    return GenericResponse(200, message, data)


class StartView(APIView):
    def post(self, request):
        serializer = StartSerializer(data=request.data)
        if serializer.is_valid():
            if len(Game.objects.all()) > 0:
                return GenericResponse(401, "Game already started")
            data = serializer.validated_data
            new_game = Game.objects.create(
                basePosX = data['base']['posX'],
                basePosY = data['base']['posY'],
                nbRobots = data['nbRobots'],
                nbRubbish = data['nbRubbish'],
            )
            generate_random_robots(data['nbRobots'], data['base'])
            generate_random_rubbish(data['nbRubbish'], data['base'])
            new_game.save()
            return MapResponse("Game started")
        else:
            return GenericResponse(400, serializer.errors)

class StopView(APIView):
    def delete(self, request):
        if (Game.objects.all().count() == 0):
            return GenericResponse(401, "Game not started")
        Game.objects.all().delete()
        Rubbish.objects.all().delete()
        Robot.objects.all().delete()
        return GenericResponse(200, "Game stopped")
