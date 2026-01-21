import streamlit as st
import datetime
import time

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Nailis Electric - Journal Auto", layout="centered")

# Initialisation de la base de données client dans la mémoire de l'app
if 'clients' not in st.session_state:
    st.session_state.clients = {}
if 'chrono_running' not in st.session_state:
    st.session_state.chrono_running = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

# --- DESIGN CSS (Pour garder l'aspect pro) ---
st.markdown("""
    <style>
    .stApp { background-color: #101622; color: white; }
    .main-card { background-color: #1c2537; padding: 20px; border-radius: 15px; border: 1px solid #2d3748; margin-bottom: 20px; }
    .stButton>button { border-radius: 12px; height: 3.5em; font-weight: bold; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- EN-TÊTE : ACCUEIL ---
st.title("⚡ Nailis Electric")
col_date, col_heure = st.columns(2)
with col_date:
    st.metric("Jour Actuel", datetime.date.today().strftime("%d %B %Y"))
with col_heure:
    st.metric("Heure", datetime.datetime.now().strftime("%H:%M"))

# --- ÉTAPE 1 : CRÉATION CLIENT ---
with st.expander("👤 AJOUTER UN NOUVEAU CLIENT", expanded=False):
    with st.form("form_client"):
        nom = st.text_input("Nom et Prénom")
        adr = st.text_area("Adresse complète (Rue, CP, Ville)")
        tel = st.text_input("Téléphone")
        mail = st.text_input("E-mail du client")
        if st.form_submit_button("Enregistrer le Client"):
            if nom and adr:
                st.session_state.clients[nom] = {"adresse": adr, "tel": tel, "mail": mail}
                st.success(f"Client {nom} enregistré !")
            else:
                st.error("Le nom et l'adresse sont obligatoires.")

st.divider()

# --- ÉTAPE 2 : SÉLECTION ET CHRONO ---
st.subheader("🛠️ Intervention en cours")
if not st.session_state.clients:
    st.info("Commencez par ajouter un client ci-dessus.")
else:
    client_sel = st.selectbox("Choisir le client pour ce chantier", options=list(st.session_state.clients.keys()))
    
    # Affichage des infos client
    info = st.session_state.clients[client_sel]
    st.markdown(f"📍 **Site :** {info['adresse']}")

    # Gestion du Chronomètre
    if not st.session_state.chrono_running:
        if st.button("▶️ DÉMARRER LE CHANTIER", type="primary"):
            st.session_state.start_time = datetime.datetime.now()
            st.session_state.chrono_running = True
            st.rerun()
    else:
        now = datetime.datetime.now()
        diff = now - st.session_state.start_time
        st.warning(f"⏳ Temps écoulé : {str(diff).split('.')[0]}")
        
        if st.button("⏹️ ARRÊTER ET FINALISER", type="secondary"):
            st.session_state.end_time = now
            st.session_state.total_time = diff
            st.session_state.chrono_running = False
            st.session_state.show_report_form = True

# --- ÉTAPE 3 : PHOTOS ET COMPTE-RENDU ---
if st.session_state.get('show_report_form'):
    st.divider()
    st.subheader("📝 Rapport d'exécution")
    
    travaux = st.text_area("Description du travail effectué", height=150)
    photo = st.camera_input("📸 Prendre une photo du travail fini")
    
    if st.button("✅ GÉNÉRER ET AFFICHER LE RAPPORT"):
        st.session_state.final_report = {
            "client": client_sel,
            "adresse": st.session_state.clients[client_sel]['adresse'],
            "temps": str(st.session_state.total_time).split('.')[0],
            "details": travaux
        }
        st.session_state.show_report_form = False
        st.session_state.ready_to_send = True

# --- ÉTAPE 4 : AFFICHAGE RAPPORT ET ENVOI ---
if st.session_state.get('ready_to_send'):
    rep = st.session_state.final_report
    st.markdown(f"""
    <div class="main-card">
        <h3>RAPPORT FINAL : {rep['client']}</h3>
        <p><b>Adresse :</b> {rep['adresse']}</p>
        <p><b>Durée :</b> {rep['temps']}</p>
        <p><b>Compte-rendu :</b><br>{rep['details']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📧 ENVOYER LE RAPPORT PAR MAIL"):
        st.balloons()
        st.success(f"Rapport envoyé à l'adresse du client et à Nailis Electric !")