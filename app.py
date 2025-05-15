from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    # 命式計算ロジック（例として年柱のみ返すダミー）
    result = {
        "center_star": "正財",
        "rows": [
            {"pillar": "年柱", "star": "偏財", "hidden_star": "劫財", "description": "第一印象は社交的で気配り上手..."},
            # 他の柱も続けて追加
        ]
    }
    return jsonify(result)
