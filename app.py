import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(page_title="Nailis Journal - Expert", layout="centered")

# --- INTERFACE DESIGN (Votre code HTML) ---
# (On garde votre variable html_code ici pour afficher le haut de l'app)
# components.html(html_code, height=600)

st.title("⚡ Gestion de Chantier")

# --- SECTION 1 : NOUVEAU CLIENT & ADRESSE ---
with st.expander("➕ Ajouter un nouveau client"):
    with st.form("form_client"):
        nom = st.text_input("Nom complet du client")
        adresse = st.text_area("Adresse complète du site")
        tel = st.text_input("Numéro de téléphone")
        submit = st.form_submit_button("Enregistrer le client")
        
        if submit:
            st.success(f"Client {nom} enregistré pour le site de {adresse}")

# --- SECTION 2 : PHOTOS DU TRAVAIL ---
st.subheader("📸 Suivi Photo")
photo_chantier = st.camera_input("Prendre une photo du travail exécuté")

if photo_chantier:
    st.image(photo_chantier, caption="Photo enregistrée dans le journal")
    # Ici, on pourrait ajouter un bouton pour envoyer la photo par mail ou sur un cloud

# --- SECTION 3 : ADRESSE ET LOCALISATION ---
st.subheader("📍 Localisation")
lieu = st.text_input("Rechercher une adresse", placeholder="Ex: 12 rue de la Paix, Paris")
if lieu:
    # Lien dynamique vers Google Maps pour le trajet
    url_maps = f"https://www.google.com/maps/search/?api=1&query={lieu.replace(' ', '+')}"
    st.link_button("🗺️ Lancer l'itinéraire", url_maps)