import streamlit as st
import pandas as pd
import yfinance as yf
import investpy as inv
import seaborn as sns 
port matplotlib.pyplot as plt
from datetime import date



st.sidebar.image('test.jpg')
st.sidebar.title ('Finanças')
st.sidebar.mardown('---')
lista_menu('home','panorama do mercado','rentabilidades mensais','fundamentos' )
escolha=st.sidebar.radio('escolha a opção',lista_menu)