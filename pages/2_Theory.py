import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def create_transitivity_example():
    """Create a figure showing transitivity in posets"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4), facecolor='#1E1E1E')
    
    # First diagram - with transitive edges
    G1 = nx.DiGraph()
    nodes = ['a', 'b', 'c']
    edges = [('a', 'b'), ('b', 'c'), ('a', 'c')]
    pos = {'a': (0, 0), 'b': (0, 1), 'c': (0, 2)}
    
    G1.add_nodes_from(nodes)
    G1.add_edges_from(edges)
    
    nx.draw_networkx_nodes(G1, pos, node_color='#4a90e2', node_size=500, ax=ax1)
    nx.draw_networkx_edges(G1, pos, edge_color='#ffffff', arrows=True, ax=ax1)
    nx.draw_networkx_labels(G1, pos, font_color='white', ax=ax1)
    ax1.set_title("With Transitive Edge", color='white', pad=20)
    ax1.axis('off')
    
    # Second diagram - Hasse diagram (without transitive edges)
    G2 = nx.DiGraph()
    G2.add_nodes_from(nodes)
    G2.add_edges_from([('a', 'b'), ('b', 'c')])
    
    nx.draw_networkx_nodes(G2, pos, node_color='#4a90e2', node_size=500, ax=ax2)
    nx.draw_networkx_edges(G2, pos, edge_color='#ffffff', arrows=True, ax=ax2)
    nx.draw_networkx_labels(G2, pos, font_color='white', ax=ax2)
    ax2.set_title("Hasse Diagram", color='white', pad=20)
    ax2.axis('off')
    
    plt.tight_layout()
    return fig

def create_minimal_maximal_example():
    """Create a figure showing minimal and maximal elements"""
    fig, ax = plt.subplots(figsize=(6, 6), facecolor='#1E1E1E')
    
    G = nx.DiGraph()
    nodes = ['a', 'b', 'c', 'd', 'e']
    edges = [('a', 'c'), ('b', 'c'), ('c', 'd'), ('c', 'e')]
    pos = {
        'a': (0, 0), 'b': (1, 0),  # minimal elements
        'c': (0.5, 1),             # middle element
        'd': (0, 2), 'e': (1, 2)   # maximal elements
    }
    
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    
    # Draw minimal elements
    nx.draw_networkx_nodes(G, pos, nodelist=['a', 'b'], 
                          node_color='#ff7f7f', node_size=500)
    # Draw maximal elements
    nx.draw_networkx_nodes(G, pos, nodelist=['d', 'e'], 
                          node_color='#7fbf7f', node_size=500)
    # Draw other elements
    nx.draw_networkx_nodes(G, pos, nodelist=['c'], 
                          node_color='#4a90e2', node_size=500)
    
    nx.draw_networkx_edges(G, pos, edge_color='#ffffff', arrows=False)
    nx.draw_networkx_labels(G, pos, font_color='white')
    
    # Add legend
    plt.plot([], [], 'o', color='#ff7f7f', label='Minimal Elements')
    plt.plot([], [], 'o', color='#7fbf7f', label='Maximal Elements')
    plt.plot([], [], 'o', color='#4a90e2', label='Other Elements')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
              facecolor='#1E1E1E', labelcolor='white')
    
    plt.title("Minimal and Maximal Elements", color='white', pad=20)
    plt.axis('off')
    return fig

def create_bounds_example():
    """Create a figure showing upper and lower bounds"""
    fig, ax = plt.subplots(figsize=(6, 6), facecolor='#1E1E1E')
    
    G = nx.DiGraph()
    nodes = ['1', '2', '3', '4', '6', '12']
    edges = [
        ('1', '2'), ('1', '3'), ('2', '4'), ('2', '6'),
        ('3', '6'), ('4', '12'), ('6', '12')
    ]
    pos = {
        '1': (0.5, 0),
        '2': (0.25, 1), '3': (0.75, 1),
        '4': (0, 2), '6': (0.5, 2),
        '12': (0.25, 3)
    }
    
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    
    nx.draw_networkx_nodes(G, pos, node_color='#4a90e2', node_size=500)
    nx.draw_networkx_edges(G, pos, edge_color='#ffffff', arrows=False)
    nx.draw_networkx_labels(G, pos, font_color='white')
    
    plt.title("Divisibility Poset Example", color='white', pad=20)
    plt.axis('off')
    return fig

def main():
    st.title("Theory of Posets and Hasse Diagrams 📚")
    
    # Enhanced styling with animations and better math formatting
    st.markdown("""
    <style>
        /* Base theme */
        .stApp {
            background-color: #2D2D2D;
        }
        
        /* Content animations */
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .animate-content {
            animation: fadeIn 0.6s ease-out;
        }
        
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 1rem;
            background: linear-gradient(90deg, #1E1E1E, #2D2D2D);
            border-radius: 10px;
            padding: 0.5rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            padding: 1rem 1.5rem;
            transition: all 0.3s ease;
            border-radius: 8px;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background: rgba(74, 144, 226, 0.1);
        }
        
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: #4a90e2;
            color: white;
        }
        
        /* Mathematical notation */
        .math-notation {
            font-family: 'Computer Modern', serif;
            background: rgba(74, 144, 226, 0.1);
            padding: 0.5rem 1rem;
            border-radius: 5px;
            border-left: 3px solid #4a90e2;
            margin: 1rem 0;
        }
        
        /* Content cards */
        .content-card {
            background: #1E1E1E;
            border-radius: 10px;
            padding: 1.5rem;
            margin: 1rem 0;
            border: 1px solid rgba(74, 144, 226, 0.2);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        /* Figures */
        .stPlot {
            background-color: #1E1E1E;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin: 20px 0;
            border: 1px solid rgba(74, 144, 226, 0.2);
        }
        
        /* Headers */
        h1, h2, h3 {
            background: linear-gradient(90deg, #4a90e2, #357abd);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
            margin-bottom: 1.5rem;
        }
    </style>
    """, unsafe_allow_html=True)

    # Create tabs with enhanced styling
    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "Posets", "Hasse Diagrams", "Minimal & Maximal Elements",
        "Upper & Lower Bounds", "Supremum & Infimum", "Examples", "Properties"
    ])

    with tab1:
        st.markdown('<div class="animate-content">', unsafe_allow_html=True)
        st.header("Partially Ordered Sets (Posets)")
        
        st.markdown(""" <div class="content-card">
            A <strong>partially ordered set</strong> (poset) is a set equipped with a binary relation that satisfies three properties:
            <div class="math-notation">
            1. <strong>Reflexivity</strong>: Every element is related to itself<br>
            • For all a ∈ P, a ≤ a
            </div>
             <div class="math-notation">
            2. <strong>Antisymmetry</strong>: If two elements are related in both directions, they must be equal<br>
            • If a ≤ b and b ≤ a, then a = b
            </div> 
            <div class="math-notation">
            3. <strong>Transitivity</strong>: If a is related to b and b is related to c, then a is related to c<br>
            • If a ≤ b and b ≤ c, then a ≤ c
            </div>
        </div>
        """, unsafe_allow_html=True)
        

        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="animate-content">', unsafe_allow_html=True)
        st.header("Hasse Diagrams")
        st.markdown("""
        A **Hasse diagram** is a graphical representation of a poset that:
        
        - Represents elements as vertices
        - Draws edges between comparable elements
        - Places larger elements above smaller ones
        - Omits edges that can be inferred by transitivity
        """)
        
        # Add bounds example which serves as a good Hasse diagram example
        st.pyplot(create_bounds_example())
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="animate-content">', unsafe_allow_html=True)
        st.header("Minimal and Maximal Elements")
        st.markdown("""
        - A **minimal element** is an element that has no element below it
        - A **maximal element** is an element that has no element above it
        
        A poset can have multiple minimal and maximal elements.
        """)
        
        # Add minimal/maximal visualization
        st.pyplot(create_minimal_maximal_example())
        st.markdown('</div>', unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="animate-content">', unsafe_allow_html=True)
        st.header("Upper and Lower Bounds")
        st.markdown("""
        For a subset S of a poset P:
        
        - An **upper bound** of S is an element u ∈ P such that s ≤ u for all s ∈ S
        - A **lower bound** of S is an element l ∈ P such that l ≤ s for all s ∈ S
        
        The set of all upper bounds is denoted U(S)
        The set of all lower bounds is denoted L(S)
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab5:
        st.markdown('<div class="animate-content">', unsafe_allow_html=True)
        st.header("Supremum and Infimum")
        st.markdown("""
        For a subset S of a poset P:
        
        - The **supremum** (least upper bound) of S is the smallest element in U(S)
        - Denoted as sup(S) or ∨S
        
        - The **infimum** (greatest lower bound) of S is the largest element in L(S)
        - Denoted as inf(S) or ∧S
        
        Not all subsets have suprema or infima. When they exist, they are unique.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab6:
        st.markdown('<div class="animate-content">', unsafe_allow_html=True)
        st.header("Examples")
        st.markdown("""
        Common examples of posets:
        
        1. **Divisibility Poset**:
        - Elements: Natural numbers
        - Relation: a ≤ b if a divides b
        
        2. **Subset Poset**:
        - Elements: Subsets of a set
        - Relation: A ≤ B if A is a subset of B
        
        3. **Integer Poset**:
        - Elements: Integers
        - Relation: a ≤ b if a is less than or equal to b
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab7:
        st.markdown('<div class="animate-content">', unsafe_allow_html=True)
        st.header("Properties of Posets")
        st.markdown("""
        Important properties of posets:
        
        - **Lattice**: A poset where every pair of elements has both a supremum and infimum
        - **Complete Lattice**: A poset where every subset has both a supremum and infimum
        - **Chain**: A totally ordered subset of a poset
        - **Antichain**: A subset where no two elements are comparable
        
        These properties help classify and understand different types of posets.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    # Footer with gradient
    st.markdown("""
        <div style="text-align: center; padding: 20px; margin-top: 50px; background: linear-gradient(90deg, #1E1E1E, #2D2D2D); border-radius: 10px; border: 1px solid rgba(74, 144, 226, 0.2);">
            <p style="color: #4a90e2;">Hasse Diagram Explorer v1.0 | © 2024 All rights reserved</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
