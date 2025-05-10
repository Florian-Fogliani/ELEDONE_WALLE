import random
from .models import Robot, Rubbish

def generate_random_robots(nbRobots, base):
    used_positions = set()
    used_positions.add((base['posX'], base['posY']))

    for _ in range(nbRobots):

        while True:
            posX = random.randint(0, 31)
            posY = random.randint(0, 31)
            if (posX, posY) not in used_positions:
                break

        used_positions.add((posX, posY))

        new_robot = Robot.objects.create(posX=posX, posY=posY)
        new_robot.save()


def generate_random_rubbish(nbRubbishs, base):
    used_positions = set()
    used_positions.add((base['posX'], base['posY']))
    for _ in range(nbRubbishs):

        while True:
            posX = random.randint(0, 31)
            posY = random.randint(0, 31)
            if (posX, posY) not in used_positions:
                break

        used_positions.add((posX, posY))

        new_rubbish = Rubbish.objects.create(posX=posX, posY=posY)
        new_rubbish.save()