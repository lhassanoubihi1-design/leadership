import streamlit as st
import random

st.set_page_config(
    page_title="Leadership Pro – Expérience Immersive",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================
# CSS MODERNE SANS ERREURS
# ==============================
st.markdown("""
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
    .stButton > button {
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
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(79, 70, 229, 0.4);
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        padding: 0 0 1.2rem;
        overflow-x: auto;
    }
    .stTabs [data-baseweb="tab"] {
        height: 48px;
        background: #f0f4ff;
        border-radius: 14px 14px 0 0;
        color: #4f46e5;
        font-weight: 600;
        font-size: 0.95rem;
        padding: 0 20px;
    }
    .stTabs [aria-selected="true"] {
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

st.title("✨ Leadership & Styles de Leadership")
st.markdown("<div style='text-align:center; margin-bottom:2rem; color:#64748b;'>Formation complète – 45 min avec activités express</div>", unsafe_allow_html=True)

# Structure mise à jour : 20 onglets max, logique claire
slide_names = [
    "0. Activité 1: Le Leader en 3 Mots",
    "1. Test DISC Leadership",
    "2. Activité 2: Mon Animal Leader",
    "3. Intro",
    "4. Activité 3: Compliment Flash",
    "5. Définitions",
    "6. Activité 4: Le Bâton de Parole",
    "7. L vs M",
    "8. Activité 5: Tour de Table des Qualités",
    "9. L vs C",
    "10. Activité 6: Journal Minute",
    "11. Théories XY",
    "12. Activité 7: Reformulation en Duo",
    "13. Visionnaire",
    "14. Coaching",
    "15. Affiliatif",
    "16. Démocratique",
    "17. Directif",
    "18. Pace-setter",
    "19. Transformationnel",
    "20. Transactionnel",
    "21. Authentique",
    "22. Serviteur",
    "23. Situationnel",
    "24. Laissez-faire",
    "25. Jeu de Rôle",
    "26. Compétences",
    "27. IE",
    "28. Cas",
    "29. Quiz 1",
    "30. Quiz 2",
    "31. Synthèse",
    "32. Secteurs",
    "33. Erreurs",
    "34. Conseils",
    "35. Ressources",
    "36. Activité 8: Mot de la Fin",
    "37. Activité 9: Applaudissement Tournant"
]

tabs = st.tabs(slide_names)

# ==============================
# ACTIVITÉ EXPRESS 1 : LE LEADER EN 3 MOTS (Slide 0)
# ==============================
with tabs[0]:
    st.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 1/9 : Le Leader en 3 Mots</h2>
    <p class="content-paragraph">Un icebreaker pour activer les représentations.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
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
    st.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Créer un climat d'échange, activer les connaissances préexistantes.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# TEST DE LEADERSHIP DISC AVEC COULEURS ET STYLES (Slide 1)
# ==============================
with tabs[1]:
    st.markdown("""
    <div class="test-section">
    <h2>🎨 Test de Leadership DISC</h2>
    <p class="content-paragraph">Découvrez votre style de leadership dominant avec ce test basé sur les 4 couleurs du modèle DISC</p>
    </div>
    """, unsafe_allow_html=True)
    # Questions avec options colorées
    disc_questions = [
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

    if 'disc_scores' not in st.session_state:
        st.session_state.disc_scores = {'red': 0, 'yellow': 0, 'green': 0, 'blue': 0}
        st.session_state.disc_responses = [None] * len(disc_questions)
        st.session_state.show_disc_results = False

    if st.button("🔄 Recommencer le test", key="reset_test"):
        st.session_state.disc_scores = {'red': 0, 'yellow': 0, 'green': 0, 'blue': 0}
        st.session_state.disc_responses = [None] * len(disc_questions)
        st.session_state.show_disc_results = False
        st.rerun()

    for i, q in enumerate(disc_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/{len(disc_questions)} :</strong> {q["question"]}</div>', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        columns = [col1, col2, col3, col4]
        for idx, option in enumerate(q["options"]):
            with columns[idx]:
                if st.button(option["text"], key=f"q{i}_opt{idx}", use_container_width=True):
                    previous_color = st.session_state.disc_responses[i]
                    if previous_color:
                        st.session_state.disc_scores[previous_color] -= 1
                    st.session_state.disc_responses[i] = option['color']
                    st.session_state.disc_scores[option['color']] += 1
                    st.rerun()
        if st.session_state.disc_responses[i] is not None:
            selected_color = st.session_state.disc_responses[i]
            selected_text = next(opt['text'] for opt in q['options'] if opt['color'] == selected_color)
            color_display = {
                'red': '🔴 Rouge',
                'yellow': '🟡 Jaune', 
                'green': '🟢 Vert',
                'blue': '🔵 Bleu'
            }
            st.markdown(f"✅ **Votre choix :** {color_display[selected_color]} - {selected_text}")
        st.markdown("---")

    all_answered = all(response is not None for response in st.session_state.disc_responses)
    if st.button("🎯 Découvrir mon style de leadership", key="calculate_disc", disabled=not all_answered):
        if not all_answered:
            st.warning("⚠️ Veuillez répondre à toutes les questions.")
        else:
            st.session_state.show_disc_results = True
            st.rerun()

    if st.session_state.get('show_disc_results', False) and all_answered:
        scores = st.session_state.disc_scores
        dominant_color = max(scores, key=scores.get)
        leadership_mapping = {
            'red': {
                'primary_styles': ['Directif', 'Pace-setter'],
                'description': 'Orientation résultats, compétitif, efficace en crise.',
                'strengths': ['Décision rapide', 'Gestion de crise'],
                'advice': 'Développez votre écoute.'
            },
            'yellow': {
                'primary_styles': ['Visionnaire', 'Coaching'],
                'description': 'Enthousiaste, motivant, inspire les autres.',
                'strengths': ['Communication', 'Optimisme'],
                'advice': 'Améliorez votre organisation.'
            },
            'green': {
                'primary_styles': ['Affiliatif', 'Serviteur'],
                'description': 'Empathique, fiable, crée de la cohésion.',
                'strengths': ['Écoute active', 'Harmonie'],
                'advice': 'Apprenez à dire non quand c'est nécessaire.'
            },
            'blue': {
                'primary_styles': ['Analytique', 'Situationnel'],
                'description': 'Précis, méthodique, base ses décisions sur les données.',
                'strengths': ['Rigueur', 'Planification'],
                'advice': 'Osez prendre des risques calculés.'
            }
        }
        profile = leadership_mapping[dominant_color]
        result_class = f"result-{dominant_color}"
        st.markdown(f'<div class="{result_class}">', unsafe_allow_html=True)
        st.markdown(f"<h2>🎯 Votre Profil de Leadership</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: {'#dc2626' if dominant_color == 'red' else '#d97706' if dominant_color == 'yellow' else '#16a34a' if dominant_color == 'green' else '#2563eb'};'>Profil {dominant_color.capitalize()}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p>{profile['description']}</p>", unsafe_allow_html=True)
        st.markdown("<h4>📊 Votre profil DISC :</h4>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f'<div class="disc-score-red disc-score-box"><strong>🔴 Rouge</strong><br>{scores["red"]}/10</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f'<div class="disc-score-yellow disc-score-box"><strong>🟡 Jaune</strong><br>{scores["yellow"]}/10</div>', unsafe_allow_html=True)
        with col3:
            st.markdown(f'<div class="disc-score-green disc-score-box"><strong>🟢 Vert</strong><br>{scores["green"]}/10</div>', unsafe_allow_html=True)
        with col4:
            st.markdown(f'<div class="disc-score-blue disc-score-box"><strong>🔵 Bleu</strong><br>{scores["blue"]}/10</div>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ==============================
# ACTIVITÉ 2 : MON ANIMAL LEADER (Slide 2)
# ==============================
with tabs[2]:
    st.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 2/9 : Mon Animal Leader</h2>
    <p class="content-paragraph">Une activité créative pour explorer son style de leadership.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="modern-card">
        <h3>🐾 Question</h3>
        <p><strong>Durée :</strong> 10 minutes</p>
        <p>« Si tu étais un animal leader, lequel serais-tu et pourquoi ? »</p>
        <p><strong>Exemples :</strong></p>
        <ul class="content-list">
            <li><strong>Lion :</strong> Décideur, protecteur</li>
            <li><strong>Abeille :</strong> Organisé, travail d'équipe</li>
            <li><strong>Dauphin :</strong> Communicatif, intelligent</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Rendre le leadership personnel et concret à travers une métaphore simple.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDE 3 : INTRODUCTION
# ==============================
with tabs[3]:
    st.markdown("""
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
# ACTIVITÉ 3 : COMPLIMENT FLASH (Slide 4)
# ==============================
with tabs[4]:
    st.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 3/9 : Compliment Flash</h2>
    <p class="content-paragraph">Créer un climat de reconnaissance.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="modern-card">
        <h3>🤝 Déroulement</h3>
        <p><strong>Durée :</strong> 8 minutes</p>
        <p>Former des duos. Chaque personne donne un compliment spécifique à l'autre pendant 2 minutes.</p>
        <p>Changer de partenaire 3 fois.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Renforcer la bienveillance et la confiance dès le début.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDE 5 : DÉFINITIONS
# ==============================
with tabs[5]:
    st.markdown("""
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
# ACTIVITÉ 4 : LE BÂTON DE PAROLE (Slide 6)
# ==============================
with tabs[6]:
    st.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 4/9 : Le Bâton de Parole</h2>
    <p class="content-paragraph">Parler à tour de rôle pour garantir l'équité.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="modern-card">
        <h3>🪵 Règle</h3>
        <p><strong>Durée :</strong> 10 minutes</p>
        <p>Seule la personne qui tient l'objet symbolique peut parler.</p>
        <p><strong>Sujet :</strong> "Qu'est-ce qu'un bon leader selon vous ?"</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Encourager l'écoute active et donner la parole à tous.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDE 7 : LEADERSHIP VS MANAGEMENT
# ==============================
with tabs[7]:
    st.markdown("""
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
# ACTIVITÉ 5 : TOUR DE TABLE DES QUALITÉS (Slide 8)
# ==============================
with tabs[8]:
    st.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 5/9 : Tour de Table des Qualités</h2>
    <p class="content-paragraph">Explorer collectivement les qualités d’un bon leader.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="modern-card">
        <h3>👥 Consigne</h3>
        <p><strong>Durée :</strong> 15 minutes</p>
        <p>Chacun nomme <strong>une qualité essentielle</strong> d’un leader.</p>
        <p><strong>Interdit :</strong> Répéter une qualité déjà citée.</p>
        <p><strong>Objectif :</strong> Créer une liste collective riche.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Stimuler la créativité et l’écoute active.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDE 9 : LEADERSHIP VS COMMANDement
# ==============================
with tabs[9]:
    st.markdown("""
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
    💡 <strong>Exemple concret :</strong> Dans l'armée, un sergent utilise le commandement (ordres), un caporal développe du leadership (respect gagné).
    </div>
    <div class="quote-card">
    « Le commandement fait respecter les règles, le leadership fait adhérer aux valeurs. »
    </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# ACTIVITÉ 6 : JOURNAL MINUTE (Slide 10)
# ==============================
with tabs[10]:
    st.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 6/9 : Journal Minute</h2>
    <p class="content-paragraph">Réfléchir en toute simplicité.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="modern-card">
        <h3>📝 Questions</h3>
        <p><strong>Durée :</strong> 5 minutes</p>
        <ul class="content-list">
            <li>Une décision que j'ai prise récemment</li>
            <li>Comment j'ai influencé quelqu'un cette semaine</li>
            <li>Ce que j'ai appris sur le leadership aujourd'hui</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Transformer l'expérience en apprentissage.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDE 11 : THÉORIES X ET Y
# ==============================
with tabs[11]:
    st.markdown("""
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
# ACTIVITÉ 7 : REFORMULATION EN DUO (Slide 12)
# ==============================
with tabs[12]:
    st.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 7/9 : Reformulation en Duo</h2>
    <p class="content-paragraph">Pratiquer l'écoute active après les théories.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="modern-card">
        <h3>👂 Étapes</h3>
        <p><strong>Durée :</strong> 10 minutes</p>
        <ol class="content-list">
            <li><strong>Personne A</strong> parle 1 minute d’un projet ou d’une idée</li>
            <li><strong>Personne B</strong> reformule en 30 secondes</li>
            <li>Vérification puis inversion des rôles</li>
        </ol>
        <div class="example-box">
            💡 <strong>Exemple :</strong> "Tu dis que tu veux améliorer la collaboration entre les équipes ?"
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Renforcer l'écoute active, une compétence fondamentale pour tout leader.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDES POUR LES 10 STYLES DE LEADERSHIP (13 à 22)
# ==============================
leadership_styles_data = [
    {
        "name": "Visionnaire",
        "slogan": "« Viens avec moi vers l'avenir »",
        "description": "Le leader visionnaire inspire en partageant une vision claire et motivante de l'avenir. Il donne du sens au travail et guide son équipe vers des objectifs ambitieux.",
        "forces": ["Inspire et motive", "Donne une direction claire", "Favorise l'innovation", "Crée de l'engagement"],
        "faiblesses": ["Peut manquer de détails pratiques", "Trop focalisé sur le long terme", "Peut négliger les problèmes courants"],
        "exemple": "Elon Musk avec sa vision de coloniser Mars et de transition énergétique.",
        "couleur": "#8B5CF6",
        "utilisation": "Idéal pour : inspirer le changement, créer une vision partagée, motiver vers des objectifs ambitieux."
    },
    {
        "name": "Coaching",
        "slogan": "« Essayez et je vous aiderai à réussir »",
        "description": "Le leader coaching se concentre sur le développement personnel et professionnel de chaque membre de l'équipe. Il investit du temps pour identifier les forces et aider à surmonter les faiblesses.",
        "forces": ["Développe les talents", "Améliore les performances", "Fidélise les collaborateurs", "Crée une culture d'apprentissage"],
        "faiblesses": ["Consommateurs de temps", "Difficile avec les équipes nombreuses", "Dépend de la motivation des collaborateurs"],
        "exemple": "Un manager qui consacre 30 minutes par semaine à chaque collaborateur pour son développement.",
        "couleur": "#10B981",
        "utilisation": "Idéal pour : développer les talents, améliorer les compétences, fidéliser les collaborateurs."
    },
    {
        "name": "Affiliatif",
        "slogan": "« Les personnes d'abord »",
        "description": "Le leader affiliatif privilégie l'harmonie et les relations humaines. Il crée un environnement de travail positif où les membres se sentent valorisés et connectés.",
        "forces": ["Excellente gestion des conflits", "Forte cohésion d'équipe", "Environnement de confiance", "Bien-être au travail"],
        "faiblesses": ["Peut éviter les confrontations nécessaires", "Performance parfois sacrifiée à l'harmonie", "Manque de direction claire"],
        "exemple": "Une cheffe d'équipe qui célèbre les succès personnels.",
        "couleur": "#3B82F6",
        "utilisation": "Idéal pour : résoudre les conflits, renforcer la cohésion, créer un environnement positif."
    },
    {
        "name": "Démocratique",
        "slogan": "« Qu'en pensez-vous ? »",
        "description": "Le leader démocratique valorise la participation et la collaboration. Il consulte son équipe avant de prendre des décisions importantes.",
        "forces": ["Meilleures décisions collectives", "Fort engagement de l'équipe", "Innovation et créativité", "Respect mutuel"],
        "faiblesses": ["Lenteur du processus décisionnel", "Difficile en situation d'urgence", "Risque de consensus mou"],
        "exemple": "Chez Google, les équipes utilisent des votes et consultations.",
        "couleur": "#6366F1",
        "utilisation": "Idéal pour : prendre des décisions importantes, impliquer l'équipe, favoriser l'innovation."
    },
    {
        "name": "Directif",
        "slogan": "« Faites ce que je vous dis »",
        "description": "Le leader directif donne des instructions claires et spécifiques. Il attend une exécution précise et contrôle étroitement le travail.",
        "forces": ["Décisions rapides", "Clarté des attentes", "Efficace en urgence", "Contrôle serré"],
        "faiblesses": ["Démotivant à long terme", "Tue l'initiative", "Faible développement des collaborateurs", "Résistance passive"],
        "exemple": "Lors de l'incendie de Notre-Dame de Paris, les pompiers ont suivi des ordres directs.",
        "couleur": "#EF4444",
        "utilisation": "Idéal pour : situations de crise, équipes inexpérimentées, besoin de résultats immédiats."
    },
    {
        "name": "Pace-setter",
        "slogan": "« Faites comme moi, maintenant ! »",
        "description": "Le leader pace-setter établit des standards d'excellence très élevés et montre l'exemple. Il s'attend à ce que l'équipe suive son rythme.",
        "forces": ["Haute performance", "Résultats rapides", "Excellence technique", "Auto-motivation"],
        "faiblesses": ["Épuisement de l'équipe", "Manque de délégation", "Démotivation si standards trop hauts", "Faible collaboration"],
        "exemple": "Steve Jobs chez Apple.",
        "couleur": "#F59E0B",
        "utilisation": "Idéal pour : équipes très compétentes et motivées, besoin de résultats rapides."
    },
    {
        "name": "Transformationnel",
        "slogan": "« Ensemble, transformons notre réalité »",
        "description": "Le leader transformationnel inspire un changement profond en challengeant les statu quo et en encourageant l'innovation radicale.",
        "forces": ["Changement profond", "Innovation disruptive", "Développement des leaders", "Vision à long terme"],
        "faiblesses": ["Résistance au changement", "Difficile à maintenir", "Nécessite une forte adhésion", "Risque de burnout"],
        "exemple": "Jacques Servier a transformé l'industrie pharmaceutique française.",
        "couleur": "#7C3AED",
        "utilisation": "Idéal pour : conduire des changements majeurs, innover radicalement."
    },
    {
        "name": "Transactionnel",
        "slogan": "« Vous serez récompensé pour vos résultats »",
        "description": "Le leader transactionnel fonctionne sur un système de récompenses et punitions basé sur la performance.",
        "forces": ["Clarté des attentes", "Performance mesurable", "Efficacité à court terme", "Système équitable"],
        "faiblesses": ["Limite la créativité", "Relation transactionnelle", "Démotivation si récompenses insuffisantes", "Focus court terme"],
        "exemple": "Les systèmes de commissions dans les ventes.",
        "couleur": "#6B7280",
        "utilisation": "Idéal pour : environnements structurés, objectifs clairs, récompenses basées sur la performance."
    },
    {
        "name": "Authentique",
        "slogan": "« Je suis vrai et transparent »",
        "description": "Le leader authentique montre sa vulnérabilité, admet ses erreurs et reste fidèle à ses valeurs.",
        "forces": ["Confiance élevée", "Loyauté de l'équipe", "Culture d'apprentissage", "Respect authentique"],
        "faiblesses": ["Vulnérabilité perçue comme faiblesse", "Nécessite une grande maturité"],
        "exemple": "Brené Brown, chercheuse sur le leadership vulnérable.",
        "couleur": "#059669",
        "utilisation": "Idéal pour : construire la confiance, créer une culture transparente."
    },
    {
        "name": "Serviteur",
        "slogan": "« Je suis là pour vous servir »",
        "description": "Le leader serviteur met les besoins de son équipe avant les siens. Il se concentre sur leur développement.",
        "forces": ["Engagement exceptionnel", "Développement des talents", "Culture de service", "Rétention des talents"],
        "faiblesses": ["Peut manquer d'autorité", "Risque d'épuisement du leader"],
        "exemple": "Nelson Mandela qui a mis les besoins de son peuple avant les siens.",
        "couleur": "#0EA5E9",
        "utilisation": "Idéal pour : développer les talents, créer un engagement profond."
    }
]

for i, style in enumerate(leadership_styles_data):
    with tabs[13 + i]:
        st.markdown(f"""
        <div class="modern-card">
            <h2>🎨 Style {style['name']}</h2>
            <p style="font-size:1.3rem; font-weight:600; color:{style['couleur']}; margin:1rem 0;">
                {style['slogan']}
            </p>
            <p class="content-paragraph">{style['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div class="example-box">
            💡 <strong>Exemple concret :</strong> {style['exemple']}
        </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        <div class="forces-defis-grid">
            <div class="forces-box">
                <h4>✅ Forces</h4>
                <ul class="content-list">
        """, unsafe_allow_html=True)
        for force in style['forces']:
            st.markdown(f"<li>{force}</li>", unsafe_allow_html=True)
        st.markdown("""
                </ul>
            </div>
            <div class="defis-box">
                <h4>⚠️ Défis</h4>
                <ul class="content-list">
        """, unsafe_allow_html=True)
        for faiblesse in style['faiblesses']:
            st.markdown(f"<li>{faiblesse}</li>", unsafe_allow_html=True)
        st.markdown("""
                </ul>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<h4>🎯 Quand utiliser ce style ?</h4>", unsafe_allow_html=True)
        st.markdown(f"<p class='content-paragraph'>{style['utilisation']}</p>", unsafe_allow_html=True)

# ==============================
# SLIDE 23 : SITUATIONNEL
# ==============================
with tabs[23]:
    st.markdown("""
    <div class="modern-card">
    <h2>🔄 Leadership Situationnel</h2>
    <p style="font-size:1.3rem; font-weight:600; color:#7C3AED; margin:1rem 0;">
        « Adaptons notre style à la situation »
    </p>
    <p class="content-paragraph">Le leader situationnel adapte son style en fonction de la maturité, des compétences et de la motivation de ses collaborateurs.</p>
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Un manager utilise un style directif avec un nouveau (faible comp., forte motivation) et délégatif avec un expert (forte comp., forte motivation).
    </div>
    <h3>📈 Les 4 niveaux de développement</h3>
    <ul class="content-list">
    <li><strong>D1 :</strong> Faible comp., forte motivation → Style directif</li>
    <li><strong>D2 :</strong> Faible à moyenne comp., faible motivation → Style persuasif</li>
    <li><strong>D3 :</strong> Moyenne à forte comp., motivation variable → Style participatif</li>
    <li><strong>D4 :</strong> Forte comp., forte motivation → Style délégatif</li>
    </ul>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="forces-defis-grid">
        <div class="forces-box">
            <h4>✅ Forces</h4>
            <ul class="content-list">
                <li>Adaptation optimale</li>
                <li>Développement progressif</li>
                <li>Efficacité contextuelle</li>
                <li>Respect des individualités</li>
            </ul>
        </div>
        <div class="defis-box">
            <h4>⚠️ Défis</h4>
            <ul class="content-list">
                <li>Nécessite une grande flexibilité</li>
                <li>Complexe à maîtriser</li>
                <li>Analyse fine des situations</li>
                <li>Risque d'incohérence</li>
            </ul>
        </div>
    </div>
    <h4>🎯 Quand utiliser ce style ?</h4>
    <p class="content-paragraph">
        Idéal pour : adapter son leadership à chaque collaborateur, développer les compétences, gérer des équipes hétérogènes.
    </p>
    <h3>🎥 Vidéo explicative</h3>
    <a href="https://youtu.be/iRBQqfJaoo4?si=Kbhele-WRaC6wqGw" target="_blank" class="video-link">▶ Le leadership situationnel</a>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDE 24 : LAISSEZ-FAIRE
# ==============================
with tabs[24]:
    st.markdown("""
    <div class="modern-card">
    <h2>🎨 Style Laissez-faire</h2>
    <p style="font-size:1.3rem; font-weight:600; color:#6B7280; margin:1rem 0;">
        « À toi de jouer »
    </p>
    <p class="content-paragraph">Le leader laissez-faire donne une autonomie totale à son équipe. Il fournit les ressources mais intervient peu.</p>
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Chez Pixar, les réalisateurs ont une liberté créative totale.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="forces-defis-grid">
        <div class="forces-box">
            <h4>✅ Forces</h4>
            <ul class="content-list">
                <li>Autonomie et créativité</li>
                <li>Responsabilisation</li>
                <li>Innovation libre</li>
                <li>Adaptation aux experts</li>
            </ul>
        </div>
        <div class="defis-box">
            <h4>⚠️ Défis</h4>
            <ul class="content-list">
                <li>Manque de direction</li>
                <li>Manque de coordination</li>
                <li>Risque de désengagement</li>
                <li>Peut créer de la confusion</li>
            </ul>
        </div>
    </div>
    <h4>🎯 Quand utiliser ce style ?</h4>
    <p class="content-paragraph">
        Idéal pour : équipes d'experts, environnements créatifs, projets innovants.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# JEU DE RÔLE - SLIDE 25
# ==============================
with tabs[25]:
    st.markdown("""
    <div class="test-section">
    <h2>🎭 Jeu de Rôle - Mise en Pratique</h2>
    <p class="content-paragraph">Pratiquez les styles en binômes</p>
    </div>
    """, unsafe_allow_html=True)
    roleplay_scenarios = [
        {
            "titre": "🚀 Lancement Nouveau Projet",
            "description": "Vous devez lancer un projet innovant avec une équipe réticente",
            "roles": [
                "Leader : Convaincre l'équipe",
                "Collaborateur : Exprimer des réserves"
            ],
            "styles_recommandes": ["Visionnaire", "Coaching", "Démocratique"],
            "duree": "10 minutes"
        },
        {
            "titre": "🔥 Gestion de Crise",
            "description": "Une urgence nécessite une action immédiate",
            "roles": [
                "Leader : Prendre des décisions rapides",
                "Collaborateur : Suivre les instructions"
            ],
            "styles_recommandes": ["Directif", "Pace-setter"],
            "duree": "8 minutes"
        }
    ]
    if 'current_scenario' not in st.session_state:
        st.session_state.current_scenario = None
    if 'time_left' not in st.session_state:
        st.session_state.time_left = 0
    if 'initial_time' not in st.session_state:
        st.session_state.initial_time = 0
    if 'timer_running' not in st.session_state:
        st.session_state.timer_running = False
    if 'timer_finished' not in st.session_state:
        st.session_state.timer_finished = False

    st.markdown("### 🎯 Choisissez un Scénario")
    for i, scenario in enumerate(roleplay_scenarios):
        if st.button(f"{scenario['titre']} - {scenario['duree']}", key=f"scenario_{i}", use_container_width=True):
            st.session_state.current_scenario = scenario
            st.session_state.timer_running = False
            st.session_state.timer_finished = False
            minutes = int(scenario['duree'].split()[0])
            st.session_state.time_left = minutes * 60
            st.session_state.initial_time = minutes * 60
            st.rerun()

    if st.session_state.current_scenario:
        scenario = st.session_state.current_scenario
        st.markdown(f"""
        <div class="roleplay-card">
            <h3>🎭 {scenario['titre']}</h3>
            <p><strong>Description :</strong> {scenario['description']}</p>
            <p><strong>Durée :</strong> {scenario['duree']}</p>
            <p><strong>Styles recommandés :</strong> {', '.join(scenario['styles_recommandes'])}</p>
        </div>
        """, unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="roleplay-scenario">
                <h4>🎯 Rôle du Leader</h4>
                <p>{scenario['roles'][0]}</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
            <div class="roleplay-scenario">
                <h4>👤 Rôle du Collaborateur</h4>
                <p>{scenario['roles'][1]}</p>
            </div>
            """, unsafe_allow_html=True)

        timer_placeholder = st.empty()
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("▶️ Démarrer", key="start_timer", use_container_width=True):
                st.session_state.timer_running = True
                st.session_state.timer_finished = False
                st.rerun()
        with col2:
            if st.button("⏸️ Pause", key="pause_timer", use_container_width=True):
                st.session_state.timer_running = False
                st.rerun()
        with col3:
            if st.button("🔄 Réinitialiser", key="reset_timer", use_container_width=True):
                st.session_state.timer_running = False
                st.session_state.timer_finished = False
                st.session_state.time_left = st.session_state.initial_time
                st.rerun()

        if st.session_state.timer_running and st.session_state.time_left > 0:
            st.session_state.time_left -= 1
            if st.session_state.time_left <= 0:
                st.session_state.timer_running = False
                st.session_state.timer_finished = True
        minutes = st.session_state.time_left // 60
        seconds = st.session_state.time_left % 60
        if st.session_state.initial_time > 0:
            progress = st.session_state.time_left / st.session_state.initial_time
            if progress > 0.5:
                timer_color = "#10B981"
            elif progress > 0.25:
                timer_color = "#F59E0B"
            else:
                timer_color = "#EF4444"
        else:
            timer_color = "#6B7280"

        with timer_placeholder.container():
            st.markdown("### ⏱️ Timer")
            st.markdown(f"""
            <div class="timer-box" style="border-color: {timer_color};">
                <div style="font-size: 3rem; color: {timer_color};">
                    {minutes:02d}:{seconds:02d}
                </div>
            </div>
            """, unsafe_allow_html=True)
            if st.session_state.initial_time > 0:
                progress_value = 1 - (st.session_state.time_left / st.session_state.initial_time)
                st.progress(progress_value)
                st.caption(f"Progression : {int(progress_value*100)}%")
        if st.session_state.timer_running and st.session_state.time_left > 0:
            import time
            time.sleep(1)
            st.rerun()
        if st.session_state.timer_finished:
            st.balloons()
            st.success("🎉 Temps écoulé !")
            if st.button("🔄 Recommencer", key="restart"):
                st.session_state.timer_running = False
                st.session_state.timer_finished = False
                st.session_state.time_left = st.session_state.initial_time
                st.rerun()
        st.markdown("### 📝 Debriefing")
        st.markdown("""
        <div class="conseil-box">
            <h4>Questions :</h4>
            <ul>
                <li>Quel style a été utilisé ?</li>
                <li>Comment s'est senti le collaborateur ?</li>
                <li>Qu'est-ce qui aurait pu être amélioré ?</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ==============================
# SLIDES RESTANTS (26 à 35)
# ==============================
# (Compétences, IE, Cas, Quiz, etc.)
# Copiez ici les contenus restants depuis le fichier original

# ==============================
# ACTIVITÉ 8 : MOT DE LA FIN (Slide 36)
# ==============================
with tabs[36]:
    st.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 8/9 : Mot de la Fin</h2>
    <p class="content-paragraph">Clôturez en puissance.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="modern-card">
        <h3>🗣️ Tour de Table</h3>
        <p><strong>Durée :</strong> 5 minutes</p>
        <p>Chacun dit <strong>un mot</strong> qui résume son état d'esprit.</p>
        <div class="example-box">
            💡 <strong>Exemples :</strong> Inspiration, Dynamique, Confiance
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# ACTIVITÉ 9 : APPLAUDISSEMENT TOURNANT (Slide 37)
# ==============================
with tabs[37]:
    st.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 9/9 : Applaudissement Tournant</h2>
    <p class="content-paragraph">Créer une énergie positive finale.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="modern-card">
        <h3>👏 Déroulement</h3>
        <p><strong>Durée :</strong> 3 minutes</p>
        <p>Une personne au centre. Tout le monde l'applaudit 15 secondes. Elle tourne. Autre personne.</p>
    </div>
    """, unsafe_allow_html=True)

# Message final
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; margin-top: 2rem;">
<p><strong>⏱️ Durée estimée : 45 min</strong></p>
<p>Activités : 9 x ~7 min = 63 min | Contenu : 10 min</p>
<p><strong>→ Total ajusté avec transitions</strong></p>
</div>
""", unsafe_allow_html=True)
