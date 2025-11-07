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

# Nouvelle structure simplifiée
slide_names = [
    "0. Test Leadership", "1. Intro", "2. Définitions", "3. L vs M", "4. L vs C", 
    "5. Théories XY", "6. Visionnaire", "7. Coaching", "8. Affiliatif", "9. Démocratique", 
    "10. Directif", "11. Laissez-faire", "12. Situationnel", "13. Compétences", 
    "14. IE", "15. Cas", "16. Quiz 1", "17. Quiz 2", "18. Plan d'Action", 
    "19. Synthèse", "20. Secteurs", "21. Erreurs", "22. Conseils", "23. Ressources"
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
        
        st.session_state.test_responses[i] = ["Toujours", "Souvent", "Parfois", "Rarement"].index(response)
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
            <p>Vous avez des qualités de leadership exceptionnelles.</p>
            """, unsafe_allow_html=True)
        elif total_score >= 40:
            st.markdown("""
            <p><strong>💪 Profil : Leader Émergent</strong></p>
            <p>Vous avez de solides bases de leadership et un bon potentiel.</p>
            """, unsafe_allow_html=True)
        elif total_score >= 30:
            st.markdown("""
            <p><strong>🌱 Profil : Leader en Développement</strong></p>
            <p>Vous avez les bases nécessaires et un bon potentiel de croissance.</p>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <p><strong>📚 Profil : Leader en Apprentissage</strong></p>
            <p>Vous avez conscience de l'importance du leadership.</p>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

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
    </div>
    """, unsafe_allow_html=True)

# --- Slide 4 : Leadership vs Commandement ---
with tabs[4]:
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

# --- Slide 5 : Théories X et Y de McGregor ---
with tabs[5]:
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

# --- Slides 6-11 : Styles de Goleman ---
styles_data = [
    ("Visionnaire", "« Viens, on va là-bas ! »", 
     "Centré sur la vision à long terme. Idéal lors des changements stratégiques.",
     "Satya Nadella chez Microsoft a redéfini la mission autour de l'autonomisation."),
    
    ("Coaching", "« Je t'aide à grandir »", 
     "Développement personnel. Le leader agit comme un coach.",
     "Un manager consacre 30 minutes par semaine à chaque collaborateur."),
    
    ("Affiliatif", "« L'harmonie d'abord »", 
     "Relations humaines et cohésion d'équipe.",
     "Après un licenciement, organisation d'un week-end de cohésion."),
    
    ("Démocratique", "« Qu'en pensez-vous ? »", 
     "Co-construction et consultation.",
     "Chez Decathlon, les équipes votent sur les nouveaux produits."),
    
    ("Directif", "« Fais ça, maintenant ! »", 
     "Ordres clairs, contrôle strict. Indispensable en situation de crise.",
     "Lors de l'incendie de Notre-Dame, ordres précis sans discussion."),
    
    ("Laissez-faire", "« À toi de jouer »", 
     "Autonomie totale. Fonctionne avec des experts motivés.",
     "Chez Pixar, les réalisateurs ont liberté créative.")
]

for i, (nom, phrase, desc, exemple) in enumerate(styles_data):
    with tabs[6 + i]:
        st.markdown(f"""
        <div class="modern-card">
        <h2>🎨 Style {nom}</h2>
        <p style="font-size:1.3rem; font-weight:600; color:#4f46e5; margin:1rem 0;">{phrase}</p>
        <p class="content-paragraph">{desc}</p>
        
        <div class="example-box">
        💡 <strong>Exemple concret :</strong> {exemple}
        </div>
        
        <h3>📋 Quand l'utiliser ?</h3>
        <ul class="content-list">
        <li><strong>Forces :</strong> {['Inspiration et vision', 'Développement des talents', 'Cohésion d\'équipe', 'Implication collective', 'Rapidité d\'exécution', 'Autonomie et créativité'][i]}</li>
        <li><strong>Risques :</strong> {['Trop théorique sans action', 'Consommation de temps', 'Évitement des conflits', 'Lenteur décisionnelle', 'Démotivation à long terme', 'Manque de direction'][i]}</li>
        </ul>
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
    </div>
    """, unsafe_allow_html=True)

# --- Slide 13 : Compétences Clés ---
with tabs[13]:
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

# --- Slide 16 : QUIZ 1 - Fondamentaux (10 questions) ---
with tabs[16]:
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
        },
        {
            "question": "Le style de leadership directif doit toujours être évité car il est toxique.",
            "correct": False,
            "explication": "❌ Faux - Le style directif est nécessaire en situation de crise ou avec des débutants."
        },
        {
            "question": "On peut exercer un leadership efficace sans avoir de position hiérarchique officielle.",
            "correct": True,
            "explication": "✅ Vrai - C'est le leadership informel, basé sur l'influence et le respect."
        },
        {
            "question": "L'intelligence émotionnelle représente environ 80% de la performance en leadership selon Daniel Goleman.",
            "correct": True,
            "explication": "✅ Vrai - La capacité à gérer ses émotions et celles des autres est cruciale."
        },
        {
            "question": "Un leader visionnaire se concentre principalement sur le contrôle des tâches quotidiennes.",
            "correct": False,
            "explication": "❌ Faux - Le leader visionnaire se concentre sur la vision à long terme."
        },
        {
            "question": "Le leadership situationnel implique d'adapter son style à la maturité de chaque collaborateur.",
            "correct": True,
            "explication": "✅ Vrai - Adapter le style selon la compétence et la motivation de chacun."
        },
        {
            "question": "Un leader doit toujours prendre les décisions seul pour montrer son autorité.",
            "correct": False,
            "explication": "❌ Faux - Un bon leader sait quand déléguer et impliquer son équipe."
        },
        {
            "question": "Le feedback régulier est une pratique essentielle du leadership coaching.",
            "correct": True,
            "explication": "✅ Vrai - Le leader coaching utilise le feedback pour développer les compétences."
        },
        {
            "question": "Le leadership et le management sont deux concepts identiques.",
            "correct": False,
            "explication": "❌ Faux - Le leadership inspire le changement, le management organise l'exécution."
        }
    ]
    
    score_quiz1 = 0
    user_answers_quiz1 = []
    
    for i, q in enumerate(quiz1_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/10 :</strong> {q["question"]}</div>', unsafe_allow_html=True)
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
        <p><strong>Score : {score_quiz1}/10</strong></p>
        <p><strong>Niveau :</strong> {'🌟 Expert en leadership' if score_quiz1 >= 9 
            else '💡 Leader avancé' if score_quiz1 >= 7
            else '📚 Bonnes bases' if score_quiz1 >= 5
            else '🎯 En développement'}</p>
        </div>
        """, unsafe_allow_html=True)

