import streamlit as st
from recommandation import film_reco, df_encode, df
import base64
import streamlit.components.v1 as components

st.markdown("""
<style>
/* Encadré autour du contenu */
section[data-testid="stMain"] > div {
    background: rgba(255, 255, 255, 0.06) !important;
    border: 0.5px solid rgba(255, 255, 255, 0.12) !important;
    border-radius: 16px !important;
    padding: 2.5rem 3rem !important;
    backdrop-filter: blur(4px) !important;
    max-width: 950px !important;
    margin: 2rem auto !important;
}

/* Espacement titre */
h1 { margin-bottom: 0.3rem !important; }

/* Espacement sous-titre */
h2, h3 { margin-bottom: 1.5rem !important; }

/* Espacement selectbox */
div[data-testid="stSelectbox"] {
    margin-bottom: 1.5rem !important;
}

/* Espacement bouton */
div[data-testid="stButton"] {
    margin-bottom: 2rem !important;
}

/* Bouton visible au hover */
.stButton > button {
    background-color: rgba(255, 255, 255, 0.1) !important;
    color: #ffffff !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    border-radius: 8px !important;
}
.stButton > button:hover {
    background-color: rgba(255, 255, 255, 0.25) !important;
    color: #ffffff !important;
    border: 1px solid rgba(255, 255, 255, 0.6) !important;
}
</style>
""", unsafe_allow_html=True)

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


st.title("Découvrez des films similaires")
st.subheader("Entrez le titre d'un film et trouvez 5 recommandations personnalisées")

df_encode['titre_note'] = df_encode['title'] + " " + df_encode['averageRating'].round(1).astype(str) + "⭐"

film_choisi = st.selectbox(
    "Choisissez un film :",
    options=df_encode['title'].tolist()
)



if st.button("Recommander"):
    resultats = film_reco(film_choisi)
    resultats = resultats.merge(
        df[["title", "poster_url", "youtube_url", "averageRating"]],
        on="title",
        how="left"
    )

    cards_html = ""
    for _, row in resultats.iterrows():
        annee = str(row['release_date'])[:4]
        cards_html += f"""
        <div class="film-card">
            <img src="{row['poster_url']}" alt="{row['title']}"/>
            <div class="film-info">
                <div class="film-title">{row['title']}</div>
                <div class="film-meta">{annee} · {row['genres']}</div>
                <div class="film-rating">⭐ {row['averageRating']}</div>
            </div>
        </div>
        """

    components.html(f"""
    <style>
        body {{ margin: 0; background: transparent; }}
        .wrapper {{
            position: relative;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .arrow {{
            flex-shrink: 0;
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: rgba(255,255,255,0.1);
            border: 0.5px solid rgba(255,255,255,0.25);
            color: white;
            font-size: 20px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            user-select: none;
            transition: background 0.2s;
        }}
        .arrow:hover {{ background: rgba(255,255,255,0.25); }}
        .carousel {{
            display: flex;
            gap: 12px;
            overflow: hidden;
            flex: 1;
            padding: 12px 0;
        }}
        .film-card {{
            flex: 0 0 calc(20% - 10px);
            background: rgba(255,255,255,0.07);
            border: 0.5px solid rgba(255,255,255,0.15);
            border-radius: 12px;
            overflow: hidden;
            transition: transform 0.3s ease, opacity 0.4s ease;
        }}
        .film-card.fading {{ opacity: 0; transform: scale(0.97); }}
        .film-card:hover {{ transform: translateY(-4px); }}
        .film-card img {{
            width: 100%;
            height: auto;
            display: block;
        }}
        .film-info {{
            padding: 10px 10px 14px;
            display: flex;
            flex-direction: column;
            gap: 5px;
        }}
        .film-title {{
            font-size: 12px;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.3;
            min-height: 32px;
            font-family: sans-serif;
        }}
        .film-meta {{
            font-size: 11px;
            color: rgba(255,255,255,0.5);
            font-family: sans-serif;
        }}
        .film-rating {{
            font-size: 12px;
            color: #f5c518;
            font-weight: 600;
            font-family: sans-serif;
        }}
    </style>

    <div class="wrapper">
        <div class="arrow" id="prev">‹</div>
        <div class="carousel" id="carousel">
            {cards_html}
        </div>
        <div class="arrow" id="next">›</div>
    </div>

<script>
        const carousel = document.getElementById('carousel');
        const cards = Array.from(carousel.children);
        const total = cards.length;
        let current = 0;
        let animating = false;

        function showFrom(index) {{
            cards.forEach((card, i) => {{
                const pos = ((i - index) % total + total) % total;
                card.style.order = pos;
            }});
        }}

        function rotate(dir) {{
            if (animating) return;
            animating = true;

            const slideOut = dir === 1 ? '-8%' : '8%';
            const slideIn  = dir === 1 ? '8%'  : '-8%';

            // Glissement sortie — opacité reste haute (0.85)
            cards.forEach(c => {{
                c.style.transition = 'transform 0.28s ease, opacity 0.28s ease';
                c.style.transform  = `translateX(${{slideOut}})`;
                c.style.opacity    = '0.85';
            }});

            setTimeout(() => {{
                cards.forEach(c => {{
                    c.style.transition = 'none';
                    c.style.transform  = `translateX(${{slideIn}})`;
                    c.style.opacity    = '0.85';
                }});

                current = (current + dir + total) % total;
                showFrom(current);

                requestAnimationFrame(() => {{
                    requestAnimationFrame(() => {{
                        cards.forEach(c => {{
                            c.style.transition = 'transform 0.32s ease, opacity 0.2s ease';
                            c.style.transform  = 'translateX(0)';
                            c.style.opacity    = '1';
                        }});
                        setTimeout(() => {{ animating = false; }}, 320);
                    }});
                }});
            }}, 280);
        }}

        document.getElementById('next').addEventListener('click', () => rotate(1));
        document.getElementById('prev').addEventListener('click', () => rotate(-1));

        showFrom(0);
        
    </script>
    """, height=420, scrolling=False)

    st.markdown("""
<div style="
    text-align: center;
    padding: 1.2rem;
    margin-top: 1rem;
    background: rgba(255,255,255,0.05);
    border: 0.5px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    font-family: sans-serif;
">
    <span style="font-size: 13px; color: rgba(255,255,255,0.5);">
        © 2026 &nbsp;<strong style="color: rgba(255,255,255,0.8);">Cinéma Lumière</strong>
        &nbsp;·&nbsp; Trouvez votre prochain film préféré
    </span>
</div>
""", unsafe_allow_html=True)