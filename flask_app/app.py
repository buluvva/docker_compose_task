from flask import Flask, jsonify
from database_setup import create_table, execute


app = Flask(__name__)
create_table()


@app.route('/api/categories', methods=['GET'])
def categories():
    category = execute('SELECT DISTINCT category FROM Films')
    data = {}
    for row in category:
        category_name = row[0]
        if category_name != "":
            data.update({f'{category_name}': execute(f"SELECT product FROM Films WHERE category='{row[0]}'")})
    return jsonify({'categories': data})


@app.route('/api/products', methods=['GET'])
def products():
    product = execute('SELECT DISTINCT product FROM Films')
    data = {}
    for row in product:
        product_name = row[0]
        if product_name != "":
            data.update({f'{product_name}': execute(f"SELECT category FROM Films WHERE product='{row[0]}'")})
    return jsonify({'products': data})


@app.route('/api/pairs', methods=['GET'])
def pairs():
    product = execute('SELECT DISTINCT product, category FROM Films')
    return jsonify({'pairs': product})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
