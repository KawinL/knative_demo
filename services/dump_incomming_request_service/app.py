import os

from flask import Flask, request
from flask.logging import create_logger


app = Flask(__name__)
logger = create_logger(app)


@app.route("/", methods=["GET", "POST"])
def dump_requst_info_to_log():
   print("Request headers: {}".format(request.headers))
   print("Request body: {}".format(request.data))
   print("Request args: {}".format(request.args))
   print("Request form: {}".format(request.form))
   print("Request files: {}".format(request.files))
   print("Request cookies: {}".format(request.cookies))
   print("Request method: {}".format(request.method))
   print("Request path: {}".format(request.path))
   print("Request full path: {}".format(request.full_path))
   print("Request url: {}".format(request.url))
   print("Request base url: {}".format(request.base_url))
   print("Request url root: {}".format(request.url_root))
   print("Request host url: {}".format(request.host_url))

   return "log suscessfully"


if __name__ == "__main__":
   app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
