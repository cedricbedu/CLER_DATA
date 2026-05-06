import streamlit as st
from recommandation import film_reco, df_encode

st.title("Système de recommandation de films")

film_choisi = st.selectbox(
    "Choisis un film :",
    options=df_encode['title'].tolist()
)

if st.button("Recommander"):
    resultats = film_reco(film_choisi)
    st.write("### Films recommandés :")
    st.dataframe(resultats)