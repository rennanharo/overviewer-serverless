import pandas as pd
import sqlalchemy as sa
import pymysql
import configparser

config = configparser.ConfigParser()
config.read("../global_assets/etc/secrets.py")

def conn():
  host = config.get('DATABASE', 'host')
  user = config.get('DATABASE', 'user')
  pwd = config.get('DATABASE', 'password')

  db = pymysql.connect(host, user, pwd)
  engine = sa.create_engine(f'mysql+pymysql://{user}:{pwd}@{host}/test')

  return engine