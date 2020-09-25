import streamlit as st
import pandas as pd
import numpy as np

def clean_insta(df, source, term):
    df = df[['timestamp', 'likes', 'captions', 'comments']]
    df = df.assign(comments=df.comments.str.split("','")).explode('comments').reset_index(drop=True)
    df = df.assign(source=source, term=term)
    df = df[['source', 'term', 'timestamp', 'likes', 'captions', 'comments']]
    df.dropna(inplace=True)

    flags = ['defeito','problema','pane','fogo','incendio','incêndio']
    def assign_flags(s):
        for flag in flags:
            if flag in s:
                return 1
            else:
                return 0

    df["flags"] = df["comments"].apply(assign_flags)
    df.dropna(inplace=True)

    return df

def clean_twitter(df, source, term):
    pass