from textblob import TextBlob
import pandas as pd
import streamlit as st
from PIL import Image
from googletrans import Translator

st.title('Análisis de Sentimiento')
image = Image.open('emoticones.jpg')
st.image(image)
st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

translator = Translator()

with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo 😊')
            image_positivo = Image.open('feliz.jpeg')
            st.image(image_positivo)
            audio_file = open('feliz.mp3', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='feliz/mp3', start_time=0)
        if x <= -0.5:
            st.write('Es un sentimiento Negativo 😔')
            image_negativo = Image.open('tristeza3.jpeg')
            st.image(image_negativo)
            audio_file = open('tristeza.mp3', 'rb')
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format='tristeza/mp3', start_time=0)

        else:
            st.write( 'Es un sentimiento Neutral 😐')
