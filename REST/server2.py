from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calc', methods=['GET'])
def calculate():
    try:
        a = int(request.args.get('a'))
        b = int(request.args.get('b'))

        x = a + b
        y = a * b

        return jsonify({'add': x, 'mul': y})

    except (TypeError, ValueError):
        return jsonify({'error': 'invalid input'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5152)