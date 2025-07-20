from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample products
products = [
    {
        'id': 1,
        'name': 'Wireless Headphones',
        'price': 59.99,
        'description': 'High quality wireless headphones with noise cancellation.',
        'image': 'images/product1.jpg'
    },
    {
        'id': 2,
        'name': 'Smart Watch',
        'price': 129.99,
        'description': 'Smart watch with fitness tracking and notifications.',
        'image': 'images/product2.jpg'
    },
    {
        'id': 3,
        'name': 'Portable Speaker',
        'price': 39.99,
        'description': 'Compact portable speaker with great sound.',
        'image': 'images/product3.jpg'
    }
]

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product_detail(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return "Product not found", 404

    if request.method == 'POST':
        quantity = request.form.get('quantity', '1')
        # Redirect to cart with product id and quantity in query params
        return redirect(url_for('cart', product_id=product_id, quantity=quantity))

    return render_template('product.html', product=product)

@app.route('/cart')
def cart():
    product_id = request.args.get('product_id')
    quantity = request.args.get('quantity', '1')

    cart_item = None
    if product_id:
        try:
            pid = int(product_id)
            product = next((p for p in products if p['id'] == pid), None)
            if product:
                cart_item = {
                    'product': product,
                    'quantity': int(quantity)
                }
        except ValueError:
            pass

    return render_template('cart.html', cart_item=cart_item)

if __name__ == '__main__':
    app.run(debug=True)
