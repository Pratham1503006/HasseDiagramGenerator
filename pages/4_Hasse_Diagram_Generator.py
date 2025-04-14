import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import numpy as np
from Hasse import HasseDiagram
import pandas as pd

def set_page_style():
    st.markdown("""
    <style>
        /* Main container styling */
        .main .block-container {
            padding: 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Title and headers */
        h1 {
            color: #4a90e2;
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
            text-align: center;
            padding: 20px;
            background: linear-gradient(90deg, #1E1E1E, #2D2D2D);
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        h2, h3 {
            color: #4a90e2;
            margin-top: 1.5rem;
        }
        
        /* Input containers */
        .stTextArea, .stTextInput {
            background: #2D2D2D;
            border-radius: 10px;
            padding: 10px;
            margin: 10px 0;
        }
        
        /* Button styling */
        .stButton > button {
            width: 100%;
            background: linear-gradient(90deg, #4a90e2, #357abd);
            color: white;
            border: none;
            padding: 15px 30px;
            border-radius: 8px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(74, 144, 226, 0.3);
        }
        
        /* DataFrame styling */
        .dataframe {
            background: #2D2D2D;
            border-radius: 10px;
            padding: 10px;
            margin: 10px 0;
        }
        
        /* Info boxes */
        .info-box {
            background: #2D2D2D;
            border-radius: 10px;
            padding: 20px;
            margin: 10px 0;
            border-left: 4px solid #4a90e2;
        }
        
        /* Dividers */
        hr {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, #4a90e2, transparent);
            margin: 2rem 0;
        }
    </style>
    """, unsafe_allow_html=True)

def create_hasse_diagram(relations, elements=None):
    try:
        hasse = HasseDiagram(relations, elements)
        return hasse, None
    except ValueError as e:
        return None, str(e)

def draw_hasse_diagram(hasse):
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(12, 10), dpi=100, facecolor='#1E1E1E')
    ax = fig.add_subplot(111)
    ax.set_facecolor('#1E1E1E')
    
    levels = hasse.get_levels()
    pos = {}
    max_level = max(levels.keys())
    max_nodes_in_level = max(len(nodes) for nodes in levels.values())
    
    # Calculate positions with improved spacing
    for level, nodes in levels.items():
        y = level / max_level if max_level > 0 else 1
        num_nodes = len(nodes)
        if num_nodes == 1:
            x_positions = [0.5]
        else:
            spacing = 1.0 / (max_nodes_in_level + 1)
            start_x = (1.0 - (num_nodes - 1) * spacing) / 2
            x_positions = [start_x + i * spacing for i in range(num_nodes)]
        
        sorted_nodes = sorted(nodes)
        for node, x in zip(sorted_nodes, x_positions):
            pos[node] = (x, y)

    # Draw edges with gradient effect
    edge_collection = nx.draw_networkx_edges(
        hasse.G, pos,
        edge_color='#4a90e2',
        width=2,
        alpha=0.7,
        arrows=False,
        style='solid'
    )

    # Draw nodes with glow effect
    node_collection = nx.draw_networkx_nodes(
        hasse.G, pos,
        node_size=2000,
        node_color='#2D2D2D',
        edgecolors='#4a90e2',
        linewidths=2,
        alpha=1.0
    )
    
    # Add glow effect to nodes
    node_collection.set_path_effects([
        PathEffects.withStroke(linewidth=5, foreground='#4a90e2', alpha=0.3)
    ])

    # Draw labels with enhanced style
    labels = nx.draw_networkx_labels(
        hasse.G, pos,
        font_size=12,
        font_weight='bold',
        font_color='white'
    )
    
    # Add glow to labels
    for label in labels.values():
        label.set_path_effects([
            PathEffects.withStroke(linewidth=3, foreground='#4a90e2', alpha=0.3)
        ])

    plt.grid(True, linestyle='--', alpha=0.1, color='#404040')
    plt.title("Hasse Diagram", 
              fontsize=16, 
              pad=20,
              fontweight='bold',
              color='#4a90e2',
              fontfamily='sans-serif')
    
    plt.axis('off')
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 1.1)
    plt.tight_layout(pad=0.4)
    
    return fig

