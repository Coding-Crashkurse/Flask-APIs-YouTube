from flask import Flask, request
from flask_restx import Resource, Api

store = [{
    "item": "laptop",
    "price": 799.99
}]

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

api = Api(app, version="0.0.1", title="Basic API", description="Simple Testapp")

@api.route("/items")
class Test(Resource):
    def get(self):
        return {"items": store}, 200

@api.route("/additem")
class AddItem(Resource):
    def post(self):
        item = request.get_json()["item"]
        price = request.get_json()["price"]
        new_item = {
            "item": item,
            "price": price
        }
        items = [x.get("item") for x in store]
        if item not in items:
            store.append(new_item)
            return {"message": "item created"}, 201
        return {"message": "item already created"}, 403


@api.route("/deleteitem")
class DeleteItem(Resource):
    def delete(self):
        item = request.get_json()["item"]
        items = [x.get("item") for x in store]
        if item in items:
            index = items.index(item)
            store.pop(index)
            return {"message": "item deleted"}, 200
        return {"message": "item not found"}, 404


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


if __name__ == "__main__":
    app.run()