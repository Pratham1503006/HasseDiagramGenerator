import streamlit as st
from PIL import Image
import base64

def main():
    # Enhanced CSS for beautiful animations and styling
    st.markdown("""
    <style>
        /* Modern Animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
            100% { transform: translateY(0px); }
        }
        
        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* Base Styles */
        .stApp {
            background: linear-gradient(135deg, #1a1a1a, #2D2D2D);
        }
        
        /* Hero Section */
        .hero-container {
            background: linear-gradient(45deg, #2D2D2D, #1E1E1E);
            border-radius: 20px;
            padding: 2rem;
            margin: 2rem 0;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            border: 1px solid rgba(74, 144, 226, 0.2);
        }
        
        .hero-title {
            background: linear-gradient(90deg, #4a90e2, #357abd, #4a90e2);
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientBG 3s ease infinite;
            font-size: 3.5rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
        }
        
        .hero-subtitle {
            color: #e0e0e0;
            font-size: 1.5rem;
            line-height: 1.6;
            margin-bottom: 2rem;
        }
        
        /* Feature Cards */
        .feature-card {
            background: rgba(45, 45, 45, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 25px;
            margin: 15px 0;
            border: 1px solid rgba(74, 144, 226, 0.2);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 40px rgba(74, 144, 226, 0.2);
            border-color: rgba(74, 144, 226, 0.4);
        }
        
        .feature-icon {
            font-size: 3em;
            margin-bottom: 20px;
            background: linear-gradient(45deg, #4a90e2, #357abd);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        .feature-title {
            color: #ffffff;
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 15px;
        }
        
        .feature-description {
            color: #b0b0b0;
            font-size: 1.1rem;
            line-height: 1.6;
        }

        /* Images */
        .card-image {
            width: 100%;
            border-radius: 10px;
            margin: 15px 0;
            transition: transform 0.3s ease;
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }
        
        .card-image:hover {
            transform: scale(1.03);
        }
        
        /* Quick Start Section */
        .quick-start {
            background: linear-gradient(135deg, #2D2D2D, #1E1E1E);
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
            border: 1px solid rgba(74, 144, 226, 0.2);
        }
        
        .quick-start-title {
            color: #4a90e2;
            font-size: 2rem;
            margin-bottom: 1.5rem;
        }
        
        .quick-start-step {
            background: rgba(74, 144, 226, 0.1);
            border-left: 4px solid #4a90e2;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 0 10px 10px 0;
        }
        
        /* Footer */
        .footer {
            background: linear-gradient(90deg, #1E1E1E, #2D2D2D);
            padding: 2rem;
            margin-top: 3rem;
            border-radius: 15px;
            text-align: center;
            border-top: 1px solid rgba(74, 144, 226, 0.2);
        }
        
        .footer-text {
            color: #b0b0b0;
            font-size: 1rem;
        }
        
        .footer-heart {
            color: #ff4d4d;
            animation: float 2s ease-in-out infinite;
            display: inline-block;
        }
    </style>
    """, unsafe_allow_html=True)

    # Hero Section
    st.markdown("""
    <div class="hero-container animate-fade-in">
        <h1 class="hero-title">Welcome to Hasse Diagram Explorer! 🎯</h1>
        <p class="hero-subtitle">Discover the beauty of mathematical structures through interactive visualizations and comprehensive analysis tools.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Features Section
    st.markdown("<h2 style='color: #4a90e2; margin: 2rem 0;'>✨ Key Features</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">🎨</div>
            <h3 class="feature-title">Interactive Visualization</h3>
            <p class="feature-description">Create stunning Hasse diagrams with our intuitive interface. Explore relationships and structures with ease.</p>
            <img class="card-image" src="https://images.unsplash.com/photo-1509228468518-180dd4864904" alt="Interactive Visualization">
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3 class="feature-title">Advanced Analysis</h3>
            <p class="feature-description">Generate comprehensive analysis of posets including supremum/infimum tables and special elements.</p>
            <img class="card-image" src="https://images.unsplash.com/photo-1551288049-bebda4e38f71" alt="Data Analysis">
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-icon">📚</div>
            <h3 class="feature-title">Learning Hub</h3>
            <p class="feature-description">Master poset theory through interactive examples and clear, concise explanations.</p>
            <img class="card-image" src="https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8" alt="Education">
        </div>
        """, unsafe_allow_html=True)

    # Quick Start Guide
    st.markdown("""
    <div class="quick-start">
        <h2 class="quick-start-title">🚀 Quick Start Guide</h2>
        <div class="quick-start-step">
            <strong>1.</strong> Navigate to the "Hasse Diagram Generator" page
        </div>
        <div class="quick-start-step">
            <strong>2.</strong> Enter your poset relations (e.g., "a b" means a ≤ b)
        </div>
        <div class="quick-start-step">
            <strong>3.</strong> Click "Generate" to visualize your diagram
        </div>
        <div style="margin-top: 20px;">
            <strong>Example Input:</strong>
            <pre style="background: #1E1E1E; padding: 15px; border-radius: 10px; margin-top: 10px;">
                1 1
                1 2
                1 3
                2 2
                2 3
                3 3
            </pre>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Learn More Section
    st.markdown("<h2 style='color: #4a90e2; margin: 2rem 0;'>📖 Learn More</h2>", unsafe_allow_html=True)
    
    learn_cols = st.columns(2)
    with learn_cols[0]:
        st.markdown("""
        <div class="feature-card">
            <h3 class="feature-title">Theory Section</h3>
            <p class="feature-description">Dive deep into poset theory and Hasse diagrams with our comprehensive guide.</p>
            <img class="card-image" src="https://images.unsplash.com/photo-1453733190371-0a9bedd82893" alt="Theory">
            <a href="/Theory" style="color: #4a90e2; text-decoration: none; font-weight: bold;">Learn More →</a>
        </div>
        """, unsafe_allow_html=True)
    
    with learn_cols[1]:
        st.markdown("""
        <div class="feature-card">
            <h3 class="feature-title">Examples Gallery</h3>
            <p class="feature-description">Explore our collection of example posets and their visualizations.</p>
            <img class="card-image" src="https://images.unsplash.com/photo-1509228627152-72ae9ae6848d" alt="Examples">
            <a href="/Hasse_Diagram_Generator" style="color: #4a90e2; text-decoration: none; font-weight: bold;">View Gallery →</a>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        <p class="footer-text">Hasse Diagram Explorer v1.0 | © 2024 All rights reserved</p>
        <p class="footer-text">Made with <span class="footer-heart">❤️</span> for mathematics enthusiasts</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 
