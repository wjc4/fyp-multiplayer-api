from flask import request, jsonify

from multiplayer import application as app

@app.route('/join', methods=['POST','PUT'])
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
    return jsonify({'status':'ok'})

@app.route('/update_lobby', methods=['POST','PUT'])
def update_lobby():
    """
    data should be in this format
    {
        "id": int or "name": int,
        "status": bool
    }
    """
    """
    data returned in this format
    {
        "players": arr of {"name":str,"status":bool}
        "start": bool ##trigger game start
    }
    """

    data = request.get_json()
    # print(data)
    return jsonify({'status':'ok'})

@app.route('/update', methods=['POST','PUT'])
def command():
    """
    data should be in this format
    {
        "id": int,
        "name": int,
        "checkpoint":int,
        "section":int,
        "complete":bool
    }
    """
    """
    data returned in this format
    {
        "id": int,
        "name": int,
        "checkpoint":int,
        "section":int,
        "rank":int,
        "num_players": int
        "buffs": arr of {"id":int,"buff":str}
    }
    """

    data = request.get_json()
    # print(data)
    return jsonify({'status':'ok'})

@app.route('/complete', methods=['POST','PUT'])
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
    return jsonify({'status':'ok'})