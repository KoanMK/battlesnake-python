import bottle
import os
import random


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
        'name': 'battlesnake-python'
    }

<<<<<<< HEAD
# only change should be this comment
=======

>>>>>>> 00fd34bf52c449112f32569c5a63a10037d50019
	
@bottle.post('/move')
def move():
    data = bottle.request.json

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']
	if 
    return {
        #'move': random.choice(directions),
<<<<<<< HEAD
        'move': 'left',
        'taunt': 'battlesnake-python!'
    }	
=======
        'move': 
		head = data[coords[0]]
	if head[0]==data['width'-1]
		return 'down'
	if head[1]==data['hieght'-1]
		return 'left'
	if head[0]==0
		return 'up'
	if head[1]==0
		return 'right',
        'taunt': 'Boop the snoot'
    }
>>>>>>> 00fd34bf52c449112f32569c5a63a10037d50019


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
