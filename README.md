# Hasse Diagram Explorer 🎯

An interactive web application for visualizing and exploring partially ordered sets (posets) through Hasse diagrams. Built with Streamlit, NetworkX, and Matplotlib.

## Features ✨

- **Interactive Visualization**: Generate beautiful Hasse diagrams with a modern, dark-themed interface
- **Comprehensive Analysis**: View supremum and infimum tables, identify minimal and maximal elements
- **Educational Content**: Learn about poset theory through interactive examples and clear explanations
- **User-Friendly Interface**: Simple input format for poset relations and elements

## Installation 🚀

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hasse-diagram-explorer.git
cd hasse-diagram-explorer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage 📝

1. Navigate to the "Hasse Diagram Generator" page
2. Enter your poset relations in the format 'a b' (meaning a ≤ b)
3. Optionally specify the elements of your poset
4. Click "Generate Hasse Diagram" to visualize

Example input:
```
1 1
1 2
1 3
2 2
2 3
3 3
```

## Project Structure 📂

```
hasse-diagram-explorer/
├── app.py                 # Main application entry point
├── Hasse.py              # Core Hasse diagram implementation
├── requirements.txt      # Project dependencies
└── pages/
    ├── 1_Home.py        # Home page with features overview
    ├── 2_Theory.py      # Educational content about posets
    ├── 3_Contact.py     # Contact form and information
    └── 4_Hasse_Diagram_Generator.py  # Main diagram generator
```

## Dependencies 📚

- streamlit==1.32.0
- networkx==3.2.1
- matplotlib==3.8.3
- pandas==2.2.1

## Features in Detail 🔍

### Visualization
- Interactive Hasse diagram generation
- Dark theme with modern UI elements
- Customizable diagram layouts

### Analysis Tools
- Supremum and infimum tables
- Minimal and maximal elements identification
- Hierarchical level analysis

### Educational Resources
- Comprehensive theory section
- Interactive examples
- Step-by-step tutorials

## Contributing 🤝

Contributions are welcome! Please feel free to submit a Pull Request.

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact 📧

- Email: support@hassediagramexplorer.com
- Twitter: [@hassediagram](https://twitter.com/hassediagram)
- GitHub: [hassediagramexplorer](https://github.com/hassediagramexplorer)

## Acknowledgments 🙏

- Thanks to all contributors who have helped shape this project
- Special thanks to the mathematical community for their valuable feedback