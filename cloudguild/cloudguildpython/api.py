from flask import Flask, jsonify, request
from flask_cors import CORS
from cloudguildpython.models.dynamodb import set_dynamodb_item, get_dynamodb_item
app = Flask(__name__)
CORS(app)


@app.route("/cloudguild/<id>/<user>", methods=["POST"])
def set_items(id, user):
    return set_dynamodb_item(id,user)

@app.route("/cloudguild/<id>", methods=["GET"])
def list_items(id):
    return get_dynamodb_item(id)



if __name__=='__main__':
    set_items('hans','maulwurf')