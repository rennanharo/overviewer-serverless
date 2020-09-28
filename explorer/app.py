import streamlit as st
from pathlib import Path
from datetime import datetime

from models.app.img_display import img_to_bytes
import models.app.SessionState as SessionState

from models.loader import conn
from models.params import filters, query


def local_css(file_name):
    with open(Path(file_name)) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("assets/style.css")

engine = conn()

def main():
    # Logo
    header_html = "<img src='data:image/png;base64,{}' class='home-logo'>".format(img_to_bytes("../global_assets/files/Logo_Fiat_Chrysler_Automobiles.png"))
    st.markdown(header_html, unsafe_allow_html=True)

    # Main header
    st.markdown("<h1 class='main-header'>Explore o que o mundo está dizendo sobre nós.</h1>", unsafe_allow_html=True)

    session_state = SessionState.get(search=False, end_date='', start_date='', sources=[], models=[], flags=[], selectors={})

    if session_state.search == False:
        st.markdown("""
            Comece customizando o seu filtro no painel à esqueda.
        """)

    session_state.selectors = filters()
    
    session_state.sources = st.sidebar.multiselect('Quais fontes você está buscando?', session_state.selectors['sources'])
    session_state.models = st.sidebar.multiselect('Quais modelos você está buscando?', session_state.selectors['models'])
    
    session_state.start_date = st.sidebar.date_input('A partir de quando?', session_state.selectors['stdate'])
    if session_state.start_date < session_state.selectors['stdate']:
        st.sidebar.warning(f"A data selecionada é anterior ao último registro disponível. Por favor, selecione uma data a partir de {session_state.selectors['stdate']}")
        session_state.start_date = session_state.selectors['stdate']

    session_state.end_date = st.sidebar.date_input('Até quando?', datetime.date(datetime.now()))

    #session_state.flags = st.sidebar.multiselect('Flags', session_state.selectors['flags'])

    params = {
        'sources': session_state.sources,
        'models': session_state.models,
        'stdate': session_state.start_date,
        'endate': session_state.end_date,
        #'flags': session_state.flags
    }

    search = st.sidebar.button('Pesquisar')
    if search:
        session_state.search = True
    
    if session_state.search == True:
        df = query(params['sources'], params['models'], params['stdate'], params['endate'])  

        visuals = ['Núvem de palavras', 'Tabela']
        visual = st.selectbox('Qual visualização você quer renderizar?', visuals)

        if visual == 'Núvem de palavras':
            st.write('wordcloud')
        if visual == 'Tabela':
            st.write('Tabela')


if __name__ == "__main__":
    main()