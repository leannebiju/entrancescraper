from flask import Flask, jsonify, request, render_template
from scrapers.neet import fetch_neet_updates
from scrapers.keam import fetch_keam_updates
from scrapers.mhtcet import fetch_mhtcet_updates
from scrapers.tnmedical import fetch_tnmedical_updates
from scrapers.karnataka import fetch_karnataka_updates

import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-updates")
def get_updates():
    exam = request.args.get("exam")
    if exam == "neet":
        return jsonify(fetch_neet_updates())
    elif exam == "keam":
        return jsonify(fetch_keam_updates())
    elif exam == "mhtcet":
        return jsonify(fetch_mhtcet_updates())
    elif exam == "tnmedical":
        return jsonify(fetch_tnmedical_updates())
    elif exam == "karnataka":
        return jsonify(fetch_karnataka_updates())
    else:
        return jsonify(["Invalid exam selected."])
        
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))  # use Render's PORT or default to 5000 locally
    app.run(host='0.0.0.0', port=port, debug = True)
