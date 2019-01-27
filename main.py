from app import app
from sanic_cors import CORS, cross_origin

import api

CORS(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)