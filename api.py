from sanic.response import json
from app import app
from db import session
from models import Puzzle

import random

@app.route("/")
async def test(request):
  return json({"hello": "world"})


@app.route('/map/<level>')
async def map(req, level):
  maps = session.query(Puzzle).\
    filter(Puzzle.level == level).\
    all()

  return json(random.choice(maps).to_json())