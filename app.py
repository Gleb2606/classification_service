from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)


@app.route('/check_stability', methods=['POST'])
def check_stability():
    try:
        # Получаем данные из запроса
        data = request.get_json()

        # Преобразуем данные в DataFrame
        df = pd.DataFrame(data)

        # Проверяем, есть ли значения больше 180 в столбце "value"
        if (df['delta'] > 180).any():
            return jsonify(message="Устойчивость нарушилась"), 200
        else:
            return jsonify(message="Устойчивость не нарушилась"), 200

    except Exception as e:
        return jsonify(error=str(e)), 400


if __name__ == '__main__':
    app.run(debug=True)
