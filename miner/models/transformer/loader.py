import streamlit as st
import pandas as pd
import sqlalchemy as sa
import pymysql
import configparser

from models.transformer.json_parser import clean_json
from models.transformer.cleaner import clean_insta
from models.transformer.cleaner import clean_twitter
from models.extraction.instagram.get_posts import get_posts
from models.extraction.twitter.get_tweets import get_tweets

config = configparser.ConfigParser()
config.read("miner/assets/etc/secrets.py")

def etl(params):
  
  #insta
  insta_df = get_posts(params)
  insta_df = clean_insta(insta_df, 'Instagram', params['ig_tag'])

  host = config.get('DATABASE', 'host')
  user = config.get('DATABASE', 'user')
  pwd = config.get('DATABASE', 'password')

  db = pymysql.connect(host, user, pwd)
  cursor = db.cursor()
  cursor.execute("USE test")

  engine = sa.create_engine(f'mysql+pymysql://{user}:{pwd}@{host}/test')
  insta_df.to_sql('dev', engine, if_exists='append', index=False)
  cursor.connection.commit()