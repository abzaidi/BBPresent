import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="BrainBridge | Neurodiversity in Tech",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS matching original React app exactly
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Inter:wght@400;500;600;700&display=swap');
    
    /* Global styles */
    .stApp {
        background: linear-gradient(to bottom, #111827, #030712);
        color: white;
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding and sidebar */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .css-1d391kg {display: none;}
    
    /* Fixed top navigation bar */
    .top-nav {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        z-index: 50;
        background: rgba(17, 24, 39, 0.8);
        backdrop-filter: blur(12px);
        border-bottom: 1px solid #374151;
        padding: 1rem 0;
    }
    
    .nav-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 1.5rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .nav-logo {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .nav-brand {
        font-size: 1.25rem;
        font-weight: 700;
        background: linear-gradient(135deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Poppins', sans-serif;
    }
    
    .nav-links {
        display: flex;
        gap: 1.5rem;
        align-items: center;
    }
    
    .nav-link {
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        background: rgba(255, 255, 255, 0.05);
        color: #e5e7eb;
        text-decoration: none;
        font-size: 0.875rem;
        font-weight: 500;
        transition: all 0.3s ease;
        cursor: pointer;
        border: none;
    }
    
    .nav-link:hover {
        background: rgba(255, 255, 255, 0.1);
        color: white;
        transform: translateY(-1px);
    }
    
    /* Section styling */
    .section {
        min-height: 100vh;
        padding: 2rem 0;
        position: relative;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .section-header {
        color: #60a5fa;
        font-family: 'Poppins', sans-serif;
        font-size: 3rem;
        font-weight: 700;
        margin: 1rem 0 1rem 0;
        text-align: center;
        line-height: 1.2;
    }
    
    .main-header {
        text-align: center;
        background: linear-gradient(135deg, #60a5fa, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-family: 'Poppins', sans-serif;
        font-size: 5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        line-height: 1.1;
    }
    
    .tagline {
        text-align: center;
        font-size: 1.5rem;
        color: #9ca3af;
        margin-bottom: 3rem;
        font-weight: 400;
        line-height: 1.6;
    }
    
    .team-card {
        background: linear-gradient(135deg, rgba(31, 41, 55, 0.5), rgba(55, 65, 81, 0.5));
        backdrop-filter: blur(8px);
        padding: 1.5rem;
        border-radius: 1rem;
        border: 1px solid rgba(75, 85, 99, 0.5);
        margin: 0.5rem 0;
        text-align: center;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .team-card:hover {
        transform: translateY(-10px);
        border-color: rgba(96, 165, 250, 0.5);
    }
    
    .feature-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.5), rgba(51, 65, 85, 0.5));
        backdrop-filter: blur(8px);
        padding: 1.5rem;
        border-radius: 1rem;
        border: 1px solid rgba(71, 85, 105, 0.5);
        margin: 0.5rem 0;
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .problem-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.5), rgba(51, 65, 85, 0.5));
        backdrop-filter: blur(8px);
        padding: 1rem;
        border-radius: 1rem;
        border: 1px solid rgba(71, 85, 105, 0.5);
        margin: 0.5rem 0;
        display: flex;
        align-items: flex-start;
        gap: 1rem;
    }
    
    .metric-card {
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.8), rgba(30, 41, 59, 0.8));
        backdrop-filter: blur(8px);
        padding: 2rem;
        border-radius: 1rem;
        border: 1px solid rgba(51, 65, 85, 0.5);
        text-align: center;
        height: 100%;
    }
    
    .roadmap-phase {
        background: linear-gradient(135deg, rgba(30, 27, 75, 0.6), rgba(49, 46, 129, 0.6));
        backdrop-filter: blur(8px);
        padding: 1.5rem;
        border-radius: 1rem;
        border: 1px solid rgba(76, 29, 149, 0.5);
        margin: 1rem 0;
    }
    
    /* Scroll indicators */
    .scroll-indicator {
        position: fixed;
        right: 2rem;
        bottom: 2rem;
        z-index: 1000;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.5rem;
        color: #6b7280;
        font-size: 0.75rem;
    }
    
    .back-to-top {
        position: fixed;
        right: 2rem;
        bottom: 6rem;
        z-index: 1000;
        width: 3rem;
        height: 3rem;
        border-radius: 50%;
        background: rgba(31, 41, 55, 0.8);
        backdrop-filter: blur(12px);
        border: 1px solid #374151;
        color: #9ca3af;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .back-to-top:hover {
        color: white;
        border-color: #60a5fa;
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# Fixed top navigation bar (matching original React structure)
st.markdown("""
<nav class="top-nav">
    <div class="nav-container">
        <div class="nav-logo">
            <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #60a5fa, #a78bfa); border-radius: 8px; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 1.2rem;">
                B
            </div>
            <span class="nav-brand">BrainBridge</span>
        </div>
        <div class="nav-links">
            <a class="nav-link" href="#home">Greetings</a>
            <a class="nav-link" href="#problem">The Problem</a>
            <a class="nav-link" href="#features">The Solution</a>
            <a class="nav-link" href="#market">Market Landscape</a>
            <a class="nav-link" href="#revenue">Revenue Streams</a>
            <a class="nav-link" href="#roadmap">Roadmap</a>
        </div>
    </div>
</nav>
""", unsafe_allow_html=True)

# Main content with proper spacing for fixed nav
st.markdown('<div style="padding-top: 80px;"></div>', unsafe_allow_html=True)

# Hero Section - Full screen like original
st.markdown("""
<section id="home" class="section" style="display: flex; flex-direction: column; align-items: center; justify-content: center; position: relative; overflow: hidden;">
    <div style="position: absolute; inset: 0; background: radial-gradient(circle at center, rgba(59, 130, 246, 0.1), transparent);"></div>
    <div style="position: relative; z-index: 10; text-align: center; margin-bottom: 4rem;">
        <h1 class="main-header">BrainBridge</h1>
        <p class="tagline">Where Unique Minds Meet Inclusive Opportunities, Employers Find Their Unicorns</p>
    </div>
</section>
""", unsafe_allow_html=True)

# Team Section
st.markdown('<h2 class="section-header">Our Team</h2>', unsafe_allow_html=True)

team_members = [
    {"name": "Sridar", "role": "Full Stack Developer, QA, Product Manager", "description": "Leading the technical vision and product strategy"},
    {"name": "Monika", "role": "Full Stack AI Engineer", "description": "Developing AI-driven matching algorithms"},
    {"name": "Zaidi", "role": "Back-end AI Engineer", "description": "Building scalable backend services"},
    {"name": "Noor", "role": "Front-end AI Engineer", "description": "Creating intuitive user interfaces"},
    {"name": "Bilal", "role": "Front-end Developer", "description": "Implementing responsive designs"}
]

cols = st.columns(5)
for i, member in enumerate(team_members):
    with cols[i]:
        st.markdown(f"""
        <div class="team-card">
            <div style="width: 80px; height: 80px; margin: 0 auto 1rem auto; background: linear-gradient(135deg, #60a5fa, #a78bfa); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 2rem; font-weight: bold; color: white;">
                {member['name'][0]}
            </div>
            <h3 style="color: white; margin-bottom: 0.5rem;">{member['name']}</h3>
            <p style="color: #60a5fa; font-size: 0.9rem; margin-bottom: 0.5rem;">{member['role']}</p>
            <p style="color: #9ca3af; font-size: 0.8rem;">{member['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Problem Section
st.markdown("""
<section id="problem" class="section">
    <h1 class="section-header">Untapped Neurodivergent Potential</h1>
    <p style="text-align: center; font-size: 1.25rem; color: #9ca3af; margin-bottom: 3rem; max-width: 800px; margin-left: auto; margin-right: auto;">
        While rare skill demands are rising, more than 0.75 Billion high skill neuro divergents are job less
    </p>
</section>
""", unsafe_allow_html=True)

problems = [
    "The Paradox: Solutions only reach a few. The vast majority of neurodivergent talent is left behind.",
    "The Skills Gap: Demand for focused jobs is rising, yet 75% of neurodivergent people are unemployed globally.",
    "The Waste: Late diagnosis leads to wasted time, stress, and misaligned careers.",
    "The Barrier: Companies want DEI, but high costs and poor guidance from consultants make it hard to achieve."
]

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### Key Challenges")
    for i, problem in enumerate(problems):
        st.markdown(f"""
        <div class="problem-card">
            <div style="width: 2rem; height: 2rem; background: linear-gradient(135deg, #60a5fa, #a78bfa); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; flex-shrink: 0; margin-top: 0.1rem;">
                {i + 1}
            </div>
            <p style="color: #e5e7eb; margin: 0;">{problem}</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("### Core Problem")
    st.markdown("""
    <div class="feature-card">
        <div style="text-align: center; margin-bottom: 1.5rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">💡</div>
            <h3 style="color: white; margin-bottom: 1rem;">The Real Challenge</h3>
        </div>
        <div style="text-align: left;">
            <p style="color: #e5e7eb; margin-bottom: 1rem;">
                <strong style="color: #60a5fa;">1. Complications on ND Strengths-JD Matching:</strong>
                It's not enough to just know the theory behind matching neurodivergent strengths to job roles.
            </p>
            <p style="color: #e5e7eb; margin: 0;">
                <strong style="color: #60a5fa;">2. A Deeper Gap, not diving deep:</strong>
                The real challenge lies in accurately evaluating an individual's unique neurodivergent profile and precisely interpreting a job description to ensure a confident and accurate match.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Features Section
st.markdown("""
<section id="features" class="section">
    <h1 class="section-header">Comprehensive Features</h1>
    <p style="text-align: center; font-size: 1.25rem; color: #9ca3af; margin-bottom: 3rem; max-width: 800px; margin-left: auto; margin-right: auto;">
        BrainBridge empowers neurodiverse talent and inclusive employers through intelligent tools.
    </p>
</section>
""", unsafe_allow_html=True)

features = [
    {
        "title": "Self-Discovery Engine",
        "icon": "🧠",
        "description": "Interactive tool that helps neurodiverse talent uncover cognitive strengths and work preferences.",
        "benefits": [
            "Gamified quizzes and cognitive pattern tests",
            "Generates a personalized Neuro Work Profile", 
            "Guides learners towards tailored training and jobs"
        ]
    },
    {
        "title": "JD Normalizer",
        "icon": "📄",
        "description": "AI-powered engine that rewrites job descriptions to be more neuro-inclusive and accessible.",
        "benefits": [
            "Detects exclusionary or biased wording in job posts",
            "Suggests inclusive alternatives automatically",
            "Improves accessibility for neurodiverse applicants"
        ]
    },
    {
        "title": "Job Matching Engine", 
        "icon": "⚡",
        "description": "AI-driven matching system that aligns cognitive strengths of ND talent with role requirements.",
        "benefits": [
            "Analyzes role tasks and cognitive fit profiles",
            "Recommends best-matched ND candidates",
            "Continuously learns from hiring outcomes"
        ]
    }
]

cols = st.columns(3)
for i, feature in enumerate(features):
    with cols[i]:
        st.markdown(f"""
        <div class="feature-card">
            <div style="text-align: center; margin-bottom: 1rem;">
                <div style="font-size: 3rem; margin-bottom: 1rem;">{feature['icon']}</div>
                <h3 style="color: white; margin-bottom: 0.5rem;">{feature['title']}</h3>
                <p style="color: #9ca3af; margin-bottom: 1.5rem;">{feature['description']}</p>
            </div>
            <div>
                <h4 style="color: #6b7280; font-size: 0.9rem; margin-bottom: 1rem; text-transform: uppercase; letter-spacing: 0.05em;">Benefits</h4>
                <ul style="list-style: none; padding: 0; margin: 0;">
        """, unsafe_allow_html=True)
        
        for benefit in feature['benefits']:
            st.markdown(f"""
                    <li style="display: flex; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.75rem;">
                        <span style="color: #10b981; font-size: 0.8rem; margin-top: 0.1rem;">✓</span>
                        <span style="color: #e5e7eb; font-size: 0.9rem;">{benefit}</span>
                    </li>
            """, unsafe_allow_html=True)
        
        st.markdown("</ul></div></div>", unsafe_allow_html=True)

# Market Section
st.markdown("""
<section id="market" class="section">
    <h1 class="section-header">Competitive Landscape</h1>
    <p style="text-align: center; font-size: 1.25rem; color: #9ca3af; margin-bottom: 3rem; max-width: 900px; margin-left: auto; margin-right: auto;">
        While there are platforms addressing employment for neurodiverse individuals or corporate DEI training, 
        none integrate talent discovery, adaptive learning, employer certification, and AI-driven job matching 
        in one ecosystem like BrainBridge does with AI
    </p>
</section>
""", unsafe_allow_html=True)

# Market sizing
market_data = [
    {
        "title": "Total Addressable Market (TAM)",
        "value": "$50B+",
        "description": "Global EdTech + HRTech intersection targeting neurodiversity inclusion"
    },
    {
        "title": "Serviceable Available Market (SAM)", 
        "value": "$5B",
        "description": "ND-focused job placement, LMS, employer DEI services in North America + Europe"
    },
    {
        "title": "Serviceable Obtainable Market (SOM)",
        "value": "$10-20M",
        "description": "Year 1-2 potential revenue with 10k ND adults + 500 employers"
    }
]

cols = st.columns(3)
for i, market in enumerate(market_data):
    with cols[i]:
        st.markdown(f"""
        <div class="metric-card">
            <h3 style="color: #60a5fa; margin-bottom: 0.5rem;">{market['title']}</h3>
            <div style="font-size: 2.5rem; font-weight: bold; color: white; margin-bottom: 1rem; font-family: 'Poppins', sans-serif;">{market['value']}</div>
            <p style="color: #9ca3af; font-size: 0.9rem;">{market['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Revenue Section
st.markdown("""
<section id="revenue" class="section">
    <h1 class="section-header">Revenue Streams</h1>
    <p style="text-align: center; font-size: 1.25rem; color: #9ca3af; margin-bottom: 3rem; max-width: 800px; margin-left: auto; margin-right: auto;">
        Multiple monetization channels to ensure sustainable growth and impact
    </p>
</section>
""", unsafe_allow_html=True)

revenue_streams = [
    {
        "title": "Talent Portal Monetization",
        "items": ["Premium microlearning access", "AI Task Coach", "Mentorship Match", "Corporate sponsorship", "Government/NGO grants"]
    },
    {
        "title": "AI Mentor Support", 
        "items": ["Premium AI mentor features", "Personalized career coaching", "Interview preparation modules", "Skill development tracking"]
    },
    {
        "title": "Corporate Certification Program",
        "items": ["DEI certification for employers", "Neurodiversity inclusion training", "Workplace accommodation guidance", "Ongoing support and resources"]
    },
    {
        "title": "Job Funnel + ATS Plugin",
        "items": ["Tailored job board", "Resume ranking for neurodiverse applicants", "Pattern-matching algorithm", "Integration with existing ATS systems"]
    }
]

cols = st.columns(2)
for i, stream in enumerate(revenue_streams):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="feature-card">
            <h3 style="color: white; margin-bottom: 1rem;">{stream['title']}</h3>
            <ul style="list-style: none; padding: 0; margin: 0;">
        """, unsafe_allow_html=True)
        
        for item in stream['items']:
            st.markdown(f"""
                <li style="display: flex; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.5rem;">
                    <span style="color: #60a5fa; margin-top: 0.1rem;">•</span>
                    <span style="color: #e5e7eb; font-size: 0.9rem;">{item}</span>
                </li>
            """, unsafe_allow_html=True)
        
        st.markdown("</ul></div>", unsafe_allow_html=True)

# Roadmap Section
st.markdown("""
<section id="roadmap" class="section">
    <h1 class="section-header">Our Roadmap</h1>
    <p style="text-align: center; font-size: 1.25rem; color: #9ca3af; margin-bottom: 3rem; max-width: 800px; margin-left: auto; margin-right: auto;">
        Strategic development phases to ensure impactful and sustainable growth
    </p>
</section>
""", unsafe_allow_html=True)

roadmap_phases = [
    {
        "phase": "Phase 1",
        "title": "Foundation & MVP",
        "items": ["Agentize Mentor Role", "Basic employer evaluation framework", "Core LMS functionality", "Initial self-assessment modules", "Basic matching algorithm"]
    },
    {
        "phase": "Phase 2", 
        "title": "Enhancement",
        "items": ["Employer Certification Program", "ND-LMS skill modules", "Dynamic self-assessments", "Algorithm refinement with real-world data", "Content library expansion"]
    },
    {
        "phase": "Phase 3",
        "title": "Expansion", 
        "items": ["Full certification platform", "Comprehensive employer portal", "Advanced analytics", "Multi-language support", "Global partnership program"]
    },
    {
        "phase": "Phase 4",
        "title": "Maturity",
        "items": ["Industry-specific solutions", "Government integration", "Research partnerships", "Global scale operations", "Continuous improvement cycle"]
    }
]

for i, phase in enumerate(roadmap_phases):
    st.markdown(f"""
    <div class="roadmap-phase">
        <div style="display: flex; align-items: center; margin-bottom: 1.5rem;">
            <div style="width: 3rem; height: 3rem; background: linear-gradient(135deg, #60a5fa, #a78bfa); border-radius: 50%; display: flex; align-items: center; justify-content: center; color: white; font-weight: bold; font-size: 1.2rem; margin-right: 1rem; flex-shrink: 0;">
                {i + 1}
            </div>
            <div>
                <div style="color: #60a5fa; font-weight: bold; font-size: 0.9rem;">{phase['phase']}</div>
                <h3 style="color: white; margin: 0; font-size: 1.5rem;">{phase['title']}</h3>
            </div>
        </div>
        <ul style="list-style: none; padding: 0; margin: 0;">
    """, unsafe_allow_html=True)
    
    for item in phase['items']:
        st.markdown(f"""
            <li style="display: flex; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.5rem;">
                <span style="color: #60a5fa; margin-top: 0.1rem;">•</span>
                <span style="color: #e5e7eb; font-size: 0.9rem;">{item}</span>
            </li>
        """, unsafe_allow_html=True)
    
    st.markdown("</ul></div>", unsafe_allow_html=True)

# Scroll indicators and back to top with keyboard navigation
st.markdown("""
<div class="scroll-indicator">
    <div style="animation: bounce 2s infinite;">↓</div>
    <span>Scroll</span>
</div>

<button class="back-to-top" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">
    ↑
</button>

<script>
// Keyboard navigation for sections
document.addEventListener('DOMContentLoaded', function() {
    const sections = ['home', 'problem', 'features', 'market', 'revenue', 'roadmap'];
    let currentSection = 0;
    
    function scrollToSection(index) {
        if (index >= 0 && index < sections.length) {
            const element = document.getElementById(sections[index]);
            if (element) {
                element.scrollIntoView({ behavior: 'smooth' });
                currentSection = index;
            }
        }
    }
    
    function getCurrentSection() {
        const scrollPosition = window.scrollY + window.innerHeight / 2;
        
        for (let i = 0; i < sections.length; i++) {
            const element = document.getElementById(sections[i]);
            if (element) {
                const rect = element.getBoundingClientRect();
                const elementTop = rect.top + window.scrollY;
                const elementBottom = elementTop + rect.height;
                
                if (scrollPosition >= elementTop && scrollPosition <= elementBottom) {
                    currentSection = i;
                    break;
                }
            }
        }
    }
    
    document.addEventListener('keydown', function(event) {
        // Only handle arrow keys when not in an input field
        if (event.target.tagName !== 'INPUT' && event.target.tagName !== 'TEXTAREA') {
            if (event.key === 'ArrowDown' || event.key === 'ArrowRight') {
                event.preventDefault();
                getCurrentSection();
                scrollToSection(currentSection + 1);
            } else if (event.key === 'ArrowUp' || event.key === 'ArrowLeft') {
                event.preventDefault();
                getCurrentSection();
                scrollToSection(currentSection - 1);
            }
        }
    });
    
    // Update current section on scroll
    window.addEventListener('scroll', getCurrentSection);
});
</script>

<style>
@keyframes bounce {
    0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
    40% { transform: translateY(-10px); }
    60% { transform: translateY(-5px); }
}
</style>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; padding: 2rem 0; border-top: 1px solid #374151; margin-top: 4rem;">
    <p style="color: #6b7280; font-size: 0.9rem;">BrainBridge - Empowering Neurodiverse Talent and Inclusive Workplaces</p>
</div>
""", unsafe_allow_html=True)
