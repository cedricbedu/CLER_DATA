import streamlit as st
from recommandation import film_reco, df_encode
import base64

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def get_base64(fichier):
    with open(fichier, "rb") as f:
        return base64.b64encode(f.read()).decode()
    
img = get_base64("assets/Fond_ecran_site.png")

st.markdown(f"""
            <style>
            .stApp {{
            background-image : url("data:image/png;base64, {img}");
            background-size : cover;
            background-position : center;
            }}
            </style>
            """, unsafe_allow_html=True)


st.title("Système de recommandation de films")

df_encode['titre_note'] = df_encode['title'] + " " + df_encode['averageRating'].round(1).astype(str) + "⭐"

film_choisi = st.selectbox(
    "Choisis un film :",
    options=df_encode['title'].tolist()
)

if st.button("Recommander"):
    resultats = film_reco(film_choisi)
    st.write("### Films recommandés :")
    st.dataframe(resultats)