import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

default_stopwords = ['a', 'agora', 'ainda', 'alguém', 'algum', 'alguma', 'algumas', 'alguns', 'ampla', 'amplas', 'amplo', 'amplos', 'ante', 'antes', 'ao', 'aos', 'após', 'aquela', 'aquelas', 'aquele', 'aqueles', 'aquilo', 'as', 'até', 'através', 'cada', 'coisa', 'coisas', 'com', 'como', 'contra', 'contudo', 'da', 'daquele', 'daqueles', 'das', 'de', 'dela', 'delas', 'dele', 'deles', 'depois', 'dessa', 'dessas', 'desse', 'desses', 'desta', 'destas', 'deste', 'deste', 'destes', 'deve', 'devem', 'devendo', 'dever', 'deverá', 'deverão', 'deveria', 'deveriam', 'devia', 'deviam', 'disse', 'disso', 'disto', 'dito', 'diz', 'dizem', 'do', 'dos', 'e', 'é', 'ela', 'elas', 'ele', 'eles', 'em', 'enquanto', 'entre', 'era', 'essa', 'essas', 'esse', 'esses', 'esta', 'está', 'estamos', 'estão', 'estas', 'estava', 'estavam', 'estávamos', 'este', 'estes', 'estou', 'eu', 'fazendo', 'fazer', 'feita', 'feitas', 'feito', 'feitos', 'foi', 'for', 'foram', 'fosse', 'fossem', 'grande', 'grandes', 'há', 'isso', 'isto', 'já', 'la', 'lá', 'lhe', 'lhes', 'lo', 'mas', 'me', 'mesma', 'mesmas', 'mesmo', 'mesmos', 'meu', 'meus', 'minha', 'minhas', 'muita', 'muitas', 'muito', 'muitos', 'na', 'não', 'nas', 'nem', 'nenhum', 'nessa', 'nessas', 'nesta', 'nestas', 'ninguém', 'no', 'nos', 'nós', 'nossa', 'nossas', 'nosso', 'nossos', 'num', 'numa', 'nunca', 'o', 'os', 'ou', 'outra', 'outras', 'outro', 'outros', 'para', 'pela', 'pelas', 'pelo', 'pelos', 'pequena', 'pequenas', 'pequeno', 'pequenos', 'per', 'perante', 'pode', 'pude', 'podendo', 'poder', 'poderia', 'poderiam', 'podia', 'podiam', 'pois', 'por', 'porém', 'porque', 'posso', 'pouca', 'poucas', 'pouco', 'poucos', 'primeiro', 'primeiros', 'própria', 'próprias', 'próprio', 'próprios', 'quais', 'qual', 'quando', 'quanto', 'quantos', 'que', 'quem', 'são', 'se', 'seja', 'sejam', 'sem', 'sempre', 'sendo', 'será', 'serão', 'seu', 'seus', 'si', 'sido', 'só', 'sob', 'sobre', 'sua', 'suas', 'talvez', 'também', 'tampouco', 'te', 'tem', 'tendo', 'tenha', 'ter', 'teu', 'teus', 'ti', 'tido', 'tinha', 'tinham', 'toda', 'todas', 'todavia', 'todo', 'todos', 'tu', 'tua', 'tuas', 'tudo', 'última', 'últimas', 'último', 'últimos', 'um', 'uma', 'umas', 'uns', 'vendo', 'ver', 'vez', 'vindo', 'vir', 'vos', 'vós', ',', "'"]
  

def word_cloud_twitter(input_stopwords, df):
  stopwords = default_stopwords

  input_stopwords = [x.strip() for x in input_stopwords.split(',')]

  for term in input_stopwords:
    stopwords.append(term)

  tweets = ' '.join(tweet for tweet in df['Text'])

  wordcloud = WordCloud(stopwords=stopwords, background_color="white", mode="RGBA", max_words=50).generate(tweets)
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis('off')
  wordcloud.to_file("assets/outputs/word_clouds/twitter/tweets.png")

def word_cloud_insta(input_stopwords, df, tag):
  stopwords = default_stopwords

  input_stopwords = [x.strip() for x in input_stopwords.split(',')]

  for term in input_stopwords:
    stopwords.append(term)

  comments = ' '.join(comment for comment in df['comments'])
  captions = ' '.join(caption for caption in df['captions'])

  terms = ' '.join([comments, captions])

  wordcloud = WordCloud(stopwords=stopwords, background_color="white", mode="RGBA", max_words=100).generate(terms)
  plt.imshow(wordcloud, interpolation='bilinear')
  plt.axis('off')
  wordcloud.to_file(f"assets/outputs/word_clouds/instagram/{tag}.png")

  # strada = ['Strada, Fiat, Nova Stsrada, Fiat Strada, Venda, Vendas, Nova, dia, fiatstrada, novastrada, você, bio, WhatsApp, fiatbr, mais, strada2021, modelo, Veículo, vai, preço, amigo, carro, pra, ano, novo, CNPJ, versão, carro, Fiat, mais, novastrada, mil, strada, fiatstrada, pra, ficou, Fiat Strada, vai, sim, versão, giubrandaooficial, nova, Gui, tá, ZERO KM, Giu, picape, vídeo, carros, novo, venda, você, vc, dia, picapes, es, valor, RODAS, fiatbr, strada2021, ano, ser, trabalho, cnpj, fora, aqui, acho, pro, car, vendas, vem, achei, www, desconto, preço']