# --- Slide 17 : QUIZ 2 - Styles et Mise en Pratique (10 questions) ---
with tabs[17]:
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
        },
        {
            "question": "Dans une situation de crise urgente, quel style est le plus approprié ?",
            "options": ["Démocratique", "Directif", "Coaching", "Affiliatif"],
            "correct": "Directif",
            "explication": "✅ Le style directif permet des décisions rapides en situation d'urgence."
        },
        {
            "question": "Quel style utilise-t-on principalement pour développer les compétences individuelles ?",
            "options": ["Visionnaire", "Coaching", "Directif", "Laissez-faire"],
            "correct": "Coaching",
            "explication": "✅ Le style coaching se concentre sur le développement personnel."
        },
        {
            "question": "Après un conflit d'équipe, quel style aide à restaurer la confiance ?",
            "options": ["Directif", "Affiliatif", "Visionnaire", "Laissez-faire"],
            "correct": "Affiliatif",
            "explication": "✅ Le style affiliatif privilégie l'harmonie et les relations."
        },
        {
            "question": "Quel style implique de consulter l'équipe avant de prendre une décision importante ?",
            "options": ["Directif", "Démocratique", "Visionnaire", "Laissez-faire"],
            "correct": "Démocratique",
            "explication": "✅ Le style démocratique valorise la participation de l'équipe."
        },
        {
            "question": "Un collaborateur débutant mais très motivé a besoin de :",
            "options": ["Autonomie totale", "Instructions claires et encouragement", "Liberté créative", "Peu de supervision"],
            "correct": "Instructions claires et encouragement",
            "explication": "✅ Le style persuasif convient aux débutants motivés."
        },
        {
            "question": "Quel style est centré sur la communication d'une vision inspirante ?",
            "options": ["Coaching", "Visionnaire", "Affiliatif", "Directif"],
            "correct": "Visionnaire",
            "explication": "✅ Le leader visionnaire explique le 'pourquoi' et inspire."
        },
        {
            "question": "Le modèle situationnel recommande d'adapter son style selon :",
            "options": ["L'ancienneté", "La compétence et la motivation", "Le salaire", "L'âge"],
            "correct": "La compétence et la motivation",
            "explication": "✅ La maturité se mesure par compétence et motivation."
        },
        {
            "question": "Quel style risque de créer de la dépendance si utilisé excessivement ?",
            "options": ["Directif", "Démocratique", "Laissez-faire", "Visionnaire"],
            "correct": "Directif",
            "explication": "✅ Le style directif peut empêcher l'autonomie."
        },
        {
            "question": "Pour un collaborateur expérimenté mais temporairement démotivé, on utilise :",
            "options": ["Style directif", "Style laissez-faire", "Style participatif", "Style visionnaire"],
            "correct": "Style participatif",
            "explication": "✅ Le style participatif redonne de la motivation par l'implication."
        }
    ]
    
    score_quiz2 = 0
    user_answers_quiz2 = []
    
    for i, q in enumerate(quiz2_questions):
        st.markdown(f'<div class="quiz-question"><strong>Question {i+1}/10 :</strong> {q["question"]}</div>', unsafe_allow_html=True)
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
        <p><strong>Score : {score_quiz2}/10</strong></p>
        <p><strong>Niveau :</strong> {'🎯 Expert en styles de leadership' if score_quiz2 >= 9 
            else '💡 Bonne maîtrise des styles' if score_quiz2 >= 7
            else '📚 Connaissances de base' if score_quiz2 >= 5
            else '🌱 Débutant en leadership'}</p>
        </div>
        """, unsafe_allow_html=True)

# --- Slide 18 : PLAN D'ACTION ---
with tabs[18]:
    st.markdown("""
    <div class="modern-card">
    <h2>📝 Votre Plan d'Action Personnalisé</h2>
    <p class="content-paragraph">Basé sur vos résultats aux quiz, voici un plan d'action concret.</p>
    </div>
    """, unsafe_allow_html=True)
    
    score_quiz1 = st.session_state.get('score_quiz1', 0)
    score_quiz2 = st.session_state.get('score_quiz2', 0)
    score_total = score_quiz1 + score_quiz2
    
    if score_total > 0:
        if score_total >= 16:
            niveau = "🌟 LEADER AVANCÉ"
            plan_content = """
            <h4>🎯 Votre Plan - 4 Semaines</h4>
            <div class="content-list">
            <li><strong>Semaine 1 : Mentorat</strong> - Coacher 2 personnes dans votre entourage</li>
            <li><strong>Semaine 2 : Innovation</strong> - Organiser un brainstorming d'équipe</li>
            <li><strong>Semaine 3 : Développement</strong> - Mettre en place un programme de feedback</li>
            <li><strong>Semaine 4 : Excellence</strong> - Mesurer votre impact et ajuster</li>
            </div>
            """
        elif score_total >= 12:
            niveau = "💡 LEADER INTERMÉDIAIRE"
            plan_content = """
            <h4>🎯 Votre Plan - 4 Semaines</h4>
            <div class="content-list">
            <li><strong>Semaine 1 : Bases solides</strong> - Pratiquer l'écoute active quotidienne</li>
            <li><strong>Semaine 2 : Expérimentation</strong> - Tester 3 styles différents</li>
            <li><strong>Semaine 3 : Intelligence émotionnelle</strong> - Tenir un journal émotionnel</li>
            <li><strong>Semaine 4 : Consolidation</strong> - Demander du feedback à votre équipe</li>
            </div>
            """
        else:
            niveau = "📚 LEADER EN DÉVELOPPEMENT"
            plan_content = """
            <h4>🎯 Votre Plan - 4 Semaines</h4>
            <div class="content-list">
            <li><strong>Semaine 1 : Fondamentaux</strong> - Lire un livre sur le leadership</li>
            <li><strong>Semaine 2 : Confiance</strong> - Prendre la parole en réunion</li>
            <li><strong>Semaine 3 : Application</strong> - Tester un premier style conscient</li>
            <li><strong>Semaine 4 : Évaluation</strong> - Établir un plan de développement sur 3 mois</li>
            </div>
            """
        
        st.markdown(f"""
        <div class="plan-action">
        <h3>{niveau}</h3>
        <p><strong>Quiz 1 :</strong> {score_quiz1}/10 | <strong>Quiz 2 :</strong> {score_quiz2}/10</p>
        {plan_content}
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.info("ℹ️ Complétez les deux quiz pour générer votre plan d'action personnalisé.")

