import os
import pandas as pd
import streamlit as st

from models.transformer.json_parser import clean_json

def get_posts(params):
  os.system(f"instagram-scraper --media-types none --tag {params['ig_tag']} --maximum {params['limit']} --comments --retry-forever --destination miner/assets/temp/instagram/")

  insta_df = clean_json(params['ig_tag'])

  os.remove(f"miner/assets/temp/instagram/{params['ig_tag']}.json")

  return insta_df