from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/meishiki', methods=['GET'])
def meishiki():
    date = request.args.get('date')
    hour = request.args.get('hour', default=None)

    if not date:
        return jsonify({'error': 'date is required'}), 400

    result = {
        "date": date,
        "hour": hour,
        "example_result": "仮の命式です"
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run()