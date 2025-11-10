import streamlit as st

# Inject custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
        padding: 2rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1, h2, h3 {
        color: #2c3e50;
    }
    .activity-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #3498db;
        margin: 1.5rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #28a745;
        color: #155724;
    }
    .error-box {
        background-color: #f8d7da;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #dc3545;
        color: #721c24;
    }
    .info-box {
        background-color: #d1ecf1;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #17a2b8;
        color: #0c5460;
    }
    .stButton>button {
        background-color: #3498db;
        color: white;
        border: none;
        padding: 0.6rem 1.5rem;
        border-radius: 6px;
        font-size: 1em;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "current_slide" not in st.session_state:
    st.session_state.current_slide = 1

def go_to_slide(n):
    st.session_state.current_slide = n

# --- SLIDE 1 : Accueil ---
if st.session_state.current_slide == 1:
    st.title("🔧 What Is Quality? — 5 Activities")
    st.subheader("Simple, Clear, Engineering-Ready")
    st.write("""
    Bienvenue dans ce workshop interactif.  
    5 activités courtes pour comprendre la qualité comme un ingénieur.
    """)
    st.info("💡 Chaque activité dure 5 à 7 minutes. Prêt à commencer ?")
    if st.button("➡️ Commencer les activités"):
        go_to_slide(2)

# --- SLIDE 2 : Activité 1 ---
elif st.session_state.current_slide == 2:
    st.title("🎯 Activité 1 : C’est de la qualité ? Oui ou Non ?")
    st.write("Lisez la situation. Répondez : **Oui** ou **Non**.")

    situations = [
        "Je rends mon rapport à 9h01, alors que la deadline est 9h00.",
        "Mon code fonctionne… mais il plante si on le lance deux fois.",
        "La pièce que j’ai usinée est à 10.02 mm, et la tolérance est 10.00 ± 0.05 mm.",
        "J’ai fait un beau schéma, mais j’ai oublié la valeur du courant.",
        "Le client a dit : “Fais-le vite.” Je l’ai fait en 1 jour, mais il ne marche pas."
    ]

    answers = []
    for i, s in enumerate(situations):
        st.write(f"**{i+1}. {s}**")
        choice = st.radio("", ["", "✅ Oui", "❌ Non"], key=f"act1_{i}")
        answers.append(choice)

    if st.button("Vérifier les réponses"):
        correct = ["❌ Non", "❌ Non", "✅ Oui", "❌ Non", "❌ Non"]
        all_correct = True
        for i, ans in enumerate(answers):
            if ans != correct[i]:
                all_correct = False
                break

        if all_correct:
            st.success("✅ Parfait ! Vous comprenez que la qualité = respect des exigences.")
        else:
            st.warning("❌ Certaines réponses sont incorrectes. Rappelez-vous : qualité = conformité, pas apparence.")
            for i in range(len(situations)):
                st.write(f"{i+1}. {situations[i]} → **{correct[i]}**")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Retour"):
            go_to_slide(1)
    with col2:
        if st.button("➡️ Activité 2"):
            go_to_slide(3)

# --- SLIDE 3 : Activité 2 ---
elif st.session_state.current_slide == 3:
    st.title("🎯 Activité 2 : Qui est mon client ?")
    st.write("Imaginez que vous avez conçu :")
    projet = st.selectbox("Sélectionnez un projet :", [
        "Un capteur de température",
        "Un logiciel de gestion de données",
        "Une pièce mécanique pour un robot",
        "Un système de freinage",
        "Un capteur de vitesse"
    ])
    st.write(f"**Question :** Qui est le client de votre {projet.lower()} ?")
    client = st.text_input("Entrez un client (autre que le professeur) :")

    if client:
        st.success(f"✅ Excellent ! Le {client} est votre client. Votre qualité, c’est ce qu’il attend de vous.")

    st.write("**Souvenez-vous :**")
    st.info("""
    - Le technicien qui monte votre pièce  
    - L’ingénieur qui utilise vos données  
    - Le client final  
    → Tous sont vos clients.
    """)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Retour"):
            go_to_slide(2)
    with col2:
        if st.button("➡️ Activité 3"):
            go_to_slide(4)

# --- SLIDE 4 : Activité 3 ---
elif st.session_state.current_slide == 4:
    st.title("🎯 Activité 3 : Trouve le mot manquant")
    st.write("Complétez cette phrase :")
    st.write("“La qualité, c’est quand [_____] est respecté(e).”")

    reponse = st.text_input("Entrez votre mot ou phrase :")

    if reponse:
        st.success(f"✅ Bien ! Vous avez dit : *“{reponse}”*")
        st.info("La meilleure réponse : *“Les exigences”* ou *“La spécification”*.")

    st.write("**Souvenez-vous :**")
    st.info("La qualité, ce n’est pas ce qu’on pense être bien. C’est ce qui est convenu.")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Retour"):
            go_to_slide(3)
    with col2:
        if st.button("➡️ Activité 4"):
            go_to_slide(5)

# --- SLIDE 5 : Activité 4 ---
elif st.session_state.current_slide == 5:
    st.title("🎯 Activité 4 : Défaut ou pas ?")
    st.write("Dites si c’est un **défaut** ou **pas un défaut**.")

    situations = [
        "Le logo sur le boîtier est un peu décalé.",
        "Le bouton poussoir ne répond pas la première fois qu’on l’appuie.",
        "Le manuel est en anglais, mais le client est français.",
        "Le logiciel prend 2 secondes pour démarrer (le cahier demande ≤ 1s).",
        "La couleur du boîtier est bleu au lieu de gris — mais ça ne change rien au fonctionnement."
    ]

    correct = ["pas", "defaut", "defaut", "defaut", "pas"]
    user_answers = []

    for i, s in enumerate(situations):
        st.write(f"**{i+1}. {s}**")
        choice = st.radio("", ["", "✅ Pas un défaut", "❌ Défaut"], key=f"act4_{i}")
        if "pas" in choice.lower():
            user_answers.append("pas")
        elif "defaut" in choice.lower():
            user_answers.append("defaut")
        else:
            user_answers.append("")

    if st.button("Vérifier les réponses"):
        all_correct = True
        for i, ans in enumerate(user_answers):
            if ans != correct[i]:
                all_correct = False
                break

        if all_correct:
            st.success("✅ Parfait ! Vous comprenez que la qualité = conformité aux exigences.")
        else:
            st.warning("❌ Certaines réponses sont incorrectes. Rappelez-vous : défaut = non-conformité.")
            for i in range(len(situations)):
                rep = "✅ Pas un défaut" if correct[i] == "pas" else "❌ Défaut"
                st.write(f"{i+1}. {situations[i]} → **{rep}**")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Retour"):
            go_to_slide(4)
    with col2:
        if st.button("➡️ Activité 5"):
            go_to_slide(6)

# --- SLIDE 6 : Activité 5 ---
elif st.session_state.current_slide == 6:
    st.title("🎯 Activité 5 : La règle du 1 mot")
    st.write("Quel mot, en un seul, définit la **qualité** selon vous ?")
    mot = st.text_input("Entrez votre mot :")

    if mot:
        st.success(f"✅ Vous avez dit : **{mot}**")
        st.info("Mots fréquents : **Conformité**, **Fiabilité**, **Exigence**, **Règle**, **Contrôle**.")
        st.write("➡️ **Souvenez-vous** : La qualité, c’est **faire ce qui a été convenu — pas ce qu’on veut faire.**")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("⬅️ Retour"):
            go_to_slide(5)
    with col2:
        if st.button("➡️ Résumé Final"):
            go_to_slide(7)

# --- SLIDE 7 : Résumé Final ---
elif st.session_state.current_slide == 7:
    st.title("✅ Résumé Final : What Is Quality?")
    st.write("Vous avez maintenant compris que :")

    st.markdown("""
    - **La qualité = respecter les exigences.**  
    - **Un défaut = non-conformité à une exigence.**  
    - **Votre client = toute personne qui reçoit votre travail.**  
    - **La qualité se mesure — pas seulement se ressent.**  
    - **La qualité, c’est votre responsabilité.**
    """)

    st.markdown('<div class="info-box">', unsafe_allow_html=True)
    st.write("""
    💡 **Phrase à retenir** :  
    > *“La qualité, ce n’est pas ‘ça marche’.  
    C’est ‘ça marche comme convenu — chaque fois, pour tous les clients.’”*
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    st.balloons()
    st.success("🎉 Félicitations ! Vous avez terminé le workshop interactif sur la qualité.")
    st.write("Maintenant, vous pouvez l’appliquer dans vos projets et stages.")

    if st.button("🔄 Recommencer le workshop"):
        go_to_slide(1)
