from sanic.response import json, text
from app import app
from db import session
from models import Puzzle

import random

@app.route("/")
async def test(req):
  return json({"hello": "world"})


@app.route('/map/<level>')
async def map(req, level):
  maps = session.query(Puzzle).\
    filter(Puzzle.level == level).\
    all()
  return json(random.choice(maps).to_json())

@app.route('/clear', methods=['POST', 'OPTIONS'])
async def clear(req):
  print(req)
  if req.method == 'POST':
    return text('OK')

  res = {}
  res['id'] = req.json['id']
  res['delta'] = req.json['delta']
  res['level'] = req.json['level']
  # res['clearAt'] =  TODO. clear time 적어야함

  print(f'map id {res["id"]}를(난이도 {res["level"]}) {res["delta"]}초 만에 클리어')
  import pdb
  pdb.set_trace()
  return text('OK')