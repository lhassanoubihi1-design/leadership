import streamlit as st
import random

st.set_page_config(
    page_title="Leadership & Styles de Management",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS moderne pour une présentation en classe
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    .presentation-card {
        background: white;
        border-radius: 20px;
        padding: 3rem;
        margin: 2rem 0;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        border: none;
    }
    .slide-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-align: center;
        margin-bottom: 2rem;
    }
    .slide-subtitle {
        font-size: 2.2rem;
        font-weight: 700;
        color: #3730a3;
        margin: 2rem 0 1.5rem;
        text-align: center;
    }
    .content-box {
        background: #f8fafc;
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        border-left: 5px solid #4f46e5;
    }
    .example-card {
        background: #f0fdf4;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        border-left: 4px solid #10b981;
    }
    .theory-card {
        background: linear-gradient(135deg, #fef7ff, #faf5ff);
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        border: 2px solid #e9d5ff;
    }
    .quiz-container {
        background: linear-gradient(135deg, #fff7ed, #fffbeb);
        padding: 2.5rem;
        border-radius: 20px;
        margin: 2rem 0;
        border: 3px solid #fed7aa;
    }
    .navigation {
        display: flex;
        justify-content: space-between;
        margin: 2rem 0;
        padding: 1rem;
        background: #f8fafc;
        border-radius: 12px;
    }
</style>
""", unsafe_allow_html=True)

# Navigation entre slides
if 'current_slide' not in st.session_state:
    st.session_state.current_slide = 0

# Fonctions de navigation
def next_slide():
    st.session_state.current_slide += 1

def prev_slide():
    if st.session_state.current_slide > 0:
        st.session_state.current_slide -= 1

# Contenu des slides
slides = [
    # Slide 0: Page de titre
    """
    <div class="presentation-card">
        <h1 class="slide-title">🎯 Leadership & Styles de Management</h1>
        <div style="text-align: center; margin: 3rem 0;">
            <h2 style="color: #64748b; font-size: 1.8rem; margin-bottom: 2rem;">
                Formation Interactive - Présentation en Classe
            </h2>
            <div style="font-size: 1.2rem; color: #475569; line-height: 1.8;">
                <p><strong>Durée :</strong> 45 minutes</p>
                <p><strong>Niveau :</strong> Débutant à Intermédiaire</p>
                <p><strong>Objectifs :</strong> Comprendre les bases du leadership et identifier son style</p>
            </div>
        </div>
    </div>
    """,
    
    # Slide 1: Introduction
    """
    <div class="presentation-card">
        <h1 class="slide-title">🚀 Pourquoi le Leadership ?</h1>
        
        <div class="content-box">
            <h3>💡 Le leadership n'est plus optionnel</h3>
            <p style="font-size: 1.3rem; line-height: 1.8;">
                Dans un monde en constante transformation, le leadership est devenu une <strong>compétence essentielle</strong> 
                pour tous, pas seulement pour les dirigeants.
            </p>
        </div>
        
        <div class="example-card">
            <h4>🌍 Exemples concrets :</h4>
            <ul style="font-size: 1.2rem; line-height: 1.8;">
                <li><strong>En entreprise :</strong> Manager d'équipe projet</li>
                <li><strong>À l'école :</strong> Chef de groupe de travail</li>
                <li><strong>Dans la vie quotidienne :</strong> Organisation d'événements</li>
            </ul>
        </div>
        
        <div style="text-align: center; margin-top: 3rem;">
            <h3 style="color: #4f46e5;">« Le leadership, c'est l'art d'influencer sans contraindre »</h3>
        </div>
    </div>
    """,
    
    # Slide 2: Définitions
    """
    <div class="presentation-card">
        <h1 class="slide-title">📚 Les Concepts Clés</h1>
        
        <div class="content-box">
            <h3>🎯 Qu'est-ce que le Leadership ?</h3>
            <p style="font-size: 1.3rem; line-height: 1.8;">
                <strong>Capacité à influencer, inspirer et guider</strong> des personnes ou des groupes 
                vers l'atteinte d'objectifs communs.
            </p>
        </div>
        
        <div class="content-box">
            <h3>⚖️ Leadership vs Management</h3>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 1rem;">
                <div style="padding: 1.5rem; background: #eff6ff; border-radius: 10px;">
                    <h4 style="color: #1e40af;">Leadership</h4>
                    <ul style="line-height: 1.6;">
                        <li>Inspire le changement</li>
                        <li>Crée une vision</li>
                        <li>Développe les personnes</li>
                        <li>Fait adhérer</li>
                    </ul>
                </div>
                <div style="padding: 1.5rem; background: #f0fdf4; border-radius: 10px;">
                    <h4 style="color: #065f46;">Management</h4>
                    <ul style="line-height: 1.6;">
                        <li>Organise l'exécution</li>
                        <li>Planifie les processus</li>
                        <li>Contrôle les résultats</li>
                        <li>Gère les ressources</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    """,
    
    # Slide 3: Théories de McGregor
    """
    <div class="presentation-card">
        <h1 class="slide-title">🧠 Théories X et Y de McGregor</h1>
        
        <div class="theory-card">
            <h3>📋 Théorie X - Vision traditionnelle</h3>
            <p><strong>Postulats :</strong></p>
            <ul style="line-height: 1.8; font-size: 1.2rem;">
                <li>Les personnes n'aiment pas naturellement le travail</li>
                <li>Elles doivent être contrôlées et dirigées</li>
                <li>Elles évitent les responsabilités</li>
                <li>Elles recherchent la sécurité avant tout</li>
            </ul>
        </div>
        
        <div class="theory-card">
            <h3>📈 Théorie Y - Vision moderne</h3>
            <p><strong>Postulats :</strong></p>
            <ul style="line-height: 1.8; font-size: 1.2rem;">
                <li>Le travail est aussi naturel que le jeu</li>
                <li>Les personnes peuvent s'auto-contrôler</li>
                <li>Elles recherchent les responsabilités</li>
                <li>La créativité est largement répandue</li>
            </ul>
        </div>
        
        <div class="example-card">
            <h4>💡 Application pratique :</h4>
            <p style="font-size: 1.2rem;">
                Un manager utilise la <strong>Théorie X</strong> en situation de crise (directif) 
                et la <strong>Théorie Y</strong> pour l'innovation (participatif).
            </p>
        </div>
    </div>
    """,
    
    # Slide 4: Styles de Leadership (Goleman)
    """
    <div class="presentation-card">
        <h1 class="slide-title">🎨 Les 6 Styles de Leadership</h1>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 2rem 0;">
            <div style="padding: 1.5rem; background: #fef7ff; border-radius: 12px; border-left: 4px solid #8b5cf6;">
                <h4>👁️ Visionnaire</h4>
                <p><em>"Viens avec moi vers cette vision"</em></p>
                <p style="font-size: 0.95rem;">Idéal pour les changements et l'innovation</p>
            </div>
            <div style="padding: 1.5rem; background: #f0fdf4; border-radius: 12px; border-left: 4px solid #10b981;">
                <h4>🎯 Coaching</h4>
                <p><em>"Je t'aide à te développer"</em></p>
                <p style="font-size: 0.95rem;">Développe les compétences individuelles</p>
            </div>
            <div style="padding: 1.5rem; background: #fefce8; border-radius: 12px; border-left: 4px solid #eab308;">
                <h4>🤝 Affiliatif</h4>
                <p><em>"Les relations d'abord"</em></p>
                <p style="font-size: 0.95rem;">Crée l'harmonie et résout les conflits</p>
            </div>
            <div style="padding: 1.5rem; background: #eff6ff; border-radius: 12px; border-left: 4px solid #3b82f6;">
                <h4>🗳️ Démocratique</h4>
                <p><em>"Qu'en pensez-vous ?"</em></p>
                <p style="font-size: 0.95rem;">Implique l'équipe dans les décisions</p>
            </div>
            <div style="padding: 1.5rem; background: #fef2f2; border-radius: 12px; border-left: 4px solid #ef4444;">
                <h4>⚡ Directif</h4>
                <p><em>"Fais ce que je te dis"</em></p>
                <p style="font-size: 0.95rem;">En situation de crise ou urgence</p>
            </div>
            <div style="padding: 1.5rem; background: #faf5ff; border-radius: 12px; border-left: 4px solid #8b5cf6;">
                <h4>🕊️ Laissez-faire</h4>
                <p><em>"À toi de jouer"</em></p>
                <p style="font-size: 0.95rem;">Avec des experts très autonomes</p>
            </div>
        </div>
    </div>
    """,
    
    # Slide 5: Intelligence Emotionnelle
    """
    <div class="presentation-card">
        <h1 class="slide-title">🧠 Intelligence Émotionnelle</h1>
        
        <div style="text-align: center; margin: 2rem 0;">
            <h3 style="color: #4f46e5; font-size: 1.8rem;">
                "L'IE représente 80% de la performance en leadership"<br>
                <small>- Daniel Goleman</small>
            </h3>
        </div>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 1rem; margin: 2rem 0;">
            <div style="text-align: center; padding: 1.5rem; background: #f8fafc; border-radius: 10px;">
                <h4 style="color: #7c3aed;">👁️ Conscience de soi</h4>
                <p style="font-size: 0.9rem;">Reconnaître ses émotions et leur impact</p>
            </div>
            <div style="text-align: center; padding: 1.5rem; background: #f8fafc; border-radius: 10px;">
                <h4 style="color: #7c3aed;">🎭 Maîtrise de soi</h4>
                <p style="font-size: 0.9rem;">Gérer ses réactions émotionnelles</p>
            </div>
            <div style="text-align: center; padding: 1.5rem; background: #f8fafc; border-radius: 10px;">
                <h4 style="color: #7c3aed;">👥 Conscience sociale</h4>
                <p style="font-size: 0.9rem;">Percevoir les émotions des autres</p>
            </div>
            <div style="text-align: center; padding: 1.5rem; background: #f8fafc; border-radius: 10px;">
                <h4 style="color: #7c3aed;">🤝 Gestion des relations</h4>
                <p style="font-size: 0.9rem;">Influencer positivement le groupe</p>
            </div>
        </div>
        
        <div class="example-card">
            <h4>💡 Exercice pratique :</h4>
            <p style="font-size: 1.1rem;">
                <strong>Journal émotionnel :</strong> Notez chaque jour une situation où vos émotions 
                ont influencé votre prise de décision.
            </p>
        </div>
    </div>
    """,
    
    # Slide 6: Quiz interactif
    """
    <div class="presentation-card">
        <h1 class="slide-title">🎯 Quiz Interactif</h1>
        
        <div class="quiz-container">
            <h3 style="text-align: center; color: #ea580c; margin-bottom: 2rem;">
                Testez vos connaissances sur le leadership
            </h3>
            
            <div style="background: white; padding: 2rem; border-radius: 12px; margin: 1rem 0;">
                <h4>Question 1/5 :</h4>
                <p style="font-size: 1.2rem; font-weight: 600;">
                    Quel style de leadership est le plus adapté pour une équipe d'experts très autonomes ?
                </p>
                
                <div style="margin: 1.5rem 0;">
                    <button style="width: 100%; padding: 1rem; margin: 0.5rem 0; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 8px; cursor: pointer;">
                        A) Style directif
                    </button>
                    <button style="width: 100%; padding: 1rem; margin: 0.5rem 0; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 8px; cursor: pointer;">
                        B) Style laissez-faire
                    </button>
                    <button style="width: 100%; padding: 1rem; margin: 0.5rem 0; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 8px; cursor: pointer;">
                        C) Style visionnaire
                    </button>
                    <button style="width: 100%; padding: 1rem; margin: 0.5rem 0; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 8px; cursor: pointer;">
                        D) Style affiliatif
                    </button>
                </div>
            </div>
            
            <div style="text-align: center; margin-top: 2rem;">
                <button style="background: #10b981; color: white; padding: 1rem 2rem; border: none; border-radius: 8px; font-size: 1.1rem; cursor: pointer;">
                    Vérifier la réponse
                </button>
            </div>
        </div>
    </div>
    """,
    
    # Slide 7: Études de cas
    """
    <div class="presentation-card">
        <h1 class="slide-title">📊 Études de Cas</h1>
        
        <div class="content-box">
            <h3>🏢 Cas 1 : Transformation digitale</h3>
            <p style="font-size: 1.2rem; line-height: 1.7;">
                <strong>Contexte :</strong> Une PME familiale doit se digitaliser<br>
                <strong>Défi :</strong> Résistance au changement des équipes historiques<br>
                <strong>Solution :</strong> Leadership visionnaire + coaching progressif<br>
                <strong>Résultat :</strong> 90% d'adoption des nouveaux outils en 6 mois
            </p>
        </div>
        
        <div class="content-box">
            <h3>🏭 Cas 2 : Fusion d'entreprises</h3>
            <p style="font-size: 1.2rem; line-height: 1.7;">
                <strong>Contexte :</strong> Deux entreprises fusionnent avec cultures différentes<br>
                <strong>Défi :</strong> Choc culturel et perte de repères<br>
                <strong>Solution :</strong> Leadership affiliatif + démocratique<br>
                <strong>Résultat :</strong> 75% de rétention des talents clés
            </p>
        </div>
        
        <div style="text-align: center; margin-top: 2rem;">
            <h3 style="color: #4f46e5;">💬 Discussion de groupe :</h3>
            <p style="font-size: 1.2rem;">
                Quel style de leadership auriez-vous utilisé dans ces situations ?
            </p>
        </div>
    </div>
    """,
    
    # Slide 8: Plan d'action personnel
    """
    <div class="presentation-card">
        <h1 class="slide-title">📝 Votre Plan d'Action</h1>
        
        <div class="content-box">
            <h3>🎯 Développez votre leadership en 4 semaines</h3>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 2rem 0;">
                <div style="padding: 1.5rem; background: #f0fdf4; border-radius: 10px;">
                    <h4>📅 Semaine 1 : Auto-évaluation</h4>
                    <ul style="line-height: 1.6;">
                        <li>Identifier son style dominant</li>
                        <li>Analyser 3 situations récentes</li>
                        <li>Demander du feedback</li>
                    </ul>
                </div>
                <div style="padding: 1.5rem; background: #eff6ff; border-radius: 10px;">
                    <h4>📅 Semaine 2 : Expérimentation</h4>
                    <ul style="line-height: 1.6;">
                        <li>Tester un nouveau style</li>
                        <li>Pratiquer l'écoute active</li>
                        <li>Tenir un journal</li>
                    </ul>
                </div>
                <div style="padding: 1.5rem; background: #fefce8; border-radius: 10px;">
                    <h4>📅 Semaine 3 : Développement</h4>
                    <ul style="line-height: 1.6;">
                        <li>Lire un livre sur le leadership</li>
                        <li>Trouver un mentor</li>
                        <li>Participer à une formation</li>
                    </ul>
                </div>
                <div style="padding: 1.5rem; background: #fef7ff; border-radius: 10px;">
                    <h4>📅 Semaine 4 : Consolidation</h4>
                    <ul style="line-height: 1.6;">
                        <li>Mesurer ses progrès</li>
                        <li>Adapter son approche</li>
                        <li>Partager ses apprentissages</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
    """,
    
    # Slide 9: Conclusion
    """
    <div class="presentation-card">
        <h1 class="slide-title">🎓 Synthèse & Conclusion</h1>
        
        <div style="text-align: center; margin: 3rem 0;">
            <h2 style="color: #4f46e5; font-size: 2.5rem; margin-bottom: 2rem;">
                Les 5 Clés du Leadership Réussi
            </h2>
        </div>
        
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin: 2rem 0;">
            <div style="text-align: center; padding: 2rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🎯</div>
                <h4>Vision Claire</h4>
                <p>Savoir où l'on va et pourquoi</p>
            </div>
            <div style="text-align: center; padding: 2rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">👂</div>
                <h4>Écoute Active</h4>
                <p>Comprendre avant d'être compris</p>
            </div>
            <div style="text-align: center; padding: 2rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">🔄</div>
                <h4>Adaptabilité</h4>
                <p>Changer de style selon la situation</p>
            </div>
            <div style="text-align: center; padding: 2rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">💪</div>
                <h4>Authenticité</h4>
                <p>Être cohérent et vrai</p>
            </div>
        </div>
        
        <div style="text-align: center; margin-top: 3rem; padding: 2rem; background: #f8fafc; border-radius: 15px;">
            <h3 style="color: #64748b;">« Le leadership n'est pas une position, c'est une action »</h3>
            <p style="font-size: 1.2rem; margin-top: 1rem;">
                Merci pour votre attention ! Questions ?
            </p>
        </div>
    </div>
    """
]

# Affichage de la slide actuelle
st.markdown(slides[st.session_state.current_slide], unsafe_allow_html=True)

# Navigation
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.session_state.current_slide > 0:
        if st.button('◀ Précédent', use_container_width=True):
            prev_slide()

with col2:
    progress = (st.session_state.current_slide + 1) / len(slides)
    st.progress(progress)
    st.caption(f"Slide {st.session_state.current_slide + 1} sur {len(slides)}")

with col3:
    if st.session_state.current_slide < len(slides) - 1:
        if st.button('Suivant ▶', use_container_width=True):
            next_slide()
    else:
        if st.button('Recommencer 🔄', use_container_width=True):
            st.session_state.current_slide = 0

# Informations pour la présentation en classe
with st.expander("🎓 Guide pour l'enseignant"):
    st.markdown("""
    **Durée estimée :** 45-60 minutes
    **Matériel nécessaire :** Projecteur, connexion internet
    **Public cible :** Étudiants en management, leadership, ressources humaines
    
    **Points clés à souligner :**
    - Différence entre leadership et management
    - Importance de l'adaptabilité du style
    - Rôle crucial de l'intelligence émotionnelle
    
    **Activités interactives suggérées :**
    - Quiz en groupe sur les styles de leadership
    - Discussion sur les études de cas
    - Partage d'expériences personnelles
    """)

# Lien pour partager la présentation
st.markdown("---")
st.markdown("### 📤 Partager cette présentation")
st.code("https://leadership-presentation.streamlit.app", language="text")