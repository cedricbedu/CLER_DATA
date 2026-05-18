import pandas as pd
import streamlit as st

# CONFIG PAGE
st.set_page_config(
    page_title="CinéMatch",
    layout="wide"
)

# CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #020617 0%,
        #020b2d 100%
    );
    color: white;
}

.block-container {
    padding: 2rem 4rem;
}

/* BOUTON */
div.stButton > button {
    background-color: #16213e;
    color: white;
    border-radius: 12px;
    border: 1px solid #2b3656;
    padding: 10px 18px;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #22304f;
    color: white;
}

/* TITRE */
.movie-title {
    font-size: 56px;
    font-weight: 900;
    color: white;
}

/* INFOS */
.info {
    color: #d1d5db;
    font-size: 18px;
    margin: 15px 0;
    line-height: 1.8;
}

/* GENRES */
.badge {
    background-color: #5b21b6;
    color: white;
    padding: 8px 15px;
    border-radius: 20px;
    margin-right: 10px;
    display: inline-block;
    font-weight: 600;
}

/* SECTIONS */
.section {
    font-size: 28px;
    font-weight: 800;
    margin-top: 25px;
    margin-bottom: 10px;
    color: white;
}

/* SYNOPSIS */
.synopsis {
    font-size: 16px;
    line-height: 1.7;
    color: #e5e7eb;
}

/* POSTER */
.poster img {
    border-radius: 22px;
    box-shadow: 0 20px 40px rgba(0,0,0,0.6);
}

</style>
""", unsafe_allow_html=True)

# DATASET
df = pd.read_csv("data/DF_FILMS_TMDB.csv")

# ENLEVER DOUBLONS
df = df.drop_duplicates(subset=["tconst"])

# FILM FIXE = LES ÉVADÉS
film = df[df["tconst"] == "tt0111161"].iloc[0]

# HEADER
st.markdown("# 🎞️ CinéMatch")
st.caption("powered by Cinema Lumiere")

# BOUTON RETOUR
if st.button("← Retour"):
    st.switch_page("app.py")

st.write("")

# LAYOUT
left, right = st.columns([1, 1.8], gap="large")

# POSTER
with left:

    st.markdown(
        '<div class="poster">',
        unsafe_allow_html=True
    )

    st.image(
        film["poster_url"],
        use_container_width=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

# INFOS FILM
with right:

    st.markdown(
        f'<div class="movie-title">{film["title"]}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'''
        <div class="info">
        Date de sortie : {film["release_date"]}
        <br>
        Note IMDb : {film["averageRating"]}/10
        </div>
        ''',
        unsafe_allow_html=True
    )

    # GENRES
    badges = ""

    for genre in str(film["genres"]).split(","):

        badges += f'''
        <span class="badge">
        {genre.strip()}
        </span>
        '''

    st.markdown(
        badges,
        unsafe_allow_html=True
    )

    # SYNOPSIS
    st.markdown(
        '<div class="section">Synopsis</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'''
        <div class="synopsis">
        {film["overview"]}
        </div>
        ''',
        unsafe_allow_html=True
    )

    # BANDE ANNONCE
    st.markdown(
        '<div class="section">Bande-annonce</div>',
        unsafe_allow_html=True
    )

    st.video(film["youtube_url"])