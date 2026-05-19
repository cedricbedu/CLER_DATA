import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="CinéMatch - Film",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #050816 0%, #0b1026 50%, #111827 100%);
    color: white;
}
.block-container {
    padding: 2rem 4rem;
    max-width: 1400px;
}
.logo {
    font-size: 42px;
    font-weight: 900;
    margin-bottom: 5px;
}
.subtitle {
    color: #a1a1aa;
    font-size: 15px;
    margin-bottom: 25px;
}
div.stButton > button {
    background: rgba(255,255,255,0.08);
    color: white;
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 14px;
    padding: 12px 22px;
    font-weight: 700;
}
div.stButton > button:hover {
    background: #4f46e5;
    color: white;
}
.movie-title {
    font-size: 64px;
    font-weight: 900;
    line-height: 1.05;
    margin-bottom: 25px;
}
.info-box {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 24px;
    padding: 24px;
    margin-bottom: 25px;
    width: 100%;
}
.info-line {
    font-size: 18px;
    color: #f3f4f6;
    margin-bottom: 10px;
}
.badge {
    background: linear-gradient(135deg, #7c3aed, #2563eb);
    color: white;
    padding: 9px 18px;
    border-radius: 999px;
    margin-right: 10px;
    margin-bottom: 10px;
    display: inline-block;
    font-weight: 700;
    font-size: 14px;
}
.section {
    font-size: 30px;
    font-weight: 900;
    margin-top: 35px;
    margin-bottom: 15px;
}
.synopsis {
    font-size: 17px;
    line-height: 1.8;
    color: #e5e7eb;
    max-width: 850px;
}
.poster-img {
    border-radius: 28px;
    box-shadow: 0 30px 70px rgba(0,0,0,0.65);
    width: 100%;
}
.actor-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 20px;
    padding: 20px;
    text-align: center;
    font-weight: 700;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

df = pd.read_csv("data/DF_FILMS_TMDB_FINAL.csv")
df = df.drop_duplicates(subset=["tconst"])

st.markdown("""
<div class="logo">🎞️ CinéMatch</div>
<div class="subtitle">Powered By CLER Data</div>
""", unsafe_allow_html=True)

if st.button("← Retour à l'accueil"):
    st.switch_page("app.py")

if "film_selectionne" in st.session_state:
    film_id = st.session_state["film_selectionne"]
    film_data = df[df["tconst"] == film_id]

    if film_data.empty:
        st.error("Film introuvable.")
        st.stop()

    film = film_data.iloc[0]
else:
    film = df[df["tconst"] == "tt0111161"].iloc[0]

left, right = st.columns([1, 1.7], gap="large")

with left:
    st.markdown(
        f'<img class="poster-img" src="{film["poster_url"]}">',
        unsafe_allow_html=True
    )

with right:
    st.markdown(
        f'<div class="movie-title">{film["title"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"""
    <div class="info-box">
        <div class="info-line">📅 Date de sortie : <b>{film["release_date"]}</b></div>
        <div class="info-line">⭐ Note IMDb : <b>{film["averageRating"]}/10</b></div>
    </div>
    """, unsafe_allow_html=True)

    badges = ""
    for genre in str(film["genres"]).split(","):
        badges += f'<span class="badge">{genre.strip()}</span>'

    st.markdown(badges, unsafe_allow_html=True)

    st.markdown('<div class="section">Synopsis</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="synopsis">
        {film["overview"]}
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section">Bande-annonce</div>', unsafe_allow_html=True)

if "youtube_url" in df.columns and pd.notna(film["youtube_url"]):
    st.video(film["youtube_url"])
else:
    st.warning("Aucune bande-annonce disponible pour ce film.")

st.markdown('<div class="section">Acteurs principaux</div>', unsafe_allow_html=True)

if "actors" in df.columns and pd.notna(film["actors"]):
    actors = str(film["actors"]).split(",")

    cols = st.columns(4)

    for index, actor in enumerate(actors[:8]):
        actor_name = actor.strip()

        with cols[index % 4]:
            st.markdown(f"""
            <div class="actor-card">
                🎭<br>{actor_name}
            </div>
            """, unsafe_allow_html=True)

            if st.button("Voir acteur", key=f"actor_{actor_name}_{index}"):
                st.session_state["acteur_selectionne"] = actor_name
                st.switch_page("pages/page_acteur.py")
else:
    st.info("La colonne des acteurs n'existe pas encore dans le dataframe.")