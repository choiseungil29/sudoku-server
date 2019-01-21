import requests
import random

from models import Puzzle
from db import session

def crawl():
  levels = ['easy', 'medium', 'hard', 'expert']
  level = random.choice(levels)
  r = requests.get(f'https://sudoku.com/api/getLevel/{level}').json()

  problem = r['desc'][0]
  answer = r['desc'][1]
  print(f'level : {level}')
  print(f'problem : {problem}')
  print(f'answer : {answer}')

  return {
    'level': level,
    'problem': r['desc'][0],
    'answer': r['desc'][1]
  }

if __name__ == '__main__':

  for i in range(0, 10):
    puzzle = Puzzle(**crawl())
    session.add(puzzle)
  session.commit()