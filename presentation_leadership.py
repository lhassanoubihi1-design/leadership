import streamlit as streamlit_interface
import random

streamlit_interface.set_page_config(
    page_title="Leadership Pro – Expérience Immersive",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================
# CSS MODERNE SANS ERREURS
# ==============================
streamlit_interface.markdown("""
<style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body, html {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background: #fafbff;
        color: #1e293b;
        line-height: 1.6;
    }
    h1 {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-align: center;
        margin: 1.8rem 0;
    }
    h2 {
        font-size: 1.9rem;
        font-weight: 700;
        color: #3730a3;
        margin: 1.6rem 0 1.1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e0e7ff;
    }
    h3 {
        font-size: 1.5rem;
        font-weight: 600;
        color: #4f46e5;
        margin: 1.3rem 0 0.8rem;
    }
    .modern-card {
        background: white;
        border-radius: 16px;
        padding: 1.6rem;
        margin: 1.4rem 0;
        box-shadow: 0 4px 20px rgba(79, 70, 229, 0.08);
        border: 1px solid #f0f4ff;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .modern-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 6px 25px rgba(79, 70, 229, 0.15);
    }
    .example-box {
        background: #f0fdf4;
        border-left: 4px solid #10b981;
        padding: 1.2rem;
        margin: 1.2rem 0;
        border-radius: 0 10px 10px 0;
        font-style: italic;
        line-height: 1.6;
    }
    .example-box strong {
        color: #059669;
    }
    .streamlit_interfaceButton > button {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.8rem 1.8rem;
        font-weight: 600;
        font-size: 1.05rem;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
        transition: all 0.25s ease;
    }
    .streamlit_interfaceButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(79, 70, 229, 0.4);
    }
    .streamlit_interfaceTabs [data-baseweb="tab-list"] {
        gap: 8px;
        padding: 0 0 1.2rem;
        overflow-x: auto;
    }
    .streamlit_interfaceTabs [data-baseweb="tab"] {
        height: 48px;
        background: #f0f4ff;
        border-radius: 14px 14px 0 0;
        color: #4f46e5;
        font-weight: 600;
        font-size: 0.95rem;
        padding: 0 20px;
    }
    .streamlit_interfaceTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        color: white;
    }
    .quote-card {
        font-style: italic;
        color: #4b5563;
        padding: 1.2rem;
        background: #f8fafc;
        border-radius: 14px;
        margin: 1.2rem 0;
        border-left: 4px solid #4f46e5;
        position: relative;
        line-height: 1.6;
    }
    .quote-card::before {
        content: '"';
        position: absolute;
        top: -15px;
        left: 10px;
        font-size: 3.5rem;
        color: #e0e7ff;
        font-family: Georgia, serif;
    }
    .video-link {
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        background: #f0f4ff;
        color: #4f46e5;
        padding: 0.7rem 1.3rem;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        margin: 0.5rem 0;
        transition: all 0.2s;
    }
    .video-link:hover {
        background: #e0e7ff;
        transform: translateX(4px);
    }
    .content-paragraph {
        margin: 1rem 0;
        line-height: 1.7;
    }
    .content-list {
        padding-left: 1.5rem;
        margin: 1.2rem 0;
    }
    .content-list li {
        margin: 0.8rem 0;
        line-height: 1.6;
    }
    .quiz-question {
        background: #f8fafc;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 4px solid #4f46e5;
    }
    .quiz-section {
        background: linear-gradient(135deg, #fef7ff, #faf5ff);
        padding: 2rem;
        border-radius: 16px;
        margin: 2rem 0;
        border: 2px solid #e9d5ff;
    }
    .evaluation-box {
        background: linear-gradient(135deg, #eff6ff, #f0f9ff);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 4px solid #3b82f6;
    }
    .theory-box {
        background: linear-gradient(135deg, #fef7ff, #faf5ff);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 4px solid #8b5cf6;
    }
    .comparison-table {
        width: 100%;
        border-collapse: collapse;
        margin: 1.5rem 0;
    }
    .comparison-table th, .comparison-table td {
        padding: 1rem;
        text-align: left;
        border-bottom: 1px solid #e2e8f0;
    }
    .comparison-table th {
        background: #4f46e5;
        color: white;
        font-weight: 600;
    }
    .comparison-table tr:nth-child(even) {
        background: #f8fafc;
    }
    .test-section {
        background: linear-gradient(135deg, #fff7ed, #fffbeb);
        padding: 2rem;
        border-radius: 16px;
        margin: 2rem 0;
        border: 2px solid #fed7aa;
    }
    .conseil-box {
        background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
        padding: 1.2rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #0ea5e9;
    }
    .color-red { 
        background: linear-gradient(135deg, #fee2e2, #fecaca); 
        border-left: 4px solid #dc2626; 
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s;
    }
    .color-yellow { 
        background: linear-gradient(135deg, #fef3c7, #fde68a); 
        border-left: 4px solid #d97706; 
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s;
    }
    .color-green { 
        background: linear-gradient(135deg, #dcfce7, #bbf7d0); 
        border-left: 4px solid #16a34a; 
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s;
    }
    .color-blue { 
        background: linear-gradient(135deg, #dbeafe, #bfdbfe); 
        border-left: 4px solid #2563eb; 
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        cursor: pointer;
        transition: all 0.2s;
    }
    .color-option:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .result-red { 
        background: linear-gradient(135deg, #fef2f2, #fee2e2); 
        border: 2px solid #dc2626; 
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
    }
    .result-yellow { 
        background: linear-gradient(135deg, #fffbeb, #fef3c7); 
        border: 2px solid #d97706; 
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
    }
    .result-green { 
        background: linear-gradient(135deg, #f0fdf4, #dcfce7); 
        border: 2px solid #16a34a; 
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
    }
    .result-blue { 
        background: linear-gradient(135deg, #eff6ff, #dbeafe); 
        border: 2px solid #2563eb; 
        border-radius: 16px;
        padding: 2rem;
        margin: 1rem 0;
    }
    .leader-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border-left: 5px solid;
        transition: transform 0.3s ease;
    }
    .leader-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    .disc-score-box {
        text-align: center;
        padding: 0.8rem;
        border-radius: 8px;
        margin: 0.2rem;
        font-weight: 600;
    }
    .disc-score-red { background: #fee2e2; border: 2px solid #dc2626; color: #dc2626; }
    .disc-score-yellow { background: #fef3c7; border: 2px solid #d97706; color: #d97706; }
    .disc-score-green { background: #dcfce7; border: 2px solid #16a34a; color: #16a34a; }
    .disc-score-blue { background: #dbeafe; border: 2px solid #2563eb; color: #2563eb; }
    .disc-score-dominant { 
        box-shadow: 0 0 0 3px rgba(220, 38, 38, 0.3); 
        transform: scale(1.05);
    }
    .forces-defis-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 1.5rem;
        margin: 1.5rem 0;
    }
    .forces-box {
        background: #f0fdf4;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #10b981;
    }
    .defis-box {
        background: #fef2f2;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #ef4444;
    }
    .roleplay-card {
        background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
        border: 2px solid #0ea5e9;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    .roleplay-scenario {
        background: white;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
        border-left: 4px solid #8b5cf6;
    }
    .timer-box {
        background: linear-gradient(135deg, #fffbeb, #fef3c7);
        border: 2px solid #d97706;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 1rem 0;
    }
    #MainMenu, footer, header { visibility: hidden !important; }
</style>
""", unsafe_allow_html=True)

streamlit_interface.title("✨ Leadership & Styles de Leadership")
streamlit_interface.markdown("<div style='text-align:center; margin-bottom:2rem; color:#64748b;'>Formation complète avec 8 activités express + 5 activités de clôture</div>", unsafe_allow_html=True)

# Structure corrigée sans chevauchement
slide_names = [
    # ACTIVITÉS EXPRESS (8)
    "0. Activité 1: Le Leader en 3 Mots", 
    "1. Test DISC Leadership", 
    "2. Activité 2: Reformulation en Duo", 
    "3. Introduction", 
    "4. Activité 3: Post-it de Réflexion", 
    "5. Définitions", 
    "6. Activité 4: Question Puissante", 
    "7. Leadership vs Management", 
    "8. Activité 5: Écoute Active Rapide", 
    "9. Leadership vs Commandement", 
    "10. Activité 6: Tour de Table des Qualités", 
    "11. Théories X et Y", 
    "12. Activité 7: Mini-Jeu de Rôle : Vision", 
    
    # STYLES DE LEADERSHIP (10)
    "13. Style Visionnaire",
    "14. Style Coaching", 
    "15. Style Affiliatif",
    "16. Style Démocratique",
    "17. Style Directif",
    "18. Style Pace-setter",
    "19. Style Transformationnel",
    "20. Style Transactionnel", 
    "21. Style Authentique",
    "22. Style Serviteur",
    
    # ACTIVITÉ 8
    "23. Activité 8: Carte Mentale Express",
    
    # CONTENU THÉORIQUE
    "24. Leadership Situationnel",
    "25. Leadership Laissez-faire", 
    "26. Jeu de Rôle Principal",
    "27. Compétences Clés", 
    "28. Intelligence Émotionnelle",
    "29. Études de Cas",
    "30. Quiz 1 - Fondamentaux",
    "31. Quiz 2 - Styles Avancés",
    "32. Synthèse",
    "33. Secteurs d'Application", 
    "34. Erreurs Courantes",
    "35. Conseils Pratiques",
    "36. Ressources",
    
    # ACTIVITÉS DE CLÔTURE (5)
    "37. Activité 9: Mot de la Fin",
    "38. Activité 10: Action Immédiate", 
    "39. Activité 11: Gratitude Leader",
    "40. Activité 12: Retour d'Expérience",
    "41. Activité 13: Applaudissement Tournant"
]

onglets = streamlit_interface.tabs(slide_names)

# ==============================
# ACTIVITÉ EXPRESS 1 : LE LEADER EN 3 MOTS (Slide 0)
# ==============================
with onglets[0]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 1/13 : Le Leader en 3 Mots</h2>
    <p class="content-paragraph">Un icebreaker pour activer les représentations.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="modern-card">
        <h3>💬 Consigne</h3>
        <p><strong>Durée :</strong> 5 minutes</p>
        <p>Chacun écrit <strong>3 mots</strong> qui définissent le leadership pour lui.</p>
        <p><strong>Partage :</strong> Tour de table rapide (1 mot par personne).</p>
        <div class="example-box">
            💡 <strong>Exemple :</strong> Inspiration, Confiance, Vision
        </div>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Créer un climat d'échange, activer les connaissances préexistantes.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# TEST DE LEADERSHIP DISC AVEC COULEURS ET 10 STYLES (Slide 1)
# ==============================
with onglets[1]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎨 Test de Leadership DISC</h2>
    <p class="content-paragraph">Découvrez votre style de leadership dominant avec ce test basé sur les 4 couleurs du modèle DISC</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Questions avec options colorées
    questions_disc = [
        {
            "question": "Face à un nouveau projet, je préfère :",
            "options": [
                {"text": "Prendre rapidement le leadership et fixer les objectifs", "color": "red"},
                {"text": "Motiver l'équipe avec une vision inspirante", "color": "yellow"},
                {"text": "Écouter les idées de chacun avant de décider", "color": "green"},
                {"text": "Analyser en détail tous les aspects du projet", "color": "blue"}
            ]
        },
        {
            "question": "En réunion, je suis plutôt :",
            "options": [
                {"text": "Direct et orienté résultats", "color": "red"},
                {"text": "Enthousiaste et communicatif", "color": "yellow"},
                {"text": "À l'écoute et conciliant", "color": "green"},
                {"text": "Précis et méthodique", "color": "blue"}
            ]
        },
        {
            "question": "Quand je dois prendre une décision difficile :",
            "options": [
                {"text": "Je prends rapidement ma décision et j'assume", "color": "red"},
                {"text": "Je consulte rapidement quelques personnes de confiance", "color": "yellow"},
                {"text": "Je cherche le consensus avec toute l'équipe", "color": "green"},
                {"text": "J'analyse soigneusement tous les scénarios", "color": "blue"}
            ]
        },
        {
            "question": "Mon approche face aux conflits :",
            "options": [
                {"text": "Je confronte directement le problème", "color": "red"},
                {"text": "Je cherche à désamorcer par la communication", "color": "yellow"},
                {"text": "Je privilégie l'harmonie et la compréhension", "color": "green"},
                {"text": "J'analyse les faits objectivement", "color": "blue"}
            ]
        },
        {
            "question": "Ce qui me motive le plus :",
            "options": [
                {"text": "Atteindre des objectifs ambitieux", "color": "red"},
                {"text": "Inspirer et être reconnu", "color": "yellow"},
                {"text": "Créer des relations harmonieuses", "color": "green"},
                {"text": "Réussir grâce à l'expertise et la précision", "color": "blue"}
            ]
        },
        {
            "question": "Face à l'échec :",
            "options": [
                {"text": "J'analyse rapidement ce qui n'a pas marché et je passe à autre chose", "color": "red"},
                {"text": "Je partage l'expérience avec l'équipe pour rebondir", "color": "yellow"},
                {"text": "Je prends soin du moral de l'équipe", "color": "green"},
                {"text": "J'étudie en profondeur les causes de l'échec", "color": "blue"}
            ]
        },
        {
            "question": "Quand je délègue :",
            "options": [
                {"text": "Je donne l'objectif final et je laisse faire", "color": "red"},
                {"text": "J'explique la vision globale et je motive", "color": "yellow"},
                {"text": "Je vérifie que la personne se sent à l'aise", "color": "green"},
                {"text": "Je fournis des instructions détaillées", "color": "blue"}
            ]
        },
        {
            "question": "Ma communication préférée :",
            "options": [
                {"text": "Claire, concise et directe", "color": "red"},
                {"text": "Inspirante et persuasive", "color": "yellow"},
                {"text": "Empathique et encourageante", "color": "green"},
                {"text": "Précise et documentée", "color": "blue"}
            ]
        },
        {
            "question": "Face au changement :",
            "options": [
                {"text": "Je l'impose rapidement si je le juge nécessaire", "color": "red"},
                {"text": "Je le présente comme une opportunité excitante", "color": "yellow"},
                {"text": "Je l'introduis progressivement en rassurant", "color": "green"},
                {"text": "Je le planifie méticuleusement", "color": "blue"}
            ]
        },
        {
            "question": "Ce qu'on me reconnaît généralement :",
            "options": [
                {"text": "Ma détermination et mon efficacité", "color": "red"},
                {"text": "Mon enthousiasme et ma capacité à motiver", "color": "yellow"},
                {"text": "Mon écoute et ma bienveillance", "color": "green"},
                {"text": "Ma rigueur et mon expertise", "color": "blue"}
            ]
        }
    ]
    
    # Initialisation des scores
    if 'scores_disc' not in streamlit_interface.session_state:
        streamlit_interface.session_state.scores_disc = {'red': 0, 'yellow': 0, 'green': 0, 'blue': 0}
        streamlit_interface.session_state.reponses_disc = [None] * len(questions_disc)
        streamlit_interface.session_state.afficher_resultats_disc = False
    
    # Réinitialiser le test
    if streamlit_interface.button("🔄 Recommencer le test", key="reinitialiser_test"):
        streamlit_interface.session_state.scores_disc = {'red': 0, 'yellow': 0, 'green': 0, 'blue': 0}
        streamlit_interface.session_state.reponses_disc = [None] * len(questions_disc)
        streamlit_interface.session_state.afficher_resultats_disc = False
        streamlit_interface.rerun()
    
    # Affichage des questions
    for index, question in enumerate(questions_disc):
        streamlit_interface.markdown(f'<div class="quiz-question"><strong>Question {index+1}/{len(questions_disc)} :</strong> {question["question"]}</div>', unsafe_allow_html=True)
        
        # Création des options colorées
        colonne1, colonne2, colonne3, colonne4 = streamlit_interface.columns(4)
        colonnes = [colonne1, colonne2, colonne3, colonne4]
        
        for indice_option, option in enumerate(question["options"]):
            with colonnes[indice_option]:
                classe_couleur = f"color-{option['color']}"
                if streamlit_interface.button(option["text"], key=f"question{index}_option{indice_option}", use_container_width=True):
                    # Réinitialiser le score pour cette question
                    couleur_precedente = streamlit_interface.session_state.reponses_disc[index]
                    if couleur_precedente:
                        streamlit_interface.session_state.scores_disc[couleur_precedente] -= 1
                    # Ajouter le nouveau score
                    streamlit_interface.session_state.reponses_disc[index] = option['color']
                    streamlit_interface.session_state.scores_disc[option['color']] += 1
                    streamlit_interface.rerun()
        
        # Afficher la réponse sélectionnée
        if streamlit_interface.session_state.reponses_disc[index] is not None:
            couleur_selectionnee = streamlit_interface.session_state.reponses_disc[index]
            texte_selectionne = next(opt['text'] for opt in question['options'] if opt['color'] == couleur_selectionnee)
            affichage_couleur = {
                'red': '🔴 Rouge',
                'yellow': '🟡 Jaune', 
                'green': '🟢 Vert',
                'blue': '🔵 Bleu'
            }
            streamlit_interface.markdown(f"✅ **Votre choix :** {affichage_couleur[couleur_selectionnee]} - {texte_selectionne}")
        
        streamlit_interface.markdown("---")
    
    # Vérifier si toutes les questions sont répondues
    toutes_questions_repondues = all(reponse is not None for reponse in streamlit_interface.session_state.reponses_disc)
    
    # Bouton pour voir les résultats
    if streamlit_interface.button("🎯 Découvrir mon style de leadership", key="calculer_disc", disabled=not toutes_questions_repondues):
        if not toutes_questions_repondues:
            streamlit_interface.warning("⚠️ Veuillez répondre à toutes les questions avant de voir vos résultats.")
        else:
            streamlit_interface.session_state.afficher_resultats_disc = True
            streamlit_interface.rerun()
    
    # Affichage des résultats
    if streamlit_interface.session_state.get('afficher_resultats_disc', False) and toutes_questions_repondues:
        scores = streamlit_interface.session_state.scores_disc
        # Détermination du style dominant
        couleur_dominante = max(scores, key=scores.get)
        
        # CORRECTION : Chaîne de caractères corrigée avec des guillemets doubles
        mapping_leadership = {
            'red': {
                'styles_principaux': ['Directif', 'Pace-setter'],
                'styles_secondaires': ['Transactionnel'],
                'description': 'Vous êtes orienté résultats, compétitif et décidé. Vous excellez dans les situations qui demandent des décisions rapides et une forte direction.',
                'forces': ['Décision rapide', 'Orientation résultats', 'Leadership fort', 'Gestion de crise'],
                'defis': ['Peut être perçu comme autoritaire', 'Manque de patience', 'Néglige les relations'],
                'conseil': 'Développez votre écoute active et apprenez à valoriser les relations humaines.'
            },
            'yellow': {
                'styles_principaux': ['Visionnaire', 'Transformationnel', 'Coaching'],
                'styles_secondaires': ['Démocratique'],
                'description': 'Vous êtes enthousiaste, inspirant et relationnel. Vous motivez les autres par votre énergie communicative et votre vision positive.',
                'forces': ['Communication inspirante', 'Motivation des équipes', 'Créativité', 'Optimisme'],
                'defis': ['Manque de suivi', 'Trop d\'optimisme', 'Organisation variable'],
                'conseil': 'Renforcez votre sens de l\'organisation et votre capacité à suivre les détails.'
            },
            'green': {
                'styles_principaux': ['Affiliatif', 'Serviteur', 'Authentique'],
                'styles_secondaires': ['Démocratique'],
                'description': 'Vous êtes empathique, fiable et harmonieux. Vous créez un environnement de confiance et favorisez la coopération.',
                'forces': ['Écoute active', 'Cohésion d\'équipe', 'Empathie', 'Fiabilité'],  # CORRIGÉ : guillemet échappé
                'defis': ['Évitement des conflits', 'Difficulté à dire non', 'Lenteur décisionnelle'],
                'conseil': 'Apprenez à prendre des décisions difficiles et à confronter les problèmes directement.'
            },
            'blue': {
                'styles_principaux': ['Analytique', 'Situationnel'],
                'styles_secondaires': ['Transactionnel'],
                'description': 'Vous êtes précis, méthodique et organisé. Vous basez vos décisions sur des faits et des données solides.',
                'forces': ['Pensée analytique', 'Précision', 'Planification', 'Expertise technique'],
                'defis': ['Perfectionnisme excessif', 'Lenteur d\'analyse', 'Manque de spontanéité'],
                'conseil': 'Développez votre capacité à prendre des décisions rapides et à vous adapter à l\'imprévu.'
            }
        }
        
        profil = mapping_leadership[couleur_dominante]
        classe_resultat = f"result-{couleur_dominante}"
        
        # Affichage des résultats
        streamlit_interface.markdown(f'<div class="{classe_resultat}">', unsafe_allow_html=True)
        streamlit_interface.markdown(f"<h2>🎯 Votre Profil de Leadership</h2>", unsafe_allow_html=True)
        streamlit_interface.markdown(f"<h3 style='color: {'#dc2626' if couleur_dominante == 'red' else '#d97706' if couleur_dominante == 'yellow' else '#16a34a' if couleur_dominante == 'green' else '#2563eb'};'>Profil {couleur_dominante.capitalize()} - Leader {', '.join(profil['styles_principaux'])}</h3>", unsafe_allow_html=True)
        streamlit_interface.markdown(f"<p><strong>Description :</strong> {profil['description']}</p>", unsafe_allow_html=True)
        
        # Section scores DISC
        streamlit_interface.markdown("<h4>📊 Votre profil DISC :</h4>", unsafe_allow_html=True)
        colonne1, colonne2, colonne3, colonne4 = streamlit_interface.columns(4)
        with colonne1:
            classe_dominante = "disc-score-dominant" if couleur_dominante == 'red' else ""
            streamlit_interface.markdown(f'<div class="disc-score-red disc-score-box {classe_dominante}"><strong>🔴 Rouge</strong><br>{scores["red"]}/10</div>', unsafe_allow_html=True)
        with colonne2:
            classe_dominante = "disc-score-dominant" if couleur_dominante == 'yellow' else ""
            streamlit_interface.markdown(f'<div class="disc-score-yellow disc-score-box {classe_dominante}"><strong>🟡 Jaune</strong><br>{scores["yellow"]}/10</div>', unsafe_allow_html=True)
        with colonne3:
            classe_dominante = "disc-score-dominant" if couleur_dominante == 'green' else ""
            streamlit_interface.markdown(f'<div class="disc-score-green disc-score-box {classe_dominante}"><strong>🟢 Vert</strong><br>{scores["green"]}/10</div>', unsafe_allow_html=True)
        with colonne4:
            classe_dominante = "disc-score-dominant" if couleur_dominante == 'blue' else ""
            streamlit_interface.markdown(f'<div class="disc-score-blue disc-score-box {classe_dominante}"><strong>🔵 Bleu</strong><br>{scores["blue"]}/10</div>', unsafe_allow_html=True)
        
        # Styles de leadership dominants
        streamlit_interface.markdown("<h4>🎨 Vos Styles de Leadership Dominants</h4>", unsafe_allow_html=True)
        colonnes = streamlit_interface.columns(2)
        for index, style in enumerate(profil['styles_principaux']):
            with colonnes[index % 2]:
                streamlit_interface.markdown(f"""
                <div style="background: {'#fef2f2' if couleur_dominante == 'red' else '#fffbeb' if couleur_dominante == 'yellow' else '#f0fdf4' if couleur_dominante == 'green' else '#eff6ff'}; 
                            padding: 1rem; border-radius: 8px; border-left: 4px solid {'#dc2626' if couleur_dominante == 'red' else '#d97706' if couleur_dominante == 'yellow' else '#16a34a' if couleur_dominante == 'green' else '#2563eb'}; margin: 0.5rem 0;">
                    <strong>★ {style}</strong>
                </div>
                """, unsafe_allow_html=True)
        
        # Forces et défis
        colonne1, colonne2 = streamlit_interface.columns(2)
        with colonne1:
            streamlit_interface.markdown("<h4>✅ Vos Forces</h4>", unsafe_allow_html=True)
            for force in profil['forces']:
                streamlit_interface.markdown(f"<div style='background: #f0fdf4; padding: 0.5rem; margin: 0.2rem 0; border-radius: 6px;'>✓ {force}</div>", unsafe_allow_html=True)
        with colonne2:
            streamlit_interface.markdown("<h4>⚠️ Défis à Relever</h4>", unsafe_allow_html=True)
            for defi in profil['defis']:
                streamlit_interface.markdown(f"<div style='background: #fef2f2; padding: 0.5rem; margin: 0.2rem 0; border-radius: 6px;'>⚠ {defi}</div>", unsafe_allow_html=True)
        
        # Conseil de développement
        streamlit_interface.markdown(f"""
        <div class="conseil-box">
            <h4>💡 Conseil de Développement</h4>
            <p>{profil['conseil']}</p>
        </div>
        """, unsafe_allow_html=True)
        streamlit_interface.markdown('</div>', unsafe_allow_html=True)
        
        # Vidéo recommandée
        streamlit_interface.markdown("""
        <div class="modern-card">
            <h3>🎥 Vidéo Recommandée</h3>
            <p>Regardez cette vidéo pour mieux comprendre votre style de leadership :</p>
            <a href="https://youtu.be/NY82yptNp5E?si=_SrSJ8F5t2RY1ywK" target="_blank" class="video-link">
                ▶ Les 10 types de leadership - Comprendre votre profil
            </a>
        </div>
        """, unsafe_allow_html=True)

# ==============================
# ACTIVITÉ EXPRESS 2 : REFORMULATION EN DUO (Slide 2)
# ==============================
with onglets[2]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 2/13 : Reformulation en Duo</h2>
    <p class="content-paragraph">Pratiquez l'écoute active après le test DISC.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="modern-card">
        <h3>👂 Étapes</h3>
        <p><strong>Durée :</strong> 10 minutes</p>
        <ol class="content-list">
            <li><strong>Personne A</strong> parle 1 minute d'un projet ou d'une idée</li>
            <li><strong>Personne B</strong> reformule en 30 secondes</li>
            <li>Vérification puis inversion des rôles</li>
        </ol>
        <div class="example-box">
            💡 <strong>Exemple :</strong> "Tu dis que tu veux améliorer la collaboration entre les équipes ?"
        </div>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Renforcer l'écoute active, une compétence fondamentale pour tout leader.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDE 3 : INTRODUCTION
# ==============================
with onglets[3]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>🚀 Bienvenue dans l'univers du leadership moderne</h2>
    <p class="content-paragraph">
    Le leadership n'est plus réservé aux dirigeants : c'est une <strong>compétence essentielle</strong> pour inspirer, mobiliser et transformer. 
    </p>
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Marie, enseignante en collège, utilise le leadership affiliatif pour recréer du lien après le confinement.
    </div>
    <h3>🎥 Vidéos recommandées</h3>
    <a href="https://youtu.be/hCtFbHJQHvk?si=r00mEZ8Mnnzecd1I" target="_blank" class="video-link">▶ Définition d'un leader</a>
    <a href="https://youtu.be/Ej9M-U1EiGY?si=kgqe2lA8Pe6oF26Q" target="_blank" class="video-link">▶ Définition du leadership</a>
    <a href="https://youtu.be/NY82yptNp5E?si=_SrSJ8F5t2RY1ywK" target="_blank" class="video-link">▶ Les 10 types de leadership</a>
    <div class="quote-card">
    « Le leadership n'est pas un titre, c'est une responsabilité envers les autres. » — Simon Sinek
    </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# ACTIVITÉ EXPRESS 3 : POST-IT DE RÉFLEXION (Slide 4)
# ==============================
with onglets[4]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 3/13 : Post-it de Réflexion</h2>
    <p class="content-paragraph">Une pause réflexive après l'introduction.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="modern-card">
        <h3>📝 Matériel</h3>
        <p><strong>Durée :</strong> 8 minutes</p>
        <p>Post-its de 3 couleurs :</p>
        <ul class="content-list">
            <li><span style="color:green; font-weight:bold;">🟩 Vert</span> : Ce que je fais bien comme leader</li>
            <li><span style="color:orange; font-weight:bold;">🟧 Orange</span> : Ce que je veux améliorer</li>
            <li><span style="color:blue; font-weight:bold;">🟦 Bleu</span> : Une action concrète pour demain</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Passer du concept à l'action personnelle et concrète.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDE 5 : DÉFINITIONS
# ==============================
with onglets[5]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>📘 Définitions clés avec exemples</h2>
    <p class="content-paragraph"><strong>Leadership</strong> : Capacité à influencer, inspirer et guider vers un objectif commun.</p>
    <div class="example-box">
    💡 <strong>Exemple :</strong> Joséphine, infirmière chef, inspire son équipe en partageant quotidiennement les témoignages de patients guéris.
    </div>
    <p class="content-paragraph"><strong>Management</strong> : Processus de planification, organisation et contrôle des ressources.</p>
    <div class="example-box">
    💡 <strong>Exemple :</strong> Un chef de projet qui organise les tâches et les délais pour son équipe.
    </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# ACTIVITÉ EXPRESS 4 : QUESTION PUISSANTE (Slide 6)
# ==============================
with onglets[6]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 4/13 : Question Puissante</h2>
    <p class="content-paragraph">Ouvrir la réflexion avec une seule question ouverte.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="modern-card">
        <h3>💬 Consigne</h3>
        <p><strong>Durée :</strong> 10 minutes</p>
        <p>Poser une seule <strong>question ouverte</strong> à son partenaire.</p>
        <p><strong>Exemples :</strong></p>
        <ul class="content-list">
            <li>"Qu'est-ce qui te passionne dans ce projet ?"</li>
            <li>"Comment vois-tu les choses ?"</li>
            <li>"Quel impact veux-tu avoir ?"</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Apprendre à poser des questions qui ouvrent la voie à la compréhension, pas à la défense.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDE 7 : LEADERSHIP VS MANAGEMENT
# ==============================
with onglets[7]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>⚖️ Leadership vs Management</h2>
    <p class="content-paragraph">Beaucoup pensent que leadership et management s'opposent. En réalité, ils sont <strong>complémentaires</strong>.</p>
    <div class="content-paragraph">
    <strong>Management :</strong> Gérer les processus, planifier, organiser, contrôler.
    </div>
    <div class="content-paragraph">
    <strong>Leadership :</strong> Inspirer les personnes, créer une vision, innover.
    </div>
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> À Google, les managers allient leadership (vision) et management (KPIs mensuels).
    </div>
    <h3>🎥 Vidéo explicative</h3>
    <a href="https://youtu.be/mhkLc0HEtR0?si=n4rAkltZW8gIGu7g" target="_blank" class="video-link">▶ Différence entre leader et management</a>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# ACTIVITÉ EXPRESS 5 : ÉCOUTE ACTIVE RAPIDE (Slide 8)
# ==============================
with onglets[8]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 5/13 : Écoute Active Rapide</h2>
    <p class="content-paragraph">Pratiquer l'écoute sans jugement ni préparation de réponse.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="modern-card">
        <h3>👂 Consigne</h3>
        <p><strong>Durée :</strong> 8 minutes</p>
        <p>Chaque participant parle pendant 2 minutes sur un sujet simple (ex : "Un projet qui me passionne").</p>
        <p><strong>Règle :</strong> L'auditeur ne peut pas interrompre, ni répondre. Il doit juste écouter.</p>
        <p>Ensuite, on inverse les rôles.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Apprendre à écouter pour comprendre, pas pour répondre — compétence fondamentale du leadership.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDE 9 : LEADERSHIP VS COMMANDEMENT
# ==============================
with onglets[9]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>⚔️ Leadership vs Commandement</h2>
    <p class="content-paragraph">Le leadership s'acquiert par l'influence, le commandement par la position hiérarchique.</p>
    <div class="content-paragraph">
    <strong>Commandement :</strong> Autorité formelle, contrôle, structure hiérarchique.
    </div>
    <div class="content-paragraph">
    <strong>Leadership :</strong> Influence informelle, inspiration, relations.
    </div>
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Dans l'armée, un sergent utilise le commandement (ordres) alors qu'un caporal chef peut développer du leadership (respect gagné).
    </div>
    <div class="quote-card">
    « Le commandement fait respecter les règles, le leadership fait adhérer aux valeurs. »
    </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# ACTIVITÉ EXPRESS 6 : TOUR DE TABLE DES QUALITÉS (Slide 10)
# ==============================
with onglets[10]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 6/13 : Tour de Table des Qualités</h2>
    <p class="content-paragraph">Explorer collectivement les qualités essentielles du leader.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="modern-card">
        <h3>👥 Consigne</h3>
        <p><strong>Durée :</strong> 15 minutes</p>
        <p>Chacun nomme <strong>une qualité essentielle</strong> d'un bon leader.</p>
        <p><strong>Interdit :</strong> Répéter une qualité déjà citée.</p>
        <p><strong>Objectif :</strong> Créer une liste riche et variée.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Activer la créativité, favoriser l'écoute active, élargir la définition du leadership.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDE 11 : THÉORIES X ET Y
# ==============================
with onglets[11]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>🧠 Théories X et Y de Douglas McGregor</h2>
    <p class="content-paragraph">Douglas McGregor (1960) a identifié <strong>deux visions opposées de la nature humaine</strong> au travail.</p>
    <div class="theory-box">
    <h3>📋 Théorie X - Vision traditionnelle</h3>
    <p><strong>Postulats :</strong></p>
    <ul class="content-list">
    <li>Les employés n'aiment pas naturellement le travail</li>
    <li>Ils doivent être contrôlés, dirigés et menacés de sanctions</li>
    <li>Ils évitent les responsabilités et recherchent la sécurité</li>
    </ul>
    </div>
    <div class="theory-box">
    <h3>📈 Théorie Y - Vision moderne</h3>
    <p><strong>Postulats :</strong></p>
    <ul class="content-list">
    <li>Le travail est aussi naturel que le jeu ou le repos</li>
    <li>Les personnes peuvent s'auto-contrôler et s'auto-motiver</li>
    <li>Elles recherchent et acceptent les responsabilités</li>
    </ul>
    </div>
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Une usine traditionnelle (Théorie X) vs une startup tech (Théorie Y).
    </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# ACTIVITÉ EXPRESS 7 : MINI-JEU DE RÔLE (Slide 12)
# ==============================
with onglets[12]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 7/13 : Mini-Jeu de Rôle - Vision</h2>
    <p class="content-paragraph">Pratiquer le style visionnaire.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="modern-card">
        <h3>🎭 Scénario</h3>
        <p><strong>Durée :</strong> 10 minutes</p>
        <p><strong>Situation :</strong> Un leader doit présenter une vision de projet à une équipe réticente.</p>
        <p><strong>Rôles :</strong> Leader et 2-3 collaborateurs.</p>
        <p><strong>Objectif :</strong> Inspirer et motiver l'équipe avec la vision.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Pratiquer la communication d'une vision inspirante et mobilisatrice.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# STYLES DE LEADERSHIP (Slides 13-22)
# ==============================
donnees_styles_leadership = [
    {
        "nom": "Visionnaire",
        "slogan": "« Viens avec moi vers l'avenir »",
        "description": "Le leader visionnaire inspire en partageant une vision claire et motivante de l'avenir. Il donne du sens au travail et guide son équipe vers des objectifs ambitieux.",
        "forces": ["Inspire et motive", "Donne une direction claire", "Favorise l'innovation", "Crée de l'engagement"],
        "faiblesses": ["Peut manquer de détails pratiques", "Trop focalisé sur le long terme", "Peut négliger les problèmes courants"],
        "exemple": "Elon Musk avec sa vision de coloniser Mars et de transition énergétique.",
        "couleur": "#8B5CF6",
        "utilisation": "Idéal pour : inspirer le changement, créer une vision partagée, motiver vers des objectifs ambitieux."
    },
    {
        "nom": "Coaching",
        "slogan": "« Essayez et je vous aiderai à réussir »",
        "description": "Le leader coaching se concentre sur le développement personnel et professionnel de chaque membre de l'équipe. Il investit du temps pour identifier les forces et aider à surmonter les faiblesses.",
        "forces": ["Développe les talents", "Améliore les performances", "Fidélise les collaborateurs", "Crée une culture d'apprentissage"],
        "faiblesses": ["Consommateurs de temps", "Difficile avec les équipes nombreuses", "Dépend de la motivation des collaborateurs"],
        "exemple": "Un manager qui consacre 30 minutes par semaine à chaque collaborateur pour son développement.",
        "couleur": "#10B981",
        "utilisation": "Idéal pour : développer les talents, améliorer les compétences, fidéliser les collaborateurs."
    },
    {
        "nom": "Affiliatif",
        "slogan": "« Les personnes d'abord »",
        "description": "Le leader affiliatif privilégie l'harmonie et les relations humaines. Il crée un environnement de travail positif où les membres se sentent valorisés et connectés.",
        "forces": ["Excellente gestion des conflits", "Forte cohésion d'équipe", "Environnement de confiance", "Bien-être au travail"],
        "faiblesses": ["Peut éviter les confrontations nécessaires", "Performance parfois sacrifiée à l'harmonie", "Manque de direction claire"],
        "exemple": "Une cheffe d'équipe qui organise des déjeuners d'équipe réguliers et célèbre les succès personnels.",
        "couleur": "#3B82F6",
        "utilisation": "Idéal pour : résoudre les conflits, renforcer la cohésion, créer un environnement positif."
    },
    {
        "nom": "Démocratique",
        "slogan": "« Qu'en pensez-vous ? »",
        "description": "Le leader démocratique valorise la participation et la collaboration. Il consulte son équipe avant de prendre des décisions importantes et encourage le partage d'idées.",
        "forces": ["Meilleures décisions collectives", "Fort engagement de l'équipe", "Innovation et créativité", "Respect mutuel"],
        "faiblesses": ["Lenteur du processus décisionnel", "Difficile en situation d'urgence", "Risque de consensus mou"],
        "exemple": "Chez Google, les équipes utilisent des votes et consultations pour les décisions importantes.",
        "couleur": "#6366F1",
        "utilisation": "Idéal pour : prendre des décisions importantes, impliquer l'équipe, favoriser l'innovation."
    },
    {
        "nom": "Directif",
        "slogan": "« Faites ce que je vous dis »",
        "description": "Le leader directif donne des instructions claires et spécifiques. Il attend une exécution précise et contrôle étroitement le travail. Efficace en situation de crise.",
        "forces": ["Décisions rapides", "Clarté des attentes", "Efficace en urgence", "Contrôle serré"],
        "faiblesses": ["Démotivant à long terme", "Tue l'initiative", "Faible développement des collaborateurs", "Résistance passive"],
        "exemple": "Lors de l'incendie de Notre-Dame de Paris, les pompiers ont suivi des ordres directs et précis.",
        "couleur": "#EF4444",
        "utilisation": "Idéal pour : situations de crise, équipes inexpérimentées, besoin de résultats immédiats."
    },
    {
        "nom": "Pace-setter",
        "slogan": "« Faites comme moi, maintenant ! »",
        "description": "Le leader pace-setter établit des standards d'excellence très élevés et montre l'exemple. Il s'attend à ce que l'équipe suive son rythme et sa qualité de travail.",
        "forces": ["Haute performance", "Résultats rapides", "Excellence technique", "Auto-motivation"],
        "faiblesses": ["Épuisement de l'équipe", "Manque de délégation", "Démotivation si standards trop hauts", "Faible collaboration"],
        "exemple": "Steve Jobs était connu pour ses standards d'excellence extrêmement élevés chez Apple.",
        "couleur": "#F59E0B",
        "utilisation": "Idéal pour : équipes très compétentes et motivées, besoin de résultats rapides de haute qualité."
    },
    {
        "nom": "Transformationnel",
        "slogan": "« Ensemble, transformons notre réalité »",
        "description": "Le leader transformationnel inspire un changement profond en challengeant les statu quo et en encourageant l'innovation radicale. Il transforme les individus et l'organisation.",
        "forces": ["Changement profond et durable", "Innovation disruptive", "Développement des leaders", "Vision à long terme"],
        "faiblesses": ["Résistance au changement", "Difficile à maintenir", "Nécessite une forte adhésion", "Risque de burnout"],
        "exemple": "Jacques Servier a transformé l'industrie pharmaceutique française par son approche innovante.",
        "couleur": "#7C3AED",
        "utilisation": "Idéal pour : conduire des changements majeurs, innover radicalement, développer une culture forte."
    },
    {
        "nom": "Transactionnel",
        "slogan": "« Vous serez récompensé pour vos résultats »",
        "description": "Le leader transactionnel fonctionne sur un système de récompenses et punitions basé sur la performance. Il établit des objectifs clairs et des incitations correspondantes.",
        "forces": ["Clarté des attentes", "Performance mesurable", "Efficacité à court terme", "Système équitable"],
        "faiblesses": ["Limite la créativité", "Relation transactionnelle", "Démotivation si récompenses insuffisantes", "Focus court terme"],
        "exemple": "Les systèmes de commissions dans les ventes où les performances sont directement récompensées.",
        "couleur": "#6B7280",
        "utilisation": "Idéal pour : environnements très structurés, objectifs clairs et mesurables, récompenses basées sur la performance."
    },
    {
        "nom": "Authentique",
        "slogan": "« Je suis vrai et transparent »",
        "description": "Le leader authentique montre sa vulnérabilité, admet ses erreurs et reste fidèle à ses valeurs. Il construit la confiance par sa transparence et son intégrité.",
        "forces": ["Confiance élevée", "Loyauté de l'équipe", "Culture d'apprentissage", "Respect authentique"],
        "faiblesses": ["Vulnérabilité peut être perçue comme faiblesse", "Difficile dans certaines cultures", "Nécessite une grande maturité"],
        "exemple": "Brené Brown, chercheuse qui prône le leadership vulnérable et authentique.",
        "couleur": "#059669",
        "utilisation": "Idéal pour : construire la confiance, créer une culture transparente, développer des relations authentiques."
    },
    {
        "nom": "Serviteur",
        "slogan": "« Je suis là pour vous servir »",
        "description": "Le leader serviteur met les besoins de son équipe avant les siens. Il se concentre sur le développement et le bien-être des collaborateurs pour atteindre les objectifs.",
        "forces": ["Engagement exceptionnel", "Développement des talents", "Culture de service", "Rétention des talents"],
        "faiblesses": ["Peut manquer d'autorité", "Difficile dans les structures hiérarchiques", "Risque d'épuisement du leader"],
        "exemple": "Nelson Mandela qui a toujours mis les besoins de son peuple avant les siens.",
        "couleur": "#0EA5E9",
        "utilisation": "Idéal pour : développer les talents, créer un engagement profond, construire une culture de service."
    }
]

# Création des slides pour chaque style (13-22)
for index, style in enumerate(donnees_styles_leadership):
    with onglets[13 + index]:
        streamlit_interface.markdown(f"""
        <div class="modern-card">
            <h2>🎨 Style {style['nom']}</h2>
            <p style="font-size:1.3rem; font-weight:600; color:{style['couleur']}; margin:1rem 0;">
                {style['slogan']}
            </p>
            <p class="content-paragraph">{style['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Exemple concret
        streamlit_interface.markdown(f"""
        <div class="example-box">
            💡 <strong>Exemple concret :</strong> {style['exemple']}
        </div>
        """, unsafe_allow_html=True)
        
        # Forces et défis
        streamlit_interface.markdown("""
        <div class="forces-defis-grid">
            <div class="forces-box">
                <h4>✅ Forces</h4>
                <ul class="content-list">
        """, unsafe_allow_html=True)
        for force in style['forces']:
            streamlit_interface.markdown(f"<li>{force}</li>", unsafe_allow_html=True)
        streamlit_interface.markdown("""
                </ul>
            </div>
            <div class="defis-box">
                <h4>⚠️ Défis</h4>
                <ul class="content-list">
        """, unsafe_allow_html=True)
        for faiblesse in style['faiblesses']:
            streamlit_interface.markdown(f"<li>{faiblesse}</li>", unsafe_allow_html=True)
        streamlit_interface.markdown("""
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Quand utiliser ce style
        streamlit_interface.markdown("<h4>🎯 Quand utiliser ce style ?</h4>", unsafe_allow_html=True)
        streamlit_interface.markdown(f"<p class='content-paragraph'>{style['utilisation']}</p>", unsafe_allow_html=True)

# ==============================
# ACTIVITÉ EXPRESS 8 : CARTE MENTALE EXPRESS (Slide 23)
# ==============================
with onglets[23]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 8/13 : Carte Mentale Express</h2>
    <p class="content-paragraph">Visualiser ses forces de leader en un clin d'œil.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="modern-card">
        <h3>🧠 Consigne</h3>
        <p><strong>Durée :</strong> 10 minutes</p>
        <p>Créer une carte mentale sur une feuille :</p>
        <p><strong>Centre :</strong> MOI</p>
        <p><strong>Branches :</strong> Mes talents naturels en tant que leader.</p>
        <p><strong>Exemples :</strong> Écoute, Résilience, Vision, Empathie...</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Renforcer l'estime de soi et la conscience de ses forces.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDES THÉORIQUES RESTANTS (24-36)
# ==============================

# Slide 24 : Leadership Situationnel
with onglets[24]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>🔄 Leadership Situationnel</h2>
    <p class="content-paragraph">Le leadership situationnel adapte le style du leader à la maturité et aux compétences des collaborateurs.</p>
    <div class="content-paragraph">
    <strong>Niveaux de maturité :</strong>
    </div>
    <ul class="content-list">
    <li><strong>M1 :</strong> Faible compétence, faible motivation → Style Directif</li>
    <li><strong>M2 :</strong> Faible compétence, forte motivation → Style Persuasif</li>
    <li><strong>M3 :</strong> Forte compétence, motivation variable → Style Participatif</li>
    <li><strong>M4 :</strong> Forte compétence, forte motivation → Style Délégatif</li>
    </ul>
    <div class="example-box">
    💡 <strong>Exemple :</strong> Un manager utilise le style directif avec un nouveau stagiaire (M1) et le style délégatif avec son adjoint expérimenté (M4).
    </div>
    </div>
    """, unsafe_allow_html=True)

# Slide 25 : Leadership Laissez-faire
with onglets[25]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>🏖️ Leadership Laissez-faire</h2>
    <p class="content-paragraph">Le leader laissez-faire donne une grande autonomie à son équipe et intervient minimalement.</p>
    <div class="content-paragraph">
    <strong>Caractéristiques :</strong>
    </div>
    <ul class="content-list">
    <li>Délégation totale</li>
    <li>Intervention minimale</li>
    <li>Liberté d'action complète</li>
    <li>Support sur demande seulement</li>
    </ul>
    <div class="example-box">
    💡 <strong>Exemple :</strong> Dans les équipes de recherche et développement très expérimentées, où l'innovation nécessite de la liberté.
    </div>
    <div class="conseil-box">
    <h4>⚠️ Attention :</h4>
    <p>Ce style peut mener au chaos si l'équipe n'est pas suffisamment mature ou motivée.</p>
    </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# JEU DE RÔLE PRINCIPAL - SLIDE 26
# ==============================
with onglets[26]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎭 Jeu de Rôle - Mise en Pratique</h2>
    <p class="content-paragraph">Pratiquez les différents styles de leadership à travers des scénarios réalistes en binômes</p>
    </div>
    """, unsafe_allow_html=True)
    
    scenarios_jeu_role = [
        {
            "titre": "🚀 Lancement d'un Nouveau Projet",
            "description": "Vous devez lancer un projet innovant avec une équipe réticente au changement",
            "roles": [
                "Leader : Convaincre l'équipe de l'importance du projet",
                "Collaborateur : Exprimer des réserves et des préoccupations"
            ],
            "styles_recommandes": ["Visionnaire", "Coaching", "Démocratique"],
            "duree": "10 minutes"
        },
        {
            "titre": "🔥 Gestion de Crise",
            "description": "Une urgence nécessite une action immédiate et coordonnée",
            "roles": [
                "Leader : Prendre des décisions rapides sous pression",
                "Collaborateur : Suivre les instructions et signaler les problèmes"
            ],
            "styles_recommandes": ["Directif", "Pace-setter"],
            "duree": "8 minutes"
        },
        {
            "titre": "🤝 Résolution de Conflit",
            "description": "Deux membres de l'équipe sont en conflit ouvert",
            "roles": [
                "Leader : Médier le conflit et rétablir l'harmonie",
                "Collaborateur en conflit : Exprimer son point de vue"
            ],
            "styles_recommandes": ["Affiliatif", "Authentique", "Serviteur"],
            "duree": "12 minutes"
        },
        {
            "titre": "💡 Innovation et Créativité",
            "description": "Brainstorming pour résoudre un problème complexe",
            "roles": [
                "Leader : Stimuler la créativité sans imposer de solutions",
                "Collaborateur : Proposer des idées innovantes"
            ],
            "styles_recommandes": ["Démocratique", "Laissez-faire", "Transformationnel"],
            "duree": "15 minutes"
        },
        {
            "titre": "📈 Performance d'Équipe",
            "description": "L'équipe n'atteint pas ses objectifs de performance",
            "roles": [
                "Leader : Identifier les problèmes et motiver l'équipe",
                "Collaborateur : Expliquer les difficultés rencontrées"
            ],
            "styles_recommandes": ["Coaching", "Transactionnel", "Pace-setter"],
            "duree": "10 minutes"
        }
    ]
    
    # Initialisation de l'état
    if 'scenario_actuel' not in streamlit_interface.session_state:
        streamlit_interface.session_state.scenario_actuel = None
    if 'temps_restant' not in streamlit_interface.session_state:
        streamlit_interface.session_state.temps_restant = 0
    if 'temps_initial' not in streamlit_interface.session_state:
        streamlit_interface.session_state.temps_initial = 0
    if 'timer_en_cours' not in streamlit_interface.session_state:
        streamlit_interface.session_state.timer_en_cours = False
    if 'timer_termine' not in streamlit_interface.session_state:
        streamlit_interface.session_state.timer_termine = False
    
    # Sélection du scénario
    streamlit_interface.markdown("### 🎯 Choisissez un Scénario")
    for index, scenario in enumerate(scenarios_jeu_role):
        if streamlit_interface.button(f"{scenario['titre']} - {scenario['duree']}", key=f"scenario_{index}", use_container_width=True):
            streamlit_interface.session_state.scenario_actuel = scenario
            streamlit_interface.session_state.timer_en_cours = False
            streamlit_interface.session_state.timer_termine = False
            # Convertir la durée en secondes
            minutes = int(scenario['duree'].split()[0])
            streamlit_interface.session_state.temps_restant = minutes * 60
            streamlit_interface.session_state.temps_initial = minutes * 60
            streamlit_interface.rerun()
    
    # Affichage du scénario sélectionné
    if streamlit_interface.session_state.scenario_actuel:
        scenario = streamlit_interface.session_state.scenario_actuel
        streamlit_interface.markdown(f"""
        <div class="roleplay-card">
            <h3>🎭 {scenario['titre']}</h3>
            <p><strong>Description :</strong> {scenario['description']}</p>
            <p><strong>Durée :</strong> {scenario['duree']}</p>
            <p><strong>Styles recommandés :</strong> {', '.join(scenario['styles_recommandes'])}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Rôles
        streamlit_interface.markdown("### 👥 Rôles à Distribuer")
        colonne1, colonne2 = streamlit_interface.columns(2)
        with colonne1:
            streamlit_interface.markdown(f"""
            <div class="roleplay-scenario">
                <h4>🎯 Rôle du Leader</h4>
                <p>{scenario['roles'][0]}</p>
            </div>
            """, unsafe_allow_html=True)
        with colonne2:
            streamlit_interface.markdown(f"""
            <div class="roleplay-scenario">
                <h4>👤 Rôle du Collaborateur</h4>
                <p>{scenario['roles'][1]}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Conteneur pour le timer qui sera mis à jour
        emplacement_timer = streamlit_interface.empty()
        
        # Contrôles du timer
        streamlit_interface.markdown("### ⏱️ Contrôles du Timer")
        colonne1, colonne2, colonne3 = streamlit_interface.columns(3)
        with colonne1:
            if streamlit_interface.button("▶️ Démarrer", key="demarrer_timer", use_container_width=True):
                streamlit_interface.session_state.timer_en_cours = True
                streamlit_interface.session_state.timer_termine = False
                streamlit_interface.rerun()
        with colonne2:
            if streamlit_interface.button("⏸️ Pause", key="pause_timer", use_container_width=True):
                streamlit_interface.session_state.timer_en_cours = False
                streamlit_interface.rerun()
        with colonne3:
            if streamlit_interface.button("🔄 Réinitialiser", key="reinitialiser_timer", use_container_width=True):
                streamlit_interface.session_state.timer_en_cours = False
                streamlit_interface.session_state.timer_termine = False
                streamlit_interface.session_state.temps_restant = streamlit_interface.session_state.temps_initial
                streamlit_interface.rerun()
        
        # Logique du timer
        if streamlit_interface.session_state.timer_en_cours and streamlit_interface.session_state.temps_restant > 0:
            # Mettre à jour le temps
            streamlit_interface.session_state.temps_restant -= 1
            # Si le temps est écoulé
            if streamlit_interface.session_state.temps_restant <= 0:
                streamlit_interface.session_state.timer_en_cours = False
                streamlit_interface.session_state.timer_termine = True
                streamlit_interface.session_state.temps_restant = 0
        
        # Affichage du timer
        minutes = streamlit_interface.session_state.temps_restant // 60
        secondes = streamlit_interface.session_state.temps_restant % 60
        
        # Couleur du timer
        if streamlit_interface.session_state.temps_initial > 0:
            progression = streamlit_interface.session_state.temps_restant / streamlit_interface.session_state.temps_initial
            if progression > 0.5:
                couleur_timer = "#10B981"  # Vert
            elif progression > 0.25:
                couleur_timer = "#F59E0B"  # Orange
            else:
                couleur_timer = "#EF4444"  # Rouge
        else:
            couleur_timer = "#6B7280"
        
        # Afficher le timer dans le placeholder
        with emplacement_timer.container():
            streamlit_interface.markdown("### ⏱️ Timer de la Session")
            streamlit_interface.markdown(f"""
            <div class="timer-box" style="border-color: {couleur_timer};">
                <div style="font-size: 3rem; font-weight: bold; color: {couleur_timer};">
                    {minutes:02d}:{secondes:02d}
                </div>
                <div style="margin-top: 0.5rem;">
                    {'⏰ En cours...' if streamlit_interface.session_state.timer_en_cours else '⏸️ En pause' if streamlit_interface.session_state.temps_restant < streamlit_interface.session_state.temps_initial else '⏹️ Prêt'}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Barre de progression
            if streamlit_interface.session_state.temps_initial > 0:
                valeur_progression = 1 - (streamlit_interface.session_state.temps_restant / streamlit_interface.session_state.temps_initial)
                streamlit_interface.progress(valeur_progression)
                streamlit_interface.caption(f"Progression : {int(valeur_progression * 100)}%")
        
        # Si le timer est en cours, planifier un rerun
        if streamlit_interface.session_state.timer_en_cours and streamlit_interface.session_state.temps_restant > 0:
            # Ajouter un petit délai avant le rerun
            import time
            time.sleep(1)
            streamlit_interface.rerun()
        
        # Message de fin
        if streamlit_interface.session_state.timer_termine:
            streamlit_interface.balloons()
            streamlit_interface.success("🎉 Temps écoulé ! La session est terminée.")
            if streamlit_interface.button("🔄 Recommencer", key="recommencer_termine"):
                streamlit_interface.session_state.timer_en_cours = False
                streamlit_interface.session_state.timer_termine = False
                streamlit_interface.session_state.temps_restant = streamlit_interface.session_state.temps_initial
                streamlit_interface.rerun()
        
        # Consignes pour le débriefing
        streamlit_interface.markdown("### 📝 Debriefing")
        streamlit_interface.markdown("""
        <div class="conseil-box">
            <h4>Questions pour le debriefing :</h4>
            <ul>
                <li>Quel style de leadership a été utilisé ?</li>
                <li>Comment s'est senti le collaborateur ?</li>
                <li>Qu'est-ce qui a bien fonctionné ?</li>
                <li>Qu'est-ce qui pourrait être amélioré ?</li>
                <li>Quel autre style aurait pu être efficace ?</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Instructions générales
    streamlit_interface.markdown("---")
    streamlit_interface.markdown("""
    <div class="modern-card">
        <h3>📋 Instructions pour le Jeu de Rôle</h3>
        <ol class="content-list">
            <li><strong>Formez des binômes</strong> - Un leader et un collaborateur</li>
            <li><strong>Choisissez un scénario</strong> - Cliquez sur un des scénarios ci-dessus</li>
            <li><strong>Distribuez les rôles</strong> - Chacun joue son rôle selon la description</li>
            <li><strong>Utilisez le timer</strong> - Respectez le temps imparti</li>
            <li><strong>Débriefer</strong> - À la fin, échangez vos retours d'expérience</li>
            <li><strong>Inversez les rôles</strong> - Changez de rôle pour le scénario suivant</li>
        </ol>
        <div class="example-box">
            💡 <strong>Conseil :</strong> Essayez d'utiliser différents styles de leadership pour le même scénario et comparez les résultats !
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDES THÉORIQUES SUIVANTS
# ==============================

# Slide 27 : Compétences Clés
with onglets[27]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>🔑 Compétences Clés du Leader Moderne</h2>
    <h3>🏆 Les 5 compétences indispensables</h3>
    <ul class="content-list">
    <li><strong>Vision stratégique :</strong> Voir loin et large</li>
    <li><strong>Communication inspirante :</strong> Parler avec cœur et conviction</li>
    <li><strong>Décision courageuse :</strong> Assumer ses choix avec humilité</li>
    <li><strong>Délégation efficace :</strong> Faire confiance et responsabiliser</li>
    <li><strong>Résilience émotionnelle :</strong> Rebondir face aux échecs</li>
    </ul>
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Indra Nooyi, ancienne CEO de PepsiCo, combinait vision stratégique et attention aux détails humains.
    </div>
    <h3>🎥 Vidéo sur les compétences</h3>
    <a href="https://youtu.be/2tDKptsgvVU?si=fSS4rwyv7EM9biy9" target="_blank" class="video-link">▶ Les compétences d'un leader</a>
    </div>
    """, unsafe_allow_html=True)

# Slide 28 : Intelligence Émotionnelle
with onglets[28]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>🧠 Intelligence Émotionnelle (IE) au service du leadership</h2>
    <p class="content-paragraph">L'IE représente <strong>80% de la performance</strong> en leadership selon Daniel Goleman.</p>
    <h3>🎯 Les 4 piliers de l'IE</h3>
    <ul class="content-list">
    <li><strong>Conscience de soi :</strong> Comprendre ses émotions et leur impact</li>
    <li><strong>Maîtrise de soi :</strong> Gérer ses réactions émotionnelles</li>
    <li><strong>Conscience sociale :</strong> Percevoir les émotions des autres</li>
    <li><strong>Gestion des relations :</strong> Influencer positivement les émotions collectives</li>
    </ul>
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Lors d'une restructuration, Pierre, directeur RH, reconnaît sa propre anxiété et celle de son équipe, et organise des entretiens individuels pour rassurer.
    </div>
    <h3>🎥 Vidéo explicative</h3>
    <a href="https://youtu.be/UOS8X33jOZo?si=IXlKW4TF9CEi6E3h" target="_blank" class="video-link">▶ Intelligence émotionnelle pour un meilleur leadership</a>
    </div>
    """, unsafe_allow_html=True)

# Slide 29 : Études de Cas
with onglets[29]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>📊 Études de Cas Concrets</h2>
    <h3>🏢 Cas 1 : Transformation digitale</h3>
    <p class="content-paragraph"><strong>Contexte :</strong> Une PME familiale doit se digitaliser face à la concurrence.</p>
    <p class="content-paragraph"><strong>Défi :</strong> Résistance au changement des équipes historiques.</p>
    <p class="content-paragraph"><strong>Solution :</strong> Leadership visionnaire + coaching progressif.</p>
    <div class="example-box">
    💡 <strong>Résultat :</strong> 6 mois pour la transition, 90% d'adoption des nouveaux outils.
    </div>
    <h3>🏭 Cas 2 : Fusion d'entreprises</h3>
    <p class="content-paragraph"><strong>Contexte :</strong> Deux entreprises de cultures différentes fusionnent.</p>
    <p class="content-paragraph"><strong>Défi :</strong> Choc culturel et perte de repères.</p>
    <p class="content-paragraph"><strong>Solution :</strong> Leadership affiliatif pour créer du lien + démocratique pour co-construire.</p>
    <div class="example-box">
    💡 <strong>Résultat :</strong> 75% de rétention des talents clés, nouvelle identité partagée.
    </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# QUIZ 1 - SLIDE 30
# ==============================
with onglets[30]:
    streamlit_interface.markdown("""
    <div class="quiz-section">
    <h2>🧠 Quiz 1 - Fondamentaux du Leadership</h2>
    <p class="content-paragraph">Testez vos connaissances sur les bases du leadership avec ce quiz de 10 questions</p>
    </div>
    """, unsafe_allow_html=True)
    
    questions_quiz1 = [
        {
            "question": "Quelle est la définition la plus précise du leadership ?",
            "options": [
                "Exercer un pouvoir hiérarchique sur des subordonnés",
                "Influencer et guider des personnes vers un objectif commun",
                "Prendre toutes les décisions importantes seul",
                "Contrôler strictement le travail des autres"
            ],
            "correct": 1,
            "explication": "Le leadership est avant tout une capacité à influencer et guider, pas à contrôler ou dominer."
        },
        {
            "question": "Quelle est la principale différence entre leadership et management ?",
            "options": [
                "Le leadership rapporte plus d'argent",
                "Le leadership concerne la vision, le management l'organisation",
                "Le management est plus important que le leadership",
                "Il n'y a aucune différence"
            ],
            "correct": 1,
            "explication": "Le leadership inspire le changement et fixe la vision, tandis que le management organise et planifie l'exécution."
        },
        {
            "question": "Selon la théorie X et Y de McGregor, quelle affirmation correspond à la théorie Y ?",
            "options": [
                "Les employés sont naturellement paresseux et doivent être contrôlés",
                "Les employés sont créatifs et cherchent à s'impliquer",
                "Seul l'argent motive les employés",
                "Les employés ne peuvent pas être fiables"
            ],
            "correct": 1,
            "explication": "La théorie Y considère que les employés sont naturellement motivés, créatifs et cherchent à prendre des responsabilités."
        },
        {
            "question": "Quel style de leadership est centré sur le développement des collaborateurs ?",
            "options": [
                "Leadership directif",
                "Leadership coaching",
                "Leadership pace-setter", 
                "Leadership laissez-faire"
            ],
            "correct": 1,
            "explication": "Le leadership coaching se concentre sur le développement à long terme des compétences des collaborateurs."
        },
        {
            "question": "Quelle compétence est la plus cruciale pour un leader selon la plupart des études ?",
            "options": [
                "Compétences techniques avancées",
                "Intelligence émotionnelle",
                "Connaissances financières",
                "Maîtrise des outils technologiques"
            ],
            "correct": 1,
            "explication": "L'intelligence émotionnelle permet de comprendre et gérer les émotions, essentielle pour motiver et inspirer."
        },
        {
            "question": "Dans le modèle situationnel de Hersey-Blanchard, quel style utiliser avec une équipe compétente mais peu motivée ?",
            "options": [
                "Directif",
                "Persuasif", 
                "Participatif",
                "Délégatif"
            ],
            "correct": 2,
            "explication": "Avec une équipe compétente mais peu motivée, le style participatif qui implique l'équipe dans les décisions est le plus efficace."
        },
        {
            "question": "Quel est le principal avantage du leadership démocratique ?",
            "options": [
                "Décisions très rapides",
                "Fort engagement des collaborateurs",
                "Contrôle total du leader",
                "Peu de discussions nécessaires"
            ],
            "correct": 1,
            "explication": "Le leadership démocratique favorise l'engagement car les collaborateurs se sentent écoutés et impliqués."
        },
        {
            "question": "Quel type de leader inspire par son exemple et son intégrité ?",
            "options": [
                "Leader transactionnel",
                "Leader authentique",
                "Leader directif",
                "Leader laissez-faire"
            ],
            "correct": 1,
            "explication": "Le leader authentique inspire par sa transparence, son intégrité et son alignement entre ses paroles et ses actions."
        },
        {
            "question": "Quelle est la caractéristique principale du leadership serviteur ?",
            "options": [
                "Servir les intérêts du leader",
                "Servir en premier, diriger ensuite",
                "Servir seulement les actionnaires",
                "Servir sous la direction des subordonnés"
            ],
            "correct": 1,
            "explication": "Le leader serviteur met les besoins des autres en premier et considère le leadership comme un service."
        },
        {
            "question": "Quelle erreur un leader débutant doit-il absolument éviter ?",
            "options": [
                "Écouter trop son équipe",
                "Micro-manager et ne pas faire confiance",
                "Communiquer trop fréquemment",
                "Faire trop de compliments"
            ],
            "correct": 1,
            "explication": "Le micro-management tue la motivation et l'autonomie, c'est une erreur fréquente des leaders débutants."
        }
    ]
    
    # Initialisation du quiz 1
    if 'reponses_quiz1' not in streamlit_interface.session_state:
        streamlit_interface.session_state.reponses_quiz1 = [None] * len(questions_quiz1)
    if 'score_quiz1' not in streamlit_interface.session_state:
        streamlit_interface.session_state.score_quiz1 = 0
    if 'afficher_resultats_quiz1' not in streamlit_interface.session_state:
        streamlit_interface.session_state.afficher_resultats_quiz1 = False
    
    # Affichage des questions
    for index, question in enumerate(questions_quiz1):
        streamlit_interface.markdown(f'<div class="quiz-question"><strong>Question {index+1}/10 :</strong> {question["question"]}</div>', unsafe_allow_html=True)
        options = question["options"]
        reponse = streamlit_interface.radio(
            "Choisissez votre réponse :",
            options,
            key=f"quiz1_{index}",
            index=streamlit_interface.session_state.reponses_quiz1[index] if streamlit_interface.session_state.reponses_quiz1[index] is not None else None
        )
        # Stocker la réponse
        if reponse in options:
            streamlit_interface.session_state.reponses_quiz1[index] = options.index(reponse)
    
    # Vérifier si toutes les questions sont répondues
    toutes_repondues = all(reponse is not None for reponse in streamlit_interface.session_state.reponses_quiz1)
    
    if streamlit_interface.button("📝 Voir mes résultats du Quiz 1", key="voir_resultats_quiz1", disabled=not toutes_repondues):
        if not toutes_repondues:
            streamlit_interface.warning("⚠️ Veuillez répondre à toutes les questions avant de voir vos résultats.")
        else:
            streamlit_interface.session_state.afficher_resultats_quiz1 = True
            # Calcul du score
            score = 0
            for index, question in enumerate(questions_quiz1):
                if streamlit_interface.session_state.reponses_quiz1[index] == question["correct"]:
                    score += 1
            streamlit_interface.session_state.score_quiz1 = score
            streamlit_interface.rerun()
    
    # Affichage des résultats
    if streamlit_interface.session_state.get('afficher_resultats_quiz1', False) and toutes_repondues:
        score = streamlit_interface.session_state.score_quiz1
        streamlit_interface.markdown(f"""
        <div class="evaluation-box">
            <h3>📊 Résultats du Quiz 1</h3>
            <p><strong>Score : {score}/10</strong></p>
            <p><strong>Pourcentage : {score * 10}%</strong></p>
        """, unsafe_allow_html=True)
        if score >= 9:
            streamlit_interface.markdown("<p>🎉 <strong>Excellent !</strong> Vous maîtrisez parfaitement les fondamentaux du leadership.</p>", unsafe_allow_html=True)
        elif score >= 7:
            streamlit_interface.markdown("<p>👍 <strong>Très bien !</strong> Vous avez de bonnes connaissances en leadership.</p>", unsafe_allow_html=True)
        elif score >= 5:
            streamlit_interface.markdown("<p>💪 <strong>Bien !</strong> Vous avez les bases, continuez à apprendre.</p>", unsafe_allow_html=True)
        else:
            streamlit_interface.markdown("<p>📚 <strong>À travailler.</strong> Revoyez les concepts fondamentaux.</p>", unsafe_allow_html=True)
        streamlit_interface.markdown("</div>", unsafe_allow_html=True)
        
        # Affichage des corrections
        streamlit_interface.markdown("### 📖 Corrections détaillées")
        for index, question in enumerate(questions_quiz1):
            reponse_utilisateur = streamlit_interface.session_state.reponses_quiz1[index]
            est_correct = reponse_utilisateur == question["correct"]
            streamlit_interface.markdown(f"""
            <div class="modern-card">
                <h4>Question {index+1} : {question['question']}</h4>
                <p><strong>Votre réponse :</strong> {question['options'][reponse_utilisateur]} {'✅' if est_correct else '❌'}</p>
                <p><strong>Réponse correcte :</strong> {question['options'][question['correct']]}</p>
                <p><strong>Explication :</strong> {question['explication']}</p>
            </div>
            """, unsafe_allow_html=True)

# ==============================
# QUIZ 2 - SLIDE 31
# ==============================
with onglets[31]:
    streamlit_interface.markdown("""
    <div class="quiz-section">
    <h2>🧠 Quiz 2 - Styles de Leadership Avancés</h2>
    <p class="content-paragraph">Testez vos connaissances sur les styles de leadership avec ce quiz de 10 questions</p>
    </div>
    """, unsafe_allow_html=True)
    
    questions_quiz2 = [
        {
            "question": "Quel style de leadership est le plus adapté en situation de crise nécessitant une action immédiate ?",
            "options": [
                "Leadership démocratique",
                "Leadership directif",
                "Leadership laissez-faire",
                "Leadership affiliatif"
            ],
            "correct": 1,
            "explication": "En situation de crise, le leadership directif permet de prendre des décisions rapides et d'orienter clairement l'action."
        },
        {
            "question": "Quel leader est connu pour son approche 'Servant Leadership' ?",
            "options": [
                "Steve Jobs",
                "Robert Greenleaf",
                "Jack Welch",
                "Bill Gates"
            ],
            "correct": 1,
            "explication": "Robert Greenleaf a développé le concept de 'Servant Leadership' où le leader sert d'abord son équipe."
        },
        {
            "question": "Dans le leadership transformationnel, quelle est la technique clé pour inspirer les collaborateurs ?",
            "options": [
                "Stimulation intellectuelle",
                "Contrôle renforcé",
                "Punitions fréquentes",
                "Délégation totale"
            ],
            "correct": 0,
            "explication": "La stimulation intellectuelle pousse les collaborateurs à innover et penser différemment, clé du leadership transformationnel."
        },
        {
            "question": "Quel style de leadership risque de créer le plus de burn-out dans l'équipe ?",
            "options": [
                "Leadership visionnaire",
                "Leadership pace-setter",
                "Leadership coaching",
                "Leadership démocratique"
            ],
            "correct": 1,
            "explication": "Le leadership pace-setter, où le leader montre l'exemple à un rythme effréné, peut épuiser l'équipe qui peine à suivre."
        },
        {
            "question": "Quelle est la principale caractéristique du leadership authentique ?",
            "options": [
                "Transparence et alignement valeurs-actions",
                "Charisme exceptionnel",
                "Expertise technique suprême",
                "Richesse personnelle"
            ],
            "correct": 0,
            "explication": "L'authenticité se manifeste par la transparence, l'intégrité et l'alignement entre les valeurs professées et les actions."
        },
        {
            "question": "Selon le modèle situationnel, quel style utiliser avec un collaborateur débutant et motivé ?",
            "options": [
                "Délégatif",
                "Directif",
                "Participatif",
                "Persuasif"
            ],
            "correct": 1,
            "explication": "Avec un débutant motivé, le style directif fournit la structure et les instructions nécessaires à l'apprentissage."
        },
        {
            "question": "Quel type de leader utilise principalement des récompenses et punitions ?",
            "options": [
                "Leader transformationnel",
                "Leader transactionnel",
                "Leader authentique",
                "Leader serviteur"
            ],
            "correct": 1,
            "explication": "Le leader transactionnel fonctionne sur le principe 'donnant-donnant' avec des récompenses pour les performances."
        },
        {
            "question": "Quelle est la limite principale du leadership laissez-faire ?",
            "options": [
                "Manque de structure et de direction",
                "Trop de contrôle",
                "Communication excessive",
                "Décisions trop rapides"
            ],
            "correct": 0,
            "explication": "Le laissez-faire peut mener au manque de coordination et à l'absence de vision claire pour l'équipe."
        },
        {
            "question": "Quel style de leadership est le plus efficace pour construire l'harmonie d'équipe ?",
            "options": [
                "Leadership affiliatif",
                "Leadership directif",
                "Leadership pace-setter",
                "Leadership transactionnel"
            ],
            "correct": 0,
            "explication": "Le leadership affiliatif se concentre sur les relations et l'harmonie, créant un environnement de travail positif."
        },
        {
            "question": "Quelle compétence un leader visionnaire doit-il particulièrement développer ?",
            "options": [
                "Capacité à communiquer une vision inspirante",
                "Compétences en micro-management",
                "Maîtrise des détails opérationnels",
                "Capacité à punir les mauvaises performances"
            ],
            "correct": 0,
            "explication": "Un leader visionnaire excelle dans l'art de communiquer une vision qui inspire et mobilise l'équipe."
        }
    ]
    
    # Initialisation du quiz 2
    if 'reponses_quiz2' not in streamlit_interface.session_state:
        streamlit_interface.session_state.reponses_quiz2 = [None] * len(questions_quiz2)
    if 'score_quiz2' not in streamlit_interface.session_state:
        streamlit_interface.session_state.score_quiz2 = 0
    if 'afficher_resultats_quiz2' not in streamlit_interface.session_state:
        streamlit_interface.session_state.afficher_resultats_quiz2 = False
    
    # Affichage des questions
    for index, question in enumerate(questions_quiz2):
        streamlit_interface.markdown(f'<div class="quiz-question"><strong>Question {index+1}/10 :</strong> {question["question"]}</div>', unsafe_allow_html=True)
        options = question["options"]
        reponse = streamlit_interface.radio(
            "Choisissez votre réponse :",
            options,
            key=f"quiz2_{index}",
            index=streamlit_interface.session_state.reponses_quiz2[index] if streamlit_interface.session_state.reponses_quiz2[index] is not None else None
        )
        # Stocker la réponse
        if reponse in options:
            streamlit_interface.session_state.reponses_quiz2[index] = options.index(reponse)
    
    # Vérifier si toutes les questions sont répondues
    toutes_repondues = all(reponse is not None for reponse in streamlit_interface.session_state.reponses_quiz2)
    
    if streamlit_interface.button("📝 Voir mes résultats du Quiz 2", key="voir_resultats_quiz2", disabled=not toutes_repondues):
        if not toutes_repondues:
            streamlit_interface.warning("⚠️ Veuillez répondre à toutes les questions avant de voir vos résultats.")
        else:
            streamlit_interface.session_state.afficher_resultats_quiz2 = True
            # Calcul du score
            score = 0
            for index, question in enumerate(questions_quiz2):
                if streamlit_interface.session_state.reponses_quiz2[index] == question["correct"]:
                    score += 1
            streamlit_interface.session_state.score_quiz2 = score
            streamlit_interface.rerun()
    
    # Affichage des résultats
    if streamlit_interface.session_state.get('afficher_resultats_quiz2', False) and toutes_repondues:
        score = streamlit_interface.session_state.score_quiz2
        streamlit_interface.markdown(f"""
        <div class="evaluation-box">
            <h3>📊 Résultats du Quiz 2</h3>
            <p><strong>Score : {score}/10</strong></p>
            <p><strong>Pourcentage : {score * 10}%</strong></p>
        """, unsafe_allow_html=True)
        if score >= 9:
            streamlit_interface.markdown("<p>🎉 <strong>Exceptionnel !</strong> Vous maîtrisez les styles de leadership avancés.</p>", unsafe_allow_html=True)
        elif score >= 7:
            streamlit_interface.markdown("<p>👍 <strong>Très bon !</strong> Vous avez une excellente compréhension des différents styles.</p>", unsafe_allow_html=True)
        elif score >= 5:
            streamlit_interface.markdown("<p>💪 <strong>Bon !</strong> Vous connaissez les bases, continuez à vous perfectionner.</p>", unsafe_allow_html=True)
        else:
            streamlit_interface.markdown("<p>📚 <strong>À revoir.</strong> Étudiez les différents styles de leadership.</p>", unsafe_allow_html=True)
        streamlit_interface.markdown("</div>", unsafe_allow_html=True)
        
        # Affichage des corrections
        streamlit_interface.markdown("### 📖 Corrections détaillées")
        for index, question in enumerate(questions_quiz2):
            reponse_utilisateur = streamlit_interface.session_state.reponses_quiz2[index]
            est_correct = reponse_utilisateur == question["correct"]
            streamlit_interface.markdown(f"""
            <div class="modern-card">
                <h4>Question {index+1} : {question['question']}</h4>
                <p><strong>Votre réponse :</strong> {question['options'][reponse_utilisateur]} {'✅' if est_correct else '❌'}</p>
                <p><strong>Réponse correcte :</strong> {question['options'][question['correct']]}</p>
                <p><strong>Explication :</strong> {question['explication']}</p>
            </div>
            """, unsafe_allow_html=True)

# ==============================
# SLIDES THÉORIQUES FINAUX (32-36)
# ==============================

# Slide 32 : Synthèse
with onglets[32]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>🎓 Synthèse du Parcours Leadership</h2>
    <h3>🔑 Les 5 points clés à retenir</h3>
    <ul class="content-list">
    <li><strong>1. Adaptabilité :</strong> Un bon leader adapte son style à la situation</li>
    <li><strong>2. Authenticité :</strong> La cohérence entre paroles et actions</li>
    <li><strong>3. Vision :</strong> Savoir où aller et emmener les autres</li>
    <li><strong>4. Humilité :</strong> Reconnaître ses erreurs et apprendre</li>
    <li><strong>5. Impact :</strong> Mesurer son leadership par l'impact positif</li>
    </ul>
    <div class="quote-card">
    « Le véritable leadership ne consiste pas à avoir une position, mais à avoir une influence positive. »
    </div>
    </div>
    """, unsafe_allow_html=True)

# Slide 33 : Secteurs d'Application
with onglets[33]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>🏥 Leadership dans Différents Secteurs</h2>
    <h3>💻 Technologie</h3>
    <p class="content-paragraph"><strong>Style dominant :</strong> Visionnaire + Laissez-faire</p>
    <h3>🏭 Industrie</h3>
    <p class="content-paragraph"><strong>Style dominant :</strong> Directif + Démocratique</p>
    <h3>🏥 Santé</h3>
    <p class="content-paragraph"><strong>Style dominant :</strong> Affiliatif + Coaching</p>
    <h3>🎓 Éducation</h3>
    <p class="content-paragraph"><strong>Style dominant :</strong> Visionnaire + Coaching</p>
    </div>
    """, unsafe_allow_html=True)

# Slide 34 : Erreurs Courantes
with onglets[34]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>🚫 Erreurs Courantes en Leadership</h2>
    <h3>❌ Les 7 pièges à éviter</h3>
    <ul class="content-list">
    <li><strong>1. Micro-management :</strong> Tuer l'autonomie et la créativité</li>
    <li><strong>2. Incohérence :</strong> Dire une chose et faire le contraire</li>
    <li><strong>3. Manque de reconnaissance :</strong> Oublier de valoriser les efforts</li>
    <li><strong>4. Communication insuffisante :</strong> Ne pas partager l'information</li>
    <li><strong>5. Éviter les conflits :</strong> Laisser pourrir les situations</li>
    <li><strong>6. Style unique :</strong> Même style dans toutes les situations</li>
    <li><strong>7. Négliger son développement :</strong> Arrêter d'apprendre</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Slide 35 : Conseils Pratiques
with onglets[35]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>💡 Conseils Pratiques</h2>
    <h3>🎯 5 conseils pour développer votre leadership</h3>
    <ul class="content-list">
    <li><strong>1. Pratiquez l'écoute active</strong> - Écoutez pour comprendre, pas pour répondre</li>
    <li><strong>2. Donnez du feedback régulier</strong> - Constructif, spécifique et opportun</li>
    <li><strong>3. Développez votre intelligence émotionnelle</strong> - Comprenez vos émotions et celles des autres</li>
    <li><strong>4. Communiquez clairement votre vision</strong> - Expliquez le "pourquoi" derrière chaque action</li>
    <li><strong>5. Investissez dans votre développement</strong> - Le leadership s'apprend et se perfectionne</li>
    </ul>
    <h3>🎥 Vidéos sur les styles</h3>
    <a href="https://youtu.be/vilZazhIjoc?si=b4PNNY5P8SAqu9_p" target="_blank" class="video-link">▶ Les 5 styles de leadership</a>
    </div>
    """, unsafe_allow_html=True)

# Slide 36 : Ressources
with onglets[36]:
    streamlit_interface.markdown("""
    <div class="modern-card">
    <h2>📚 Ressources Complémentaires</h2>
    <h3>🎥 Toutes les vidéos recommandées</h3>
    <a href="https://youtu.be/hCtFbHJQHvk?si=r00mEZ8Mnnzecd1I" target="_blank" class="video-link">▶ Définition d'un leader</a>
    <a href="https://youtu.be/Ej9M-U1EiGY?si=kgqe2lA8Pe6oF26Q" target="_blank" class="video-link">▶ Définition du leadership</a>
    <a href="https://youtu.be/mhkLc0HEtR0?si=n4rAkltZW8gIGu7g" target="_blank" class="video-link">▶ Différence leader/management</a>
    <a href="https://youtu.be/vilZazhIjoc?si=b4PNNY5P8SAqu9_p" target="_blank" class="video-link">▶ Les 5 styles de leadership</a>
    <a href="https://youtu.be/iRBQqfJaoo4?si=Kbhele-WRaC6wqGw" target="_blank" class="video-link">▶ Leadership situationnel</a>
    <a href="https://youtu.be/2tDKptsgvVU?si=fSS4rwyv7EM9biy9" target="_blank" class="video-link">▶ Compétences d'un leader</a>
    <a href="https://youtu.be/UOS8X33jOZo?si=IXlKW4TF9CEi6E3h" target="_blank" class="video-link">▶ Intelligence émotionnelle</a>
    <a href="https://youtu.be/NY82yptNp5E?si=_SrSJ8F5t2RY1ywK" target="_blank" class="video-link">▶ Les 10 types de leadership</a>
    <div class="quote-card">
    « L'investissement le plus important que vous puissiez faire est d'investir en vous-même. »
    </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# ACTIVITÉS DE CLÔTURE (37-41)
# ==============================

# Activité 9 : Mot de la Fin
with onglets[37]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 9/13 : Mot de la Fin</h2>
    <p class="content-paragraph">Clôturez en puissance avec une dernière participation collective.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="modern-card">
        <h3>🗣️ Tour de Table</h3>
        <p><strong>Durée :</strong> 5 minutes</p>
        <p>Chacun dit <strong>un mot</strong> qui résume son état d'esprit ou son énergie de leadership.</p>
        <div class="example-box">
            💡 <strong>Exemples :</strong> Inspiration, Dynamique, Confiance, Action
        </div>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Créer une mémoire collective positive de la session.</p>
    </div>
    """, unsafe_allow_html=True)

# Activité 10 : Action Immédiate
with onglets[38]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 10/13 : Action Immédiate</h2>
    <p class="content-paragraph">Transformer l'apprentissage en action concrète.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="modern-card">
        <h3>✍️ Consigne</h3>
        <p><strong>Durée :</strong> 3 minutes</p>
        <p>Quelle petite action de leadership puis-je faire avant la fin de la journée ?</p>
        <p><strong>Exemples :</strong></p>
        <ul class="content-list">
            <li>Donner un compliment spécifique à un collègue</li>
            <li>Écouter quelqu'un sans interrompre</li>
            <li>Prendre une décision que je remettais à plus tard</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Passer de la théorie à l'action immédiate.</p>
    </div>
    """, unsafe_allow_html=True)

# Activité 11 : Gratitude Leader
with onglets[39]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 11/13 : Gratitude Leader</h2>
    <p class="content-paragraph">Reconnaître l'impact des autres sur notre parcours.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="modern-card">
        <h3>🙏 Exercice</h3>
        <p><strong>Durée :</strong> 7 minutes</p>
        <p>Identifier mentalement <strong>3 personnes</strong> qui ont été des leaders pour vous.</p>
        <p>Leur dire mentalement : <em>"Merci pour ton impact."</em></p>
        <p><strong>Effet :</strong> Crée un sentiment de connexion et d'humilité.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Renforcer la gratitude, clé de la résilience et de l'humilité dans le leadership.</p>
    </div>
    """, unsafe_allow_html=True)

