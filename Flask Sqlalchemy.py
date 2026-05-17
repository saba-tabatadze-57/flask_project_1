from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }

    def response(success, data=None, message=""):
        return jsonify({
            "success": success,
            "data": data,
            "message": message
        })

    @app.route("/products", methods=["POST"])
    def create_product():
        data = request.json

        product = Product(
            name=data["name"],
            price=data["price"]
        )

        db.session.add(product)
        db.session.commit()

        return response(True, product.to_dict(), "Product created")

    @app.route("/products", methods=["POST"])
    def create_product():
        data = request.json

        product = Product(
            name=data["name"],
            price=data["price"]
        )

        db.session.add(product)
        db.session.commit()

        return response(True, product.to_dict(), "Product created")

    @app.route("/products", methods=["GET"])
    def get_products():
        products = Product.query.all()
        return response(True, [p.to_dict() for p in products], "All products")

    @app.route("/products/<int:id>", methods=["GET"])
    def get_product(id):
        product = Product.query.get(id)

        if not product:
            return response(False, None, "Not found"), 404

        return response(True, product.to_dict(), "Product found")

    @app.route("/products/<int:id>", methods=["PUT"])
    def update_product(id):

        product = Product.query.get(id)

        if not product:
            return response(False, None, "Not found"), 404

        data = request.json

        product.name = data["name"]
        product.price = data["price"]

        db.session.commit()

        return response(True, product.to_dict(), "Updated")

    @app.route("/products/<int:id>", methods=["DELETE"])
    def delete_product(id):

        product = Product.query.get(id)

        if not product:
            return response(False, None, "Not found"), 404

        db.session.delete(product)
        db.session.commit()

        return response(True, None, "Deleted")

    if __name__ == "__main__":
        with app.app_context():
            db.create_all()

        app.run(debug=True)