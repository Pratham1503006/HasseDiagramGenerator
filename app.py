import streamlit as st
import networkx as nx
import matplotlib
matplotlib.use('Agg')  # Set the backend to non-interactive Agg
import matplotlib.pyplot as plt
from Hasse import HasseDiagram
import pandas as pd
import time
import numpy as np

# Import page modules
home_module = __import__('pages.1_Home', fromlist=['main'])
theory_module = __import__('pages.2_Theory', fromlist=['main'])
contact_module = __import__('pages.3_Contact', fromlist=['main'])
generator_module = __import__('pages.4_Hasse_Diagram_Generator', fromlist=['main'])

st.set_page_config(
    page_title="Hasse Diagram Explorer",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enhanced dark theme styling with more sophisticated animations
st.markdown("""
<style>
    /* Main background with gradient */
    .stApp {
        background: linear-gradient(135deg, #1E1E1E, #2D2D2D);
        color: #FFFFFF;
    }
    
    /* Main content area with glass morphism */
    .main .block-container {
        padding: 2rem;
        background: rgba(30, 30, 30, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }
    
    /* Sidebar with gradient */
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2D2D2D, #1E1E1E);
        color: #FFFFFF;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Text elements with gradient */
    h1 {
        background: linear-gradient(90deg, #4a90e2, #357abd);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        letter-spacing: -0.5px;
    }
    
    h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
        font-weight: 600;
        letter-spacing: -0.3px;
    }
    
    p, div, span {
        color: rgba(255, 255, 255, 0.9) !important;
        line-height: 1.6;
    }
    
    /* Enhanced input fields */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: rgba(45, 45, 45, 0.8);
        color: #FFFFFF;
        border: 1px solid rgba(74, 144, 226, 0.3);
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: #4a90e2;
        box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2);
    }
    
    /* Gradient buttons */
    .stButton > button {
        background: linear-gradient(90deg, #4a90e2, #357abd);
        color: white;
        border: none;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(74, 144, 226, 0.4);
        background: linear-gradient(90deg, #357abd, #4a90e2);
    }
    
    /* Glass morphism cards */
    .feature-card {
        background: rgba(45, 45, 45, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 25px;
        margin: 15px 0;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .feature-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
        border-color: rgba(74, 144, 226, 0.3);
    }

    /* Enhanced animations */
    @keyframes fadeIn {
        from { 
            opacity: 0; 
            transform: translateY(30px);
            filter: blur(10px);
        }
        to { 
            opacity: 1; 
            transform: translateY(0);
            filter: blur(0);
        }
    }

    @keyframes slideIn {
        from { 
            transform: translateX(-100%);
            opacity: 0;
        }
        to { 
            transform: translateX(0);
            opacity: 1;
        }
    }

    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-10px) rotate(1deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }

    .animate-fade-in {
        animation: fadeIn 1.2s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .animate-slide-in {
        animation: slideIn 1s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* Floating footer with glass morphism */
    .footer {
        position: fixed;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(45, 45, 45, 0.8);
        backdrop-filter: blur(10px);
        padding: 15px 30px;
        border-radius: 50px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        animation: float 3s ease-in-out infinite;
        z-index: 1000;
    }

    /* Plot styling */
    .stPlot {
        background: rgba(45, 45, 45, 0.7);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.3s ease;
    }

    .stPlot:hover {
        transform: scale(1.02);
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.2);
    }
</style>
""", unsafe_allow_html=True)

def create_example_hasse():
    """Create an example Hasse diagram for demonstration"""
    plt.figure(figsize=(6, 4), facecolor='#1E1E1E')
    G = nx.DiGraph()
    nodes = [1, 2, 3, 4]
    edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    
    pos = {1: (0.5, 0), 2: (0.25, 0.5), 3: (0.75, 0.5), 4: (0.5, 1)}
    
    nx.draw_networkx_nodes(G, pos, node_color='#4a90e2', node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color='#ffffff', arrows=False)
    nx.draw_networkx_labels(G, pos, font_color='white')
    
    plt.title("Example Hasse Diagram", color='white', pad=20)
    plt.axis('off')
    return plt.gcf()

def create_poset_visualization():
    """Create a visual representation of a poset relation"""
    plt.figure(figsize=(6, 4), facecolor='#1E1E1E')
    elements = ['a', 'b', 'c']
    x = np.arange(len(elements))
    
    plt.scatter(x, [0.5]*len(elements), c='#4a90e2', s=300)
    plt.plot([0, 1], [0.5, 0.5], 'w--', alpha=0.5)
    plt.plot([1, 2], [0.5, 0.5], 'w--', alpha=0.5)
    
    for i, elem in enumerate(elements):
        plt.annotate(elem, (x[i], 0.5), color='white', 
                    xytext=(0, 10), textcoords='offset points',
                    ha='center', va='bottom', fontsize=12)
    
    plt.title("Poset Relation Example", color='white', pad=20)
    plt.axis('off')
    return plt.gcf()

def main():
    # Animated title
    st.markdown('<div class="animate-fade-in">', unsafe_allow_html=True)
    st.title("Welcome to Hasse Diagram Explorer! 🎯")
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Hero section with example diagram
    with st.container():
        st.markdown('<div class="animate-slide-in">', unsafe_allow_html=True)
        col1, col2 = st.columns([3, 2])
        
        with col1:
            st.markdown("""
            ## Visualize and Explore Partially Ordered Sets
            This interactive application helps you understand and work with Hasse diagrams 
            and partially ordered sets (posets). Generate beautiful visualizations, analyze 
            properties, and learn about poset theory.
            """)
        
        with col2:
            st.pyplot(create_example_hasse())
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Features section with cards
    st.markdown("### ✨ Key Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>🎨 Interactive Visualization</h4>
            <p>Generate and explore Hasse diagrams with a modern, dark-themed interface</p>
            <div class="feature-image-container">
                <div class="feature-image"></div>  <!-- Add your image here -->
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>📊 Comprehensive Analysis</h4>
            <p>View supremum and infimum tables, identify minimal and maximal elements</p>
        </div>
        """, unsafe_allow_html=True)
        st.pyplot(create_poset_visualization())
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>📚 Educational Content</h4>
            <p>Learn about poset theory and properties through interactive examples</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quick start section with visual guide
    st.markdown('<div class="animate-fade-in">', unsafe_allow_html=True)
    st.markdown("### 🚀 Quick Start")
    
    quick_start_cols = st.columns([1, 1])
    with quick_start_cols[0]:
        st.markdown("""
        1. Navigate to the "Hasse Diagram Generator" page
        2. Enter your poset relations in the format 'a b' (meaning a ≤ b)
        3. Optionally specify the elements of your poset
        4. Click "Generate Hasse Diagram" to visualize your poset
        """)
    
    with quick_start_cols[1]:
        # Create a simple example diagram
        example_fig = plt.figure(figsize=(6, 4), facecolor='#1E1E1E')
        plt.text(0.5, 0.5, "1 2\n2 3\n1 3", 
                color='white', fontfamily='monospace',
                ha='center', va='center', fontsize=12)
        plt.axis('off')
        st.pyplot(example_fig)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Add the CSS for image styling
    st.markdown("""
    <style>
        /* Existing styles... */
        
        /* Image styling */
        .feature-image-container {
            margin-top: 15px;
            border-radius: 8px;
            overflow: hidden;
            transition: transform 0.3s ease;
        }
        
        .feature-image-container:hover {
            transform: scale(1.05);
        }
        
        .feature-image-container img {
            width: 100%;
            height: auto;
            object-fit: cover;
        }
        
        /* Figure styling */
        .stPlot {
            background-color: #2D2D2D;
            border-radius: 10px;
            padding: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s ease;
        }
        
        .stPlot:hover {
            transform: translateY(-5px);
        }
    </style>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        Hasse Diagram Explorer v1.0 | © 2025 All rights reserved
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
