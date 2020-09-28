import datetime, time
import base64
import streamlit as st
import pandas as pd
from pathlib import Path

from models.app.params import get_params
from models.app.img_display import img_to_bytes
from models.app.params import get_params
import models.app.SessionState as SessionState

from models.transformer.loader import etl

def local_css(file_name):
    with open(Path(file_name)) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("./assets/style.css")

def main():
    # Logo
    header_html = "<img src='data:image/png;base64,{}' class='home-logo'>".format(img_to_bytes("../global_assets/files/Logo_Fiat_Chrysler_Automobiles.png"))
    st.markdown(header_html, unsafe_allow_html=True)

    # Main header
    st.markdown("<h1 class='main-header'>Explore o que o mundo está dizendo sobre nós.</h1>", unsafe_allow_html=True)

    session_state = SessionState.get(search=False, end_date='', start_date='', query_selector='', source_selector=[], limit='', ig_tag='', tt_query='', params={})
    
    if session_state.search == False:
       session_state.params = get_params()
    
    if session_state.params['sources'] != []:
        search = st.button('Autalizar base')
        if search:
           session_state.search = True

    if session_state.search:
        with st.spinner("Aguarde, minerando dados e atualizando base..."):
            time.sleep(1)
        
        etl(session_state.params)

        st.success(f"Done! Base de dados atualizada com os posts mais recentes sobre {session_state.params['tt_query']}. ")
        st.balloons()
        
        link = f"<a href='http://52.201.220.9:8502' target='_self'>Explore</a>"
        st.markdown(link, unsafe_allow_html=True)     

    session_state.search = False
    
    st.markdown('-'*7)
    st.markdown("""
                    You can check the [source code here.](https://github.com/rennanharo/overviewer)\n
                    Feel free to contribute with any suggestions or pull requests. Developed by [`Rennan Haro.`](https://github.com/rennanharo)
                """)

if __name__ == "__main__":
    main()
