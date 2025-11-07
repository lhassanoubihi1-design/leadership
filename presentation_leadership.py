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
    .plan-action {
        background: linear-gradient(135deg, #f0fdf4, #ecfdf5);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 4px solid #10b981;
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
    .advice-card {
        background: linear-gradient(135deg, #ecfdf5, #f0fdf4);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 4px solid #10b981;
    }
    #MainMenu, footer, header { visibility: hidden !important; }
</style>
""", unsafe_allow_html=True)

st.title("✨ Leadership & Styles de Leadership")
st.markdown("<div style='text-align:center; margin-bottom:2rem; color:#64748b;'>Formation complète avec exemples concrets et vidéos</div>", unsafe_allow_html=True)

# Nouvelle structure sans styles de commandement
slide_names = [
    "0. Test Leadership", "1. Intro", "2. Définitions", "3. L vs M", "4. Théories XY", 
    "5. Visionnaire", "6. Coaching", "7. Affiliatif", "8. Démocratique", "9. Directif", 
    "10. Laissez-faire", "11. Autres Théories", "12. Situationnel", "13. Compétences", 
    "14. IE", "15. Cas", "16. Quiz 1", "17. Quiz 2", "18. Plan d'Action", 
    "19. Synthèse", "20. Secteurs", "21. Erreurs", "22. Développement", "23. Conseils", "24. Ressources"
]

tabs = st.tabs(slide_names)

# --- Slide 0 : TEST DE LEADERSHIP INITIAL ---
with tabs[0]:
    st.markdown("""
    <div class="test-section">
    <h2>🧪 Test : Êtes-vous un leader naturel ?</h2>
    <p class="content-paragraph">Découvrez votre profil de leadership avec ce test de 20 questions</p>
    </div>
    """, unsafe_allow_html=True)
    
    leadership_test_questions = [
        {"question": "Je prends naturellement les devants dans un groupe", "points": [3, 2, 1, 0]},
        {"question": "J'écoute activement les opinions des autres avant de décider", "points": [3, 2, 1, 0]},
        {"question": "Je motive facilement les autres à se dépasser", "points": [3, 2, 1, 0]},
        {"question": "Je reste calme et rationnel sous pression", "points": [3, 2, 1, 0]},
        {"question": "Je délègue facilement et fais confiance aux autres", "points": [3, 2, 1, 0]},
        {"question": "Je prends des décisions difficiles quand il le faut", "points": [3, 2, 1, 0]},
        {"question": "Je donne régulièrement du feedback constructif", "points": [3, 2, 1, 0]},
        {"question": "Je reconnais mes erreurs et en tire des leçons", "points": [3, 2, 1, 0]},
        {"question": "Je crée facilement une ambiance positive dans l'équipe", "points": [3, 2, 1, 0]},
        {"question": "Je sais dire non quand c'est nécessaire", "points": [3, 2, 1, 0]},
        {"question": "Je m'adapte rapidement aux changements", "points": [3, 2, 1, 0]},
        {"question": "Je communique clairement mes attentes", "points": [3, 2, 1, 0]},
        {"question": "Je résous les conflits de manière constructive", "points": [3, 2, 1, 0]},
        {"question": "Je prends des risques calculés", "points": [3, 2, 1, 0]},
        {"question": "Je célèbre les succès de mon équipe", "points": [3, 2, 1, 0]},
        {"question": "Je donne du sens au travail de l'équipe", "points": [3, 2, 1, 0]},
        {"question": "Je développe les compétences de mes collaborateurs", "points": [3, 2, 1, 0]},
        {"question": "Je prends en compte les émotions des autres", "points": [3, 2, 1, 0]},
        {"question": "Je fixe des objectifs clairs et atteignables", "points": [3, 2, 1, 0]},
        {"question": "Je suis cohérent entre mes paroles et mes actions", "points": [3, 2, 1, 0]}
    ]
    
    if 'test_score' not in st.session_state:
        st.session_state.test_score = 0
        st.session_state.test_responses = [None] * 20
    
    total_score = 0
    
    for i, q in enumerate(leadership_test_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/20 :</strong> {q["question"]}</div>', unsafe_allow_html=True)
        response = st.radio(
            "Votre réponse :",
            ["Toujours", "Souvent", "Parfois", "Rarement"],
            key=f"leadership_test_{i}",
            index=st.session_state.test_responses[i] if st.session_state.test_responses[i] is not None else 0
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
        <p><strong>Score : {total_score}/60 points</strong></p>
        """, unsafe_allow_html=True)
        
        if total_score >= 50:
            st.markdown("""
            <p><strong>🎯 Profil : Leader Confirmé</strong></p>
            <p>Vous avez des qualités de leadership exceptionnelles. Vous inspirez naturellement les autres et savez guider une équipe vers le succès.</p>
            <p><strong>Conseil :</strong> Continuez à développer votre impact et à mentorer les futurs leaders.</p>
            """, unsafe_allow_html=True)
        elif total_score >= 40:
            st.markdown("""
            <p><strong>💪 Profil : Leader Émergent</strong></p>
            <p>Vous avez de solides bases de leadership et un bon potentiel. Vous êtes sur la bonne voie pour devenir un leader accompli.</p>
            <p><strong>Conseil :</strong> Travaillez votre assertivité et votre vision stratégique.</p>
            """, unsafe_allow_html=True)
        elif total_score >= 30:
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
        
        st.info("💡 **Note :** Ce test donne une indication de votre profil actuel. Le leadership se développe continuellement tout au long de la vie.")

# --- Slide 1 : Introduction ---
with tabs[1]:
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

# --- Slide 2 : Définitions ---
with tabs[2]:
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
    
    <h3>🎥 Vidéos explicatives</h3>
    <a href="https://youtu.be/hCtFbHJQHvk?si=r00mEZ8Mnnzecd1I" target="_blank" class="video-link">▶ Définition d'un leader</a>
    <a href="https://youtu.be/Ej9M-U1EiGY?si=kgqe2lA8Pe6oF26Q" target="_blank" class="video-link">▶ Définition du leadership</a>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 3 : Leadership vs Management ---
with tabs[3]:
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

# --- Slide 4 : Théories X et Y de McGregor ---
with tabs[4]:
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
    
    <div class="example-box">
    💡 <strong>Style correspondant :</strong> Autoritaire, directif, contrôle strict.
    </div>
    </div>
    
    <div class="theory-box">
    <h3>📈 Théorie Y - Vision moderne</h3>
    <p><strong>Postulats :</strong></p>
    <ul class="content-list">
    <li>Le travail est aussi naturel que le jeu ou le repos</li>
    <li>Les personnes peuvent s'auto-contrôler et s'auto-motiver</li>
    <li>Elles recherchent et acceptent les responsabilités</li>
    </ul>
    
    <div class="example-box">
    💡 <strong>Style correspondant :</strong> Participatif, délégatif, développement des compétences.
    </div>
    </div>
    
    <h3>📊 Tableau Comparatif</h3>
    <table class="comparison-table">
    <tr>
        <th>Aspect</th>
        <th>Théorie X</th>
        <th>Théorie Y</th>
    </tr>
    <tr>
        <td><strong>Vision de l'humain</strong></td>
        <td>Paresseux, à contrôler</td>
        <td>Motivé, responsable</td>
    </tr>
    <tr>
        <td><strong>Style de direction</strong></td>
        <td>Autoritaire</td>
        <td>Participatif</td>
    </tr>
    <tr>
        <td><strong>Communication</strong></td>
        <td>Descendante</td>
        <td>Bidirectionnelle</td>
    </tr>
    </table>
    
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Une usine traditionnelle (Théorie X) vs une startup tech (Théorie Y).
    </div>
    </div>
    """, unsafe_allow_html=True)

# --- Slides 5-10 : Styles de Goleman ---
styles_data = [
    ("Visionnaire", "« Viens, on va là-bas ! »", 
     "Centré sur la vision à long terme. Idéal lors des changements stratégiques.",
     "Satya Nadella chez Microsoft a redéfini la mission autour de l'autonomisation.",
     "Théorie Y"),
    
    ("Coaching", "« Je t'aide à grandir »", 
     "Développement personnel. Le leader agit comme un coach.",
     "Un manager consacre 30 minutes par semaine à chaque collaborateur.",
     "Théorie Y"),
    
    ("Affiliatif", "« L'harmonie d'abord »", 
     "Relations humaines et cohésion d'équipe.",
     "Après un licenciement, organisation d'un week-end de cohésion.",
     "Théorie Y"),
    
    ("Démocratique", "« Qu'en pensez-vous ? »", 
     "Co-construction et consultation.",
     "Chez Decathlon, les équipes votent sur les nouveaux produits.",
     "Théorie Y"),
    
    ("Directif", "« Fais ça, maintenant ! »", 
     "Ordres clairs, contrôle strict. Indispensable en situation de crise.",
     "Lors de l'incendie de Notre-Dame, ordres précis sans discussion.",
     "Théorie X"),
    
    ("Laissez-faire", "« À toi de jouer »", 
     "Autonomie totale. Fonctionne avec des experts motivés.",
     "Chez Pixar, les réalisateurs ont liberté créative.",
     "Théorie Y")
]

for i, (nom, phrase, desc, exemple, theorie) in enumerate(styles_data):
    with tabs[5 + i]:
        st.markdown(f"""
        <div class="modern-card">
        <h2>🎨 Style {nom}</h2>
        <p style="font-size:1.3rem; font-weight:600; color:#4f46e5; margin:1rem 0;">{phrase}</p>
        <p class="content-paragraph">{desc}</p>
        
        <div class="example-box">
        💡 <strong>Exemple concret :</strong> {exemple}
        </div>
        
        <h3>🔗 Lien avec McGregor</h3>
        <p class="content-paragraph">Ce style correspond à la <strong>{theorie}</strong> de McGregor</p>
        
        <h3>📋 Quand l'utiliser ?</h3>
        <ul class="content-list">
        <li><strong>Forces :</strong> {['Inspiration et vision', 'Développement des talents', 'Cohésion d\'équipe', 'Implication collective', 'Rapidité d\'exécution', 'Autonomie et créativité'][i]}</li>
        <li><strong>Risques :</strong> {['Trop théorique sans action', 'Consommation de temps', 'Évitement des conflits', 'Lenteur décisionnelle', 'Démotivation à long terme', 'Manque de direction'][i]}</li>
        </ul>
        
        <h3>🎥 Vidéo sur les styles</h3>
        <a href="https://youtu.be/vilZazhIjoc?si=b4PNNY5P8SAqu9_p" target="_blank" class="video-link">▶ Les 6 styles de leadership</a>
        </div>
        """, unsafe_allow_html=True)

# --- Slide 11 : Autres Théories de Leadership ---
with tabs[11]:
    st.markdown("""
    <div class="modern-card">
    <h2>🎓 Autres Théories Importantes du Leadership</h2>
    
    <p class="content-paragraph">Au-delà de McGregor et Goleman, plusieurs théories ont marqué la compréhension du leadership.</p>
    
    <div class="theory-box">
    <h3>🏛️ Théorie des Traits</h3>
    <p><strong>Concept :</strong> Les leaders naissent avec des traits de personnalité spécifiques.</p>
    <ul class="content-list">
    <li><strong>Traits clés :</strong> Intelligence, confiance en soi, charisme, intégrité</li>
    <li><strong>Limite :</strong> Ne prend pas en compte l'apprentissage et le contexte</li>
    </ul>
    </div>
    
    <div class="theory-box">
    <h3>🔄 Leadership Transformationnel</h3>
    <p><strong>Concept :</strong> Le leader transforme et inspire ses followers au-delà de leurs intérêts immédiats.</p>
    <ul class="content-list">
    <li><strong>4 composantes :</strong> Influence idéalisée, motivation inspirante, stimulation intellectuelle, considération individualisée</li>
    <li><strong>Avantage :</strong> Crée un engagement profond et durable</li>
    </ul>
    </div>
    
    <div class="theory-box">
    <h3>🚀 Leadership Serviteur</h3>
    <p><strong>Concept :</strong> Le leader sert d'abord ses collaborateurs avant de les diriger.</p>
    <ul class="content-list">
    <li><strong>Principes :</strong> Écoute, empathie, conscientisation, persuasion</li>
    <li><strong>Bénéfice :</strong> Crée une culture de confiance et d'engagement</li>
    </ul>
    </div>
    
    <div class="example-box">
    💡 <strong>Exemple :</strong> Herb Kelleher, fondateur de Southwest Airlines, priorisait le bien-être des employés avant les profits.
    </div>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 12 : Style Situationnel ---
with tabs[12]:
    st.markdown("""
    <div class="modern-card">
    <h2>🔄 Modèle Situationnel de Hersey-Blanchard</h2>
    <p class="content-paragraph">Il n'existe pas un seul bon style, mais un <strong>style adapté à la maturité</strong> de chaque collaborateur.</p>
    
    <h3>📈 Les 4 niveaux de maturité</h3>
    <ul class="content-list">
    <li><strong>M1 :</strong> Incompétent et non motivé → Style directif</li>
    <li><strong>M2 :</strong> Incompétent mais motivé → Style persuasif</li>
    <li><strong>M3 :</strong> Compétent mais démotivé → Style participatif</li>
    <li><strong>M4 :</strong> Compétent et motivé → Style délégatif</li>
    </ul>
    
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Sophie, manager dans la vente, utilise le style directif avec les nouveaux vendeurs (M1) et délégatif avec ses tops vendeurs (M4).
    </div>
    
    <h3>🔗 Lien avec McGregor</h3>
    <p class="content-paragraph">Le modèle situationnel montre qu'un bon leader sait <strong>alterner entre approches</strong> selon la situation.</p>
    
    <h3>🎥 Vidéo explicative</h3>
    <a href="https://youtu.be/iRBQqfJaoo4?si=Kbhele-WRaC6wqGw" target="_blank" class="video-link">▶ Le leadership situationnel</a>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 13 : Compétences Clés ---
with tabs[13]:
    st.markdown("""
    <div class="modern-card">
    <h2>🔑 Compétences Clés du Leader Moderne</h2>
    
    <h3>💪 Compétences techniques vs soft skills</h3>
    
    <div class="content-paragraph">
    <strong>Hard Skills :</strong> Connaissances métier, expertise technique, analyse de données
    </div>
    
    <div class="content-paragraph">
    <strong>Soft Skills :</strong> Intelligence émotionnelle, communication, adaptabilité, résilience
    </div>
    
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
    </div>
    """, unsafe_allow_html=True)

# --- Slide 14 : Intelligence Émotionnelle ---
with tabs[14]:
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

# --- Slide 15 : Études de Cas ---
with tabs[15]:
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

# --- Slide 16 : QUIZ 1 - Fondamentaux ---
with tabs[16]:
    st.markdown("""
    <div class="quiz-section">
    <h2>🧠 QUIZ 1 - Fondamentaux du Leadership</h2>
    <p class="content-paragraph">Testez vos connaissances sur les concepts de base du leadership</p>
    </div>
    """, unsafe_allow_html=True)
    
    quiz1_questions = [
        {
            "question": "Selon la Théorie X de McGregor, les employés sont naturellement paresseux et évitent le travail.",
            "correct": True,
            "explication": "✅ Vrai - La Théorie X postule que les employés n'aiment pas le travail et doivent être contrôlés."
        },
        {
            "question": "Le leadership est une compétence exclusivement innée qui ne peut pas s'apprendre.",
            "correct": False,
            "explication": "❌ Faux - Des études montrent que 70% des compétences de leadership s'acquièrent par la pratique."
        },
        {
            "question": "L'intelligence émotionnelle représente environ 80% de la performance en leadership selon Daniel Goleman.",
            "correct": True,
            "explication": "✅ Vrai - La capacité à gérer ses émotions et celles des autres est cruciale."
        }
    ]
    
    score_quiz1 = 0
    user_answers_quiz1 = []
    
    for i, q in enumerate(quiz1_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/3 :</strong> {q["question"]}</div>', unsafe_allow_html=True)
        rep = st.radio(f"Choisissez votre réponse :", ["Vrai", "Faux"], key=f"quiz1_{i}")
        user_answers_quiz1.append(rep)
        
        if st.session_state.get(f"show_answers_quiz1", False):
            if (rep == "Vrai") == q["correct"]:
                st.success(f"✅ Correct! {q['explication']}")
            else:
                st.error(f"❌ Incorrect! {q['explication']}")
    
    if st.button("📊 Corriger le Quiz 1", key="corriger_quiz1"):
        st.session_state.show_answers_quiz1 = True
        score_quiz1 = sum(1 for i, q in enumerate(quiz1_questions) 
                        if (user_answers_quiz1[i] == "Vrai") == q["correct"])
        st.session_state.score_quiz1 = score_quiz1
        
        st.markdown(f"""
        <div class="evaluation-box">
        <h3>📊 Résultats du Quiz 1</h3>
        <p><strong>Score : {score_quiz1}/3</strong></p>
        <p>{'🌟 Excellent !' if score_quiz1 >= 3 else '💡 Continue à apprendre !'}</p>
        </div>
        """, unsafe_allow_html=True)

# --- Slide 17 : QUIZ 2 - Styles et Pratique ---
with tabs[17]:
    st.markdown("""
    <div class="quiz-section">
    <h2>🎯 QUIZ 2 - Styles de Leadership</h2>
    <p class="content-paragraph">Testez votre capacité à identifier les styles de leadership</p>
    </div>
    """, unsafe_allow_html=True)
    
    quiz2_questions = [
        {
            "question": "Quel style convient le mieux à une équipe d'experts hautement motivés ?",
            "options": ["Directif", "Laissez-faire", "Visionnaire", "Affiliatif"],
            "correct": "Laissez-faire",
            "explication": "✅ Le style laissez-faire fonctionne bien avec des experts autonomes."
        },
        {
            "question": "Dans une situation de crise urgente, quel style est le plus approprié ?",
            "options": ["Démocratique", "Directif", "Coaching", "Affiliatif"],
            "correct": "Directif",
            "explication": "✅ Le style directif permet des décisions rapides en situation d'urgence."
        }
    ]
    
    score_quiz2 = 0
    user_answers_quiz2 = []
    
    for i, q in enumerate(quiz2_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/2 :</strong> {q["question"]}</div>', unsafe_allow_html=True)
        rep = st.radio(f"Choisissez la bonne réponse :", q["options"], key=f"quiz2_{i}")
        user_answers_quiz2.append(rep)
        
        if st.session_state.get(f"show_answers_quiz2", False):
            if rep == q["correct"]:
                st.success(f"✅ Correct! {q['explication']}")
            else:
                st.error(f"❌ Incorrect! La bonne réponse était : {q['correct']}. {q['explication']}")
    
    if st.button("📊 Corriger le Quiz 2", key="corriger_quiz2"):
        st.session_state.show_answers_quiz2 = True
        score_quiz2 = sum(1 for i, q in enumerate(quiz2_questions) 
                        if user_answers_quiz2[i] == q["correct"])
        st.session_state.score_quiz2 = score_quiz2
        
        st.markdown(f"""
        <div class="evaluation-box">
        <h3>📊 Résultats du Quiz 2</h3>
        <p><strong>Score : {score_quiz2}/2</strong></p>
        <p>{'🎯 Excellent jugement situationnel !' if score_quiz2 >= 2 else '💡 Continue à pratiquer !'}</p>
        </div>
        """, unsafe_allow_html=True)

# --- Slide 18 : PLAN D'ACTION ---
with tabs[18]:
    st.markdown("""
    <div class="modern-card">
    <h2>📝 Votre Plan d'Action Personnalisé</h2>
    <p class="content-paragraph">Basé sur vos résultats, voici un plan d'action concret.</p>
    </div>
    """, unsafe_allow_html=True)
    
    score_quiz1 = st.session_state.get('score_quiz1', 0)
    score_quiz2 = st.session_state.get('score_quiz2', 0)
    
    if score_quiz1 + score_quiz2 > 0:
        st.markdown(f"""
        <div class="plan-action">
        <h3>🎯 Votre Plan de Développement</h3>
        <p><strong>Quiz 1 (Théories) :</strong> {score_quiz1}/3 | <strong>Quiz 2 (Pratique) :</strong> {score_quiz2}/2</p>
        
        <h4>📈 Prochaines étapes recommandées :</h4>
        <div class="content-list">
        <li><strong>Semaine 1 :</strong> Pratiquer l'écoute active quotidienne</li>
        <li><strong>Semaine 2 :</strong> Tester un nouveau style de leadership</li>
        <li><strong>Semaine 3 :</strong> Demander du feedback à votre équipe</li>
        <li><strong>Semaine 4 :</strong> Établir un plan de développement à 3 mois</li>
        </div>
        
        <div class="example-box">
        💡 <strong>Conseil :</strong> Le leadership se développe par la pratique régulière et la réflexion.
        </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("ℹ️ Complétez les quiz pour générer votre plan d'action personnalisé.")

# --- Slide 19 : Synthèse ---
with tabs[19]:
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

# --- Slide 20 : Secteurs d'Application ---
with tabs[20]:
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
    
    <div class="example-box">
    💡 <strong>Conseil :</strong> Adaptez votre style au contexte sectoriel tout en restant authentique.
    </div>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 21 : Erreurs Courantes ---
with tabs[21]:
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

# --- Slide 22 : Développement Personnel ---
with tabs[22]:
    st.markdown("""
    <div class="modern-card">
    <h2>🌱 Développement de Votre Leadership</h2>
    
    <h3>📈 Parcours de progression</h3>
    
    <div class="content-paragraph">
    <strong>Niveau 1 : Leadership de soi</strong> - Se connaître, s'auto-discipliner
    </div>
    
    <div class="content-paragraph">
    <strong>Niveau 2 : Leadership d'équipe</strong> - Influencer un petit groupe
    </div>
    
    <div class="content-paragraph">
    <strong>Niveau 3 : Leadership organisationnel</strong> - Développer une culture
    </div>
    
    <h3>🛠️ Outils de développement</h3>
    <ul class="content-list">
    <li><strong>Auto-évaluation :</strong> Tests de personnalité</li>
    <li><strong>Mentorat :</strong> Apprendre auprès de leaders</li>
    <li><strong>Feedback 360° :</strong> Retours de tous les côtés</li>
    <li><strong>Formation continue :</strong> Lectures, séminaires</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 23 : Conseils Pratiques ---
with tabs[23]:
    st.markdown("""
    <div class="modern-card">
    <h2>💡 Conseils Pratiques pour Développer Votre Leadership</h2>
    
    <div class="advice-card">
    <h3>🎯 Conseil 1 : Commencez par vous connaître</h3>
    <p>Identifiez vos forces et zones d'amélioration.</p>
    </div>
    
    <div class="advice-card">
    <h3>👂 Conseil 2 : Développez l'écoute active</h3>
    <p>Pratiquez l'écoute sans interruption.</p>
    </div>
    
    <div class="advice-card">
    <h3>🔄 Conseil 3 : Expérimentez différents styles</h3>
    <p>Testez un style différent chaque semaine.</p>
    </div>
    
    <div class="advice-card">
    <h3>📚 Conseil 4 : Cultivez l'apprentissage continu</h3>
    <p>Lisez un livre par mois sur le leadership.</p>
    </div>
    
    <div class="advice-card">
    <h3>🤝 Conseil 5 : Construisez votre réseau</h3>
    <p>Entourez-vous de mentors inspirants.</p>
    </div>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 24 : Ressources ---
with tabs[24]:
    st.markdown("""
    <div class="modern-card">
    <h2>📚 Ressources Complémentaires</h2>
    
    <h3>🎥 Vidéos recommandées</h3>
    <a href="https://youtu.be/hCtFbHJQHvk?si=r00mEZ8Mnnzecd1I" target="_blank" class="video-link">▶ Définition d'un leader</a>
    <a href="https://youtu.be/Ej9M-U1EiGY?si=kgqe2lA8Pe6oF26Q" target="_blank" class="video-link">▶ Définition du leadership</a>
    <a href="https://youtu.be/vilZazhIjoc?si=b4PNNY5P8SAqu9_p" target="_blank" class="video-link">▶ Les styles de leadership</a>
    <a href="https://youtu.be/iRBQqfJaoo4?si=Kbhele-WRaC6wqGw" target="_blank" class="video-link">▶ Leadership situationnel</a>
    
    <h3>📖 Lectures recommandées</h3>
    <ul class="content-list">
    <li><strong>"La Dimension Humaine de l'Entreprise"</strong> - Douglas McGregor</li>
    <li><strong>"Leaders Eat Last"</strong> - Simon Sinek</li>
    <li><strong>"L'Intelligence Émotionnelle"</strong> - Daniel Goleman</li>
    <li><strong>"Les 7 Habitudes des Gens Efficaces"</strong> - Stephen Covey</li>
    </ul>
    
    <div class="quote-card">
    « L'investissement le plus important que vous puissiez faire est d'investir en vous-même. »
    </div>
    </div>
    """, unsafe_allow_html=True)

# Message final
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; margin-top: 2rem;">
<p><strong>✨ Présentation Leadership Pro - Formation Complète ✨</strong></p>
<p>Test initial • 6 styles de leadership • Théories fondamentales • Quiz interactifs • Plan d'action personnalisé</p>
</div>
""", unsafe_allow_html=True)
