# import logging

from flask import request, jsonify

from robot import application as app

# logger = logging.getLogger(__name__)

# @app.route('/child', methods=['POST'])
# def update_child():
#     user_id = 'child'
#     data = request.get_json()
#     db.get(user_id)
#     db.update(user_id, data)
#     return jsonify(data)

# @app.route('/child', methods=['GET'])
# def get_child():
#     user_id = 'child'
#     data = db.get(user_id)
#     return jsonify(data)

# @app.route('/parent', methods=['POST'])
# def update_p():
#     user_id = 'parent'
#     data = request.get_json()
#     db.get(user_id)
#     db.update(user_id, data)
#     return jsonify(data)

# @app.route('/parent', methods=['GET'])
# def get_p():
#     user_id = 'parent'
#     data = db.get(user_id)
#     return jsonify(data)