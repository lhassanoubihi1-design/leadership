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
st.markdown("<div style='text-align:center; margin-bottom:2rem; color:#64748b;'>Formation express en 45 min</div>", unsafe_allow_html=True)

# Structure mise à jour avec 5 activités clés
slide_names = [
    "0. Activités Express", "1. Test DISC", "2. Intro", "3. L vs M", "4. L vs C", 
    "5. Théories XY", "6. Visionnaire", "7. Coaching", "8. Affiliatif", "9. Démocratique", 
    "10. Directif", "11. Pace-setter", "12. Transformationnel", "13. Transactionnel", 
    "14. Authentique", "15. Serviteur", "16. Situationnel", "17. Laissez-faire",
    "18. Jeu de Rôle", "19. Synthèse"
]

tabs = st.tabs(slide_names)

# ==============================
# ACTIVITÉ EXPRESS 1 : LEADER EN 3 MOTS (Slide 0)
# ==============================
with tabs[0]:
    st.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 1/5 : Le Leader en 3 Mots</h2>
    <p class="content-paragraph">Une activité rapide pour démarrer et faire émerger vos premières idées sur le leadership.</p>
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
        <p>Cette activité permet d'activer les représentations initiales et de créer un climat d'échange.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# TEST DE LEADERSHIP DISC
