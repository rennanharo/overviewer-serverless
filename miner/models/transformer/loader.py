import streamlit as st
import pandas as pd
import sqlalchemy as sa
import pymysql

from models.transformer.json_parser import clean_json
from models.transformer.cleaner import clean_insta
from models.transformer.cleaner import clean_twitter
from models.extraction.instagram.get_posts import get_posts
from models.extraction.twitter.get_tweets import get_tweets

def etl(params):
  
  #insta
  insta_df = get_posts(params)
  insta_df = clean_insta(insta_df, 'Instagram', params['ig_tag'])
  st.dataframe(insta_df)