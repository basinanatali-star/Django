from pathlib import Path
from flask import Flask, send_from_directory

BASE_DIR = Path(__file__).resolve().parent

SRC_DIR = BASE_DIR / "src"
BOOTSTRAP_DIR = BASE_DIR / "bootstrap-5.3.8-dist"

app = Flask(__name__)

@app.route("/Django/bootstrap-5.3.8-dist/<path:filename>")
def bootstrap(filename):
    return send_from_directory(BOOTSTRAP_DIR, filename)

@app.route("/", defaults={"_path": ""}, methods=["GET"])
@app.route("/<path:_path>", methods=["GET"])
def contacts_page(_path):
    return send_from_directory( SRC_DIR, "page_contacts.html", mimetype="text/html" )
