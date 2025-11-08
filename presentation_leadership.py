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
    .schema-container {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        text-align: center;
    }
    .schema-title {
        font-weight: 600;
        color: #4f46e5;
        margin-bottom: 1rem;
    }
    .naturel-test-box {
        background: linear-gradient(135deg, #f0f9ff, #e0f2fe);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 4px solid #0ea5e9;
    }
    #MainMenu, footer, header { visibility: hidden !important; }
</style>
""", unsafe_allow_html=True)

st.title("✨ Leadership & Styles de Leadership")
st.markdown("<div style='text-align:center; margin-bottom:2rem; color:#64748b;'>Formation complète avec tests, jeux de rôle et outils pratiques</div>", unsafe_allow_html=True)

# Structure avec les tests au début
slide_names = [
    "0. Test Leadership Naturel", "1. Test DISC", "2. Intro", "3. Définitions", "4. L vs M", 
    "5. L vs C", "6. Théories XY", "7. Visionnaire", "8. Coaching", "9. Affiliatif", 
    "10. Démocratique", "11. Directif", "12. Pace-setter", "13. Transformationnel", 
    "14. Transactionnel", "15. Authentique", "16. Serviteur", "17. Situationnel", 
    "18. Laissez-faire", "19. Jeu de Rôle", "20. Compétences", "21. IE", "22. Cas", 
    "23. Quiz 1", "24. Quiz 2", "25. Synthèse", "26. Secteurs", "27. Erreurs", 
    "28. Conseils", "29. Ressources"
]

tabs = st.tabs(slide_names)

# ==============================
# TEST DE LEADERSHIP NATUREL - SLIDE 0 (CORRIGÉ)
# ==============================
with tabs[0]:
    st.markdown("""
    <div class="test-section">
    <h2>🧪 Test : Êtes-vous un leader naturel ?</h2>
    <p class="content-paragraph">Découvrez votre profil de leadership avec ce test de 10 questions</p>
    </div>
    """, unsafe_allow_html=True)
    
    leadership_test_questions = [
        {"question": "Dans un groupe, je prends naturellement les devants", "points": [3, 2, 1, 0]},
        {"question": "J'écoute activement les opinions des autres avant de décider", "points": [3, 2, 1, 0]},
        {"question": "Je motive facilement les autres à se dépasser", "points": [3, 2, 1, 0]},
        {"question": "Je reste calme et rationnel sous pression", "points": [3, 2, 1, 0]},
        {"question": "Je délègue facilement et fais confiance aux autres", "points": [3, 2, 1, 0]},
        {"question": "Je prends des décisions difficiles quand il le faut", "points": [3, 2, 1, 0]},
        {"question": "Je donne régulièrement du feedback constructif", "points": [3, 2, 1, 0]},
        {"question": "Je reconnais mes erreurs et en tire des leçons", "points": [3, 2, 1, 0]},
        {"question": "Je crée facilement une ambiance positive dans l'équipe", "points": [3, 2, 1, 0]},
        {"question": "Je sais dire non quand c'est nécessaire", "points": [3, 2, 1, 0]}
    ]
    
    # Initialisation de l'état
    if 'test_responses' not in st.session_state:
        st.session_state.test_responses = [None] * len(leadership_test_questions)
    if 'test_score' not in st.session_state:
        st.session_state.test_score = 0
    if 'show_test_results' not in st.session_state:
        st.session_state.show_test_results = False
    
    total_score = 0
    all_answered = True
    
    for i, q in enumerate(leadership_test_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/10 :</strong> {q["question"]}</div>', unsafe_allow_html=True)
        
        # Déterminer l'index sélectionné
        options = ["Toujours", "Souvent", "Parfois", "Rarement"]
        default_index = st.session_state.test_responses[i] if st.session_state.test_responses[i] is not None else 0
        
        response = st.radio(
            "Votre réponse :",
            options,
            key=f"leadership_test_{i}",
            index=default_index
        )
        
        # Stocker la réponse
        response_index = options.index(response)
        st.session_state.test_responses[i] = response_index
        
        # Calculer le score
        total_score += q["points"][response_index]
    
    st.session_state.test_score = total_score
    
    # Vérifier si toutes les questions sont répondues
    all_answered = all(response is not None for response in st.session_state.test_responses)
    
    if st.button("📊 Voir mes résultats du test", key="view_test_results", disabled=not all_answered):
        if not all_answered:
            st.warning("⚠️ Veuillez répondre à toutes les questions avant de voir vos résultats.")
        else:
            st.session_state.show_test_results = True
            st.rerun()
    
    if st.session_state.show_test_results and all_answered:
        st.markdown(f"""
        <div class="evaluation-box">
        <h3>📊 Résultats de votre Test de Leadership</h3>
        <p><strong>Score : {total_score}/30 points</strong></p>
        """, unsafe_allow_html=True)
        
        if total_score >= 25:
            st.markdown("""
            <p><strong>🎯 Profil : Leader Confirmé</strong></p>
            <p>Vous avez des qualités de leadership exceptionnelles. Vous inspirez naturellement les autres et savez guider une équipe vers le succès.</p>
            <p><strong>Conseil :</strong> Continuez à développer votre impact et à mentorer les futurs leaders.</p>
            """, unsafe_allow_html=True)
        elif total_score >= 20:
            st.markdown("""
            <p><strong>💪 Profil : Leader Émergent</strong></p>
            <p>Vous avez de solides bases de leadership et un bon potentiel. Vous êtes sur la bonne voie pour devenir un leader accompli.</p>
            <p><strong>Conseil :</strong> Travaillez votre assertivité et votre vision stratégique.</p>
            """, unsafe_allow_html=True)
        elif total_score >= 15:
            st.markdown("""
            <p><strong>🌱 Profil : Leader en Développement</strong></p>
            <p>Vous avez les bases nécessaires et un bon potentiel de croissance. Le leadership s'apprend et se développe.</p>
            <p><strong>Conseil :</strong> Pratiquez la prise de décision et le feedback régulier.</p>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <p><strong>📚 Profil : Leader en Apprentissage</strong></p>
            <p>Vous avez conscience de l'importance du leadership. C'est le premier pas vers le développement de vos compétences.</p>
            <p><strong>Conseil :</strong> Commencez par observer les bons leaders et pratiquez l'écoute active.</p>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Schéma des profils
        st.markdown("""
        <div class="schema-container">
            <div class="schema-title">📈 Schéma des Profils de Leadership</div>
            <div style="display: flex; justify-content: space-between; align-items: end; height: 200px; margin: 2rem 0;">
                <div style="text-align: center; flex: 1;">
                    <div style="background: #fee2e2; height: 60px; margin: 0 10px; border-radius: 8px 8px 0 0;"></div>
                    <div>Apprentissage</div>
                </div>
                <div style="text-align: center; flex: 1;">
                    <div style="background: #fef3c7; height: 100px; margin: 0 10px; border-radius: 8px 8px 0 0;"></div>
                    <div>Développement</div>
                </div>
                <div style="text-align: center; flex: 1;">
                    <div style="background: #dcfce7; height: 140px; margin: 0 10px; border-radius: 8px 8px 0 0;"></div>
                    <div>Émergent</div>
                </div>
                <div style="text-align: center; flex: 1;">
                    <div style="background: #dbeafe; height: 180px; margin: 0 10px; border-radius: 8px 8px 0 0;"></div>
                    <div>Confirmé</div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("💡 **Note :** Ce test donne une indication de votre profil actuel. Le leadership se développe continuellement tout au long de la vie.")

# ==============================
# TEST DISC - SLIDE 1 (10 QUESTIONS)
# ==============================
with tabs[1]:
    st.markdown("""
    <div class="test-section">
    <h2>🎨 Test de Leadership DISC</h2>
    <p class="content-paragraph">Découvrez votre style de leadership dominant avec ce test basé sur les 4 couleurs du modèle DISC</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Questions avec options colorées (10 questions)
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
    
    # Initialisation des scores
    if 'disc_scores' not in st.session_state:
        st.session_state.disc_scores = {'red': 0, 'yellow': 0, 'green': 0, 'blue': 0}
        st.session_state.disc_responses = [None] * len(disc_questions)
        st.session_state.show_disc_results = False
    
    # Réinitialiser le test
    if st.button("🔄 Recommencer le test", key="reset_test"):
        st.session_state.disc_scores = {'red': 0, 'yellow': 0, 'green': 0, 'blue': 0}
        st.session_state.disc_responses = [None] * len(disc_questions)
        st.session_state.show_disc_results = False
        st.rerun()
    
    # Affichage des questions
    for i, q in enumerate(disc_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/{len(disc_questions)} :</strong> {q["question"]}</div>', unsafe_allow_html=True)
        
        # Création des options colorées
        col1, col2, col3, col4 = st.columns(4)
        columns = [col1, col2, col3, col4]
        
        for idx, option in enumerate(q["options"]):
            with columns[idx]:
                if st.button(option["text"], key=f"q{i}_opt{idx}", use_container_width=True):
                    # Réinitialiser le score pour cette question
                    previous_color = st.session_state.disc_responses[i]
                    if previous_color:
                        st.session_state.disc_scores[previous_color] -= 1
                    
                    # Ajouter le nouveau score
                    st.session_state.disc_responses[i] = option['color']
                    st.session_state.disc_scores[option['color']] += 1
                    st.rerun()
        
        # Afficher la réponse sélectionnée
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
    
    # Vérifier si toutes les questions sont répondues
    all_answered = all(response is not None for response in st.session_state.disc_responses)
    
    # Bouton pour voir les résultats
    if st.button("🎯 Découvrir mon style de leadership", key="calculate_disc", disabled=not all_answered):
        if not all_answered:
            st.warning("⚠️ Veuillez répondre à toutes les questions avant de voir vos résultats.")
        else:
            st.session_state.show_disc_results = True
            st.rerun()
    
    # Affichage des résultats
    if st.session_state.get('show_disc_results', False) and all_answered:
        scores = st.session_state.disc_scores
        
        # Détermination du style dominant
        dominant_color = max(scores, key=scores.get)
        
        # Mapping des couleurs DISC vers les styles de leadership
        leadership_mapping = {
            'red': {
                'primary_styles': ['Directif', 'Pace-setter'],
                'secondary_styles': ['Transactionnel'],
                'description': 'Vous êtes orienté résultats, compétitif et décidé. Vous excellez dans les situations qui demandent des décisions rapides et une forte direction.',
                'strengths': ['Décision rapide', 'Orientation résultats', 'Leadership fort', 'Gestion de crise'],
                'challenges': ['Peut être perçu comme autoritaire', 'Manque de patience', 'Néglige les relations'],
                'advice': 'Développez votre écoute active et apprenez à valoriser les relations humaines.'
            },
            'yellow': {
                'primary_styles': ['Visionnaire', 'Transformationnel', 'Coaching'],
                'secondary_styles': ['Démocratique'],
                'description': 'Vous êtes enthousiaste, inspirant et relationnel. Vous motivez les autres par votre énergie communicative et votre vision positive.',
                'strengths': ['Communication inspirante', 'Motivation des équipes', 'Créativité', 'Optimisme'],
                'challenges': ['Manque de suivi', 'Trop d\'optimisme', 'Organisation variable'],
                'advice': 'Renforcez votre sens de l\'organisation et votre capacité à suivre les détails.'
            },
            'green': {
                'primary_styles': ['Affiliatif', 'Serviteur', 'Authentique'],
                'secondary_styles': ['Démocratique'],
                'description': 'Vous êtes empathique, fiable et harmonieux. Vous créez un environnement de confiance et favorisez la coopération.',
                'strengths': ['Écoute active', 'Cohésion d\'équipe', 'Empathie', 'Fiabilité'],
                'challenges': ['Évitement des conflits', 'Difficulté à dire non', 'Lenteur décisionnelle'],
                'advice': 'Apprenez à prendre des décisions difficiles et à confronter les problèmes directement.'
            },
            'blue': {
                'primary_styles': ['Analytique', 'Situationnel'],
                'secondary_styles': ['Transactionnel'],
                'description': 'Vous êtes précis, méthodique et organisé. Vous basez vos décisions sur des faits et des données solides.',
                'strengths': ['Pensée analytique', 'Précision', 'Planification', 'Expertise technique'],
                'challenges': ['Perfectionnisme excessif', 'Lenteur d\'analyse', 'Manque de spontanéité'],
                'advice': 'Développez votre capacité à prendre des décisions rapides et à vous adapter à l\'imprévu.'
            }
        }
        
        profile = leadership_mapping[dominant_color]
        result_class = f"result-{dominant_color}"
        
        # Affichage des résultats
        st.markdown(f'<div class="{result_class}">', unsafe_allow_html=True)
        
        st.markdown(f"<h2>🎯 Votre Profil de Leadership</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='color: {'#dc2626' if dominant_color == 'red' else '#d97706' if dominant_color == 'yellow' else '#16a34a' if dominant_color == 'green' else '#2563eb'};'>Profil {dominant_color.capitalize()} - Leader {', '.join(profile['primary_styles'])}</h3>", unsafe_allow_html=True)
        
        st.markdown(f"<p><strong>Description :</strong> {profile['description']}</p>", unsafe_allow_html=True)
        
        # Section scores DISC
        st.markdown("<h4>📊 Votre profil DISC :</h4>", unsafe_allow_html=True)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            dominant_class = "disc-score-dominant" if dominant_color == 'red' else ""
            st.markdown(f'<div class="disc-score-red disc-score-box {dominant_class}"><strong>🔴 Rouge</strong><br>{scores["red"]}/10</div>', unsafe_allow_html=True)
        with col2:
            dominant_class = "disc-score-dominant" if dominant_color == 'yellow' else ""
            st.markdown(f'<div class="disc-score-yellow disc-score-box {dominant_class}"><strong>🟡 Jaune</strong><br>{scores["yellow"]}/10</div>', unsafe_allow_html=True)
        with col3:
            dominant_class = "disc-score-dominant" if dominant_color == 'green' else ""
            st.markdown(f'<div class="disc-score-green disc-score-box {dominant_class}"><strong>🟢 Vert</strong><br>{scores["green"]}/10</div>', unsafe_allow_html=True)
        with col4:
            dominant_class = "disc-score-dominant" if dominant_color == 'blue' else ""
            st.markdown(f'<div class="disc-score-blue disc-score-box {dominant_class}"><strong>🔵 Bleu</strong><br>{scores["blue"]}/10</div>', unsafe_allow_html=True)
        
        # Styles de leadership dominants
        st.markdown("<h4>🎨 Vos Styles de Leadership Dominants</h4>", unsafe_allow_html=True)
        
        cols = st.columns(2)
        for idx, style in enumerate(profile['primary_styles']):
            with cols[idx % 2]:
                st.markdown(f"""
                <div style="background: {'#fef2f2' if dominant_color == 'red' else '#fffbeb' if dominant_color == 'yellow' else '#f0fdf4' if dominant_color == 'green' else '#eff6ff'}; 
                            padding: 1rem; border-radius: 8px; border-left: 4px solid {'#dc2626' if dominant_color == 'red' else '#d97706' if dominant_color == 'yellow' else '#16a34a' if dominant_color == 'green' else '#2563eb'}; margin: 0.5rem 0;">
                    <strong>★ {style}</strong>
                </div>
                """, unsafe_allow_html=True)
        
        # Forces et défis
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h4>✅ Vos Forces</h4>", unsafe_allow_html=True)
            for strength in profile['strengths']:
                st.markdown(f"<div style='background: #f0fdf4; padding: 0.5rem; margin: 0.2rem 0; border-radius: 6px;'>✓ {strength}</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("<h4>⚠️ Défis à Relever</h4>", unsafe_allow_html=True)
            for challenge in profile['challenges']:
                st.markdown(f"<div style='background: #fef2f2; padding: 0.5rem; margin: 0.2rem 0; border-radius: 6px;'>⚠ {challenge}</div>", unsafe_allow_html=True)
        
        # Conseil de développement
        st.markdown(f"""
        <div class="conseil-box">
            <h4>💡 Conseil de Développement</h4>
            <p>{profile['advice']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# QUIZ 1 - SLIDE 23 (10 QUESTIONS)
# ==============================
with tabs[23]:
    st.markdown("""
    <div class="quiz-section">
    <h2>🧠 Quiz 1 - Fondamentaux du Leadership</h2>
    <p class="content-paragraph">Testez vos connaissances sur les bases du leadership avec ce quiz de 10 questions</p>
    </div>
    """, unsafe_allow_html=True)
    
    quiz1_questions = [
        {
            "question": "Quelle est la définition la plus précise du leadership ?",
            "options": [
                "Exercer un pouvoir hiérarchique sur des subordonnés",
                "Influencer et guider des personnes vers un objectif commun",
                "Prendre toutes les décisions importantes seul",
                "Contrôler strictement le travail des autres"
            ],
            "correct": 1,
            "explanation": "Le leadership est avant tout une capacité à influencer et guider, pas à contrôler ou dominer."
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
            "explanation": "Le leadership inspire le changement et fixe la vision, tandis que le management organise et planifie l'exécution."
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
            "explanation": "La théorie Y considère que les employés sont naturellement motivés, créatifs et cherchent à prendre des responsabilités."
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
            "explanation": "Le leadership coaching se concentre sur le développement à long terme des compétences des collaborateurs."
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
            "explanation": "L'intelligence émotionnelle permet de comprendre et gérer les émotions, essentielle pour motiver et inspirer."
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
            "explanation": "Avec une équipe compétente mais peu motivée, le style participatif qui implique l'équipe dans les décisions est le plus efficace."
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
            "explanation": "Le leadership démocratique favorise l'engagement car les collaborateurs se sentent écoutés et impliqués."
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
            "explanation": "Le leader authentique inspire par sa transparence, son intégrité et son alignement entre ses paroles et ses actions."
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
            "explanation": "Le leader serviteur met les besoins des autres en premier et considère le leadership comme un service."
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
            "explanation": "Le micro-management tue la motivation et l'autonomie, c'est une erreur fréquente des leaders débutants."
        }
    ]
    
    # Initialisation du quiz 1
    if 'quiz1_responses' not in st.session_state:
        st.session_state.quiz1_responses = [None] * len(quiz1_questions)
    if 'quiz1_score' not in st.session_state:
        st.session_state.quiz1_score = 0
    if 'show_quiz1_results' not in st.session_state:
        st.session_state.show_quiz1_results = False
    
    # Affichage des questions
    for i, q in enumerate(quiz1_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/10 :</strong> {q["question"]}</div>', unsafe_allow_html=True)
        
        options = q["options"]
        response = st.radio(
            "Choisissez votre réponse :",
            options,
            key=f"quiz1_{i}",
            index=st.session_state.quiz1_responses[i] if st.session_state.quiz1_responses[i] is not None else None
        )
        
        # Stocker la réponse
        if response in options:
            st.session_state.quiz1_responses[i] = options.index(response)
    
    # Vérifier si toutes les questions sont répondues
    all_answered = all(response is not None for response in st.session_state.quiz1_responses)
    
    if st.button("📝 Voir mes résultats du Quiz 1", key="view_quiz1_results", disabled=not all_answered):
        if not all_answered:
            st.warning("⚠️ Veuillez répondre à toutes les questions avant de voir vos résultats.")
        else:
            st.session_state.show_quiz1_results = True
            # Calcul du score
            score = 0
            for i, q in enumerate(quiz1_questions):
                if st.session_state.quiz1_responses[i] == q["correct"]:
                    score += 1
            st.session_state.quiz1_score = score
            st.rerun()
    
    # Affichage des résultats
    if st.session_state.get('show_quiz1_results', False) and all_answered:
        score = st.session_state.quiz1_score
        st.markdown(f"""
        <div class="evaluation-box">
            <h3>📊 Résultats du Quiz 1</h3>
            <p><strong>Score : {score}/10</strong></p>
            <p><strong>Pourcentage : {score * 10}%</strong></p>
        """, unsafe_allow_html=True)
        
        if score >= 9:
            st.markdown("<p>🎉 <strong>Excellent !</strong> Vous maîtrisez parfaitement les fondamentaux du leadership.</p>", unsafe_allow_html=True)
        elif score >= 7:
            st.markdown("<p>👍 <strong>Très bien !</strong> Vous avez de bonnes connaissances en leadership.</p>", unsafe_allow_html=True)
        elif score >= 5:
            st.markdown("<p>💪 <strong>Bien !</strong> Vous avez les bases, continuez à apprendre.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p>📚 <strong>À travailler.</strong> Revoyez les concepts fondamentaux.</p>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Affichage des corrections
        st.markdown("### 📖 Corrections détaillées")
        for i, q in enumerate(quiz1_questions):
            user_answer = st.session_state.quiz1_responses[i]
            is_correct = user_answer == q["correct"]
            
            st.markdown(f"""
            <div class="modern-card">
                <h4>Question {i+1} : {q['question']}</h4>
                <p><strong>Votre réponse :</strong> {q['options'][user_answer]} {'✅' if is_correct else '❌'}</p>
                <p><strong>Réponse correcte :</strong> {q['options'][q['correct']]}</p>
                <p><strong>Explication :</strong> {q['explanation']}</p>
            </div>
            """, unsafe_allow_html=True)

# ==============================
# QUIZ 2 - SLIDE 24 (10 QUESTIONS)
# ==============================
with tabs[24]:
    st.markdown("""
    <div class="quiz-section">
    <h2>🧠 Quiz 2 - Styles de Leadership Avancés</h2>
    <p class="content-paragraph">Testez vos connaissances sur les styles de leadership avec ce quiz de 10 questions</p>
    </div>
    """, unsafe_allow_html=True)
    
    quiz2_questions = [
        {
            "question": "Quel style de leadership est le plus adapté en situation de crise nécessitant une action immédiate ?",
            "options": [
                "Leadership démocratique",
                "Leadership directif",
                "Leadership laissez-faire",
                "Leadership affiliatif"
            ],
            "correct": 1,
            "explanation": "En situation de crise, le leadership directif permet de prendre des décisions rapides et d'orienter clairement l'action."
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
            "explanation": "Robert Greenleaf a développé le concept de 'Servant Leadership' où le leader sert d'abord son équipe."
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
            "explanation": "La stimulation intellectuelle pousse les collaborateurs à innover et penser différemment, clé du leadership transformationnel."
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
            "explanation": "Le leadership pace-setter, où le leader montre l'exemple à un rythme effréné, peut épuiser l'équipe qui peine à suivre."
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
            "explanation": "L'authenticité se manifeste par la transparence, l'intégrité et l'alignement entre les valeurs professées et les actions."
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
            "explanation": "Avec un débutant motivé, le style directif fournit la structure et les instructions nécessaires à l'apprentissage."
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
            "explanation": "Le leader transactionnel fonctionne sur le principe 'donnant-donnant' avec des récompenses pour les performances."
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
            "explanation": "Le laissez-faire peut mener au manque de coordination et à l'absence de vision claire pour l'équipe."
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
            "explanation": "Le leadership affiliatif se concentre sur les relations et l'harmonie, créant un environnement de travail positif."
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
            "explanation": "Un leader visionnaire excelle dans l'art de communiquer une vision qui inspire et mobilise l'équipe."
        }
    ]
    
    # Initialisation du quiz 2
    if 'quiz2_responses' not in st.session_state:
        st.session_state.quiz2_responses = [None] * len(quiz2_questions)
    if 'quiz2_score' not in st.session_state:
        st.session_state.quiz2_score = 0
    if 'show_quiz2_results' not in st.session_state:
        st.session_state.show_quiz2_results = False
    
    # Affichage des questions
    for i, q in enumerate(quiz2_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/10 :</strong> {q["question"]}</div>', unsafe_allow_html=True)
        
        options = q["options"]
        response = st.radio(
            "Choisissez votre réponse :",
            options,
            key=f"quiz2_{i}",
            index=st.session_state.quiz2_responses[i] if st.session_state.quiz2_responses[i] is not None else None
        )
        
        # Stocker la réponse
        if response in options:
            st.session_state.quiz2_responses[i] = options.index(response)
    
    # Vérifier si toutes les questions sont répondues
    all_answered = all(response is not None for response in st.session_state.quiz2_responses)
    
    if st.button("📝 Voir mes résultats du Quiz 2", key="view_quiz2_results", disabled=not all_answered):
        if not all_answered:
            st.warning("⚠️ Veuillez répondre à toutes les questions avant de voir vos résultats.")
        else:
            st.session_state.show_quiz2_results = True
            # Calcul du score
            score = 0
            for i, q in enumerate(quiz2_questions):
                if st.session_state.quiz2_responses[i] == q["correct"]:
                    score += 1
            st.session_state.quiz2_score = score
            st.rerun()
    
    # Affichage des résultats
    if st.session_state.get('show_quiz2_results', False) and all_answered:
        score = st.session_state.quiz2_score
        st.markdown(f"""
        <div class="evaluation-box">
            <h3>📊 Résultats du Quiz 2</h3>
            <p><strong>Score : {score}/10</strong></p>
            <p><strong>Pourcentage : {score * 10}%</strong></p>
        """, unsafe_allow_html=True)
        
        if score >= 9:
            st.markdown("<p>🎉 <strong>Exceptionnel !</strong> Vous maîtrisez les styles de leadership avancés.</p>", unsafe_allow_html=True)
        elif score >= 7:
            st.markdown("<p>👍 <strong>Très bon !</strong> Vous avez une excellente compréhension des différents styles.</p>", unsafe_allow_html=True)
        elif score >= 5:
            st.markdown("<p>💪 <strong>Bon !</strong> Vous connaissez les bases, continuez à vous perfectionner.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p>📚 <strong>À revoir.</strong> Étudiez les différents styles de leadership.</p>", unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Affichage des corrections
        st.markdown("### 📖 Corrections détaillées")
        for i, q in enumerate(quiz2_questions):
            user_answer = st.session_state.quiz2_responses[i]
            is_correct = user_answer == q["correct"]
            
            st.markdown(f"""
            <div class="modern-card">
                <h4>Question {i+1} : {q['question']}</h4>
                <p><strong>Votre réponse :</strong> {q['options'][user_answer]} {'✅' if is_correct else '❌'}</p>
                <p><strong>Réponse correcte :</strong> {q['options'][q['correct']]}</p>
                <p><strong>Explication :</strong> {q['explanation']}</p>
            </div>
            """, unsafe_allow_html=True)

# ==============================
# CONTENU DES AUTRES SLIDES (abrégé)
# ==============================

# Slide 2 : Introduction
with tabs[2]:
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
    
    <div class="quote-card">
    « Le leadership n'est pas un titre, c'est une responsabilité envers les autres. » — Simon Sinek
    </div>
    </div>
    """, unsafe_allow_html=True)

# Slide 3 : Définitions
with tabs[3]:
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

# [Les autres slides continuent...]

# Message final
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; margin-top: 2rem;">
<p><strong>✨ Leadership Pro - Formation Complète ✨</strong></p>
<p>Tests interactifs • 10 styles de leadership • Jeux de rôle réalistes • Outils pratiques</p>
</div>
""", unsafe_allow_html=True)
