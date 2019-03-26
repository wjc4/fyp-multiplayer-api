from flask import request, jsonify

from multiplayer import application as app

from distutils.util import strtobool
import copy

other_data = {'game_started': False,'complete_count':0,'order':[]}
# 'id':'name'
players = {}
progress = {}


@app.route('/join', methods=['POST', 'PUT'])
def join_game():
    """
    data should be in this format
    {
        "id": int, #unique hash on client # or can consider to use request.remote_addr
        "name": int
    }
    """
    """
    data returned in this format
    {
        "id": int,
        "name": int
    }
    """

    data = request.get_json()
    # print(data)

    if 'id' not in data or 'name' not in data:
        return jsonify({'status': 'invalid request'})

    if data['id'] in players:
        return jsonify({'status': 'player already registered'})

    players[data['id']] = {
        'name': data['name'],
        'ready': False
    }

    return jsonify(data)


@app.route('/update_lobby', methods=['POST', 'PUT'])
def update_lobby():
    """
    data should be in this format
    {
        "id": int or "name": int,
        "ready": bool
    }
    """
    """
    data returned in this format
    {
        "players": arr of {"name":str,"ready":bool}
        "start": bool ##trigger game start
    }
    """

    data = request.get_json()
    # print(data)

    if 'id' not in data or 'ready' not in data:
        return jsonify({'status': 'invalid request'})

    if data['id'] not in players:
        return jsonify({'status': 'not registered'})

    # players[data['id']]['ready'] = True if strtobool(data['ready']) else False
    players[data['id']]['ready'] = data['ready']

    output = {
        "players": [],
        "start": True
    }
    for key in players:
        output["players"].append(players[key])
        if not players[key]['ready']:
            output["start"] = False
    if len(players) == 1:
        output["start"] = False

    if output["start"]:
        start_game()
    
    # print(data)
    # print(output)
    return jsonify(output)


def start_game():
    other_data['game_started'] = True
    count = 1
    num_players = len(players)
    for key in players:
        progress[key] = {
            "id": key,
            "checkpoint": 1,
            "lap": 1,
            "rank": count,
            "num_players": num_players,
            "buffs": []
        }
        other_data['order'].append(key)
        count += 1


@app.route('/update', methods=['POST', 'PUT'])
def command():
    """
    data should be in this format
    {
        "id": int,
        "checkpoint":int,
        "lap":int
    }
    """
    """
    data returned in this format
    {
        "id": int,
        "checkpoint":int,
        "lap":int,
        "rank":int,
        "num_players": int
        "buffs": arr of {"id":int,"buff":str}
    }
    """

    data = request.get_json()
    required_keys = ("id", "checkpoint", "lap")
    if not all(k in data for k in required_keys):
        return jsonify({'status': 'invalid request'})
    
    if data["checkpoint"] != progress[data['id']]["checkpoint"]:
        progress[data['id']]["checkpoint"] = data["checkpoint"]
        progress[data['id']]["lap"] = data["lap"]
        update_rank()



    # print(data)
    return jsonify(progress[data['id']])

def update_rank():
    players_arr = []
    for player_id in progress:
        players_arr.append(progress[player_id])

    def cust_sort(x):
        return x['lap']*3+x['checkpoint']-other_data['order'].index(x['id'])/(len(other_data['order']))

    players_arr.sort(key=cust_sort, reverse=True)

    rank = 1
    for player_data in players_arr:
        progress[player_data['id']]['rank'] = rank
        rank += 1
        

@app.route('/complete', methods=['POST', 'PUT'])
def complete():
    """
    data should be in this format
    {
        "id": int or "name": int,
    }
    """
    """
    data returned in this format
    {
        "rank":int,
        "num_players": int
    }
    """

    data = request.get_json()
    # print(data)
    if data['id'] in progress:
        other_data['complete_count'] += 1
    else:
        return jsonify({'status': 'not in game'})
    return jsonify({'rank': other_data['complete_count']})
