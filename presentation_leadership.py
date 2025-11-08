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
        
        # Affichage des résultats avec Streamlit native pour éviter les problèmes d'HTML
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
# SLIDES 2-18 : CONTENU DES STYLES DE LEADERSHIP
# ==============================

# Données pour les 10 styles de leadership
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
        "exemple": "Une cheffe d'équipe qui organise des déjeuners d'équipe réguliers et célèbre les succès personnels.",
        "couleur": "#3B82F6",
        "utilisation": "Idéal pour : résoudre les conflits, renforcer la cohésion, créer un environnement positif."
    },
    {
        "name": "Démocratique",
        "slogan": "« Qu'en pensez-vous ? »",
        "description": "Le leader démocratique valorise la participation et la collaboration. Il consulte son équipe avant de prendre des décisions importantes et encourage le partage d'idées.",
        "forces": ["Meilleures décisions collectives", "Fort engagement de l'équipe", "Innovation et créativité", "Respect mutuel"],
        "faiblesses": ["Lenteur du processus décisionnel", "Difficile en situation d'urgence", "Risque de consensus mou"],
        "exemple": "Chez Google, les équipes utilisent des votes et consultations pour les décisions importantes.",
        "couleur": "#6366F1",
        "utilisation": "Idéal pour : prendre des décisions importantes, impliquer l'équipe, favoriser l'innovation."
    },
    {
        "name": "Directif",
        "slogan": "« Faites ce que je vous dis »",
        "description": "Le leader directif donne des instructions claires et spécifiques. Il attend une exécution précise et contrôle étroitement le travail. Efficace en situation de crise.",
        "forces": ["Décisions rapides", "Clarté des attentes", "Efficace en urgence", "Contrôle serré"],
        "faiblesses": ["Démotivant à long terme", "Tue l'initiative", "Faible développement des collaborateurs", "Résistance passive"],
        "exemple": "Lors de l'incendie de Notre-Dame de Paris, les pompiers ont suivi des ordres directs et précis.",
        "couleur": "#EF4444",
        "utilisation": "Idéal pour : situations de crise, équipes inexpérimentées, besoin de résultats immédiats."
    },
    {
        "name": "Pace-setter",
        "slogan": "« Faites comme moi, maintenant ! »",
        "description": "Le leader pace-setter établit des standards d'excellence très élevés et montre l'exemple. Il s'attend à ce que l'équipe suive son rythme et sa qualité de travail.",
        "forces": ["Haute performance", "Résultats rapides", "Excellence technique", "Auto-motivation"],
        "faiblesses": ["Épuisement de l'équipe", "Manque de délégation", "Démotivation si standards trop hauts", "Faible collaboration"],
        "exemple": "Steve Jobs était connu pour ses standards d'excellence extrêmement élevés chez Apple.",
        "couleur": "#F59E0B",
        "utilisation": "Idéal pour : équipes très compétentes et motivées, besoin de résultats rapides de haute qualité."
    },
    {
        "name": "Transformationnel",
        "slogan": "« Ensemble, transformons notre réalité »",
        "description": "Le leader transformationnel inspire un changement profond en challengeant les statu quo et en encourageant l'innovation radicale. Il transforme les individus et l'organisation.",
        "forces": ["Changement profond et durable", "Innovation disruptive", "Développement des leaders", "Vision à long terme"],
        "faiblesses": ["Résistance au changement", "Difficile à maintenir", "Nécessite une forte adhésion", "Risque de burnout"],
        "exemple": "Jacques Servier a transformé l'industrie pharmaceutique française par son approche innovante.",
        "couleur": "#7C3AED",
        "utilisation": "Idéal pour : conduire des changements majeurs, innover radicalement, développer une culture forte."
    },
    {
        "name": "Transactionnel",
        "slogan": "« Vous serez récompensé pour vos résultats »",
        "description": "Le leader transactionnel fonctionne sur un système de récompenses et punitions basé sur la performance. Il établit des objectifs clairs et des incitations correspondantes.",
        "forces": ["Clarté des attentes", "Performance mesurable", "Efficacité à court terme", "Système équitable"],
        "faiblesses": ["Limite la créativité", "Relation transactionnelle", "Démotivation si récompenses insuffisantes", "Focus court terme"],
        "exemple": "Les systèmes de commissions dans les ventes où les performances sont directement récompensées.",
        "couleur": "#6B7280",
        "utilisation": "Idéal pour : environnements très structurés, objectifs clairs et mesurables, récompenses basées sur la performance."
    },
    {
        "name": "Authentique",
        "slogan": "« Je suis vrai et transparent »",
        "description": "Le leader authentique montre sa vulnérabilité, admet ses erreurs et reste fidèle à ses valeurs. Il construit la confiance par sa transparence et son intégrité.",
        "forces": ["Confiance élevée", "Loyauté de l'équipe", "Culture d'apprentissage", "Respect authentique"],
        "faiblesses": ["Vulnérabilité peut être perçue comme faiblesse", "Difficile dans certaines cultures", "Nécessite une grande maturité"],
        "exemple": "Brené Brown, chercheuse qui prône le leadership vulnérable et authentique.",
        "couleur": "#059669",
        "utilisation": "Idéal pour : construire la confiance, créer une culture transparente, développer des relations authentiques."
    },
    {
        "name": "Serviteur",
        "slogan": "« Je suis là pour vous servir »",
        "description": "Le leader serviteur met les besoins de son équipe avant les siens. Il se concentre sur le développement et le bien-être des collaborateurs pour atteindre les objectifs.",
        "forces": ["Engagement exceptionnel", "Développement des talents", "Culture de service", "Rétention des talents"],
        "faiblesses": ["Peut manquer d'autorité", "Difficile dans les structures hiérarchiques", "Risque d'épuisement du leader"],
        "exemple": "Nelson Mandela qui a toujours mis les besoins de son peuple avant les siens.",
        "couleur": "#0EA5E9",
        "utilisation": "Idéal pour : développer les talents, créer un engagement profond, construire une culture de service."
    }
]

