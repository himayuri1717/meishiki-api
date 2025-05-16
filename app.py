from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    birthdate = data.get("birthdate")
    birthtime = data.get("birthtime")

    # 簡易ダミーデータ返却（本番では命式計算ロジックに差し替え）
    result = {
        "center_star": "正財",
        "center_star_summary": "正財は誠実で地道な努力を評価される星。安定志向で堅実に成果を積み上げる力を持ちます。",
        "rows": [
            {
                "pillar": "年柱",
                "star": "偏財",
                "hidden_star": "劫財",
                "description": "第一印象は社交的で気配り上手。内面は自立心・競争心が強く、家系由来の才能を示します。",
            },
            {
                "pillar": "月柱",
                "star": "正官",
                "hidden_star": "印綬",
                "description": "仕事への姿勢は真面目で責任感あり。得意なことは学びや教え育む分野。",
            },
            {
                "pillar": "日柱",
                "star": "食神",
                "hidden_star": "比肩",
                "description": "表現力があり柔らかい印象。本質は自立心が強くマイペース。",
            },
            {
                "pillar": "時柱",
                "star": "偏印",
                "hidden_star": "",
                "description": "独創的な発想や直感力に優れています（※出生時間未入力のため仮）",
            },
        ],
    }
    return jsonify(result)
