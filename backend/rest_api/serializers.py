from rest_framework import serializers
from .models import Robot, Rubbish, Game

#Models serializers
class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        exclude = ['id']


class RubbishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubbish
        exclude = ['id']


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        exclude = ['id']

#Request serializers
class PositionSerializer(serializers.Serializer):
    posX = serializers.IntegerField()
    posY = serializers.IntegerField()

    def validate(self, value):
        if value['posX'] < 0 or value['posY'] > 31 or value['posX'] > 31 or value['posY'] < 0 or value['posY'] < 0:
            raise serializers.ValidationError("Both posX and posY must be between 0 and 31")
        return value

class StartSerializer(serializers.Serializer):
    base = PositionSerializer()
    nbRobots = serializers.IntegerField()
    nbRubbish = serializers.IntegerField()

    def validate(self, value):
        if value['nbRobots'] < 1 or value['nbRubbish'] < 1 or value['nbRubbish'] > 1023 or value['nbRobots'] > 1023:
            raise serializers.ValidationError("Both robots and rubbish must be greater than 0 and less than map capacity (1023)")
        return value