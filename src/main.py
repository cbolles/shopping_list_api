from flask import Flask, request
import json
import database.interface as db
import wegmans.wegmans_interface as weggies

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/add_item")
def add_item():
    item_keyword = request.args.get('item_keyword')
    db.save_item(weggies.get_by_keyword(item_keyword))
    return 'success'


@app.route("/get_list")
def get_list():
    return json.dumps(db.get_list())


if __name__ == '__main__':
    app.run()
