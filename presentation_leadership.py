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
    .competence-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        margin: 1.5rem 0;
    }
    .competence-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        border-left: 4px solid #4f46e5;
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
# TEST DE LEADERSHIP NATUREL - SLIDE 0
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
    
    if 'test_score' not in st.session_state:
        st.session_state.test_score = 0
        st.session_state.test_responses = [None] * 10
    
    total_score = 0
    
    for i, q in enumerate(leadership_test_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/10 :</strong> {q["question"]}</div>', unsafe_allow_html=True)
        response = st.radio(
            "Votre réponse :",
            ["Toujours", "Souvent", "Parfois", "Rarement"],
            key=f"leadership_test_{i}",
            index=st.session_state.test_responses[i] if st.session_state.test_responses[i] is not None else None
        )
        
        # Stocker la réponse
        st.session_state.test_responses[i] = ["Toujours", "Souvent", "Parfois", "Rarement"].index(response)
        
        # Calculer le score
        total_score += q["points"][st.session_state.test_responses[i]]
    
    st.session_state.test_score = total_score
    
    if st.button("📊 Voir mes résultats du test", key="view_test_results"):
        st.session_state.show_test_results = True
    
    if st.session_state.get('show_test_results', False):
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
# TEST DISC - SLIDE 1
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
                color_class = f"color-{option['color']}"
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
        
        # Diagramme des styles
        st.markdown("""
        <div class="schema-container">
            <div class="schema-title">🎯 Diagramme des Styles de Leadership</div>
            <div style="display: flex; justify-content: center; margin: 2rem 0;">
                <div style="text-align: center;">
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
                        <div style="background: #fee2e2; padding: 1rem; border-radius: 8px; border-left: 4px solid #dc2626;">
                            <strong>🔴 Directif</strong><br>Décision rapide
                        </div>
                        <div style="background: #fef3c7; padding: 1rem; border-radius: 8px; border-left: 4px solid #d97706;">
                            <strong>🟡 Visionnaire</strong><br>Inspiration
                        </div>
                        <div style="background: #dcfce7; padding: 1rem; border-radius: 8px; border-left: 4px solid #16a34a;">
                            <strong>🟢 Affiliatif</strong><br>Relations
                        </div>
                        <div style="background: #dbeafe; padding: 1rem; border-radius: 8px; border-left: 4px solid #2563eb;">
                            <strong>🔵 Analytique</strong><br>Précision
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Vidéo recommandée
        st.markdown("""
        <div class="modern-card">
            <h3>🎥 Vidéo Recommandée</h3>
            <p>Regardez cette vidéo pour mieux comprendre votre style de leadership :</p>
            <a href="https://youtu.be/NY82yptNp5E?si=_SrSJ8F5t2RY1ywK" target="_blank" class="video-link">
                ▶ Les 10 types de leadership - Comprendre votre profil
            </a>
        </div>
        """, unsafe_allow_html=True)

# ==============================
# JEU DE RÔLE AMÉLIORÉ - SLIDE 19
# ==============================
with tabs[19]:
    st.markdown("""
    <div class="test-section">
    <h2>🎭 Jeu de Rôle - Mise en Pratique</h2>
    <p class="content-paragraph">Pratiquez les différents styles de leadership à travers des scénarios réalistes en binômes</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Scénarios de jeu de rôle améliorés
    roleplay_scenarios = [
        {
            "titre": "🚀 Lancement d'un Nouveau Projet",
            "description": "Vous devez lancer un projet innovant avec une équipe réticente au changement. Le projet est crucial pour l'avenir de l'entreprise.",
            "context": "Votre équipe de 5 personnes travaille ensemble depuis 2 ans. Les membres sont compétents mais habitués à leurs méthodes actuelles.",
            "roles": [
                "LEADER : Présenter le projet et convaincre l'équipe de son importance. Répondre aux préoccupations.",
                "COLLABORATEUR 1 : Exprimer des doutes sur les délais trop serrés",
                "COLLABORATEUR 2 : S'inquiéter de la charge de travail supplémentaire",
                "COLLABORATEUR 3 : Poser des questions techniques sur la faisabilité"
            ],
            "objectifs": [
                "Obtenir l'adhésion de l'équipe au projet",
                "Répondre aux préoccupations spécifiques",
                "Définir les premières étapes concrètes"
            ],
            "styles_recommandes": ["Visionnaire", "Coaching", "Démocratique"],
            "duree": "10 minutes",
            "conseils": "Écoutez activement chaque préoccupation. Reliez le projet à la vision d'ensemble. Montrez comment chacun peut contribuer."
        },
        {
            "titre": "🔥 Gestion de Crise Immédiate",
            "description": "Une urgence client nécessite une action immédiate et coordonnée. Le délai de résolution est de 2 heures.",
            "context": "Un client important menace de résilier son contrat suite à un problème technique critique. L'équipe est sous pression.",
            "roles": [
                "LEADER : Coordonner la réponse d'urgence, prendre des décisions rapides",
                "TECHNICIEN 1 : Analyser le problème technique",
                "TECHNICIEN 2 : Proposer des solutions immédiates", 
                "RELATION CLIENT : Gérer la communication avec le client"
            ],
            "objectifs": [
                "Résoudre le problème dans les 2 heures",
                "Maintenir la confiance du client",
                "Coordonner efficacement l'équipe"
            ],
            "styles_recommandes": ["Directif", "Pace-setter"],
            "duree": "8 minutes",
            "conseils": "Soyez clair et concis dans vos instructions. Montrez de la confiance dans les capacités de l'équipe. Gardez votre calme."
        },
        {
            "titre": "🤝 Résolution de Conflit Inter-Équipe",
            "description": "Deux membres de l'équipe sont en conflit ouvert, affectant la productivité du groupe.",
            "context": "Le conflit dure depuis 2 semaines. Les deux personnes évitent de travailler ensemble. L'ambiance est tendue.",
            "roles": [
                "LEADER : Médier le conflit et trouver une résolution",
                "COLLABORATEUR A : Se sent ignoré et sous-estimé",
                "COLLABORATEUR B : Pense que A ne fait pas sa part du travail"
            ],
            "objectifs": [
                "Rétablir la communication entre les deux parties",
                "Trouver un terrain d'entente",
                "Établir des règles de collaboration futures"
            ],
            "styles_recommandes": ["Affiliatif", "Authentique", "Serviteur"],
            "duree": "12 minutes",
            "conseils": "Créez un environnement sécurisé. Écoutez sans juger. Aidez à reformuler les positions de chacun."
        },
        {
            "titre": "💡 Session d'Innovation et Créativité",
            "description": "Brainstorming pour résoudre un problème complexe nécessitant des solutions innovantes.",
            "context": "L'entreprise cherche de nouvelles idées pour un produit. Les approches traditionnelles n'ont pas fonctionné.",
            "roles": [
                "LEADER : Faciliter la créativité sans imposer de solutions",
                "CRÉATIF 1 : Proposer des idées audacieuses mais peu pratiques",
                "CRÉATIF 2 : Avoir des idées conservatrices mais réalisables",
                "ANALYSTE : Évaluer la faisabilité des propositions"
            ],
            "objectifs": [
                "Générer au moins 10 idées nouvelles",
                "Sélectionner 3 idées prometteuses",
                "Créer un plan d'action pour les tester"
            ],
            "styles_recommandes": ["Démocratique", "Laissez-faire", "Transformationnel"],
            "duree": "15 minutes",
            "conseils": "Encouragez toutes les idées sans critique. Utilisez des techniques de créativité. Favorisez la collaboration."
        },
        {
            "titre": "📈 Amélioration des Performances",
            "description": "L'équipe n'atteint pas ses objectifs de performance depuis 3 mois consécutifs.",
            "context": "Les indicateurs sont au rouge. La motivation est basse. Certains membres commencent à se décourager.",
            "roles": [
                "LEADER : Identifier les problèmes et remotiver l'équipe",
                "PERFORMANT : Exprime sa frustration face aux mauvais résultats",
                "DÉMOTIVÉ : A perdu confiance dans la capacité du groupe à réussir",
                "OBSERVATEUR : A identifié des problèmes de processus"
            ],
            "objectifs": [
                "Identifier les causes racines des problèmes",
                "Redéfinir une stratégie claire",
                "Retrouver la motivation de l'équipe"
            ],
            "styles_recommandes": ["Coaching", "Transactionnel", "Pace-setter"],
            "duree": "10 minutes",
            "conseils": "Soyez honnête sur la situation. Reconnaissez les efforts passés. Impliquez l'équipe dans la solution."
        }
    ]
    
    # Initialisation de l'état du jeu de rôle
    if 'current_scenario' not in st.session_state:
        st.session_state.current_scenario = None
    if 'timer_active' not in st.session_state:
        st.session_state.timer_active = False
    if 'time_left' not in st.session_state:
        st.session_state.time_left = 0
    
    # Sélection du scénario
    st.markdown("### 🎯 Choisissez un Scénario")
    
    for i, scenario in enumerate(roleplay_scenarios):
        col1, col2 = st.columns([3, 1])
        with col1:
            if st.button(f"{scenario['titre']}", key=f"scenario_{i}", use_container_width=True):
                st.session_state.current_scenario = scenario
                st.session_state.timer_active = False
                st.session_state.time_left = int(scenario['duree'].split()[0]) * 60
                st.rerun()
        with col2:
            st.markdown(f"<div style='text-align: center; color: #64748b;'>{scenario['duree']}</div>", unsafe_allow_html=True)
    
    # Affichage du scénario sélectionné
    if st.session_state.current_scenario:
        scenario = st.session_state.current_scenario
        
        st.markdown(f"""
        <div class="roleplay-card">
            <h3>🎭 {scenario['titre']}</h3>
            <p><strong>Description :</strong> {scenario['description']}</p>
            <p><strong>Contexte :</strong> {scenario['context']}</p>
            <p><strong>Durée :</strong> {scenario['duree']}</p>
            <p><strong>Styles recommandés :</strong> {', '.join(scenario['styles_recommandes'])}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Objectifs
        st.markdown("### 🎯 Objectifs à Atteindre")
        for objectif in scenario['objectifs']:
            st.markdown(f"- {objectif}")
        
        # Rôles
        st.markdown("### 👥 Rôles à Distribuer")
        for role in scenario['roles']:
            st.markdown(f"""
            <div class="roleplay-scenario">
                {role}
            </div>
            """, unsafe_allow_html=True)
        
        # Conseils pour le leader
        st.markdown("### 💡 Conseils pour le Leader")
        st.markdown(f"""
        <div class="conseil-box">
            {scenario['conseils']}
        </div>
        """, unsafe_allow_html=True)
        
        # Timer
        st.markdown("### ⏱️ Timer de la Session")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("▶️ Démarrer le Timer", key="start_timer"):
                st.session_state.timer_active = True
                st.session_state.start_time = st.session_state.time_left
        
        with col2:
            if st.button("⏸️ Pause", key="pause_timer"):
                st.session_state.timer_active = False
        
        with col3:
            if st.button("🔄 Réinitialiser", key="reset_timer"):
                st.session_state.timer_active = False
                st.session_state.time_left = int(scenario['duree'].split()[0]) * 60
        
        # Affichage du timer
        if st.session_state.timer_active:
            st.session_state.time_left -= 1
            if st.session_state.time_left <= 0:
                st.session_state.timer_active = False
                st.session_state.time_left = 0
                st.balloons()
        
        minutes = st.session_state.time_left // 60
        seconds = st.session_state.time_left % 60
        
        st.markdown(f"""
        <div class="timer-box">
            ⏰ Temps restant : {minutes:02d}:{seconds:02d}
        </div>
        """, unsafe_allow_html=True)
        
        # Consignes pour le débriefing
        st.markdown("### 📝 Debriefing")
        st.markdown("""
        <div class="conseil-box">
            <h4>Questions pour le debriefing :</h4>
            <ul>
                <li>Quel style de leadership a été utilisé ? Était-il adapté ?</li>
                <li>Comment s'est senti le leader ? Les collaborateurs ?</li>
                <li>Qu'est-ce qui a bien fonctionné ? Qu'est-ce qui a été difficile ?</li>
                <li>Les objectifs ont-ils été atteints ? Pourquoi ?</li>
                <li>Quel autre style aurait pu être efficace ?</li>
                <li>Quels apprentissages pouvez-vous retenir pour la réalité ?</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    # Instructions générales
    st.markdown("---")
    st.markdown("""
    <div class="modern-card">
        <h3>📋 Instructions pour le Jeu de Rôle</h3>
        <ol class="content-list">
            <li><strong>Formez des groupes de 3-4 personnes</strong> - Un leader et des collaborateurs</li>
            <li><strong>Choisissez un scénario</strong> - Cliquez sur un des scénarios ci-dessus</li>
            <li><strong>Distribuez les rôles</strong> - Chacun joue son rôle selon la description</li>
            <li><strong>Utilisez le timer</strong> - Respectez le temps imparti</li>
            <li><strong>Débriefer</strong> - À la fin, échangez vos retours d'expérience (5-10 minutes)</li>
            <li><strong>Changez de rôles</strong> - Inversez les rôles pour le scénario suivant</li>
        </ol>
        
        <div class="example-box">
            💡 <strong>Conseil :</strong> Essayez d'utiliser différents styles de leadership pour le même scénario et comparez les résultats ! Notez ce que vous apprenez sur vous-même.
        </div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDES 20-29 : CONTENU PÉDAGOGIQUE SUPPLÉMENTAIRE
# ==============================

# Slide 20 : Compétences
with tabs[20]:
    st.markdown("""
    <div class="modern-card">
    <h2>🔑 Compétences Clés du Leader Moderne</h2>
    
    <p class="content-paragraph">Le leadership moderne repose sur un ensemble de compétences complémentaires qui se développent et s'entretiennent.</p>
    
    <div class="competence-grid">
        <div class="competence-card">
            <h4>🎯 Vision Stratégique</h4>
            <p>Capacité à anticiper les tendances et définir une direction claire.</p>
            <ul>
                <li>Pensée systémique</li>
                <li>Analyse prospective</li>
                <li>Alignement stratégique</li>
            </ul>
        </div>
        
        <div class="competence-card">
            <h4>💬 Communication Inspirante</h4>
            <p>Art de transmettre des messages qui mobilisent et engagent.</p>
            <ul>
                <li>Storytelling</li>
                <li>Écoute active</li>
                <li>Communication non-verbale</li>
            </ul>
        </div>
        
        <div class="competence-card">
            <h4>🤝 Intelligence Relationnelle</h4>
            <p>Capacité à construire et entretenir des relations de qualité.</p>
            <ul>
                <li>Empathie</li>
                <li>Résolution de conflits</li>
                <li>Construction de réseaux</li>
            </ul>
        </div>
        
        <div class="competence-card">
            <h4>⚡ Prise de Décision</h4>
            <p>Art de choisir rapidement et efficacement dans l'incertitude.</p>
            <ul>
                <li>Analyse risque/bénéfice</li>
                <li>Intuition éclairée</li>
                <li>Gestion de l'incertitude</li>
            </ul>
        </div>
        
        <div class="competence-card">
            <h4>🔄 Adaptabilité</h4>
            <p>Capacité à s'adapter aux changements et à faire évoluer son style.</p>
            <ul>
                <li>Agilité cognitive</li>
                <li>Résilience</li>
                <li>Apprentissage continu</li>
            </ul>
        </div>
        
        <div class="competence-card">
            <h4>🌟 Développement des Talents</h4>
            <p>Art de faire grandir les autres et de libérer leur potentiel.</p>
            <ul>
                <li>Mentorat</li>
                <li>Feedback constructif</li>
                <li>Délégation efficace</li>
            </ul>
        </div>
    </div>
    
    <div class="example-box">
    💡 <strong>Conseil pratique :</strong> Identifiez 2-3 compétences à développer prioritairement selon votre profil DISC et créez un plan d'action concret.
    </div>
    </div>
    """, unsafe_allow_html=True)

# Slide 21 : Intelligence Émotionnelle
with tabs[21]:
    st.markdown("""
    <div class="modern-card">
    <h2>🧠 Intelligence Émotionnelle (IE) au service du leadership</h2>
    
    <p class="content-paragraph">L'IE représente <strong>80% de la performance</strong> en leadership selon Daniel Goleman. C'est la capacité à reconnaître, comprendre et maîtriser ses propres émotions et à composer avec les émotions des autres.</p>
    
    <h3>🎯 Les 4 piliers de l'IE</h3>
    
    <div class="competence-grid">
        <div class="competence-card">
            <h4>1. Conscience de soi</h4>
            <p>Comprendre ses émotions et leur impact</p>
            <ul>
                <li>Reconnaître ses patterns émotionnels</li>
                <li>Identifier ses déclencheurs</li>
                <li>Comprendre son impact sur les autres</li>
            </ul>
        </div>
        
        <div class="competence-card">
            <h4>2. Maîtrise de soi</h4>
            <p>Gérer ses réactions émotionnelles</p>
            <ul>
                <li>Gérer le stress et l'anxiété</li>
                <li>Contrôler ses impulsions</li>
                <li>S'adapter aux changements</li>
            </ul>
        </div>
        
        <div class="competence-card">
            <h4>3. Conscience sociale</h4>
            <p>Percevoir les émotions des autres</p>
            <ul>
                <li>Décoder le langage non-verbal</li>
                <li>Comprendre les dynamiques de groupe</li>
                <li>Respecter les différences culturelles</li>
            </ul>
        </div>
        
        <div class="competence-card">
            <h4>4. Gestion des relations</h4>
            <p>Influencer positivement les émotions collectives</p>
            <ul>
                <li>Inspirer et motiver</li>
                <li>Gérer les conflits</li>
                <li>Favoriser la collaboration</li>
            </ul>
        </div>
    </div>
    
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Lors d'une restructuration, Pierre, directeur RH, reconnaît sa propre anxiété et celle de son équipe. Il organise des entretiens individuels pour rassurer et co-construire la nouvelle organisation.
    </div>
    
    <h3>🛠️ Outils pour développer votre IE</h3>
    <ul class="content-list">
    <li><strong>Journal des émotions :</strong> Notez quotidiennement vos réactions émotionnelles</li>
    <li><strong>Pause réflexive :</strong> Prenez 5 minutes avant de répondre à une situation tendue</li>
    <li><strong>Feedback 360° :</strong> Demandez à votre entourage comment vous êtes perçu</li>
    <li><strong>Méditation :</strong> Développez votre présence et votre conscience</li>
    </ul>
    
    <h3>🎥 Vidéo explicative</h3>
    <a href="https://youtu.be/UOS8X33jOZo?si=IXlKW4TF9CEi6E3h" target="_blank" class="video-link">▶ Intelligence émotionnelle pour un meilleur leadership</a>
    </div>
    """, unsafe_allow_html=True)

# Slide 22 : Études de Cas
with tabs[22]:
    st.markdown("""
    <div class="modern-card">
    <h2>📊 Études de Cas Concrets</h2>
    
    <h3>🏢 Cas 1 : Transformation Digitale chez RetailCorp</h3>
    <p class="content-paragraph"><strong>Contexte :</strong> Une PME familiale de 50 ans doit se digitaliser face à la concurrence des géants du e-commerce.</p>
    <p class="content-paragraph"><strong>Défi :</strong> Résistance au changement des équipes historiques, peur de la technologie, perte des repères.</p>
    <p class="content-paragraph"><strong>Solution :</strong> Leadership visionnaire pour inspirer + coaching progressif pour accompagner le changement.</p>
    
    <div class="example-box">
    💡 <strong>Résultat :</strong> 6 mois pour la transition complète, 90% d'adoption des nouveaux outils, augmentation de 35% de la productivité.
    </div>
    
    <h3>🏭 Cas 2 : Fusion Culturelle chez TechMerge</h3>
    <p class="content-paragraph"><strong>Contexte :</strong> Deux entreprises de cultures différentes fusionnent - startup agile et entreprise traditionnelle.</p>
    <p class="content-paragraph"><strong>Défi :</strong> Choc culturel, méthodes de travail incompatibles, tensions entre équipes.</p>
    <p class="content-paragraph"><strong>Solution :</strong> Leadership affiliatif pour créer du lien + démocratique pour co-construire la nouvelle culture.</p>
    
    <div class="example-box">
    💡 <strong>Résultat :</strong> 75% de rétention des talents clés, création d'une identité hybride performante, innovation accélérée.
    </div>
    
    <h3>🏥 Cas 3 : Crise Sanitaire à l'Hôpital Regional</h3>
    <p class="content-paragraph"><strong>Contexte :</strong> Pendant la pandémie, surcharge des services, épuisement du personnel, ressources limitées.</p>
    <p class="content-paragraph"><strong>Défi :</strong> Prendre des décisions rapides sous pression extrême tout en préservant le moral des équipes.</p>
    <p class="content-paragraph"><strong>Solution :</strong> Leadership situationnel alternant style directif (urgences) et serviteur (soutien aux équipes).</p>
    
    <div class="example-box">
    💡 <strong>Résultat :</strong> Gestion efficace de la crise, préservation de la qualité des soins, reconnaissance nationale des équipes.
    </div>
    
    <h3>🎯 Analyse Commune</h3>
    <ul class="content-list">
    <li><strong>Adaptabilité :</strong> Aucun style unique ne fonctionne dans toutes les situations</li>
    <li><strong>Authenticité :</strong> Les leaders efficaces restent fidèles à leurs valeurs</li>
    <li><strong>Résilience :</strong> La capacité à rebondir est cruciale face aux défis</li>
    <li><strong>Vision partagée :</strong> Le succès dépend de l'adhésion collective</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# Slide 23 : QUIZ 1 - Fondamentaux
with tabs[23]:
    st.markdown("""
    <div class="quiz-section">
    <h2>🧠 QUIZ 1 - Fondamentaux du Leadership</h2>
    <p class="content-paragraph">Testez vos connaissances sur les concepts de base du leadership</p>
    </div>
    """, unsafe_allow_html=True)
    
    quiz1_questions = [
        {
            "question": "Le leadership est une compétence exclusivement innée qui ne peut pas s'apprendre.",
            "correct": False,
            "explication": "❌ Faux - Des études montrent que 70% des compétences de leadership s'acquièrent par la pratique et la formation. Seulement 30% sont innées."
        },
        {
            "question": "Un leader efficace passe plus de temps à écouter qu'à parler.",
            "correct": True,
            "explication": "✅ Vrai - L'écoute active est cruciale pour comprendre les besoins de son équipe et prendre de meilleures décisions."
        },
        {
            "question": "Le leadership et le management sont deux concepts identiques.",
            "correct": False,
            "explication": "❌ Faux - Le leadership inspire les personnes et crée la vision, tandis que le management organise les processus et contrôle les résultats."
        },
        {
            "question": "L'intelligence émotionnelle est plus importante que le QI pour le succès en leadership.",
            "correct": True,
            "explication": "✅ Vrai - Daniel Goleman a démontré que l'IE représente 80% du succès en leadership contre 20% pour le QI."
        },
        {
            "question": "Un bon leader doit toujours être aimé de son équipe.",
            "correct": False,
            "explication": "❌ Faux - Un leader doit être respecté plutôt qu'aimé. Les décisions difficiles peuvent parfois créer des mécontentements temporaires."
        }
    ]
    
    if 'quiz1_responses' not in st.session_state:
        st.session_state.quiz1_responses = [None] * len(quiz1_questions)
    
    score = 0
    
    for i, q in enumerate(quiz1_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/{len(quiz1_questions)} :</strong> {q["question"]}</div>', unsafe_allow_html=True)
        
        response = st.radio(
            "Choisissez votre réponse :",
            ["Vrai", "Faux"],
            key=f"quiz1_{i}",
            index=st.session_state.quiz1_responses[i] if st.session_state.quiz1_responses[i] is not None else None
        )
        
        st.session_state.quiz1_responses[i] = ["Vrai", "Faux"].index(response)
        
        if st.session_state.get('show_answers_quiz1', False):
            if (response == "Vrai") == q["correct"]:
                st.success(f"✅ Correct! {q['explication']}")
                score += 1
            else:
                st.error(f"❌ Incorrect! {q['explication']}")
    
    if st.button("📊 Corriger le Quiz 1", key="corriger_quiz1"):
        st.session_state.show_answers_quiz1 = True
        st.rerun()
    
    if st.session_state.get('show_answers_quiz1', False):
        st.markdown(f"""
        <div class="evaluation-box">
            <h3>📈 Résultats du Quiz 1</h3>
            <p><strong>Score : {score}/{len(quiz1_questions)}</strong></p>
            <p><strong>Pourcentage : {int(score/len(quiz1_questions)*100)}%</strong></p>
            {"🎉 Excellent ! Vous maîtrisez les fondamentaux du leadership." if score >= 4 else "👍 Bon score ! Continuez à vous perfectionner." if score >= 3 else "📚 Continuez à apprendre, vous progressez !"}
        </div>
        """, unsafe_allow_html=True)

# Slide 24 : QUIZ 2 - Styles
with tabs[24]:
    st.markdown("""
    <div class="quiz-section">
    <h2>🎯 QUIZ 2 - Styles de Leadership</h2>
    <p class="content-paragraph">Testez votre capacité à identifier les styles de leadership</p>
    </div>
    """, unsafe_allow_html=True)
    
    quiz2_questions = [
        {
            "question": "Quel style de leadership convient le mieux à une équipe d'experts hautement motivés ?",
            "options": ["Directif", "Laissez-faire", "Visionnaire", "Affiliatif"],
            "correct": "Laissez-faire",
            "explication": "✅ Le style laissez-faire fonctionne bien avec des experts autonomes qui n'ont pas besoin de supervision étroite."
        },
        {
            "question": "Quel style utiliser en situation de crise nécessitant une action immédiate ?",
            "options": ["Démocratique", "Directif", "Coaching", "Affiliatif"],
            "correct": "Directif",
            "explication": "✅ Le style directif est le plus efficace en situation d'urgence où des décisions rapides doivent être prises."
        },
        {
            "question": "Quel style privilégier pour développer les compétences d'un collaborateur ?",
            "options": ["Pace-setter", "Coaching", "Transactionnel", "Laissez-faire"],
            "correct": "Coaching",
            "explication": "✅ Le style coaching est spécifiquement conçu pour développer les talents et les compétences des collaborateurs."
        },
        {
            "question": "Quel style est caractérisé par la recherche de consensus et la participation de l'équipe ?",
            "options": ["Directif", "Visionnaire", "Démocratique", "Pace-setter"],
            "correct": "Démocratique",
            "explication": "✅ Le style démocratique valorise la participation et la consultation de l'équipe dans les décisions."
        },
        {
            "question": "Quel style met l'accent sur l'harmonie et les relations dans l'équipe ?",
            "options": ["Affiliatif", "Transactionnel", "Directif", "Pace-setter"],
            "correct": "Affiliatif",
            "explication": "✅ Le style affiliatif privilégie l'harmonie, la cohésion d'équipe et le bien-être des collaborateurs."
        }
    ]
    
    if 'quiz2_responses' not in st.session_state:
        st.session_state.quiz2_responses = [None] * len(quiz2_questions)
    
    score = 0
    
    for i, q in enumerate(quiz2_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/{len(quiz2_questions)} :</strong> {q["question"]}</div>', unsafe_allow_html=True)
        
        response = st.radio(
            "Choisissez la bonne réponse :",
            q["options"],
            key=f"quiz2_{i}",
            index=st.session_state.quiz2_responses[i] if st.session_state.quiz2_responses[i] is not None else None
        )
        
        st.session_state.quiz2_responses[i] = q["options"].index(response)
        
        if st.session_state.get('show_answers_quiz2', False):
            if response == q["correct"]:
                st.success(f"✅ Correct! {q['explication']}")
                score += 1
            else:
                st.error(f"❌ Incorrect! La bonne réponse était : {q['correct']}. {q['explication']}")
    
    if st.button("📊 Corriger le Quiz 2", key="corriger_quiz2"):
        st.session_state.show_answers_quiz2 = True
        st.rerun()
    
    if st.session_state.get('show_answers_quiz2', False):
        st.markdown(f"""
        <div class="evaluation-box">
            <h3>📈 Résultats du Quiz 2</h3>
            <p><strong>Score : {score}/{len(quiz2_questions)}</strong></p>
            <p><strong>Pourcentage : {int(score/len(quiz2_questions)*100)}%</strong></p>
            {"🎉 Félicitations ! Vous maîtrisez parfaitement les styles de leadership." if score >= 4 else "👍 Bonne compréhension ! Vous identifiez bien la plupart des styles." if score >= 3 else "📚 Continuez à étudier les styles pour mieux les reconnaître."}
        </div>
        """, unsafe_allow_html=True)

# Slide 25 : Synthèse
with tabs[25]:
    st.markdown("""
    <div class="modern-card">
    <h2>🎓 Synthèse du Parcours Leadership</h2>
    
    <h3>🔑 Les 7 principes fondamentaux du leadership efficace</h3>
    
    <div class="competence-grid">
        <div class="competence-card">
            <h4>1. Adaptabilité Contextuelle</h4>
            <p>Il n'existe pas de style unique idéal. Le leader efficace adapte son approche à chaque situation, équipe et objectif.</p>
        </div>
        
        <div class="competence-card">
            <h4>2. Vision Inspirante</h4>
            <p>Un leader donne du sens et une direction. Il transforme les objectifs en vision partagée qui motive et engage.</p>
        </div>
        
        <div class="competence-card">
            <h4>3. Authenticité Cohérente</h4>
            <p>La crédité naît de l'alignement entre paroles et actions. Un leader authentique inspire confiance naturellement.</p>
        </div>
        
        <div class="competence-card">
            <h4>4. Développement Mutuel</h4>
            <p>Le vrai leadership fait grandir les autres. Investir dans le développement de son équipe est un multiplicateur de performance.</p>
        </div>
        
        <div class="competence-card">
            <h4>5. Intelligence Collective</h4>
            <p>Un leader sait qu'il ne détient pas toutes les réponses. Il active l'intelligence du groupe pour innover et résoudre.</p>
        </div>
        
        <div class="competence-card">
            <h4>6. Résilience Émotionnelle</h4>
            <p>Face aux défis et aux échecs, le leader maintient son cap et sert de point d'ancrage pour son équipe.</p>
        </div>
        
        <div class="competence-card">
            <h4>7. Impact Mesurable</h4>
            <p>Le leadership se juge aux résultats et à l'impact positif créé sur les personnes, l'organisation et la société.</p>
        </div>
    </div>
    
    <h3>🔄 Cycle d'Amélioration Continue</h3>
    <ol class="content-list">
    <li><strong>Auto-évaluation :</strong> Connais-toi toi-même (test DISC, feedback 360°)</li>
    <li><strong>Apprentissage :</strong> Étudie les styles et théories (formation, lecture)</li>
    <li><strong>Expérimentation :</strong> Pratique en situation réelle (jeux de rôle, projets)</li>
    <li><strong>Réflexion :</strong> Analyse tes succès et échecs (journal de bord, debriefing)</li>
    <li><strong>Adaptation :</strong> Ajuste ton approche (flexibilité, agilité)</li>
    </ol>
    
    <div class="quote-card">
    « Le véritable leadership ne consiste pas à avoir une position, mais à avoir une influence positive. Le plus grand privilège du leader est de servir ceux qu'il guide. »
    </div>
    
    <div class="example-box">
    💡 <strong>Prochaines étapes :</strong> Identifiez 3 actions concrètes à mettre en œuvre dans les 30 prochains jours pour développer votre leadership.
    </div>
    </div>
    """, unsafe_allow_html=True)

# Slide 26 : Secteurs d'Application
with tabs[26]:
    st.markdown("""
    <div class="modern-card">
    <h2>🏥 Leadership dans Différents Secteurs</h2>
    
    <p class="content-paragraph">Chaque secteur présente des spécificités qui influencent les styles de leadership les plus efficaces.</p>
    
    <div class="competence-grid">
        <div class="competence-card">
            <h4>💻 Technologie & Startups</h4>
            <p><strong>Styles dominants :</strong> Visionnaire + Laissez-faire</p>
            <p><strong>Caractéristiques :</strong> Innovation rapide, équipes experts, environnement VUCA</p>
            <p><strong>Défis :</strong> Gérer l'incertitude, maintenir l'innovation, rétention des talents</p>
            <p><strong>Exemple :</strong> Satya Nadella chez Microsoft - transformation culturelle</p>
        </div>
        
        <div class="competence-card">
            <h4>🏭 Industrie & Manufacturing</h4>
            <p><strong>Styles dominants :</strong> Directif + Démocratique</p>
            <p><strong>Caractéristiques :</strong> Processus structurés, sécurité critique, optimisation continue</p>
            <p><strong>Défis :</strong> Digitalisation, amélioration continue, sécurité des équipes</p>
            <p><strong>Exemple :</strong> Carlos Ghosn chez Renault-Nissan - turnaround industriel</p>
        </div>
        
        <div class="competence-card">
            <h4>🏥 Santé & Médical</h4>
            <p><strong>Styles dominants :</strong> Affiliatif + Coaching</p>
            <p><strong>Caractéristiques :</strong> Haut niveau d'expertise, pression émotionnelle, travail d'équipe</p>
            <p><strong>Défis :</strong> Burnout professionnel, coordination interdisciplinaire, innovation médicale</p>
            <p><strong>Exemple :</strong> Dr. Denis Mukwege - leadership humanitaire et médical</p>
        </div>
        
        <div class="competence-card">
            <h4>🎓 Éducation & Formation</h4>
            <p><strong>Styles dominants :</strong> Visionnaire + Coaching</p>
            <p><strong>Caractéristiques :</strong> Développement humain, autonomie professionnelle, impact sociétal</p>
            <p><strong>Défis :</strong> Adaptation pédagogique, motivation des équipes, ressources limitées</p>
            <p><strong>Exemple :</strong> Ken Robinson - leadership éducatif et innovation pédagogique</p>
        </div>
        
        <div class="competence-card">
            <h4>🏛️ Public & Associatif</h4>
            <p><strong>Styles dominants :</strong> Serviteur + Démocratique</p>
            <p><strong>Caractéristiques :</strong> Mission de service, complexité administrative, multiples parties prenantes</p>
            <p><strong>Défis :</strong> Contraintes budgétaires, lourdeur administrative, impact social</p>
            <p><strong>Exemple :</strong> Jacinda Ardern - leadership politique empathique</p>
        </div>
        
        <div class="competence-card">
            <h4>💼 Services & Conseil</h4>
            <p><strong>Styles dominants :</strong> Coaching + Transactionnel</p>
            <p><strong>Caractéristiques :</strong> Relation client, expertise pointue, facturation au résultat</p>
            <p><strong>Défis :</strong> Fidélisation clients, développement commercial, qualité de service</p>
            <p><strong>Exemple :</strong> Sheryl Sandberg chez Facebook - leadership opérationnel</p>
        </div>
    </div>
    
    <h3>🌍 Tendances Transversales</h3>
    <ul class="content-list">
    <li><strong>Digitalisation :</strong> Tous les secteurs sont impactés par la transformation digitale</li>
    <li><strong>Durabilité :</strong> Le leadership responsable devient une exigence dans tous les domaines</li>
    <li><strong>Diversité :</strong> L'inclusion et la diversité sont des leviers de performance reconnus</li>
    <li><strong>Agilité :</strong> La capacité d'adaptation rapide est désormais cruciale partout</li>
    </ul>
    
    <div class="example-box">
    💡 <strong>Conseil :</strong> Analysez votre secteur et identifiez les compétences de leadership les plus valorisées. Développez-les tout en conservant votre authenticité.
    </div>
    </div>
    """, unsafe_allow_html=True)

# Slide 27 : Erreurs Courantes
with tabs[27]:
    st.markdown("""
    <div class="modern-card">
    <h2>🚫 Erreurs Courantes en Leadership</h2>
    
    <p class="content-paragraph">Identifier et éviter ces pièges courants peut accélérer votre développement en leadership.</p>
    
    <h3>❌ Les 10 pièges à éviter absolument</h3>
    
    <div class="competence-grid">
        <div class="competence-card">
            <h4>1. Micro-management</h4>
            <p><strong>Symptômes :</strong> Contrôle excessif, manque de délégation, étouffement de l'autonomie</p>
            <p><strong>Impact :</strong> Démotivation, dépendance, burnout des collaborateurs</p>
            <p><strong>Solution :</strong> Déléguer avec confiance, définir des objectifs clairs, accepter les erreurs</p>
        </div>
        
        <div class="competence-card">
            <h4>2. Incohérence</h4>
            <p><strong>Symptômes :</strong> Paroles ≠ actions, règles changeantes, favoritisme</p>
            <p><strong>Impact :</strong> Perte de crédibilité, confusion, climat de méfiance</p>
            <p><strong>Solution :</strong> Alignement valeurs-actions, transparence, constance</p>
        </div>
        
        <div class="competence-card">
            <h4>3. Manque de reconnaissance</h4>
            <p><strong>Symptômes :</strong> Focus uniquement sur les problèmes, oubli des succès</p>
            <p><strong>Impact :</strong> Démotivation, sentiment d'injustice, turnover</p>
            <p><strong>Solution :</strong> Célébrer les succès, feedback positif régulier, reconnaissance personnalisée</p>
        </div>
        
        <div class="competence-card">
            <h4>4. Communication insuffisante</h4>
            <p><strong>Symptômes :</strong> Information gardée, rumeurs, surprises désagréables</p>
            <p><strong>Impact :</strong> Anxiété, perte d'engagement, mauvaises décisions</p>
            <p><strong>Solution :</strong> Sur-communiquer, être transparent, créer des canaux ouverts</p>
        </div>
        
        <div class="competence-card">
            <h4>5. Évitement des conflits</h4>
            <p><strong>Symptômes :</strong> Ignorer les tensions, reporter les discussions difficiles</p>
            <p><strong>Impact :</strong> Problèmes non résolus, climat toxique, explosion ultérieure</p>
            <p><strong>Solution :</strong> Adresser rapidement, écouter toutes les parties, rechercher des solutions</p>
        </div>
        
        <div class="competence-card">
            <h4>6. Style unique</h4>
            <p><strong>Symptômes :</strong> Même approche dans toutes les situations, rigidité</p>
            <p><strong>Impact :</strong> Inefficacité contextuelle, frustration des équipes</p>
            <p><strong>Solution :</strong> Développer sa flexibilité, adapter son style, être situationnel</p>
        </div>
        
        <div class="competence-card">
            <h4>7. Négligence du développement</h4>
            <p><strong>Symptômes :</strong> Arrêt des apprentissages, routine, stagnation</p>
            <p><strong>Impact :</strong> Obsolescence des compétences, manque d'inspiration</p>
            <p><strong>Solution :</strong> Formation continue, lecture, mentorat, réflexion</p>
        </div>
        
        <div class="competence-card">
            <h4>8. Prise de décision solitaire</h4>
            <p><strong>Symptômes :</strong> Décisions unilatérales, non-consultation de l'équipe</p>
            <p><strong>Impact :</strong> Manque d'adhésion, solutions sous-optimales, frustration</p>
            <p><strong>Solution :</strong> Impliquer l'équipe, co-construction, expliquer les décisions</p>
        </div>
        
        <div class="competence-card">
            <h4>9. Surprotection des collaborateurs</h4>
            <p><strong>Symptômes :</strong> Éviter les challenges, protéger des feedbacks difficiles</p>
            <p><strong>Impact :</strong> Stagnation professionnelle, manque de résilience</p>
            <p><strong>Solution :</strong> Donner des défis, feedback honnête, soutenir la croissance</p>
        </div>
        
        <div class="competence-card">
            <h4>10. Oubli de soi-même</h4>
            <p><strong>Symptômes :</strong> Négligence santé personnelle, déséquilibre vie pro/perso</p>
            <p><strong>Impact :</strong> Burnout, mauvaise exemplarité, baisse de performance</p>
            <p><strong>Solution :</strong> Auto-soin, boundaries claires, équilibre de vie</p>
        </div>
    </div>
    
    <h3>🛡️ Stratégie de Prévention</h3>
    <ul class="content-list">
    <li><strong>Auto-réflexion régulière :</strong> Prendre du recul pour identifier ses patterns</li>
    <li><strong>Feedback continu :</strong> Solliciter activement les retours de son équipe</li>
    <li><strong>Mentorat :</strong> Bénéficier de l'expérience de leaders plus expérimentés</li>
    <li><strong>Apprentissage par les erreurs :</strong> Transformer les échecs en apprentissages</li>
    <li><strong>Communauté de pratique :</strong> Échanger avec d'autres leaders sur les défis</li>
    </ul>
    
    <div class="example-box">
    💡 <strong>Exercice pratique :</strong> Identifiez 2-3 erreurs que vous avez tendance à commettre et créez un plan d'action concret pour les corriger.
    </div>
    </div>
    """, unsafe_allow_html=True)

# Slide 28 : Conseils
with tabs[28]:
    st.markdown("""
    <div class="modern-card">
    <h2>💡 Conseils Pratiques pour Développer votre Leadership</h2>
    
    <p class="content-paragraph">Le leadership se développe par la pratique consciente et l'apprentissage continu. Voici des conseils concrets pour progresser.</p>
    
    <h3>🎯 10 Conseils Actionnables</h3>
    
    <div class="competence-grid">
        <div class="competence-card">
            <h4>1. Pratiquez l'écoute active</h4>
            <p><strong>Action :</strong> Lors des réunions, consacrez 70% du temps à écouter, 30% à parler</p>
            <p><strong>Technique :</strong> Reformulez ce que vous entendez avant de répondre</p>
            <p><strong>Bénéfice :</strong> Meilleure compréhension, décisions plus éclairées</p>
        </div>
        
        <div class="competence-card">
            <h4>2. Donnez du feedback régulier</h4>
            <p><strong>Action :</strong> Offrez du feedback constructif à chaque collaborateur toutes les 2 semaines</p>
            <p><strong>Technique :</strong> Méthode "Sandwich" (positif → amélioration → positif)</p>
            <p><strong>Bénéfice :</strong> Amélioration continue, motivation accrue</p>
        </div>
        
        <div class="competence-card">
            <h4>3. Développez votre intelligence émotionnelle</h4>
            <p><strong>Action :</strong> Tenez un journal des émotions pendant 30 jours</p>
            <p><strong>Technique :</strong> Identifiez vos déclencheurs émotionnels et leurs impacts</p>
            <p><strong>Bénéfice :</strong> Meilleure gestion des relations et des conflits</p>
        </div>
        
        <div class="competence-card">
            <h4>4. Communiquez clairement votre vision</h4>
            <p><strong>Action :</strong> Créez un "pitch" de 2 minutes expliquant votre vision</p>
            <p><strong>Technique :</strong> Utilisez des métaphores et des histoires inspirantes</p>
            <p><strong>Bénéfice :</strong> Alignement et engagement de l'équipe</p>
        </div>
        
        <div class="competence-card">
            <h4>5. Déléguez efficacement</h4>
            <p><strong>Action :</strong> Identifiez 3 tâches à déléguer cette semaine</p>
            <p><strong>Technique :</strong> Méthode "Déléguer le quoi, pas le comment"</p>
            <p><strong>Bénéfice :</strong> Développement des collaborateurs, gain de temps</p>
        </div>
        
        <div class="competence-card">
            <h4>6. Investissez dans votre développement</h4>
            <p><strong>Action :</strong> Lisez un livre de leadership par mois</p>
            <p><strong>Technique :</strong> Appliquez une idée concrète de chaque livre lu</p>
            <p><strong>Bénéfice :</strong> Amélioration continue des compétences</p>
        </div>
        
        <div class="competence-card">
            <h4>7. Créez un environnement sûr</h4>
            <p><strong>Action :</strong> Célébrez les échecs comme des opportunités d'apprentissage</p>
            <p><strong>Technique :</strong> Organisez des "post-mortems" sans blame</p>
            <p><strong>Bénéfice :</strong> Innovation et prise de risque calculée</p>
        </div>
        
        <div class="competence-card">
            <h4>8. Adaptez votre style</h4>
            <p><strong>Action :</strong> Analysez chaque situation avant de choisir votre approche</p>
            <p><strong>Technique :</strong> Utilisez la grille des styles de leadership comme guide</p>
            <p><strong>Bénéfice :</strong> Efficacité contextuelle améliorée</p>
        </div>
        
        <div class="competence-card">
            <h4>9. Construisez votre réseau</h4>
            <p><strong>Action :</strong> Prenez un café mensuel avec un leader que vous admirez</p>
            <p><strong>Technique :</strong> Approche "Comment puis-je vous aider ?" plutôt que "Que pouvez-vous faire pour moi ?"</p>
            <p><strong>Bénéfice :</strong> Apprentissages accélérés, opportunités</p>
        </div>
        
        <div class="competence-card">
            <h4>10. Prenez soin de vous</h4>
            <p><strong>Action :</strong> Bloquez 30 minutes par jour pour votre bien-être</p>
            <p><strong>Technique :</strong> Méditation, exercice, lecture personnelle</p>
            <p><strong>Bénéfice :</strong> Énergie durable, exemplarité</p>
        </div>
    </div>
    
    <h3>📅 Plan d'Action sur 90 Jours</h3>
    <ul class="content-list">
    <li><strong>Mois 1 :</strong> Focus sur l'écoute active et le feedback régulier</li>
    <li><strong>Mois 2 :</strong> Développement de l'intelligence émotionnelle et de la délégation</li>
    <li><strong>Mois 3 :</strong> Perfectionnement de la communication visionnaire et de l'adaptabilité</li>
    </ul>
    
    <h3>🎥 Vidéos sur les styles</h3>
    <a href="https://youtu.be/vilZazhIjoc?si=b4PNNY5P8SAqu9_p" target="_blank" class="video-link">▶ Les 5 styles de leadership</a>
    <a href="https://youtu.be/2tDKptsgvVU?si=fSS4rwyv7EM9biy9" target="_blank" class="video-link">▶ Les compétences d'un leader</a>
    <a href="https://youtu.be/UOS8X33jOZo?si=IXlKW4TF9CEi6E3h" target="_blank" class="video-link">▶ Intelligence émotionnelle</a>
    
    <div class="example-box">
    💡 <strong>Prochain pas :</strong> Choisissez 3 conseils à mettre en œuvre immédiatement et planifiez-les dans votre agenda.
    </div>
    </div>
    """, unsafe_allow_html=True)

# Slide 29 : Ressources
with tabs[29]:
    st.markdown("""
    <div class="modern-card">
    <h2>📚 Ressources Complémentaires</h2>
    
    <p class="content-paragraph">Approfondissez vos connaissances avec ces ressources soigneusement sélectionnées.</p>
    
    <h3>🎥 Toutes les vidéos recommandées</h3>
    
    <div class="competence-grid">
        <div class="competence-card">
            <h4>📖 Fondamentaux</h4>
            <a href="https://youtu.be/hCtFbHJQHvk?si=r00mEZ8Mnnzecd1I" target="_blank" class="video-link">▶ Définition d'un leader</a>
            <a href="https://youtu.be/Ej9M-U1EiGY?si=kgqe2lA8Pe6oF26Q" target="_blank" class="video-link">▶ Définition du leadership</a>
            <a href="https://youtu.be/mhkLc0HEtR0?si=n4rAkltZW8gIGu7g" target="_blank" class="video-link">▶ Différence leader/management</a>
        </div>
        
        <div class="competence-card">
            <h4>🎨 Styles de Leadership</h4>
            <a href="https://youtu.be/vilZazhIjoc?si=b4PNNY5P8SAqu9_p" target="_blank" class="video-link">▶ Les 5 styles de leadership</a>
            <a href="https://youtu.be/iRBQqfJaoo4?si=Kbhele-WRaC6wqGw" target="_blank" class="video-link">▶ Leadership situationnel</a>
            <a href="https://youtu.be/NY82yptNp5E?si=_SrSJ8F5t2RY1ywK" target="_blank" class="video-link">▶ Les 10 types de leadership</a>
        </div>
        
        <div class="competence-card">
            <h4>🔧 Compétences</h4>
            <a href="https://youtu.be/2tDKptsgvVU?si=fSS4rwyv7EM9biy9" target="_blank" class="video-link">▶ Les compétences d'un leader</a>
            <a href="https://youtu.be/UOS8X33jOZo?si=IXlKW4TF9CEi6E3h" target="_blank" class="video-link">▶ Intelligence émotionnelle</a>
            <a href="https://youtu.be/6T9TyL1g0Qc?si=J6QY0w8m9Z9qy5Q6" target="_blank" class="video-link">▶ Communication efficace</a>
        </div>
        
        <div class="competence-card">
            <h4>🚀 Inspiration</h4>
            <a href="https://youtu.be/7sxpKhDbr0Q?si=8t5Y5q5y5y5y5y5y" target="_blank" class="video-link">▶ Leaders inspirants</a>
            <a href="https://youtu.be/3Kk6f7q4lq4?si=4lq4lq4lq4lq4lq4" target="_blank" class="video-link">▶ Histoires de leadership</a>
            <a href="https://youtu.be/5Y5Y5Y5Y5Y5?si=5Y5Y5Y5Y5Y5Y5Y5Y" target="_blank" class="video-link">▶ Futur du leadership</a>
        </div>
    </div>
    
    <h3>📚 Livres Essentiels</h3>
    
    <div class="competence-grid">
        <div class="competence-card">
            <h4>🏆 Classiques</h4>
            <ul>
                <li><strong>"Le Leader du Futur"</strong> - Peter Drucker</li>
                <li><strong>"Les 7 Habitudes des Gens Efficaces"</strong> - Stephen Covey</li>
                <li><strong>"Start with Why"</strong> - Simon Sinek</li>
                <li><strong>"Leadership"</strong> - James McGregor Burns</li>
            </ul>
        </div>
        
        <div class="competence-card">
            <h4>🧠 Intelligence Émotionnelle</h4>
            <ul>
                <li><strong>"L'intelligence Emotionnelle"</strong> - Daniel Goleman</li>
                <li><strong>"Leadership Émotionnel"</strong> - Richard Boyatzis</li>
                <li><strong>"Présence"</strong> - Amy Cuddy</li>
            </ul>
        </div>
        
        <div class="competence-card">
            <h4>🔄 Leadership Moderne</h4>
            <ul>
                <li><strong>"Le Leadership Authentique"</strong> - Bill George</li>
                <li><strong>"Lean In"</strong> - Sheryl Sandberg</li>
                <li><strong>"Dare to Lead"</strong> - Brené Brown</li>
                <li><strong>"Leaders Eat Last"</strong> - Simon Sinek</li>
            </ul>
        </div>
        
        <div class="competence-card">
            <h4>⚡ Pratique</h4>
            <ul>
                <li><strong>"The First 90 Days"</strong> - Michael Watkins</li>
                <li><strong>"Radical Candor"</strong> - Kim Scott</li>
                <li><strong>"Extreme Ownership"</strong> - Jocko Willink</li>
            </ul>
        </div>
    </div>
    
    <h3>🛠️ Outils Pratiques</h3>
    
    <div class="competence-grid">
        <div class="competence-card">
            <h4>📊 Auto-évaluation</h4>
            <ul>
                <li>Test DISC (inclus dans cette formation)</li>
                <li>MBTI (Myers-Briggs Type Indicator)</li>
                <li>360° Feedback tools</li>
                <li>Leadership Circle Profile</li>
            </ul>
        </div>
        
        <div class="competence-card">
            <h4>📝 Templates</h4>
            <ul>
                <li>Plan de développement personnel</li>
                <li>Grille d'évaluation des compétences</li>
                <li>Template de feedback constructif</li>
                <li>Journal de réflexion leadership</li>
            </ul>
        </div>
        
        <div class="competence-card">
            <h4>👥 Communautés</h4>
            <ul>
                <li>LinkedIn Leadership Groups</li>
                <li>Toastmasters International</li>
                <li>Professional Associations</li>
                <li>Mentoring programs</li>
            </ul>
        </div>
        
        <div class="competence-card">
            <h4>🎓 Formations</h4>
            <ul>
                <li>Cours en ligne (Coursera, EdX)</li>
                <li>Certifications leadership</li>
                <li>Programmes exécutifs</li>
                <li>Coaching individuel</li>
            </ul>
        </div>
    </div>
    
    <div class="quote-card">
    « L'investissement le plus important que vous puissiez faire est d'investir en vous-même. Votre croissance personnelle et professionnelle est le meilleur garant de votre succès en leadership. »
    </div>
    
    <div class="example-box">
    💡 <strong>Action recommandée :</strong> Créez votre plan de développement personnel en sélectionnant 3 ressources à explorer dans le mois à venir.
    </div>
    </div>
    """, unsafe_allow_html=True)

# Message final
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; margin-top: 2rem;">
<p><strong>✨ Leadership Pro - Formation Complète ✨</strong></p>
<p>Tests interactifs • 10 styles de leadership • Jeux de rôle réalistes • Outils pratiques</p>
</div>
""", unsafe_allow_html=True)

