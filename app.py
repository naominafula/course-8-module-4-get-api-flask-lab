from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 899.99, "category": "electronics"},
    {"id": 2, "name": "Book", "price": 14.99, "category": "books"},
    {"id": 3, "name": "Desk", "price": 199.99, "category": "furniture"},
]
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Products API!"})

@app.route('/products', methods=['GET'])
def get_products():
    category_filter = request.args.get('category')

    if category_filter:
        filtered_products = [p for p in products if p['category'].lower() == category_filter.lower()]
        return jsonify(filtered_products)
    
    return jsonify(products)
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((p for p in products if p['id'] == id), None)
    
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)