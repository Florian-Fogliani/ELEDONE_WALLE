from django.db import models
from django.contrib.postgres.fields import ArrayField

class Robot(models.Model):
    posX = models.IntegerField()
    posY = models.IntegerField()
    isCarrying = models.BooleanField(default=False)

class Rubbish(models.Model):
    posX = models.IntegerField()
    posY = models.IntegerField()

class Game(models.Model):
    basePosX = models.IntegerField()
    basePosY = models.IntegerField()
    nbRobots = models.IntegerField()
    nbRubbish = models.IntegerField()
    nbHarvestRubbish = models.IntegerField(default=0)
    nbTours = models.IntegerField(default=0)

