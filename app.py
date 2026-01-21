import streamlit as st
import streamlit.components.v1 as components

# 1. Configuration pour que l'app prenne tout l'écran mobile
st.set_page_config(page_title="Journal Auto", layout="centered", initial_sidebar_state="collapsed")

# 2. On cache les menus inutiles de Streamlit pour que ça ressemble à une vraie App
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {margin-top: -60px;}
    </style>
    """, unsafe_allow_html=True)

# 3. VOTRE CODE ORIGINAL (Je n'ai rien supprimé)
# J'ai juste ajouté des liens réels sur les icônes (tel:, sms:, etc.)
html_code = """
<!DOCTYPE html>
<html class="dark" lang="fr"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
<script id="tailwind-config">
        tailwind.config = {
            darkMode: "class",
            theme: {
                extend: {
                    colors: {
                        "primary": "#135bec",
                        "background-light": "#f6f6f8",
                        "background-dark": "#101622",
                    },
                    fontFamily: { "display": ["Manrope"] },
                    borderRadius: {"DEFAULT": "0.25rem", "lg": "0.5rem", "xl": "0.75rem", "full": "9999px"},
                },
            },
        }
    </script>
<style>
        .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
        body { -webkit-tap-highlight-color: transparent; min-height: 100dvh; }
</style>
</head>
<body class="bg-background-light dark:bg-background-dark font-display text-gray-900 dark:text-white">
<header class="sticky top-0 z-50 bg-background-light dark:bg-background-dark/95 backdrop-blur-md border-b border-gray-200 dark:border-gray-800">
<div class="flex items-center p-4 pb-3 justify-between max-w-md mx-auto">
<div class="flex size-10 items-center"><div class="rounded-full size-10 border-2 border-primary" style='background-image: url("https://www.w3schools.com/howto/img_avatar.png"); background-size: cover;'></div></div>
<div class="flex-1 px-4">
<h1 class="text-lg font-extrabold tracking-tight">Journal Auto</h1>
<p class="text-xs text-gray-500 font-medium">Semaine 43 • Octobre</p>
</div>
<div class="flex w-10 items-center justify-end"><span class="material-symbols-outlined">settings</span></div>
</div>
</header>
<main class="max-w-md mx-auto pb-24">
<div class="p-4"><div class="flex flex-wrap gap-3">
<div class="flex flex-1 flex-col gap-1 rounded-xl p-5 bg-white dark:bg-[#1c2537] border border-gray-100 dark:border-gray-800">
<p class="text-gray-500 text-xs font-semibold uppercase">Chantier</p>
<p class="text-2xl font-bold">38h 45m</p>
<p class="text-[#0bda5e] text-xs font-bold">+5%</p>
</div>
<div class="flex flex-1 flex-col gap-1 rounded-xl p-5 bg-white dark:bg-[#1c2537] border border-gray-100 dark:border-gray-800">
<p class="text-gray-500 text-xs font-semibold uppercase">Trajet</p>
<p class="text-2xl font-bold">4h 20m</p>
<p class="text-[#0bda5e] text-xs font-bold">-2%</p>
</div>
</div></div>
<div class="px-4 pt-4 flex justify-between items-end"><h3 class="text-xl font-extrabold">Mardi 24 Octobre</h3><span class="text-xs font-bold text-primary bg-primary/10 px-2 py-1 rounded">AUJOURD'HUI</span></div>
<div class="mt-4 px-4"><div class="grid grid-cols-[40px_1fr] gap-x-2">
<div class="flex flex-col items-center"><div class="size-10 flex items-center justify-center rounded-full bg-primary/10 text-primary"><span class="material-symbols-outlined">home_repair_service</span></div><div class="w-[2px] bg-gray-200 dark:bg-gray-800 h-10 grow"></div></div>
<div class="flex flex-col pb-6 pt-1"><div class="flex justify-between items-start"><div><p class="font-bold">M. Jean Dupont</p><p class="text-gray-500 text-sm">12 Rue de la Paix, Paris</p></div><div class="text-right"><p class="font-bold">4h 15m</p></div></div><p class="text-primary text-sm font-semibold mt-2">08:15 — 12:30</p></div>
</div></div>

<div class="px-4 mb-6">
<div class="grid grid-cols-4 gap-2 bg-white dark:bg-slate-800/50 p-2 rounded-2xl border border-slate-100 dark:border-slate-800">
<a href="tel:0600000000" class="flex flex-col items-center gap-1.5 py-2"><div class="rounded-full bg-primary/10 p-3 text-primary"><span class="material-symbols-outlined">call</span></div><p class="text-[11px] font-bold uppercase opacity-70">Appeler</p></a>
<a href="sms:0600000000" class="flex flex-col items-center gap-1.5 py-2"><div class="rounded-full bg-primary/10 p-3 text-primary"><span class="material-symbols-outlined">chat_bubble</span></div><p class="text-[11px] font-bold uppercase opacity-70">SMS</p></a>
<a href="mailto:contact@test.com" class="flex flex-col items-center gap-1.5 py-2"><div class="rounded-full bg-primary/10 p-3 text-primary"><span class="material-symbols-outlined">mail</span></div><p class="text-[11px] font-bold uppercase opacity-70">E-mail</p></a>
<a href="https://www.google.com/maps" target="_blank" class="flex flex-col items-center gap-1.5 py-2"><div class="rounded-full bg-primary/10 p-3 text-primary"><span class="material-symbols-outlined">map</span></div><p class="text-[11px] font-bold uppercase opacity-70">Trajet</p></a>
</div>
</div>
</main>

<div class="fixed bottom-24 right-6">
<button onclick="alert('Pointage démarré !')" class="bg-primary text-white size-14 rounded-full shadow-lg flex items-center justify-center active:scale-95 transition-transform"><span class="material-symbols-outlined text-3xl">add</span></button>
</div>

<nav class="fixed bottom-0 left-0 right-0 bg-white/80 dark:bg-[#101622]/80 backdrop-blur-xl border-t border-gray-200 dark:border-gray-800 pb-6 pt-2">
<div class="max-w-md mx-auto flex justify-around items-center">
<button class="flex flex-col items-center gap-1 text-primary"><span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">calendar_today</span><span class="text-[10px] font-bold">Journal</span></button>
<button class="flex flex-col items-center gap-1 text-gray-400"><span class="material-symbols-outlined">map</span><span class="text-[10px] font-bold">Chantiers</span></button>
<button class="flex flex-col items-center gap-1 text-gray-400"><span class="material-symbols-outlined">group</span><span class="text-[10px] font-bold">Clients</span></button>
<button class="flex flex-col items-center gap-1 text-gray-400"><span class="material-symbols-outlined">analytics</span><span class="text-[10px] font-bold">Stats</span></button>
</div>
</nav>
</body></html>
"""

# 4. Affichage du code HTML (On met une grande hauteur pour que tout soit visible)
components.html(html_code, height=1200, scrolling=True)