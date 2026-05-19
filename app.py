import streamlit as st
import pandas as pd
from recommandation import film_reco, df_encode, df

st.set_page_config(page_title="CinéMatch", layout="wide")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #020617 0%, #020b2d 100%);
    color: white;
}
.block-container {
    padding: 2rem 4rem;
}
div.stButton > button {
    background-color: rgba(255, 255, 255, 0.1);
    color: white;
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 10px;
    padding: 10px 18px;
    font-weight: 700;
}
div.stButton > button:hover {
    background-color: #4f46e5;
    color: white;
}
.card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 16px;
    padding: 15px;
    text-align: center;
}
.poster {
    width: 100%;
    border-radius: 12px;
}
.title {
    font-weight: 800;
    margin-top: 10px;
}
.meta {
    color: rgba(255,255,255,0.6);
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)

st.title("🎞️ CinéMatch")
st.subheader("Trouvez des films similaires et explorez les acteurs")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🎬 Page film"):
        st.switch_page("pages/pagefilms.py")

with col2:
    if st.button("🎭 Page acteur"):
        st.switch_page("pages/page_acteur.py")

with col3:
    if st.button("🏛️ Le cinéma"):
        st.switch_page("pages/cinema.py")

st.markdown("---")

film_choisi = st.selectbox(
    "Choisissez un film :",
    options=df_encode["title"].dropna().tolist()
)

if st.button("Recommander"):
    resultats = film_reco(film_choisi)

    resultats = resultats.merge(
        df[["tconst", "title", "poster_url", "averageRating", "genres", "release_date"]],
        on="title",
        how="left"
    )

    st.markdown("## Films recommandés")

    cols = st.columns(5)

    for index, row in resultats.iterrows():
        with cols[index % 5]:
            poster = row.get("poster_url", "")
            title = row.get("title", "Titre inconnu")
            rating = row.get("averageRating", "N/A")
            genres = row.get("genres", "")
            release_date = str(row.get("release_date", ""))
            year = release_date[:4] if release_date and release_date != "nan" else ""

            st.markdown(f"""
            <div class="card">
                <img class="poster" src="{poster}">
                <div class="title">{title}</div>
                <div class="meta">{year}</div>
                <div class="meta">{genres}</div>
                <div>⭐ {rating}</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("Voir le film", key=f"film_home_{row['tconst']}"):
                st.session_state["film_selectionne"] = row["tconst"]
                st.switch_page("pages/pagefilms.py")