def display_supremum_table(hasse):
    st.subheader("Supremum Table")
    elements = sorted(hasse.elements)
    supremum_table = hasse.get_supremum_table()
    
    data = []
    for a in elements:
        row = {'Element': a}
        for b in elements:
            row[b] = supremum_table[a][b]
        data.append(row)
    
    df = pd.DataFrame(data)
    df.set_index('Element', inplace=True)
    st.dataframe(df, use_container_width=True)

def display_infimum_table(hasse):
    st.subheader("Infimum Table")
    elements = sorted(hasse.elements)
    infimum_table = hasse.get_infimum_table()
    
    data = []
    for a in elements:
        row = {'Element': a}
        for b in elements:
            row[b] = infimum_table[a][b]
        data.append(row)
    
    df = pd.DataFrame(data)
    df.set_index('Element', inplace=True)
    st.dataframe(df, use_container_width=True)

def main():
    set_page_style()
    
    st.title("Hasse Diagram Generator")
    
    st.markdown("""
    <div class="info-box">
        💡 This tool helps you generate Hasse diagrams for partially ordered sets (posets).
        Enter your relations in the format 'a b' where a ≤ b, and optionally specify the elements.
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📝 Input Relations")
        st.markdown("Enter relations one per line in the format 'a b' (meaning a ≤ b)")
        relations_text = st.text_area(
            "Relations",
            height=200,
            value="1 1\n2 2\n3 3\n1 2\n1 3\n2 3",
            help="Example: '1 2' means 1 ≤ 2"
        )

    with col2:
        st.markdown("### 🔍 Elements (Optional)")
        st.markdown("Enter elements separated by spaces. If left empty, elements will be inferred from relations.")
        elements_text = st.text_input(
            "Elements",
            value="1 2 3",
            help="Leave empty to infer elements from relations"
        )

    # Process input
    relations = []
    if relations_text.strip():
        for line in relations_text.strip().split('\n'):
            if line.strip():
                try:
                    a, b = line.strip().split()
                    relations.append((a, b))
                except ValueError:
                    st.error(f"❌ Invalid line: {line}. Please use format 'a b'")
                    return

    elements = elements_text.strip().split() if elements_text.strip() else None

    if st.button("🎨 Generate Hasse Diagram"):
        if not relations:
            st.error("❌ Please enter at least one relation")
            return

        with st.spinner("Generating Hasse diagram..."):
            hasse, error = create_hasse_diagram(relations, elements)
            
            if error:
                st.error(f"❌ Error: {error}")
                return

            if hasse:
                col1, col2 = st.columns([3, 2])

                with col1:
                    st.markdown("### 📊 Hasse Diagram")
                    fig = draw_hasse_diagram(hasse)
                    st.pyplot(fig, use_container_width=True)

                with col2:
                    st.markdown("### ℹ️ Diagram Information")
                    
                    st.markdown("**🔹 Elements:**")
                    st.code(', '.join(map(str, sorted(hasse.elements))))
                    
                    st.markdown("**🔻 Minimal Elements:**")
                    st.code(', '.join(map(str, sorted(hasse.get_minimal_elements()))))
                    
                    st.markdown("**🔺 Maximal Elements:**")
                    st.code(', '.join(map(str, sorted(hasse.get_maximal_elements()))))
                    
                    st.markdown("**📊 Hierarchical Levels:**")
                    levels = hasse.get_levels()
                    for level in sorted(levels):
                        st.code(f"Level {level}: {', '.join(map(str, sorted(levels[level])))}")

                st.markdown("---")
                
                tab1, tab2 = st.tabs(["Supremum Table", "Infimum Table"])
                
                with tab1:
                    display_supremum_table(hasse)
                
                with tab2:
                    display_infimum_table(hasse)

    st.markdown("""
    <div style="text-align: center; padding: 20px; margin-top: 50px; background: linear-gradient(90deg, #1E1E1E, #2D2D2D); border-radius: 10px;">
        <p style="color: #4a90e2;">Hasse Diagram Explorer v1.0 | © 2024 All rights reserved</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 
