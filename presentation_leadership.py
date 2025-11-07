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

st.title("✨ Leadership & Styles de Commandement")
st.markdown("<div style='text-align:center; margin-bottom:2rem; color:#64748b;'>Formation complète avec exemples concrets et vidéos</div>", unsafe_allow_html=True)

# Mise à jour des noms de slides pour inclure le test initial et les conseils
slide_names = [
    "0. Test Leadership", "1. Intro", "2. Définitions", "3. L vs M", "4. L vs C", "5. McGregor XY", 
    "6. Visionnaire", "7. Coaching", "8. Affiliatif", "9. Démocratique", "10. Directif", 
    "11. Laissez-faire", "12. Autres Théories", "13. Styles Commandement", "14. Situationnel", 
    "15. Compétences", "16. IE", "17. Cas", "18. Quiz 1", "19. Quiz 2", "20. Plan d'Action", 
    "21. Synthèse", "22. Secteurs", "23. Erreurs", "24. Développement", "25. Conseils", "26. Ressources"
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
    
    <p class="content-paragraph"><strong>Commandement</strong> : Exercice de l'autorité formelle pour diriger et contrôler.</p>
    <div class="example-box">
    💡 <strong>Exemple :</strong> Un capitaine de pompiers donnant des ordres précis lors d'un incendie.
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
    
    <p class="content-paragraph">Douglas McGregor (1960) a identifié <strong>deux visions opposées de la nature humaine</strong> au travail, qui influencent le style de management.</p>
    
    <div class="theory-box">
    <h3>📋 Théorie X - Vision traditionnelle</h3>
    <p><strong>Postulats :</strong></p>
    <ul class="content-list">
    <li>Les employés n'aiment pas naturellement le travail</li>
    <li>Ils doivent être contrôlés, dirigés et menacés de sanctions</li>
    <li>Ils évitent les responsabilités et recherchent la sécurité avant tout</li>
    <li>Ils manquent d'ambition et préfèrent être dirigés</li>
    </ul>
    
    <div class="example-box">
    💡 <strong>Style de management correspondant :</strong> Autoritaire, directif, contrôle strict, système de récompenses/punitions.
    </div>
    </div>
    
    <div class="theory-box">
    <h3>📈 Théorie Y - Vision moderne</h3>
    <p><strong>Postulats :</strong></p>
    <ul class="content-list">
    <li>Le travail est aussi naturel que le jeu ou le repos</li>
    <li>Les personnes peuvent s'auto-contrôler et s'auto-motiver</li>
    <li>Elles recherchent et acceptent les responsabilités</li>
    <li>La créativité et l'innovation sont largement répandues</li>
    </ul>
    
    <div class="example-box">
    💡 <strong>Style de management correspondant :</strong> Participatif, délégatif, développement des compétences, autonomie.
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
        <td>Autoritaire, directif</td>
        <td>Participatif, délégatif</td>
    </tr>
    <tr>
        <td><strong>Communication</strong></td>
        <td>Descendante</td>
        <td>Bidirectionnelle</td>
    </tr>
    <tr>
        <td><strong>Prise de décision</strong></td>
        <td>Centralisée</td>
        <td>Décentralisée</td>
    </tr>
    <tr>
        <td><strong>Contexte d'application</strong></td>
        <td>Travail répétitif, crise</td>
        <td>Travail créatif, innovation</td>
    </tr>
    </table>
    
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Une usine traditionnelle (Théorie X) vs une startup tech comme Google (Théorie Y).
    </div>
    
    <h3>🎥 Vidéo sur McGregor</h3>
    <a href="https://youtu.be/example-mcgregor" target="_blank" class="video-link">▶ Théories X et Y de McGregor</a>
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
        
        <h3>🔗 Lien avec McGregor</h3>
        <p class="content-paragraph">
        {f"Ce style correspond à la <strong>Théorie Y</strong> de McGregor" if nom in ["Visionnaire", "Coaching", "Affiliatif", "Démocratique", "Laissez-faire"] 
         else "Ce style correspond à la <strong>Théorie X</strong> de McGregor"}
        </p>
        
        <h3>🎥 Vidéo sur les styles</h3>
        <a href="https://youtu.be/vilZazhIjoc?si=b4PNNY5P8SAqu9_p" target="_blank" class="video-link">▶ Les 5 styles de leadership</a>
        </div>
        """, unsafe_allow_html=True)

# --- NOUVEAU SLIDE 12 : Autres Théories de Leadership ---
with tabs[12]:
    st.markdown("""
    <div class="modern-card">
    <h2>🎓 Autres Théories Importantes du Leadership</h2>
    
    <p class="content-paragraph">Au-delà de McGregor et Goleman, plusieurs théories ont marqué la compréhension du leadership.</p>
    
    <div class="theory-box">
    <h3>🏛️ Théorie des Traits (Great Man Theory)</h3>
    <p><strong>Concept :</strong> Les leaders naissent avec des traits de personnalité spécifiques.</p>
    <ul class="content-list">
    <li><strong>Traits clés :</strong> Intelligence, confiance en soi, charisme, intégrité</li>
    <li><strong>Limite :</strong> Ne prend pas en compte l'apprentissage et le contexte</li>
    <li><strong>Application :</strong> Recrutement de hauts potentiels</li>
    </ul>
    
    <div class="example-box">
    💡 <strong>Exemple :</strong Winston Churchill était considéré comme un "grand homme" né pour le leadership en temps de crise.
    </div>
    </div>
    
    <div class="theory-box">
    <h3>🔄 Leadership Transformationnel (Bass)</h3>
    <p><strong>Concept :</strong> Le leader transforme et inspire ses followers au-delà de leurs intérêts immédiats.</p>
    <ul class="content-list">
    <li><strong>4 composantes :</strong> Influence idéalisée, motivation inspirante, stimulation intellectuelle, considération individualisée</li>
    <li><strong>Avantage :</strong> Crée un engagement profond et durable</li>
    <li><strong>Contexte :</strong> Changement organisationnel, innovation</li>
    </ul>
    
    <div class="example-box">
    💡 <strong>Exemple :</strong> Martin Luther King a transformé la vision de toute une société grâce à son leadership transformationnel.
    </div>
    </div>
    
    <div class="theory-box">
    <h3>📊 Modèle de Fiedler (Contingence)</h3>
    <p><strong>Concept :</strong> L'efficacité du leadership dépend de l'adéquation entre le style du leader et la situation.</p>
    <ul class="content-list">
    <li><strong>3 facteurs situationnels :</strong> Relations leader-membres, structure de la tâche, pouvoir positionnel</li>
    <li><strong>Approche :</strong> Soit on change le leader, soit on change la situation</li>
    <li><strong>Application :</strong> Affectation stratégique des leaders</li>
    </ul>
    
    <div class="example-box">
    💡 <strong>Exemple :</strong> Un leader relationnel performe mieux dans des situations de crise où la confiance est cruciale.
    </div>
    </div>
    
    <div class="theory-box">
    <h3>🚀 Leadership Serviteur (Greenleaf)</h3>
    <p><strong>Concept :</strong> Le leader sert d'abord ses collaborateurs avant de les diriger.</p>
    <ul class="content-list">
    <li><strong>Principes :</strong> Écoute, empathie, conscientisation, persuasion</li>
    <li><strong>Bénéfice :</strong> Crée une culture de confiance et d'engagement</li>
    <li><strong>Contexte :</strong> Organisations apprenantes, équipes créatives</li>
    </ul>
    
    <div class="example-box">
    💡 <strong>Exemple :</strong> Herb Kelleher, fondateur de Southwest Airlines, priorisait le bien-être des employés avant les profits.
    </div>
    </div>
    
    <h3>🎥 Vidéos sur les théories</h3>
    <a href="https://youtu.be/example" target="_blank" class="video-link">▶ Les différentes théories du leadership</a>
    <a href="https://youtu.be/example" target="_blank" class="video-link">▶ Leadership transformationnel vs transactionnel</a>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 13 : Styles de Commandement ---
with tabs[13]:
    st.markdown("""
    <div class="modern-card">
    <h2>🎯 Synthèse des Styles de Commandement</h2>
    
    <p class="content-paragraph">Les styles de commandement varient selon le contexte et les personnes.</p>
    
    <h3>📊 Intégration des théories</h3>
    
    <div class="theory-box">
    <h4>🔄 Comment McGregor influence les styles modernes</h4>
    <p class="content-paragraph">La <strong>Théorie Y</strong> de McGregor a ouvert la voie aux styles participatifs modernes :</p>
    <ul class="content-list">
    <li><strong>Visionnaire</strong> : Fait appel à l'adhésion et l'engagement (Y)</li>
    <li><strong>Coaching</strong> : Développe l'autonomie et la responsabilité (Y)</li>
    <li><strong>Démocratique</strong> : Considère l'intelligence collective (Y)</li>
    <li><strong>Directif</strong> : Correspond à la vision traditionnelle (X)</li>
    </ul>
    </div>
    
    <h3>🎚️ Le continuum des styles</h3>
    <div class="content-paragraph" style="text-align:center; padding:1rem; background:#f8fafc; border-radius:8px;">
    <strong>Autoritaire (X) ←---→ Participatif (Y)</strong><br>
    <small>Contrôle total ←---→ Autonomie totale</small>
    </div>
    
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Un chef de projet en informatique utilise le style participatif pour les choix techniques (Y) mais autoritaire pour les deadlines critiques (X).
    </div>
    
    <h3>🎥 Vidéo complémentaire</h3>
    <a href="https://youtu.be/vilZazhIjoc?si=b4PNNY5P8SAqu9_p" target="_blank" class="video-link">▶ Les styles de leadership en pratique</a>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 14 : Style Situationnel ---
with tabs[14]:
    st.markdown("""
    <div class="modern-card">
    <h2>🔄 Modèle Situationnel de Hersey-Blanchard</h2>
    <p class="content-paragraph">Il n'existe pas un seul bon style, mais un <strong>style adapté à la maturité</strong> de chaque collaborateur.</p>
    
    <h3>📈 Les 4 niveaux de maturité</h3>
    <ul class="content-list">
    <li><strong>M1 :</strong> Incompétent et non motivé → Style directif (Théorie X)</li>
    <li><strong>M2 :</strong> Incompétent mais motivé → Style persuasif (Transition X→Y)</li>
    <li><strong>M3 :</strong> Compétent mais démotivé → Style participatif (Théorie Y)</li>
    <li><strong>M4 :</strong> Compétent et motivé → Style délégatif (Théorie Y avancée)</li>
    </ul>
    
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Sophie, manager dans la vente, utilise le style directif avec les nouveaux vendeurs (M1 - Théorie X) et délégatif avec ses tops vendeurs (M4 - Théorie Y).
    </div>
    
    <h3>🔗 Lien avec McGregor</h3>
    <p class="content-paragraph">Le modèle situationnel montre qu'un bon manager sait <strong>alterner entre Théorie X et Y</strong> selon la situation et les personnes.</p>
    
    <h3>🎥 Vidéo explicative</h3>
    <a href="https://youtu.be/iRBQqfJaoo4?si=Kbhele-WRaC6wqGw" target="_blank" class="video-link">▶ Le leadership situationnel</a>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 15 : Compétences Clés ---
with tabs[15]:
    st.markdown("""
    <div class="modern-card">
    <h2>🔑 Compétences Clés du Leader Moderne</h2>
    
    <h3>💪 Compétences techniques vs soft skills</h3>
    
    <div class="content-paragraph">
    <strong>Hard Skills :</strong> Connaissances métier, expertise technique
    </div>
    
    <div class="content-paragraph">
    <strong>Soft Skills :</strong> Intelligence émotionnelle, communication, adaptabilité
    </div>
    
    <h3>🏆 Les 5 compétences indispensables</h3>
    <ul class="content-list">
    <li><strong>Vision stratégique :</strong> Voir loin et large</li>
    <li><strong>Communication inspirante :</strong> Parler avec cœur et conviction</li>
    <li><strong>Décision courageuse :</strong> Assumer ses choix</li>
    <li><strong>Délégation efficace :</strong> Faire confiance et responsabiliser</li>
    <li><strong>Résilience émotionnelle :</strong> Rebondir face aux échecs</li>
    </ul>
    
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Elon Musk combine expertise technique (hard skill) et capacité à inspirer des milliers d'employés (soft skill).
    </div>
    
    <h3>🎥 Vidéo sur les compétences</h3>
    <a href="https://youtu.be/2tDKptsgvVU?si=fSS4rwyv7EM9biy9" target="_blank" class="video-link">▶ Les compétences d'un leader</a>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 16 : Intelligence Émotionnelle ---
with tabs[16]:
    st.markdown("""
    <div class="modern-card">
    <h2>🧠 Intelligence Émotionnelle (IE) au service du leadership</h2>
    
    <p class="content-paragraph">L'IE représente <strong>80% de la performance</strong> en leadership selon Daniel Goleman.</p>
    
    <h3>🎯 Les 4 piliers de l'IE</h3>
    <ul class="content-list">
    <li><strong>Conscience de soi :</strong> Comprendre ses émotions</li>
    <li><strong>Maîtrise de soi :</strong> Gérer ses réactions émotionnelles</li>
    <li><strong>Conscience sociale :</strong> Percevoir les émotions des autres</li>
    <li><strong>Gestion des relations :</strong> Influencer positivement les émotions collectives</li>
    </ul>
    
    <div class="example-box">
    💡 <strong>Exemple concret :</strong> Lors d'une restructuration, Pierre, directeur RH, reconnaît sa propre anxiété et celle de son équipe, et organise des entretiens individuels pour rassurer.
    </div>
    
    <h3>🔗 Lien avec McGregor</h3>
    <p class="content-paragraph">L'Intelligence Émotionnelle permet de <strong>dépasser la dichotomie X/Y</strong> en comprenant les besoins émotionnels de chaque collaborateur.</p>
    
    <h3>🎥 Vidéo explicative</h3>
    <a href="https://youtu.be/UOS8X33jOZo?si=IXlKW4TF9CEi6E3h" target="_blank" class="video-link">▶ Intelligence émotionnelle pour un meilleur leadership</a>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 17 : Études de Cas ---
with tabs[17]:
    st.markdown("""
    <div class="modern-card">
    <h2>📊 Études de Cas Concrets</h2>
    
    <h3>🏢 Cas 1 : Transformation digitale</h3>
    <p class="content-paragraph"><strong>Contexte :</strong> Une PME familiale doit se digitaliser face à la concurrence.</p>
    <p class="content-paragraph"><strong>Défi :</strong> Résistance au changement des équipes historiques.</p>
    <p class="content-paragraph"><strong>Solution :</strong> Leadership visionnaire + coaching progressif.</p>
    
    <div class="example-box">
    💡 <strong>Analyse McGregor :</strong> Transition réussie de la Théorie X (habitudes ancrées) vers la Théorie Y (autonomie dans les nouveaux outils).
    </div>
    
    <h3>🏭 Cas 2 : Fusion d'entreprises</h3>
    <p class="content-paragraph"><strong>Contexte :</strong> Deux entreprises de cultures différentes fusionnent.</p>
    <p class="content-paragraph"><strong>Défi :</strong> Choc culturel et perte de repères.</p>
    <p class="content-paragraph"><strong>Solution :</strong> Leadership affiliatif pour créer du lien + démocratique pour co-construire la nouvelle culture.</p>
    
    <div class="example-box">
    💡 <strong>Analyse McGregor :</strong> Application de la Théorie Y pour valoriser l'intelligence collective et créer une nouvelle identité partagée.
    </div>
    
    <h3>🎥 Vidéo d'étude de cas</h3>
    <a href="https://youtu.be/example" target="_blank" class="video-link">▶ Cas concret de leadership</a>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 18 : QUIZ 1 - Fondamentaux du Leadership ---
with tabs[18]:
    st.markdown("""
    <div class="quiz-section">
    <h2>🧠 QUIZ 1 - Fondamentaux du Leadership</h2>
    <p class="content-paragraph">Testez vos connaissances sur les concepts de base du leadership (10 questions)</p>
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
            "explication": "❌ Faux - Des études montrent que 70% des compétences de leadership s'acquièrent par la pratique et la formation."
        },
        {
            "question": "La Théorie Y de McGregor correspond à un style de management participatif et délégatif.",
            "correct": True,
            "explication": "✅ Vrai - La Théorie Y valorise l'autonomie et la responsabilité des employés."
        },
        {
            "question": "Un leader efficace passe plus de temps à écouter qu'à parler.",
            "correct": True,
            "explication": "✅ Vrai - L'écoute active est cruciale pour comprendre les besoins de son équipe."
        },
        {
            "question": "Le style de leadership directif doit toujours être évité car il est toxique.",
            "correct": False,
            "explication": "❌ Faux - Le style directif est nécessaire en situation de crise ou avec des débutants (Théorie X contextuelle)."
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
            "explication": "❌ Faux - Le leader visionnaire se concentre sur la vision à long terme (approche Théorie Y)."
        },
        {
            "question": "Le leadership situationnel implique d'adapter son style à la maturité de chaque collaborateur.",
            "correct": True,
            "explication": "✅ Vrai - Adapter le style selon la compétence et la motivation de chacun."
        },
        {
            "question": "McGregor recommandait d'utiliser exclusivement la Théorie Y dans toutes les situations.",
            "correct": False,
            "explication": "❌ Faux - McGregor présentait deux visions, mais le leadership situationnel montre qu'il faut adapter son approche."
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
        
        # Évaluation détaillée
        st.markdown(f"""
        <div class="evaluation-box">
        <h3>📊 Évaluation du Quiz 1</h3>
        <p><strong>Score : {score_quiz1}/10</strong></p>
        <p><strong>Niveau :</strong> {'🌟 Expert en théories du leadership' if score_quiz1 >= 9 
            else '💡 Bonne maîtrise des concepts' if score_quiz1 >= 7
            else '📚 Connaissances de base' if score_quiz1 >= 5
            else '🎯 En développement'}</p>
        <p><strong>Recommandation :</strong> {
            'Vous maîtrisez parfaitement les théories fondamentales dont McGregor !' if score_quiz1 >= 9
            else 'Vous comprenez bien les concepts clés, continuez à approfondir.' if score_quiz1 >= 7
            else 'Revoyez les théories de McGregor et leurs applications pratiques.' if score_quiz1 >= 5
            else 'Reprenez les bases des théories X et Y de McGregor.'
        }</p>
        </div>
        """, unsafe_allow_html=True)

# --- Slide 19 : QUIZ 2 - Styles et Mise en Pratique ---
with tabs[19]:
    st.markdown("""
    <div class="quiz-section">
    <h2>🎯 QUIZ 2 - Styles de Leadership et McGregor</h2>
    <p class="content-paragraph">Testez votre capacité à identifier les styles de leadership et leur lien avec les théories de McGregor (10 questions)</p>
    </div>
    """, unsafe_allow_html=True)
    
    quiz2_questions = [
        {
            "question": "Quel style de leadership correspond le mieux à la Théorie X de McGregor ?",
            "options": ["Directif", "Laissez-faire", "Visionnaire", "Affiliatif"],
            "correct": "Directif",
            "explication": "✅ Le style directif correspond à la Théorie X : contrôle, supervision étroite."
        },
        {
            "question": "Dans une situation de crise urgente, quel style est le plus approprié ?",
            "options": ["Démocratique", "Directif", "Coaching", "Affiliatif"],
            "correct": "Directif",
            "explication": "✅ Le style directif permet des décisions rapides en situation d'urgence (approche Théorie X contextuelle)."
        },
        {
            "question": "Quel style utilise-t-on principalement pour développer les compétences individuelles ?",
            "options": ["Visionnaire", "Coaching", "Directif", "Laissez-faire"],
            "correct": "Coaching",
            "explication": "✅ Le style coaching se concentre sur le développement personnel (approche Théorie Y)."
        },
        {
            "question": "La Théorie Y de McGregor postule que :",
            "options": [
                "Les employés doivent être contrôlés étroitement",
                "Le travail est aussi naturel que le jeu",
                "La paresse est naturelle chez l'humain", 
                "Les sanctions sont nécessaires pour motiver"
            ],
            "correct": "Le travail est aussi naturel que le jeu",
            "explication": "✅ La Théorie Y considère que le travail est naturel et que les gens peuvent s'auto-motiver."
        },
        {
            "question": "Quel style implique de consulter l'équipe avant de prendre une décision importante ?",
            "options": ["Directif", "Démocratique", "Visionnaire", "Laissez-faire"],
            "correct": "Démocratique",
            "explication": "✅ Le style démocratique valorise la participation de l'équipe (approche Théorie Y)."
        },
        {
            "question": "Un collaborateur débutant mais très motivé a besoin de :",
            "options": ["Autonomie totale", "Instructions claires et encouragement", "Liberté créative", "Peu de supervision"],
            "correct": "Instructions claires et encouragement",
            "explication": "✅ Le style persuasif convient aux débutants motivés (transition entre Théorie X et Y)."
        },
        {
            "question": "Quel style est centré sur la communication d'une vision inspirante ?",
            "options": ["Coaching", "Visionnaire", "Affiliatif", "Directif"],
            "correct": "Visionnaire",
            "explication": "✅ Le leader visionnaire explique le 'pourquoi' et inspire (approche Théorie Y)."
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
            "explication": "✅ Le style directif peut empêcher l'autonomie (risque de la Théorie X)."
        },
        {
            "question": "Pour un collaborateur expérimenté mais temporairement démotivé, on utilise :",
            "options": ["Style directif", "Style laissez-faire", "Style participatif", "Style visionnaire"],
            "correct": "Style participatif",
            "explication": "✅ Le style participatif redonne de la motivation par l'implication (approche Théorie Y)."
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
        
        # Évaluation détaillée avec remarques basées sur les résultats
        st.markdown(f"""
        <div class="evaluation-box">
        <h3>📊 Évaluation du Quiz 2</h3>
        <p><strong>Score : {score_quiz2}/10</strong></p>
        """, unsafe_allow_html=True)
        
        if score_quiz2 >= 9:
            st.markdown("""
            <p><strong>🎯 Remarques :</strong></p>
            <ul>
            <li>Excellente compréhension des styles de leadership</li>
            <li>Maîtrise parfaite des liens entre théorie et pratique</li>
            <li>Capacité à adapter le style à la situation</li>
            </ul>
            <p><strong>💡 Conseil :</strong> Concentrez-vous maintenant sur le développement de votre intelligence situationnelle avancée.</p>
            """, unsafe_allow_html=True)
        elif score_quiz2 >= 7:
            st.markdown("""
            <p><strong>🎯 Remarques :</strong></p>
            <ul>
            <li>Bonne compréhension des concepts fondamentaux</li>
            <li>Capacité à identifier la plupart des styles appropriés</li>
            <li>Quelques hésitations dans les situations complexes</li>
            </ul>
            <p><strong>💡 Conseil :</strong> Pratiquez l'analyse de cas concrets pour renforcer votre jugement situationnel.</p>
            """, unsafe_allow_html=True)
        elif score_quiz2 >= 5:
            st.markdown("""
            <p><strong>🎯 Remarques :</strong></p>
            <ul>
            <li>Bases acquises mais besoin de renforcement</li>
            <li>Difficulté à faire les liens théorie/pratique dans certains cas</li>
            <li>Compréhension partielle des nuances situationnelles</li>
            </ul>
            <p><strong>💡 Conseil :</strong> Revoyez les études de cas et observez des leaders expérimentés en action.</p>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <p><strong>🎯 Remarques :</strong></p>
            <ul>
            <li>Début de compréhension des concepts</li>
            <li>Besoin de solidifier les bases théoriques</li>
            <li>Difficulté à appliquer les théories en pratique</li>
            </ul>
            <p><strong>💡 Conseil :</strong> Commencez par maîtriser les théories X et Y de McGregor avant de passer aux applications pratiques.</p>
            """, unsafe_allow_html=True)
        
        st.markdown("</div>", unsafe_allow_html=True)

# --- Slide 20 : PLAN D'ACTION ---
with tabs[20]:
    st.markdown("""
    <div class="modern-card">
    <h2>📝 Votre Plan d'Action Personnalisé</h2>
    <p class="content-paragraph">Basé sur vos résultats aux quiz, voici un plan d'action concret intégrant les théories de McGregor.</p>
    </div>
    """, unsafe_allow_html=True)
    
    score_quiz1 = st.session_state.get('score_quiz1', 0)
    score_quiz2 = st.session_state.get('score_quiz2', 0)
    score_total = score_quiz1 + score_quiz2
    
    if score_total > 0:
        if score_total >= 16:
            niveau = "🌟 LEADER AVANCÉ"
            plan_content = """
            <h4>🎯 Plan d'Action - 4 Semaines</h4>
            <div class="content-list">
            <li><strong>Semaine 1 : Mentorat avancé</strong> - Coacher 2 personnes en utilisant la Théorie Y</li>
            <li><strong>Semaine 2 : Innovation stratégique</strong> - Organiser un brainstorming avec approche participative</li>
            <li><strong>Semaine 3 : Développement d'équipe</strong> - Programme de feedback 360°</li>
            <li><strong>Semaine 4 : Excellence situationnelle</strong> - Mesurer votre impact et ajuster style X/Y selon contexte</li>
            </div>
            """
        elif score_total >= 12:
            niveau = "💡 LEADER INTERMÉDIAIRE"
            plan_content = """
            <h4>🎯 Plan d'Action - 4 Semaines</h4>
            <div class="content-list">
            <li><strong>Semaine 1 : Bases solides</strong> - Pratiquer l'écoute active quotidienne</li>
            <li><strong>Semaine 2 : Expérimentation</strong> - Tester 3 styles différents et noter les résultats</li>
            <li><strong>Semaine 3 : Intelligence émotionnelle</strong> - Tenir un journal émotionnel</li>
            <li><strong>Semaine 4 : Consolidation McGregor</strong> - Analyser quand utiliser Théorie X vs Y</li>
            </div>
            """
        else:
            niveau = "📚 LEADER EN DÉVELOPPEMENT"
            plan_content = """
            <h4>🎯 Plan d'Action - 4 Semaines</h4>
            <div class="content-list">
            <li><strong>Semaine 1 : Fondamentaux McGregor</strong> - Étudier les théories X et Y</li>
            <li><strong>Semaine 2 : Confiance</strong> - Prendre la parole en réunion</li>
            <li><strong>Semaine 3 : Application</strong> - Tester un premier style conscient</li>
            <li><strong>Semaine 4 : Évaluation</strong> - Établir un plan de développement sur 3 mois</li>
            </div>
            """
        
        st.markdown(f"""
        <div class="plan-action">
        <h3>{niveau}</h3>
        <p><strong>Quiz 1 (Théories) :</strong> {score_quiz1}/10 | <strong>Quiz 2 (Pratique) :</strong> {score_quiz2}/10</p>
        {plan_content}
        </div>
        """, unsafe_allow_html=True)
        
    else:
        st.info("ℹ️ Complétez les deux quiz pour générer votre plan d'action personnalisé.")

# --- Slide 21 : Synthèse ---
with tabs[21]:
    st.markdown("""
    <div class="modern-card">
    <h2>🎓 Synthèse du Parcours Leadership</h2>
    
    <h3>🔑 Les 5 points clés à retenir</h3>
    <ul class="content-list">
    <li><strong>1. Adaptabilité :</strong> Un bon leader adapte son style à la situation et aux personnes</li>
    <li><strong>2. Authenticité :</strong> Le leadership vient de la cohérence entre vos paroles et vos actions</li>
    <li><strong>3. Vision :</strong> Un leader sait où il va et emmène les autres avec lui</li>
    <li><strong>4. Humilité :</strong> Reconnaître ses erreurs et apprendre constamment</li>
    <li><strong>5. Impact :</strong> Mesurer son leadership par l'impact positif sur les autres</li>
    </ul>
    
    <div class="quote-card">
    « Le véritable leadership ne consiste pas à avoir une position, mais à avoir une influence positive. »
    </div>
    
    <h3>🚀 Prochaines étapes</h3>
    <p class="content-paragraph">Maintenant que vous avez les bases, continuez à développer vos compétences par la pratique, l'observation et la formation continue.</p>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 22 : Secteurs d'Application ---
with tabs[22]:
    st.markdown("""
    <div class="modern-card">
    <h2>🏥 Leadership dans Différents Secteurs</h2>
    
    <h3>💻 Technologie</h3>
    <p class="content-paragraph"><strong>Style dominant :</strong> Visionnaire + Laissez-faire</p>
    <div class="example-box">
    💡 <strong>Exemple :</strong> Les leaders tech comme Sundar Pichai (Google) combinent vision long terme et autonomie des ingénieurs.
    </div>
    
    <h3>🏭 Industrie</h3>
    <p class="content-paragraph"><strong>Style dominant :</strong> Directif + Démocratique</p>
    <div class="example-box">
    💡 <strong>Exemple :</strong> Dans l'automobile, sécurité stricte (directif) mais amélioration continue participative (démocratique).
    </div>
    
    <h3>🏥 Santé</h3>
    <p class="content-paragraph"><strong>Style dominant :</strong> Affiliatif + Coaching</p>
    <div class="example-box">
    💡 <strong>Exemple :</strong> Les chefs de service en hôpital priorisent la cohésion d'équipe et le développement des jeunes médecins.
    </div>
    
    <h3>🎓 Éducation</h3>
    <p class="content-paragraph"><strong>Style dominant :</strong> Visionnaire + Coaching</p>
    <div class="example-box">
    💡 <strong>Exemple :</strong> Les directeurs d'établissement inspirent une vision pédagogique tout en coachant leurs enseignants.
    </div>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 23 : Erreurs Courantes ---
with tabs[23]:
    st.markdown("""
    <div class="modern-card">
    <h2>🚫 Erreurs Courantes en Leadership</h2>
    
    <h3>❌ Les 7 pièges à éviter</h3>
    <ul class="content-list">
    <li><strong>1. Micro-management :</strong> Trop contrôler tue l'autonomie et la créativité</li>
    <li><strong>2. Incohérence :</strong> Dire une chose et faire le contraire</li>
    <li><strong>3. Manque de reconnaissance :</strong> Oublier de valoriser les efforts</li>
    <li><strong>4. Communication insuffisante :</strong> Ne pas partager l'information</li>
    <li><strong>5. Éviter les conflits :</strong> Laisser pourrir les situations difficiles</li>
    <li><strong>6. Style unique :</strong> Utiliser le même style dans toutes les situations</li>
    <li><strong>7. Négliger son développement :</strong> Arrêter d'apprendre et de s'améliorer</li>
    </ul>
    
    <div class="example-box">
    💡 <strong>Conseil :</strong> Identifiez une erreur que vous pourriez commettre et travaillez spécifiquement dessus ce mois-ci.
    </div>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 24 : Développement Personnel ---
with tabs[24]:
    st.markdown("""
    <div class="modern-card">
    <h2>🌱 Développement de Votre Leadership</h2>
    
    <h3>📈 Parcours de progression</h3>
    
    <div class="content-paragraph">
    <strong>Niveau 1 : Leadership de soi</strong> - Se connaître, s'auto-discipliner, se motiver
    </div>
    
    <div class="content-paragraph">
    <strong>Niveau 2 : Leadership d'équipe</strong> - Influencer un petit groupe, créer de la cohésion
    </div>
    
    <div class="content-paragraph">
    <strong>Niveau 3 : Leadership organisationnel</strong> - Développer une culture, structurer une organisation
    </div>
    
    <h3>🛠️ Outils de développement</h3>
    <ul class="content-list">
    <li><strong>Auto-évaluation :</strong> Tests de personnalité et de styles de leadership</li>
    <li><strong>Mentorat :</strong> Apprendre auprès de leaders expérimentés</li>
    <li><strong>Feedback 360° :</strong> Obtenir des retours de tous les côtés</li>
    <li><strong>Formation continue :</strong> Lectures, séminaires, certifications</li>
    <li><strong>Pratique réflexive :</strong> Tenir un journal de leadership</li>
    </ul>
    
    <div class="quote-card">
    « Le leadership n'est pas une destination, c'est un voyage d'apprentissage continu. »
    </div>
    </div>
    """, unsafe_allow_html=True)

# --- NOUVEAU SLIDE 25 : Conseils Pratiques ---
with tabs[25]:
    st.markdown("""
    <div class="modern-card">
    <h2>💡 Conseils Pratiques pour Développer Votre Leadership</h2>
    
    <div class="advice-card">
    <h3>🎯 Conseil 1 : Commencez par vous connaître</h3>
    <p>Identifiez vos forces et zones d'amélioration grâce à des tests de personnalité et du feedback régulier.</p>
    </div>
    
    <div class="advice-card">
    <h3>👂 Conseil 2 : Développez l'écoute active</h3>
    <p>Pratiquez l'écoute sans interruption, posez des questions ouvertes et reformulez pour confirmer votre compréhension.</p>
    </div>
    
    <div class="advice-card">
    <h3>🔄 Conseil 3 : Expérimentez différents styles</h3>
    <p>Testez consciemment un style différent chaque semaine et observez les résultats avec votre équipe.</p>
    </div>
    
    <div class="advice-card">
    <h3>📚 Conseil 4 : Cultivez l'apprentissage continu</h3>
    <p>Lisez un livre par mois sur le leadership, suivez des formations et observez les leaders que vous admirez.</p>
    </div>
    
    <div class="advice-card">
    <h3>🤝 Conseil 5 : Construisez votre réseau</h3>
    <p>Entourez-vous de mentors, de pairs et de collaborateurs qui vous challengent et vous inspirent.</p>
    </div>
    
    <div class="advice-card">
    <h3>💪 Conseil 6 : Pratiquez la résilience</h3>
    <p>Acceptez l'échec comme une opportunité d'apprentissage et développez votre capacité à rebondir.</p>
    </div>
    
    <div class="advice-card">
    <h3>🎉 Conseil 7 : Célébrez les succès</h3>
    <p>Reconnaissez et valorisez les contributions de chacun, aussi petites soient-elles.</p>
    </div>
    
    <div class="quote-card">
    « Le leadership n'est pas une position ou un titre, c'est une action et un exemple. » — Donald McGannon
    </div>
    </div>
    """, unsafe_allow_html=True)

# --- Slide 26 : Ressources ---
with tabs[26]:
    st.markdown("""
    <div class="modern-card">
    <h2>📚 Ressources Complémentaires</h2>
    <p class="content-paragraph">Toutes les vidéos recommandées pour votre formation.</p>
    
    <h3>🎥 Playlist complète</h3>
    <a href="https://youtu.be/hCtFbHJQHvk?si=r00mEZ8Mnnzecd1I" target="_blank" class="video-link">▶ Définition d'un leader</a>
    <a href="https://youtu.be/Ej9M-U1EiGY?si=kgqe2lA8Pe6oF26Q" target="_blank" class="video-link">▶ Définition du leadership</a>
    <a href="https://youtu.be/mhkLc0HEtR0?si=n4rAkltZW8gIGu7g" target="_blank" class="video-link">▶ Différence leader/management</a>
    <a href="https://youtu.be/vilZazhIjoc?si=b4PNNY5P8SAqu9_p" target="_blank" class="video-link">▶ Les 5 styles de leadership</a>
    <a href="https://youtu.be/iRBQqfJaoo4?si=Kbhele-WRaC6wqGw" target="_blank" class="video-link">▶ Leadership situationnel</a>
    <a href="https://youtu.be/2tDKptsgvVU?si=fSS4rwyv7EM9biy9" target="_blank" class="video-link">▶ Compétences d'un leader</a>
    <a href="https://youtu.be/UOS8X33jOZo?si=IXlKW4TF9CEi6E3h" target="_blank" class="video-link">▶ Intelligence émotionnelle</a>
    
    <h3>📖 Lectures recommandées</h3>
    <ul class="content-list">
    <li><strong>"La Dimension Humaine de l'Entreprise"</strong> - Douglas McGregor</li>
    <li><strong>"Leaders Eat Last"</strong> - Simon Sinek</li>
    <li><strong>"L'Intelligence Émotionnelle"</strong> - Daniel Goleman</li>
    <li><strong>"Les 7 Habitudes des Gens Efficaces"</strong> - Stephen Covey</li>
    <li><strong>"Start with Why"</strong> - Simon Sinek</li>
    <li><strong>"Le Leadership Serviteur"</strong> - Robert Greenleaf</li>
    </ul>
    
    <div class="quote-card">
    « L'investissement le plus important que vous puissiez faire est d'investir en vous-même. » — Warren Buffett
    </div>
    </div>
    """, unsafe_allow_html=True)