# Activité 12 : Retour d'Expérience
with onglets[40]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 12/13 : Retour d'Expérience</h2>
    <p class="content-paragraph">Partager ses apprentissages clés.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="modern-card">
        <h3>💬 Consigne</h3>
        <p><strong>Durée :</strong> 10 minutes</p>
        <p>En duo, partagez :</p>
        <ul class="content-list">
            <li>Une découverte sur vous-même</li>
            <li>Une idée à mettre en pratique</li>
            <li>Un défi à relever</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Consolider les apprentissages par le partage et la réflexion.</p>
    </div>
    """, unsafe_allow_html=True)

# Activité 13 : Applaudissement Tournant
with onglets[41]:
    streamlit_interface.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 13/13 : Applaudissement Tournant</h2>
    <p class="content-paragraph">Créer une énergie positive et sensorielle pour clore.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="modern-card">
        <h3>👏 Déroulement</h3>
        <p><strong>Durée :</strong> 3 minutes</p>
        <p>Une personne au centre de la salle.</p>
        <p>Tout le monde l'applaudit chaleureusement pendant 15 secondes.</p>
        <p>Elle tourne sur elle-même et s'arrête.</p>
        <p>Une autre personne prend sa place — répéter 2 à 3 fois.</p>
        <p><strong>Effet :</strong> Énergie collective, reconnaissance, bienveillance.</p>
    </div>
    """, unsafe_allow_html=True)
    streamlit_interface.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Clôturer la session sur une note positive, humaine et sensorielle.</p>
    </div>
    """, unsafe_allow_html=True)

# Message final
streamlit_interface.markdown("---")
streamlit_interface.markdown("""
<div style="text-align: center; color: #64748b; margin-top: 2rem;">
<p><strong>✨ Présentation Leadership Pro - Formation Complète ✨</strong></p>
<p>Test DISC • 10 styles de leadership • Jeu de rôle • Quiz interactifs • Ressources vidéo</p>
<p><strong>8 activités express + 5 activités de clôture</strong></p>
</div>
""", unsafe_allow_html=True)