# Création des slides pour chaque style (slides 7-16)
for i, style in enumerate(leadership_styles_data):
    with tabs[7 + i]:  # Les styles commencent à l'onglet 7
        st.markdown(f"""
        <div class="modern-card">
            <h2>🎨 Style {style['name']}</h2>
            <p style="font-size:1.3rem; font-weight:600; color:{style['couleur']}; margin:1rem 0;">
                {style['slogan']}
            </p>
            <p class="content-paragraph">{style['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Exemple concret
        st.markdown(f"""
        <div class="example-box">
            💡 <strong>Exemple concret :</strong> {style['exemple']}
        </div>
        """, unsafe_allow_html=True)
        
        # Forces et défis
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
        
        # Quand utiliser ce style
        st.markdown("<h4>🎯 Quand utiliser ce style ?</h4>", unsafe_allow_html=True)
        st.markdown(f"<p class='content-paragraph'>{style['utilisation']}</p>", unsafe_allow_html=True)

# ==============================
# SLIDES 17-18 : SITUATIONNEL ET LAISSEZ-FAIRE
# ==============================

# Slide 17 : Leadership Situationnel
with tabs[17]:
    st.markdown("""
    <div class="modern-card">
    <h2>🔄 Leadership Situationnel</h2>
    <p style="font-size:1.3rem; font-weight:600; color:#7C3AED; margin:1rem 0;">
        « Adaptons notre style à la situation »
    </p>
    
    <p class="content-paragraph">Le leader situationnel adapte son style en fonction de la maturité, des compétences et de la motivation de ses collaborateurs, ainsi que du contexte.</p>
    
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Un manager utilise un style directif avec un nouveau collaborateur (faible compétence, forte motivation) et délégatif avec un expert expérimenté (forte compétence, forte motivation).
    </div>
    
    <h3>📈 Les 4 niveaux de développement</h3>
    <ul class="content-list">
    <li><strong>D1 :</strong> Faible compétence, forte motivation → Style directif</li>
    <li><strong>D2 :</strong> Faible à moyenne compétence, faible motivation → Style persuasif</li>
    <li><strong>D3 :</strong> Moyenne à forte compétence, motivation variable → Style participatif</li>
    <li><strong>D4 :</strong> Forte compétence, forte motivation → Style délégatif</li>
    </ul>
    """, unsafe_allow_html=True)
    
    # Forces et défis pour le style situationnel
    st.markdown("""
    <div class="forces-defis-grid">
        <div class="forces-box">
            <h4>✅ Forces</h4>
            <ul class="content-list">
                <li>Adaptation optimale à chaque situation</li>
                <li>Développement progressif des collaborateurs</li>
                <li>Efficacité contextuelle</li>
                <li>Respect des individualités</li>
            </ul>
        </div>
        <div class="defis-box">
            <h4>⚠️ Défis</h4>
            <ul class="content-list">
                <li>Nécessite une grande flexibilité</li>
                <li>Complexe à maîtriser</li>
                <li>Demande une bonne analyse des situations</li>
                <li>Risque d'incohérence perçue</li>
            </ul>
        </div>
    </div>
    
    <h4>🎯 Quand utiliser ce style ?</h4>
    <p class="content-paragraph">
        Idéal pour : adapter son leadership à chaque collaborateur, développer progressivement les compétences, gérer des équipes hétérogènes.
    </p>
    
    <h3>🎥 Vidéo explicative</h3>
    <a href="https://youtu.be/iRBQqfJaoo4?si=Kbhele-WRaC6wqGw" target="_blank" class="video-link">▶ Le leadership situationnel</a>
    </div>
    """, unsafe_allow_html=True)

# Slide 18 : Laissez-faire
with tabs[18]:
    st.markdown("""
    <div class="modern-card">
    <h2>🎨 Style Laissez-faire</h2>
    <p style="font-size:1.3rem; font-weight:600; color:#6B7280; margin:1rem 0;">
        « À toi de jouer »
    </p>
    <p class="content-paragraph">Le leader laissez-faire donne une autonomie totale à son équipe. Il fournit les ressources nécessaires mais intervient peu dans le travail quotidien.</p>
    
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Chez Pixar, les réalisateurs ont une liberté créative totale pour développer leurs projets.
    </div>
    """, unsafe_allow_html=True)
    
    # Forces et défis pour le style laissez-faire
    st.markdown("""
    <div class="forces-defis-grid">
        <div class="forces-box">
            <h4>✅ Forces</h4>
            <ul class="content-list">
                <li>Autonomie et créativité</li>
                <li>Responsabilisation des équipes</li>
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
        Idéal pour : équipes d'experts très compétents et motivés, environnements créatifs, projets innovants nécessitant de l'autonomie.
    </p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# SLIDES 2-6 : CONTENU THÉORIQUE
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

# Slide 4 : Leadership vs Management
with tabs[4]:
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

# Slide 5 : Leadership vs Commandement
with tabs[5]:
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
    💡 <strong>Exemple concret :</strong> Dans l'armée, un sergent utilise le commandement (ordres) alors qu'un caporal chef peut développer du leadership (respect gagné).
    </div>
    
    <div class="quote-card">
    « Le commandement fait respecter les règles, le leadership fait adhérer aux valeurs. »
    </div>
    </div>
    """, unsafe_allow_html=True)

# Slide 6 : Théories X et Y de McGregor
with tabs[6]:
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
# SLIDES 20-29 : CONTENU PÉDAGOGIQUE SUPPLÉMENTAIRE
# ==============================

# Slide 20 : Compétences
with tabs[20]:
    st.markdown("""
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

# Slide 21 : Intelligence Émotionnelle
with tabs[21]:
    st.markdown("""
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

# Slide 22 : Études de Cas
with tabs[22]:
    st.markdown("""
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

# Slide 23 : QUIZ 1 - Fondamentaux
with tabs[23]:
    st.markdown("""
    <div class="quiz-section">
    <h2>🧠 QUIZ 1 - Fondamentaux du Leadership</h2>
    <p class="content-paragraph">Testez vos connaissances sur les concepts de base du leadership (10 questions)</p>
    </div>
    """, unsafe_allow_html=True)
    
    quiz1_questions = [
        {
            "question": "Le leadership est une compétence exclusivement innée qui ne peut pas s'apprendre.",
            "correct": False,
            "explication": "❌ Faux - Des études montrent que 70% des compétences de leadership s'acquièrent par la pratique et la formation."
        },
        {
            "question": "Un leader efficace passe plus de temps à écouter qu'à parler.",
            "correct": True,
            "explication": "✅ Vrai - L'écoute active est cruciale pour comprendre les besoins de son équipe."
        }
    ]
    
    for i, q in enumerate(quiz1_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/10 :</strong> {q["question"]}</div>', unsafe_allow_html=True)
        rep = st.radio(f"Choisissez votre réponse :", ["Vrai", "Faux"], key=f"quiz1_{i}")
        
        if st.session_state.get(f"show_answers_quiz1", False):
            if (rep == "Vrai") == q["correct"]:
                st.success(f"✅ Correct! {q['explication']}")
            else:
                st.error(f"❌ Incorrect! {q['explication']}")
    
    if st.button("📊 Corriger le Quiz 1", key="corriger_quiz1"):
        st.session_state.show_answers_quiz1 = True

# Slide 24 : QUIZ 2 - Styles
with tabs[24]:
    st.markdown("""
    <div class="quiz-section">
    <h2>🎯 QUIZ 2 - Styles de Leadership</h2>
    <p class="content-paragraph">Testez votre capacité à identifier les styles de leadership (10 questions)</p>
    </div>
    """, unsafe_allow_html=True)
    
    quiz2_questions = [
        {
            "question": "Quel style de leadership convient le mieux à une équipe d'experts hautement motivés ?",
            "options": ["Directif", "Laissez-faire", "Visionnaire", "Affiliatif"],
            "correct": "Laissez-faire",
            "explication": "✅ Le style laissez-faire fonctionne bien avec des experts autonomes."
        }
    ]
    
    for i, q in enumerate(quiz2_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/10 :</strong> {q["question"]}</div>', unsafe_allow_html=True)
        rep = st.radio(f"Choisissez la bonne réponse :", q["options"], key=f"quiz2_{i}")
        
        if st.session_state.get(f"show_answers_quiz2", False):
            if rep == q["correct"]:
                st.success(f"✅ Correct! {q['explication']}")
            else:
                st.error(f"❌ Incorrect! La bonne réponse était : {q['correct']}. {q['explication']}")
    
    if st.button("📊 Corriger le Quiz 2", key="corriger_quiz2"):
        st.session_state.show_answers_quiz2 = True

# Slide 25 : Synthèse
with tabs[25]:
    st.markdown("""
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

# Slide 26 : Secteurs d'Application
with tabs[26]:
    st.markdown("""
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

# Slide 27 : Erreurs Courantes
with tabs[27]:
    st.markdown("""
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

# Slide 28 : Conseils
with tabs[28]:
    st.markdown("""
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

# Slide 29 : Ressources
with tabs[29]:
    st.markdown("""
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

# Message final
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; margin-top: 2rem;">
<p><strong>✨ Leadership Pro - Formation Complète ✨</strong></p>
<p>Tests interactifs • 10 styles de leadership • Jeux de rôle réalistes • Outils pratiques</p>
</div>
""", unsafe_allow_html=True)
