import streamlit as st
import streamlit.components.v1 as components
import datetime

# 1. Configuration de l'application
st.set_page_config(page_title="Nailis Journal", layout="centered")

# 2. Logique de pointage (Le moteur)
if 'pointage' not in st.session_state:
    st.session_state.pointage = False

def basculer_pointage():
    st.session_state.pointage = not st.session_state.pointage

# 3. Votre design HTML mis à jour avec des liens actifs
html_code = f"""
<!DOCTYPE html>
<html class="dark" lang="fr">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
    <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
    <style>
        body {{ font-family: 'Manrope', sans-serif; -webkit-tap-highlight-color: transparent; }}
        .primary-color {{ color: #135bec; }}
        .bg-primary {{ background-color: #135bec; }}
    </style>
</head>
<body class="bg-[#101622] text-white min-h-screen">
    <main class="max-w-md mx-auto pb-32">
        <div class="p-6 text-center">
            <h1 class="text-2xl font-extrabold tracking-tight">Journal Auto</h1>
            <p class="text-gray-400">Nailis Electric • {datetime.date.today().strftime('%d %B')}</p>
        </div>

        <div class="px-4 mb-6">
            <div class="grid grid-cols-4 gap-2 bg-slate-800/50 p-2 rounded-2xl border border-slate-800">
                <a href="tel:0612345678" class="flex flex-col items-center gap-1.5 py-2">
                    <div class="rounded-full bg-blue-500/10 p-3 text-blue-500"><span class="material-symbols-outlined">call</span></div>
                    <p class="text-[10px] font-bold uppercase opacity-70">Appeler</p>
                </a>
                <a href="sms:0612345678" class="flex flex-col items-center gap-1.5 py-2">
                    <div class="rounded-full bg-blue-500/10 p-3 text-blue-500"><span class="material-symbols-outlined">chat_bubble</span></div>
                    <p class="text-[10px] font-bold uppercase opacity-70">SMS</p>
                </a>
                <a href="mailto:contact@nailis.fr" class="flex flex-col items-center gap-1.5 py-2">
                    <div class="rounded-full bg-blue-500/10 p-3 text-blue-500"><span class="material-symbols-outlined">mail</span></div>
                    <p class="text-[10px] font-bold uppercase opacity-70">E-mail</p>
                </a>
                <a href="https://www.google.com/maps/dir/?api=1&destination=15+Rue+de+Rivoli+Paris" target="_blank" class="flex flex-col items-center gap-1.5 py-2">
                    <div class="rounded-full bg-blue-500/10 p-3 text-blue-500"><span class="material-symbols-outlined">map</span></div>
                    <p class="text-[10px] font-bold uppercase opacity-70">Trajet</p>
                </a>
            </div>
        </div>

        <div class="px-4 mb-6">
            <div class="bg-[#1c2537] p-5 rounded-xl border border-slate-800">
                <p class="text-gray-400 text-xs font-bold uppercase tracking-widest mb-1">Total Semaine</p>
                <p class="text-3xl font-bold text-white">38h 45m</p>
            </div>
        </div>

        <div class="px-4">
             <div class="flex flex-col gap-4">
                <div class="bg-slate-800/30 p-4 rounded-xl border border-slate-800">
                    <p class="font-bold">M. Jean Dupont</p>
                    <p class="text-sm text-gray-400">08:15 — 12:30</p>
                    <p class="text-blue-500 font-bold text-right">4h 15m</p>
                </div>
             </div>
        </div>
    </main>
</body>
</html>
"""

# 4. Affichage du design
components.html(html_code, height=600)

# 5. Le bouton de pointage réel de l'application
st.markdown("---")
label = "🛑 ARRÊTER LE POINTAGE" if st.session_state.pointage else "⏱️ DÉMARRER LE POINTAGE"
couleur = "secondary" if st.session_state.pointage else "primary"

if st.button(label, use_container_width=True, type=couleur):
    basculer_pointage()
    if st.session_state.pointage:
        st.success(f"Pointage démarré à {datetime.datetime.now().strftime('%H:%M')}")
    else:
        st.warning(f"Pointage arrêté à {datetime.datetime.now().strftime('%H:%M')}")