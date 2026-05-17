from flask import Flask, render_template, jsonify

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 1200},
    {"id": 2, "name": "Phone", "price": 800},
    {"id": 3, "name": "Tablet", "price": 600},
]


@app.route("/")
def index():
    return render_template("index.html", products=products)


@app.route("/api/products")
def get_products():
    return jsonify(products)


if __name__ == "__main__":
    app.run(debug=True)