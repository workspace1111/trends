from flask import Flask, jsonify
from pytrends.request import TrendReq

app = Flask(__name__)

@app.route('/trending')
def trending():
    pytrends = TrendReq(hl='tr-TR', tz=180)
    trending_searches = pytrends.trending_searches(pn='turkey')  # 'turkey', 'united_states', 'worldwide' vs.
    results = []
    for i, row in trending_searches.iterrows():
        results.append({"name": row[0]})
    return jsonify(results)

if __name__ == '__main__':
    app.run(port=5000)
