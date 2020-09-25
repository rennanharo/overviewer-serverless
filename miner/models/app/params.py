import streamlit as st
import pandas as pd
import datetime

def get_params():
  # Declarations
  end_date = ''
  start_date = ''

  # Input section
  # The term to be searched for
  query_selector = st.text_input('O que você quer saber mais sobre?', 'Nova Strada')
  # The sources to search te term from
  source_selector = st.multiselect('Selecione as fontes', ['Instagram', 'Twitter'])

  # Display Instagram info
  if 'Instagram' in source_selector:
    st.info(f'O termo {query_selector} será pesquisado como uma hashtag (#) no Instagram.')
  
  # Display Twitter info and exclusive parameters
  if 'Twitter' in source_selector:
      # Start date
      start_date = st.date_input("Data de início", datetime.date(2019, 7, 30))
      # End date
      end_date = st.date_input("Data de término", datetime.date.today())
      st.info('Os campos de data só funcionam para filtrar informações do Twitter.')

  # Max number of posts to gather from each social media
  limit = st.slider("Qual o número máximo de posts que você quer buscar? (Quanto maior o número, mais tempo leva para rodar.)", 1, 500, 250, 10)

  # Query terms prep.
  ig_tag = query_selector.replace(' ', '').lower()
  tt_query = query_selector

  return {
    'sources': source_selector,
    'limit': limit,
    'ig_tag': ig_tag,
    'tt_query': tt_query,
    'stdt': start_date,
    'endt': end_date,
  }
      



