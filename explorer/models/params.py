import streamlit as st
import pandas as pd
import pandasql as ps
from datetime import datetime

from models.loader import conn

@st.cache
def filters():
  engine = conn()
  df = pd.read_sql_query("SELECT * FROM dev", engine)
  sources = list(df.source.unique())
  models = list(df.term.unique())
  # for i in range(0,len(models)):
  #   models[i] = models[i][4:].capitalize()
  stdate = datetime.strptime(min(df['timestamp'])[:10], '%Y-%m-%d').date()
  endate = datetime.strptime(max(df['timestamp'])[:10], '%Y-%m-%d').date()

  return {
    'sources': sources,
    'models': models,
    'stdate': stdate,
    'endate': endate,
  }


@st.cache
def query(sources, models, start_date, end_date):
  
  sources = tuple(sources)
  models = tuple(models)

  sources_single = ','.join(map(str, sources))
  models_single = ','.join(map(str, models))

  engine = conn()

  sql_single = f"""SELECT * FROM dev 
        WHERE timestamp BETWEEN '{start_date}' AND '{end_date}'
        AND source = '{sources_single}'
        AND term = '{models_single}'
        """

  sql_multiple = f"""SELECT * FROM dev 
        WHERE timestamp BETWEEN '{start_date}' AND '{end_date}'
        AND source = '{sources_single}'
        AND term in {models}
        """

  if len(models) == 1:
    df = pd.read_sql(sql_single, engine)
  elif len(models) > 1:
    df = pd.read_sql(sql_multiple, engine)
  return df