# ==============================
with tabs[1]: # Décalé de 1
    st.markdown("""
    <div class="test-section">
    <h2>🎨 Test de Leadership DISC</h2>
    <p class="content-paragraph">Découvrez votre style de leadership dominant</p>
    </div>
    """, unsafe_allow_html=True)
    # (Le code du test DISC reste identique mais commence à l'onglet 1)
    disc_questions = [
        {"question": "Face à un nouveau projet, je préfère :", "options": [{"text": "Prendre rapidement le leadership et fixer les objectifs", "color": "red"}, {"text": "Motiver l'équipe avec une vision inspirante", "color": "yellow"}, {"text": "Écouter les idées de chacun avant de décider", "color": "green"}, {"text": "Analyser en détail tous les aspects du projet", "color": "blue"}]},
        {"question": "En réunion, je suis plutôt :", "options": [{"text": "Direct et orienté résultats", "color": "red"}, {"text": "Enthousiaste et communicatif", "color": "yellow"}, {"text": "À l'écoute et conciliant", "color": "green"}, {"text": "Précis et méthodique", "color": "blue"}]},
        {"question": "Quand je dois prendre une décision difficile :", "options": [{"text": "Je prends rapidement ma décision et j'assume", "color": "red"}, {"text": "Je consulte rapidement quelques personnes de confiance", "color": "yellow"}, {"text": "Je cherche le consensus avec toute l'équipe", "color": "green"}, {"text": "J'analyse soigneusement tous les scénarios", "color": "blue"}]},
        {"question": "Mon approche face aux conflits :", "options": [{"text": "Je confronte directement le problème", "color": "red"}, {"text": "Je cherche à désamorcer par la communication", "color": "yellow"}, {"text": "Je privilégie l'harmonie et la compréhension", "color": "green"}, {"text": "J'analyse les faits objectivement", "color": "blue"}]},
        {"question": "Ce qui me motive le plus :", "options": [{"text": "Atteindre des objectifs ambitieux", "color": "red"}, {"text": "Inspirer et être reconnu", "color": "yellow"}, {"text": "Créer des relations harmonieuses", "color": "green"}, {"text": "Réussir grâce à l'expertise et la précision", "color": "blue"}]}
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
                    if previous_color: st.session_state.disc_scores[previous_color] -= 1
                    st.session_state.disc_responses[i] = option['color']
                    st.session_state.disc_scores[option['color']] += 1
                    st.rerun()
        if st.session_state.disc_responses[i] is not None:
            selected_color = st.session_state.disc_responses[i]
            color_display = {'red': '🔴 Rouge', 'yellow': '🟡 Jaune', 'green': '🟢 Vert', 'blue': '🔵 Bleu'}
            selected_text = next(opt['text'] for opt in q['options'] if opt['color'] == selected_color)
            st.markdown(f"✅ **Votre choix :** {color_display[selected_color]} - {selected_text}")
        st.markdown("---")
    all_answered = all(response is not None for response in st.session_state.disc_responses)
    if st.button("🎯 Voir mon style", key="calculate_disc", disabled=not all_answered):
        if not all_answered: st.warning("⚠️ Répondez à toutes les questions.")
        else: st.session_state.show_disc_results = True; st.rerun()
    if st.session_state.get('show_disc_results', False) and all_answered:
        scores = st.session_state.disc_scores
        dominant_color = max(scores, key=scores.get)
        profile_map = {
            'red': {'styles': ['Directif', 'Pace-setter'], 'desc': 'Orientation résultats, leadership fort'},
            'yellow': {'styles': ['Visionnaire', 'Transformationnel'], 'desc': 'Énergie, inspiration, motivation'},
            'green': {'styles': ['Affiliatif', 'Serviteur'], 'desc': 'Empathie, cohésion, écoute'},
            'blue': {'styles': ['Analytique', 'Situationnel'], 'desc': 'Précision, rigueur, analyse'}
        }
        profile = profile_map[dominant_color]
        result_class = f"result-{dominant_color}"
        st.markdown(f'<div class="{result_class}">', unsafe_allow_html=True)
        st.markdown(f"<h2>Profil {dominant_color.capitalize()}</h2>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>Description :</strong> {profile['desc']}</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>Styles dominants :</strong> {', '.join(profile['styles'])}</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ==============================
# SLIDES POUR LES STYLES DE LEADERSHIP
# ==============================
leadership_styles_data = [
    {"name": "Visionnaire", "slogan": "« Viens avec moi vers l'avenir »", "description": "Inspire avec une vision motivante.", "exemple": "Elon Musk"},
    {"name": "Coaching", "slogan": "« Essayez et je vous aiderai à réussir »", "description": "Développe les talents individuels.", "exemple": "Un manager qui accompagne ses collaborateurs"},
    {"name": "Affiliatif", "slogan": "« Les personnes d'abord »", "description": "Crée de l'harmonie et de la confiance.", "exemple": "Organisation de déjeuners d'équipe"},
    {"name": "Démocratique", "slogan": "« Qu'en pensez-vous ? »", "description": "Consulte l'équipe avant de décider.", "exemple": "Google utilise des votes internes"},
    {"name": "Directif", "slogan": "« Faites ce que je vous dis »", "description": "Donne des instructions claires.", "exemple": "Ordres des pompiers en urgence"},
    {"name": "Pace-setter", "slogan": "« Faites comme moi, maintenant ! »", "description": "Montre l'exemple avec excellence.", "exemple": "Steve Jobs chez Apple"},
    {"name": "Transformationnel", "slogan": "« Ensemble, transformons notre réalité »", "description": "Change profondément l'organisation.", "exemple": "Jacques Servier en pharma"},
    {"name": "Transactionnel", "slogan": "« Vous serez récompensé pour vos résultats »", "description": "Fonctionne sur récompenses/punitions.", "exemple": "Commissions en vente"},
    {"name": "Authentique", "slogan": "« Je suis vrai et transparent »", "description": "Mène par l'intégrité et la vulnérabilité.", "exemple": "Brené Brown"},
    {"name": "Serviteur", "slogan": "« Je suis là pour vous servir »", "description": "Met les besoins de l'équipe avant les siens.", "exemple": "Nelson Mandela"}
]

for i, style in enumerate(leadership_styles_data):
    with tabs[6 + i]:  # Styles commencent à l'onglet 6
        st.markdown(f"""
        <div class="modern-card">
            <h2>🎨 Style {style['name']}</h2>
            <p style="font-size:1.3rem; font-weight:600; color:#4f46e5; margin:1rem 0;">{style['slogan']}</p>
            <p class="content-paragraph">{style['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        <div class="example-box">
            💡 <strong>Exemple :</strong> {style['exemple']}
        </div>
        """, unsafe_allow_html=True)

# ==============================
# ACTIVITÉ EXPRESS 2 : REFORMULATION (Slide après Coaching)
# ==============================
with tabs[8]: # Après Coaching
    st.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 2/5 : Reformulation en Duo</h2>
    <p class="content-paragraph">Une activité de communication pour ancrer la notion d'écoute active.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="modern-card">
        <h3>👂 Étapes</h3>
        <p><strong>Durée :</strong> 8 minutes</p>
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
    st.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Pratiquer l'écoute active, essentielle pour tout leader.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# ACTIVITÉ EXPRESS 3 : POST-IT DE RÉFLEXION (Slide après Directif)
# ==============================
with tabs[11]: # Après Directif
    st.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 3/5 : Post-it de Réflexion</h2>
    <p class="content-paragraph">Une pause réflexive pour connecter théorie et pratique.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="modern-card">
        <h3>📝 Matériel</h3>
        <p><strong>Durée :</strong> 7 minutes</p>
        <p>Post-its de 3 couleurs :</p>
        <ul class="content-list">
            <li><span style="color:green; font-weight:bold;">🟩 Vert</span> : Ce que je fais bien comme leader</li>
            <li><span style="color:orange; font-weight:bold;">🟧 Orange</span> : Ce que je veux améliorer</li>
            <li><span style="color:blue; font-weight:bold;">🟦 Bleu</span> : Une action pour demain</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Passez du concept à l'action personnelle.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# ACTIVITÉ EXPRESS 4 : ENGAGEMENT (Slide après Transactionnel)
# ==============================
with tabs[14]: # Après Transactionnel
    st.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 4/5 : Engagement en 1 Phrase</h2>
    <p class="content-paragraph">Transformez les apprentissages en engagement concret.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="modern-card">
        <h3>✍️ Consigne</h3>
        <p><strong>Durée :</strong> 5 minutes</p>
        <p>Complétez cette phrase :</p>
        <p style="background:#f0f9ff; padding:1rem; border-left:4px solid #3b82f6; font-style:italic;">
            <strong>"Je m'engage à ___________ pour développer mon leadership."</strong>
        </p>
        <p><strong>Exemples :</strong> "donner un feedback chaque semaine", "écouter sans interrompre".</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Favoriser la responsabilisation et la mise en œuvre.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# ACTIVITÉ EXPRESS 5 : MOT DE LA FIN (Slide final)
# ==============================
with tabs[19]: # Slide final
    st.markdown("""
    <div class="test-section">
    <h2>🎯 Activité 5/5 : Mot de la Fin</h2>
    <p class="content-paragraph">Clôturez en puissance avec une dernière participation collective.</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="modern-card">
        <h3>🗣️ Tour de Table</h3>
        <p><strong>Durée :</strong> 5 minutes</p>
        <p>Chacun dit <strong>un mot</strong> qui résume son état d'esprit ou son énergie de leadership.</p>
        <div class="example-box">
            💡 <strong>Exemples :</strong> Inspiration, Dynamique, Confiance, Action
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div class="conseil-box">
        <h4>💡 Objectif pédagogique</h4>
        <p>Créer une mémoire collective positive de la session.</p>
    </div>
    """, unsafe_allow_html=True)

# Slides existants (décalés)
with tabs[2]:  # Intro
    st.markdown("""<div class="modern-card"><h2>🚀 Bienvenue</h2></div>""", unsafe_allow_html=True)

with tabs[3]:  # L vs M
    st.markdown("""<div class="modern-card"><h2>⚖️ Leadership vs Management</h2></div>""", unsafe_allow_html=True)

with tabs[4]:  # L vs C
    st.markdown("""<div class="modern-card"><h2>⚔️ Leadership vs Commandement</h2></div>""", unsafe_allow_html=True)

with tabs[5]:  # Théories XY
    st.markdown("""<div class="modern-card"><h2>🧠 Théories X et Y</h2></div>""", unsafe_allow_html=True)

with tabs[18]:  # Jeu de rôle
    st.markdown("""<div class="test-section"><h2>🎭 Jeu de Rôle</h2></div>""", unsafe_allow_html=True)

# Message final
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; margin-top: 2rem;">
<p><strong>⏱️ Timing estimé : 45 min</strong></p>
<p>Activités : 5 x ~7 min = 35 min | Contenu : 10 min</p>
</div>
""", unsafe_allow_html=True)
