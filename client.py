import streamlit as st
import pandas as pd

st.button("← Retour à l'accueil")  # Bouton pour revenir à la page d'accueil:

# Titre principal de l'application (affiché en haut de la page)
st.title("Cinémas Lumière Creusoise")

# Sous-titre (taille 2), utile pour organiser le contenu par sous-sections
st.subheader("Votre cinéma indépendant au cœur de la Creuse")

st.image("salle.jpg")

st.title("Informations pratiques")

st.markdown("""
<div style="
    background-color: #142850;
    padding: 20px;
    border-radius: 30px;
  color:white;
">

📍 <b>Adresse</b><br>
12 Place du Village<br>
23000 Guéret, France<br><br>

📞 <b>Téléphone</b><br>
05 55 12 34 56<br><br>

✉️ <b>Email</b><br>
contact@lumierecreusoise.fr<br><br>

🕒 <b>Horaires</b><br>
Mercredi au dimanche : 15h à 22h<br>
Fermé lundi et mardi

</div>
""", unsafe_allow_html=True)

st.subheader("🕰️ Notre Histoire")
st.markdown("""
Fondé en 1998, Cinémas Lumière Creusoise est né de la volonté de maintenir une offre culturelle en milieu rural. Depuis plus de 25 ans, il permet aux habitants de la région de profiter du cinéma sans avoir à se déplacer vers les grandes villes.

Avec ses salles à taille humaine, le cinéma privilégie une expérience conviviale et accessible à tous. Sa programmation met en avant aussi bien des films populaires que du cinéma indépendant, des documentaires et des œuvres européennes.

Attaché à son territoire, le cinéma participe activement à la vie locale en organisant des projections scolaires, des débats et des événements culturels en partenariat avec les acteurs de la région.
""")

#pour changer la couleur de fond de l'application
st.markdown("<style>.stApp {background-color:#0b1c3d;}</style>", unsafe_allow_html=True)

st.markdown("<style>.stButton > button {background:#1f3b5c;color:white;}</style>", unsafe_allow_html=True)

st.markdown("""
<div style="
    background-color: #142850;
    padding: 20px;
    border-radius: 30px;
  color:white;
">

🎥 <b>2 Salles</b><br>
De 50 à 120 places<br><br>

👥 <b>25 000+</b><br>
Spectateurs par an<br><br>

🌱 <b>Label Art & Essai</b><br>
Cinéma engagé et indépendant

</div>
""", unsafe_allow_html=True)

#changer la couleur du texte
st.markdown("<style>.stApp {background-color:#0b1c3d; color:white;}</style>", unsafe_allow_html=True)

