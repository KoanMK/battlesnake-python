import bottle
import os
import random

def food_dist(snake, food):
    dist_x = abs(snake[0] - food[0])
    dist_y = abs(snake[1] - food[1])
    return dist_x + dist_y;

def closest_food(head, food):
    min_dist = 2000
    min_food = None
    for eats in food:
        dist = food_dist(head, eats)
        if dist < min_dist:
            min_dist = dist
            min_food = eats
    return min_food;

def food_direction(head, food):
    x = head[0] - food[0]
    y = head[1] - food[1]
    move = None
    if x < 0:
        move = 'right'
    elif x > 0:
        move = 'left'
    if y < 0:
    	move = 'down'
    elif y > 0:
    	move = 'up'
    return move;

def snek_head(data, id):
    my_snake = None
    for snek in data['snakes']:
        if snek['id'] == id:
            my_snake = snek['coords'][0]
    return my_snake;

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#FF0000',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'Cobro'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    head = snek_head(data, data['you'])
    fud = closest_food(head, data['food'])


    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']

    return {
        'move': food_direction(head, fud),
        #'move': random.choice(directions),
        'taunt': 'Boop the snoot'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))