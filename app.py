import streamlit as st
import streamlit.components.v1 as components

# Configuration de la page pour mobile
st.set_page_config(page_title="Journal Auto", layout="centered")

# On stocke votre code HTML dans une variable
html_code = """
<!DOCTYPE html>
... <!DOCTYPE html>

<html class="dark" lang="fr"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Journal des Heures Auto</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
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
                    fontFamily: {
                        "display": ["Manrope"]
                    },
                    borderRadius: {"DEFAULT": "0.25rem", "lg": "0.5rem", "xl": "0.75rem", "full": "9999px"},
                },
            },
        }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        body {
            -webkit-tap-highlight-color: transparent;
        }
    </style>
<style>
    body {
      min-height: max(884px, 100dvh);
    }
  </style>
  </head>
<body class="bg-background-light dark:bg-background-dark font-display text-gray-900 dark:text-white min-h-screen">
<!-- Top Navigation Bar -->
<header class="sticky top-0 z-50 bg-background-light dark:bg-background-dark/95 backdrop-blur-md border-b border-gray-200 dark:border-gray-800">
<div class="flex items-center p-4 pb-3 justify-between max-w-md mx-auto">
<div class="flex size-10 shrink-0 items-center">
<div class="bg-center bg-no-repeat aspect-square bg-cover rounded-full size-10 border-2 border-primary" data-alt="Photo de profil de l'artisan" style='background-image: url("https://lh3.googleusercontent.com/aida-public/AB6AXuAAjIpu9qCAoQQ8PECGb8K8UKOOctcw37t6w0bvJmaFnqPyR_UX0qI-TPFrSRvTyyi7o1KkxmFlRD_hjKw_dyZE2Yujv5kaNsyBnEQPdtdOP0i2E9jlLRSQBcbiyLh_C8avncd-YwJPmNVZbQzEms9LKlQLRr3-atbuNC7ofbyO4xFhOK7viCE2HApuySW7kq5IR3e-04S9AzIQWd8Sqab6Db1ufTEmFudaUoSs96J6Xy9hf00IInhZFmEqwKgrYSe7hQd7ewGC1bI9");'>
</div>
</div>
<div class="flex-1 px-4">
<h1 class="text-gray-900 dark:text-white text-lg font-extrabold leading-tight tracking-tight">Journal Auto</h1>
<p class="text-xs text-gray-500 dark:text-gray-400 font-medium">Semaine 43 • Octobre</p>
</div>
<div class="flex w-10 items-center justify-end">
<button class="flex items-center justify-center rounded-full size-10 bg-gray-100 dark:bg-gray-800 text-gray-600 dark:text-gray-300">
<span class="material-symbols-outlined">settings</span>
</button>
</div>
</div>
</header>
<main class="max-w-md mx-auto pb-24">
<!-- Weekly Stats Summary -->
<div class="p-4">
<div class="flex flex-wrap gap-3">
<div class="flex min-w-[140px] flex-1 flex-col gap-1 rounded-xl p-5 bg-white dark:bg-[#1c2537] shadow-sm border border-gray-100 dark:border-gray-800">
<div class="flex items-center gap-2 mb-1">
<span class="material-symbols-outlined text-primary text-sm">construction</span>
<p class="text-gray-500 dark:text-gray-400 text-xs font-semibold uppercase tracking-wider">Chantier</p>
</div>
<p class="text-gray-900 dark:text-white tracking-tight text-2xl font-bold leading-tight">38h 45m</p>
<div class="flex items-center gap-1">
<span class="material-symbols-outlined text-[#0bda5e] text-xs">trending_up</span>
<p class="text-[#0bda5e] text-xs font-bold leading-normal">+5% vs sem. dernière</p>
</div>
</div>
<div class="flex min-w-[140px] flex-1 flex-col gap-1 rounded-xl p-5 bg-white dark:bg-[#1c2537] shadow-sm border border-gray-100 dark:border-gray-800">
<div class="flex items-center gap-2 mb-1">
<span class="material-symbols-outlined text-gray-400 text-sm">directions_car</span>
<p class="text-gray-500 dark:text-gray-400 text-xs font-semibold uppercase tracking-wider">Trajet</p>
</div>
<p class="text-gray-900 dark:text-white tracking-tight text-2xl font-bold leading-tight">4h 20m</p>
<div class="flex items-center gap-1">
<span class="material-symbols-outlined text-[#0bda5e] text-xs">trending_down</span>
<p class="text-[#0bda5e] text-xs font-bold leading-normal">-2% vs sem. dernière</p>
</div>
</div>
</div>
</div>
<!-- Section Header: Today -->
<div class="px-4 pt-4 flex justify-between items-end">
<h3 class="text-gray-900 dark:text-white text-xl font-extrabold tracking-tight">Mardi 24 Octobre</h3>
<span class="text-xs font-bold text-primary bg-primary/10 px-2 py-1 rounded">AUJOURD'HUI</span>
</div>
<!-- Timeline Container -->
<div class="mt-4 px-4">
<div class="grid grid-cols-[40px_1fr] gap-x-2">
<!-- Timeline: Entry 1 -->
<div class="flex flex-col items-center">
<div class="size-10 flex items-center justify-center rounded-full bg-primary/10 text-primary">
<span class="material-symbols-outlined">home_repair_service</span>
</div>
<div class="w-[2px] bg-gray-200 dark:bg-gray-800 h-10 grow"></div>
</div>
<div class="flex flex-col pb-6 pt-1">
<div class="flex justify-between items-start">
<div>
<p class="text-gray-900 dark:text-white text-base font-bold leading-none">M. Jean Dupont</p>
<p class="text-gray-500 dark:text-gray-400 text-sm mt-1 flex items-center gap-1">
<span class="material-symbols-outlined text-xs">location_on</span>
                                12 Rue de la Paix, Paris
                            </p>
</div>
<div class="text-right">
<p class="text-gray-900 dark:text-white text-base font-bold">4h 15m</p>
<p class="text-gray-400 text-[10px] font-bold uppercase">Automatisé</p>
</div>
</div>
<p class="text-primary text-sm font-semibold mt-2">08:15 — 12:30</p>
</div>
<!-- Timeline: Travel -->
<div class="flex flex-col items-center">
<div class="w-[2px] bg-gray-200 dark:bg-gray-800 h-4"></div>
<div class="size-8 flex items-center justify-center rounded-full bg-gray-100 dark:bg-gray-800 text-gray-500">
<span class="material-symbols-outlined text-lg">directions_car</span>
</div>
<div class="w-[2px] bg-gray-200 dark:bg-gray-800 h-4 grow"></div>
</div>
<div class="flex items-center py-2">
<div class="bg-gray-50 dark:bg-gray-800/50 rounded-lg px-3 py-2 border border-gray-100 dark:border-gray-800 w-full flex justify-between items-center">
<span class="text-gray-500 dark:text-gray-400 text-sm font-medium">Trajet vers prochain chantier</span>
<span class="text-gray-900 dark:text-white text-sm font-bold">25 min</span>
</div>
</div>
<!-- Timeline: Entry 2 -->
<div class="flex flex-col items-center">
<div class="w-[2px] bg-gray-200 dark:bg-gray-800 h-4"></div>
<div class="size-10 flex items-center justify-center rounded-full bg-primary/10 text-primary">
<span class="material-symbols-outlined">home_repair_service</span>
</div>
<div class="w-[2px] bg-gray-200 dark:bg-gray-800 h-8 grow"></div>
</div>
<div class="flex flex-col pb-8 pt-1">
<div class="flex justify-between items-start">
<div>
<p class="text-gray-900 dark:text-white text-base font-bold leading-none">Mme Marie Martin</p>
<p class="text-gray-500 dark:text-gray-400 text-sm mt-1 flex items-center gap-1">
<span class="material-symbols-outlined text-xs">location_on</span>
                                45 Avenue Foch, Paris
                            </p>
</div>
<div class="text-right">
<p class="text-gray-900 dark:text-white text-base font-bold">3h 45m</p>
<p class="text-gray-400 text-[10px] font-bold uppercase">Automatisé</p>
</div>
</div>
<p class="text-primary text-sm font-semibold mt-2">13:45 — 17:30</p>
</div>
</div>
</div>
<!-- Section Header: Yesterday -->
<div class="px-4 pt-4 border-t border-gray-100 dark:border-gray-800">
<h3 class="text-gray-900 dark:text-white text-xl font-extrabold tracking-tight">Lundi 23 Octobre</h3>
</div>
<div class="mt-4 px-4">
<div class="grid grid-cols-[40px_1fr] gap-x-2">
<!-- Timeline: Entry 3 -->
<div class="flex flex-col items-center">
<div class="size-10 flex items-center justify-center rounded-full bg-primary/10 text-primary">
<span class="material-symbols-outlined">home_repair_service</span>
</div>
<div class="w-[2px] bg-gray-200 dark:bg-gray-800 h-full grow"></div>
</div>
<div class="flex flex-col pb-6 pt-1">
<div class="flex justify-between items-start">
<div>
<p class="text-gray-900 dark:text-white text-base font-bold leading-none">Boulangerie L'Artisan</p>
<p class="text-gray-500 dark:text-gray-400 text-sm mt-1 flex items-center gap-1">
<span class="material-symbols-outlined text-xs">location_on</span>
                                3 Place de la Mairie, Lille
                            </p>
</div>
<div class="text-right">
<p class="text-gray-900 dark:text-white text-base font-bold">8h 00m</p>
<p class="text-orange-500 text-[10px] font-bold uppercase">Corrigé</p>
</div>
</div>
<p class="text-primary text-sm font-semibold mt-2">08:00 — 17:00 (Pause incl.)</p>
</div>
</div>
</div>
</main>
<!-- Floating Action Button -->
<div class="fixed bottom-24 right-6">
<button class="bg-primary text-white size-14 rounded-full shadow-lg shadow-primary/40 flex items-center justify-center active:scale-95 transition-transform">
<span class="material-symbols-outlined text-3xl">add</span>
</button>
</div>
<!-- Bottom Navigation Bar (iOS Style) -->
<nav class="fixed bottom-0 left-0 right-0 bg-white/80 dark:bg-[#101622]/80 backdrop-blur-xl border-t border-gray-200 dark:border-gray-800 pb-6 pt-2">
<div class="max-w-md mx-auto flex justify-around items-center">
<button class="flex flex-col items-center gap-1 text-primary">
<span class="material-symbols-outlined" style="font-variation-settings: 'FILL' 1;">calendar_today</span>
<span class="text-[10px] font-bold">Journal</span>
</button>
<button class="flex flex-col items-center gap-1 text-gray-400 dark:text-gray-500">
<span class="material-symbols-outlined">map</span>
<span class="text-[10px] font-bold">Chantiers</span>
</button>
<button class="flex flex-col items-center gap-1 text-gray-400 dark:text-gray-500">
<span class="material-symbols-outlined">group</span>
<span class="text-[10px] font-bold">Clients</span>
</button>
<button class="flex flex-col items-center gap-1 text-gray-400 dark:text-gray-500">
<span class="material-symbols-outlined">analytics</span>
<span class="text-[10px] font-bold">Stats</span>
</button>
</div>
</nav>
</body></html> ...
</html>
"""

# On demande à Streamlit d'afficher votre design
components.html(html_code, height=900, scrolling=True)