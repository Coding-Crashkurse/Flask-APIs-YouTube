from flask import Flask, request
from flask_restx import Resource, Api
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

from app.models import setup_db, Items

app = Flask(__name__)
app.secret_key = "test"
setup_db(app, database_path="postgresql://markustest:test@localhost:5432/test")
CORS(app)

api = Api(app, version="1.0", title="Portfolio RestAPI", description="A simple portfolio API")

db = SQLAlchemy(app)


@api.route("/items")
class Test(Resource):
    def get(self):
        return {"items": store}, 200

@api.route("/additem")
class AddItem(Resource):
    def post(self):
        item = request.get_json()["item"]
        price = request.get_json()["price"]
        exist = Items.query.filter_by(item=item).one_or_none()
        if exist:
            return {"message": "Item already exists"}, 403
        try:
            new_item = Items(item=item, price=price)
            new_item.insert()
        except:
            db.session.rollback()
            return {"message": "An error occured"}, 404
        finally:
            db.session.close()
        return {"message": "Item created"}, 201


@api.route("/deleteitem")
class DeleteItem(Resource):
    def delete(self):
        item = request.get_json()["item"]
        item = Items.query.filter_by(item=item).one_or_none()
        if item is None:
            return {"message": "item not found"}, 404
        try:
            item.delete()
        except:
            db.session.rollback()
        finally:
            db.session.close()
        return {"message": "item deleted"}, 200


@api.route("/updateitem")
class ChangeItem(Resource):
    def put(self):
        item = request.get_json()["item"]
        price = request.get_json()["price"]
        items = [x.get("item") for x in store]
        if item in items:
            index = items.index(item)
            store[index] = {
                "item": item,
                "price": price
            }
            return {"message": "item updated"}, 200
        return {"message": "item not found"}, 404