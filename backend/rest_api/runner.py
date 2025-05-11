import threading
import time
import random
from . import variables
from .models import Game, Robot, Rubbish


def distance(pos1_x, pos1_y, pos2_x, pos2_y):
    return abs(pos1_x - pos2_x) + abs(pos1_y - pos2_y)

def find_near_rubbish(robot):
    rubbishes = Rubbish.objects.all()
    if not rubbishes:
        return None
    
    near_rubbish = None
    distance_min = float('inf')
    
    for rubbish in rubbishes:
        dist = distance(robot.posX, robot.posY, rubbish.posX, rubbish.posY)
        if dist <= 5 and dist < distance_min:
            distance_min = dist
            near_rubbish = rubbish
            
    return near_rubbish

def calcul_movement(robot, dest_x, dest_y):
    if robot.posX < dest_x:
        return 'droite'
    elif robot.posX > dest_x:
        return 'gauche'
    elif robot.posY < dest_y:
        return 'bas'
    elif robot.posY > dest_y:
        return 'haut'
    return None

def random_move(robot):
    possible_move = []
    
    if robot.posX < 31:
        possible_move.append('droite')
    if robot.posX > 0:
        possible_move.append('gauche')
    if robot.posY < 31:
        possible_move.append('bas')
    if robot.posY > 0:
        possible_move.append('haut')
    
    if not possible_move:
        return None
    
    return random.choice(possible_move)


def play(robot, game):
    if robot.isCarrying:
        if robot.posX == game.basePosX and robot.posY == game.basePosY:
            robot.isCarrying = False
            game.nbHarvestRubbish += 1
            game.save()
            robot.save()
            return
        
        movement = calcul_movement(robot, game.basePosX, game.basePosY)
    else:
        rubbish = find_near_rubbish(robot)
        
        if not rubbish:
            if Rubbish.objects.count() == 0:
                return
            movement = random_move(robot)
        else:
            if robot.posX == rubbish.posX and robot.posY == rubbish.posY:
                robot.isCarrying = True
                robot.save()
                rubbish.delete()
                return
            
            movement = calcul_movement(robot, rubbish.posX, rubbish.posY)
    
    if movement == 'droite':
        robot.posX = min(31, robot.posX + 1)
    elif movement == 'gauche':
        robot.posX = max(0, robot.posX - 1)
    elif movement == 'bas':
        robot.posY = min(31, robot.posY + 1)
    elif movement == 'haut':
        robot.posY = max(0, robot.posY - 1)
    
    robot.save()

def worker():
    while variables.is_running:
        time.sleep((variables.waiting_time - 500) / 1000)
        game = Game.objects.first()

        robots = Robot.objects.all()
        for robot in robots:
            play(robot, game)

        if game.nbRubbish == game.nbHarvestRubbish and not any(robot.isCarrying for robot in robots):
            variables.is_running = False

        game.nbTours += 1
        game.save()

def start():
    if not variables.is_running:
        variables.is_running = True
        thread = threading.Thread(target=worker, daemon=True)
        thread.start()

def stop():
    variables.is_running = False
