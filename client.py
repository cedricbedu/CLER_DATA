import streamlit as st

# CONFIG
st.set_page_config(layout="wide")

st.markdown("""
<style>

/* 👉 centre tout le contenu Streamlit */
.block-container {
    max-width: 1100px;
    margin: auto;
}

/* option : encore plus propre sur très grand écran */
@media (min-width: 1600px) {
    .block-container {
        max-width: 1000px;
    }
}

</style>
""", unsafe_allow_html=True)

# STYLE GLOBAL
st.markdown("""
<style>
.stApp {
    background-color: #0b1c3d;
    color: white;
}

/* Cartes */
.block {
    background-color: #1c2a44;
    padding: 25px;
    border-radius: 20px;
}

.stat-card {
    background-color: #1c2a44;
    padding: 30px;
    border-radius: 20px;
    text-align: center;
}

/* CTA */
.cta {
    background: linear-gradient(90deg, #3b1c6b, #5a2ea6);
    padding: 50px;
    border-radius: 20px;
    text-align: center;
}

/* Boutons */
.stButton > button {
    background-color: #0b1c3d;
    color: white;
    border: 1px solid #3b82f6;
    border-radius: 20px;
    padding: 10px 25px;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #1f3b5c;
    color: white;
}
            
</style>
""", unsafe_allow_html=True)

# HEADER
st.button("← Retour à l'accueil")

st.title("Cinémas Lumière Creusoise")
st.write("Votre cinéma indépendant au cœur de la Creuse")

# SECTION IMAGE + INFOS
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown('<div class="block">', unsafe_allow_html=True)
    st.image("salle.jpg", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="block">', unsafe_allow_html=True)

    st.subheader("Informations pratiques")

    st.write("📍 **Adresse**")
    st.write("**12 Place du Village**")
    st.write("**23000 Guéret, France**")
    
    st.write("📞 **Téléphone : 05 55 12 34 56**")
   
    st.write("✉️ **Email : contact@lumierecreusoise.fr**")

    st.write("🕒 **Horaires: tous les jours de 14h à 23h**")
    
    st.markdown('</div>', unsafe_allow_html=True)

# HISTOIRE
st.subheader("🕰️ Notre Histoire")

st.markdown("""
<div style="font-size:18px; line-height:1.6;">
Fondé en 1998, Cinémas Lumière Creusoise est né de la volonté de maintenir une offre culturelle en milieu rural. Depuis plus de 25 ans, il permet aux habitants de la région de profiter du cinéma sans avoir à se déplacer vers les grandes villes.

Avec ses salles à taille humaine, le cinéma privilégie une expérience conviviale et accessible à tous. Sa programmation met en avant aussi bien des films populaires que du cinéma indépendant, des documentaires et des œuvres européennes.

Attaché à son territoire, le cinéma participe activement à la vie locale en organisant des projections scolaires, des débats et des événements culturels en partenariat avec les acteurs de la région.
</div>
""", unsafe_allow_html=True)

st.write("")

# STATS
col1, col2, col3 = st.columns(3)

def stat(icon, title, subtitle):
    return f"""
    <div class="stat-card">
        <div style="font-size:40px;">{icon}</div>
        <div style="font-size:24px; font-weight:bold; margin-top:10px;">{title}</div>
        <div style="opacity:0.7;">{subtitle}</div>
    </div>
    """

with col1:
    st.markdown(stat("🎬", "2 Salles", "De 50 à 120 places"), unsafe_allow_html=True)

with col2:
    st.markdown(stat("👥", "25 000+", "Spectateurs par an"), unsafe_allow_html=True)

with col3:
    st.markdown(stat("🌱", "Label Art & Essai", "Cinéma engagé et indépendant"), unsafe_allow_html=True)

st.write("")

# SECTION PARTENAIRES
st.markdown("""
<div class="cta">
    <h2>🤝 Nos partenaires</h2>
    <p>Nous collaborons avec des acteurs locaux pour faire vivre la culture en Creuse</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,2])

# IMAGE PARTENAIRE (FormatRcie)
# 🎨 STYLE CINÉMA
st.markdown("""
<style>
.partner-card {
    text-align: center;
    padding: 15px;
    border-radius: 15px;
    background: linear-gradient(145deg, #1a1a1a, #2a2a2a);
    box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    transition: all 0.3s ease;
}

.partner-card:hover {
    transform: translateY(-8px) scale(1.05);
    box-shadow: 0 8px 25px rgba(255,0,80,0.4);
}

.partner-img {
    border-radius: 50%;
    margin-bottom: 10px;
}

.partner-title {
    font-size: 14px;
    color: white;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)

# 🎞️ COLONNES
col1, col2, col3, col4, col5, col6 = st.columns(6)

def partenaire(img, name):
    return f"""
    <div class="partner-card">
        <img src="{img}" width="60" class="partner-img">
        <div class="partner-title">{name}</div>
    </div>
    """

# 🎭 PARTENAIRES
with col1:
    st.markdown(partenaire("https://cdn-icons-png.flaticon.com/512/2922/2922510.png", "Rebecca"), unsafe_allow_html=True)

with col2:
    st.markdown(partenaire("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", "Médiathèque"), unsafe_allow_html=True)

with col3:
    st.markdown(partenaire("https://cdn-icons-png.flaticon.com/512/1046/1046784.png", "Café culturel"), unsafe_allow_html=True)

with col4:
    st.markdown(partenaire("https://cdn-icons-png.flaticon.com/512/4221/4221419.png", "Festival"), unsafe_allow_html=True)

with col5:
    st.markdown(partenaire("https://cdn-icons-png.flaticon.com/512/2922/2922510.png", "Écoles"), unsafe_allow_html=True)

with col6:
    st.markdown(partenaire("https://cdn-icons-png.flaticon.com/512/684/684908.png", "Mairie"), unsafe_allow_html=True)