# --- Slides 19-23 : Contenu restant ---
with tabs[19]:
    st.markdown("""
    <div class="modern-card">
    <h2>🎓 Synthèse du Parcours Leadership</h2>
    <p class="content-paragraph">Les concepts clés à retenir pour votre développement en leadership.</p>
    </div>
    """, unsafe_allow_html=True)

with tabs[20]:
    st.markdown("""
    <div class="modern-card">
    <h2>🏥 Leadership dans Différents Secteurs</h2>
    <p class="content-paragraph">Application des styles de leadership selon les contextes professionnels.</p>
    </div>
    """, unsafe_allow_html=True)

with tabs[21]:
    st.markdown("""
    <div class="modern-card">
    <h2>🚫 Erreurs Courantes en Leadership</h2>
    <p class="content-paragraph">Les pièges à éviter pour développer un leadership efficace.</p>
    </div>
    """, unsafe_allow_html=True)

with tabs[22]:
    st.markdown("""
    <div class="modern-card">
    <h2>💡 Conseils Pratiques</h2>
    <p class="content-paragraph">Des recommandations concrètes pour améliorer votre leadership au quotidien.</p>
    </div>
    """, unsafe_allow_html=True)

with tabs[23]:
    st.markdown("""
    <div class="modern-card">
    <h2>📚 Ressources Complémentaires</h2>
    <p class="content-paragraph">Livres, vidéos et outils pour approfondir votre apprentissage.</p>
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
