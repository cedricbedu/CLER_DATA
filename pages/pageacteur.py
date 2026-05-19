import streamlit as st
import pandas as pd

st.set_page_config(page_title="CinéMatch", layout="wide")

# ---------- CSS ----------
st.markdown("""
<style>
.stApp {
    background-color: #0f172a;
    color: white;
}
.card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 16px;
    margin-bottom: 16px;
}
.movie-card {
    background: #1e293b;
    border: 1px solid #334155;
    border-radius: 12px;
    padding: 10px;
    display: flex;
    gap: 15px;
    min-height: 145px;
}
.movie-img {
    width: 95px;
    height: 130px;
    object-fit: cover;
    border-radius: 8px;
}
.actor-img {
    width: 100%;
    border-radius: 12px;
}
.small {
    color: #cbd5e1;
    font-size: 14px;
}
.purple {
    color: #d946ef;
}
</style>
""", unsafe_allow_html=True)

# ---------- DATA ----------
@st.cache_data
def load_data():
    actors = pd.read_csv("data/DF_INTERVENANTS_TMDB.csv")
    movies = pd.read_csv("data/DF_FILMS_TMDB.csv")
    links = pd.read_csv("data/DF_INTERMEDIAIRE_TMDB.csv")
    return actors, movies, links

actors, movies, links = load_data()

# ---------- HEADER ----------
st.markdown("## 🎞️ CinéMatch")
st.markdown("---")

# ---------- SELECT ACTOR ----------
actor_names = sorted(actors["name"].dropna().unique())
selected_actor = st.selectbox("Choisis un acteur", actor_names)

actor = actors[actors["name"] == selected_actor].iloc[0]

# Films connus de l'acteur
actor_links = links[links["nconst"] == actor["nconst"]]
actor_movies = actor_links.merge(movies, left_on="knownForTitles", right_on="tconst", how="inner")

# ---------- PAGE ----------
left, right = st.columns([1, 2.1], gap="large")

with left:
    if pd.notna(actor.get("url")):
        st.markdown(
            f'<img class="actor-img" src="{actor["url"]}">',
            unsafe_allow_html=True
        )

    birthday = actor.get("birthday", "Inconnu")
    birth_year = actor.get("birthYear", "Inconnu")

    st.markdown(f"""
    <div class="card">
        <p class="small">📅 Date de naissance</p>
        <b>{birthday}</b>
        <br><br>
        <p class="small">🎬 Département connu</p>
        <b>{actor.get("known_for_department", "Inconnu")}</b>
        <br><br>
        <p class="small">⭐ Popularité</p>
        <b>{actor.get("popularity", "Inconnu")}</b>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.title(actor["name"])

    st.subheader("Biographie")
    bio = actor.get("biography", "")
    if pd.isna(bio) or bio.strip() == "":
        bio = "Biographie non disponible."
    st.write(bio)

    st.markdown("## 🎞️ Filmographie")

    if actor_movies.empty:
        st.info("Aucun film trouvé pour cet acteur.")
    else:
        cols = st.columns(2)

        for index, movie in actor_movies.iterrows():
            with cols[index % 2]:
                poster = movie.get("poster_url", "")
                title = movie.get("title", "Titre inconnu")
                date = str(movie.get("release_date", ""))
                year = date[:4] if date and date != "nan" else "Année inconnue"
                rating = movie.get("averageRating", "N/A")
                genres = movie.get("genres", "Genre inconnu")

                st.markdown(f"""
                <div class="movie-card">
                    <img class="movie-img" src="{poster}">
                    <div>
                        <h3>{title}</h3>
                        <p class="small">{year}</p>
                        <p class="purple">Genres : {genres}</p>
                        <p>⭐ {rating}/10</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("## Acteurs similaires")
    similar = actors[
        (actors["known_for_department"] == actor["known_for_department"]) &
        (actors["name"] != actor["name"])
    ].head(3)

    cols = st.columns(3)
    for i, (_, person) in enumerate(similar.iterrows()):
        with cols[i]:
            st.image(person["url"], use_container_width=True)
            st.write(person["name"])
