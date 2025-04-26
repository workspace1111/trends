from flask import Flask, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)

@app.route('/trending')
def trending():
    try:
        pytrends = TrendReq(hl='tr-TR', tz=180)
        trending_searches = pytrends.trending_searches(pn='united_states')
        results = []
        for i, row in trending_searches.iterrows():
            results.append({"name": row[0]})
        return jsonify(results)
    except Exception as e:
        # Hata mesajını da döndür
        return jsonify({"error": str(e)}), 500

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
