import aiohttp
import requests
import random
import asyncio

from models import Puzzle
from db import session

async def crawl():
  levels = ['easy', 'medium', 'hard', 'expert']
  level = random.choice(levels)
  print('go')

  http = aiohttp.ClientSession()
  resp = await http.get(f'https://sudoku.com/api/getLevel/{level}')
  r = await resp.json()
  print(r)

  problem = r['desc'][0]
  answer = r['desc'][1]
  print(f'level : {level}')
  print(f'problem : {problem}')
  print(f'answer : {answer}')

  await http.close()

  return {
    'level': level,
    'problem': r['desc'][0],
    'answer': r['desc'][1]
  }


async def crawl_all():
  fts = [asyncio.ensure_future(crawl()) for _ in range(0, 50)]

  for f in asyncio.as_completed(fts):
    try:
      puzzle = await f
      puzzle = Puzzle(**puzzle)
      session.add(puzzle)
      session.commit()
    except Exception as e:
      pass

if __name__ == '__main__':
  loop = asyncio.get_event_loop()
  loop.run_until_complete(crawl_all())
