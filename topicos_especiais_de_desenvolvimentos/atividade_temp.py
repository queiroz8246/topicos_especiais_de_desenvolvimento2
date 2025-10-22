import streamlit as st
import requests


st.title("Temperatura")
st.subheader("Veja a temperatura da sua cidade aqui")
st.divider()

with st.form("Informe o nome da sua cidade:"):
    cidade = st.text_input("Nome da cidade:", placeholder="Nome da cidade").lower()
    send = st.form_submit_button("Enviar")

if send:
    url = "https://geocoding-api.open-meteo.com/v1/search?name={}".format(cidade)
    dataBase01 = requests.get(url, timeout=5)
    dataBase01 = dataBase01.json()
    lat = dataBase01["results"][0]["latitude"]
    lon = dataBase01["results"][0]["longitude"]

    url2 = "https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&daily=temperature_2m_max,temperature_2m_min,precipitation_sum&timezone=America%2FBahia".format(lat, lon)
    dataBase02 = requests.get(url2, timeout=5)
    dataBase02 = dataBase02.json()

    st.write(f"Temperatura máxima da cidade de {cidade} é: {dataBase02["daily"]["temperature_2m_max"][0]}C°")
    st.write(f"Temperatura mínima da cidade de {cidade} é: {dataBase02["daily"]["temperature_2m_min"][0]}C°")


