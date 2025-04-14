import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class HasseDiagram:
    def __init__(self, relations, elements=None):
        """
        Initialize the Hasse Diagram generator.
        
        Parameters:
        - relations: list of tuples representing partial order relations (a, b) meaning a ≤ b
        - elements (optional): explicit list of elements in the poset. If None, inferred from relations.
        """
        self.relations = set(relations)
        
        # Infer elements from relations if not provided
        if elements is None:
            self.elements = set()
            for a, b in self.relations:
                self.elements.add(a)
                self.elements.add(b)
        else:
            self.elements = set(elements)
            
        self.validate_input()
        
        # Create the directed graph
        self.G = nx.DiGraph()
        self.G.add_nodes_from(self.elements)
        self.G.add_edges_from([(a, b) for a, b in self.relations])
        
        # Perform transitive reduction
        self.transitive_reduction()
        
        # Precompute upper and lower bounds
        self._precompute_bounds()
        
    def _precompute_bounds(self):
        """Precompute upper and lower bounds for all pairs of elements."""
        self.upper_bounds = {}
        self.lower_bounds = {}
        elements = sorted(self.elements)
        
        for a in elements:
            for b in elements:
                # Find all upper bounds of {a, b}
                upper = set()
                for x in elements:
                    if (a, x) in self.relations and (b, x) in self.relations:
                        upper.add(x)
                self.upper_bounds[(a, b)] = upper
                
                # Find all lower bounds of {a, b}
                lower = set()
                for x in elements:
                    if (x, a) in self.relations and (x, b) in self.relations:
                        lower.add(x)
                self.lower_bounds[(a, b)] = lower
    
    def get_supremum(self, a, b):
        """Return the supremum (least upper bound) of a and b."""
        upper = self.upper_bounds.get((a, b), set())
        if not upper:
            return None
        
        # Find the minimal elements in the upper bounds
        minimal_upper = set()
        for x in upper:
            is_minimal = True
            for y in upper:
                if y != x and (y, x) in self.relations:
                    is_minimal = False
                    break
            if is_minimal:
                minimal_upper.add(x)
        
        # If there's exactly one minimal upper bound, it's the supremum
        return minimal_upper.pop() if len(minimal_upper) == 1 else None
    
    def get_infimum(self, a, b):
        """Return the infimum (greatest lower bound) of a and b."""
        lower = self.lower_bounds.get((a, b), set())
        if not lower:
            return None
        
        # Find the maximal elements in the lower bounds
        maximal_lower = set()
        for x in lower:
            is_maximal = True
            for y in lower:
                if y != x and (x, y) in self.relations:
                    is_maximal = False
                    break
            if is_maximal:
                maximal_lower.add(x)
        
        # If there's exactly one maximal lower bound, it's the infimum
        return maximal_lower.pop() if len(maximal_lower) == 1 else None
    
    def get_supremum_table(self):
        """Return a table of suprema for all pairs of elements."""
        elements = sorted(self.elements)
        table = {}
        for a in elements:
            row = {}
            for b in elements:
                row[b] = self.get_supremum(a, b)
            table[a] = row
        return table
    
    def get_infimum_table(self):
        """Return a table of infima for all pairs of elements."""
        elements = sorted(self.elements)
        table = {}
        for a in elements:
            row = {}
            for b in elements:
                row[b] = self.get_infimum(a, b)
            table[a] = row
        return table
    
    def validate_input(self):
        """Validate that the input forms a valid poset."""
        # Check reflexivity (each element must be related to itself)
        for a in self.elements:
            if (a, a) not in self.relations:
                raise ValueError(f"Input violates reflexivity: missing ({a},{a})")
        
        # Check antisymmetry
        for a, b in self.relations:
            if (b, a) in self.relations and a != b:
                raise ValueError(f"Input violates antisymmetry: both ({a},{b}) and ({b},{a}) present")
        
        # Check transitivity (we'll handle this in reduction)
        
        # Check all elements in relations exist in elements set
        for a, b in self.relations:
            if a not in self.elements or b not in self.elements:
                raise ValueError(f"Relation ({a},{b}) contains elements not in the provided set")
    
    def transitive_reduction(self):
        """Perform transitive reduction on the graph to remove redundant edges."""
        # Create a copy to work on
        TR = nx.DiGraph(self.G)
        
        # For each edge (u, v), check if there's a path u->...->v without this edge
        for u, v in list(TR.edges()):
            TR.remove_edge(u, v)
            if nx.has_path(TR, u, v):
                self.G.remove_edge(u, v)  # Remove from original graph if redundant
            else:
                TR.add_edge(u, v)  # Add back if not redundant
    
    def get_hasse_edges(self):
        """Return the edges of the Hasse diagram after transitive reduction."""
        return list(self.G.edges())
    
    def get_minimal_elements(self):
        """Return the minimal elements of the poset (no elements below them)."""
        return [node for node in self.G.nodes() if self.G.in_degree(node) == 0]
    
    def get_maximal_elements(self):
        """Return the maximal elements of the poset (no elements above them)."""
        return [node for node in self.G.nodes() if self.G.out_degree(node) == 0]
    
    def get_levels(self):
        """Compute the hierarchical levels for node positioning."""
        levels = defaultdict(list)
        # Use longest path from minimal elements to determine levels
        minimal = self.get_minimal_elements()
        for node in self.G.nodes():
            paths = [nx.shortest_path_length(self.G, source=m, target=node) 
                    for m in minimal if nx.has_path(self.G, m, node)]
            level = max(paths) if paths else 0
            levels[level].append(node)
        return dict(levels)
    
    def draw(self, title="Hasse Diagram"):
        """
        Draw the Hasse diagram using NetworkX and Matplotlib.
        
        Parameters:
        - title: str, title for the diagram (default: "Hasse Diagram")
        """
        # Create a layout based on levels
        levels = self.get_levels()
        pos = {}
        for level, nodes in levels.items():
            x_positions = [i/(len(nodes)+1) for i in range(1, len(nodes)+1)]
            for node, x in zip(nodes, x_positions):
                pos[node] = (x, level)
        
        plt.figure(figsize=(10, 8))
        nx.draw_networkx_nodes(self.G, pos, node_size=800, node_color='lightblue')
        nx.draw_networkx_edges(self.G, pos, width=2, arrows=False)
        nx.draw_networkx_labels(self.G, pos, font_size=12, font_weight='bold')
        
        plt.title(title, fontsize=16, pad=20)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def print_summary(self):
        """Print a formatted summary of the Hasse diagram."""
        print("="*60)
        print("HASSE DIAGRAM SUMMARY".center(60))
        print("="*60)
        print(f"\nElements ({len(self.elements)}): {', '.join(map(str, sorted(self.elements)))}")
        
        print("\nOriginal Relations:")
        for i, (a, b) in enumerate(sorted(self.relations), 1):
            print(f"{i:2}. {a} ≤ {b}")
        
        hasse_edges = self.get_hasse_edges()
        print("\nHasse Diagram Edges (after transitive reduction):")
        for i, (a, b) in enumerate(sorted(hasse_edges), 1):
            print(f"{i:2}. {a} → {b}")
        
        print("\nMinimal Elements:", ', '.join(map(str, sorted(self.get_minimal_elements()))))
        print("Maximal Elements:", ', '.join(map(str, sorted(self.get_maximal_elements()))))
        
        levels = self.get_levels()
        print("\nHierarchical Levels:")
        for level in sorted(levels):
            print(f"Level {level}: {', '.join(map(str, sorted(levels[level])))}")
        
        print("\n" + "="*60)


def get_user_input():
    """Helper function to get user input for relations and optionally elements."""
    print("\nEnter the partial order relations (one per line, format 'a b' for a ≤ b):")
    print("Enter 'done' when finished")
    relations = []
    while True:
        rel = input().strip()
        if rel.lower() == 'done':
            break
        parts = rel.split()
        if len(parts) != 2:
            print("Invalid input. Please enter exactly two elements separated by space.")
            continue
        relations.append(tuple(parts))
    
    print("\nDo you want to specify elements explicitly? (y/n)")
    if input().strip().lower() == 'y':
        print("Enter the elements of the poset (separated by spaces):")
        elements = input().split()
        return relations, elements
    else:
        return relations, None


def example_usage():
    """Demonstrate the Hasse diagram with an example."""
    # Example: Divisibility poset for the set {1,2,3,4,6,8,12}
    relations = [
        (1, 1), (2, 2), (3, 3), (4, 4), (6, 6), (8, 8), (12, 12),  # Reflexive
        (1, 2), (1, 3), (1, 4), (1, 6), (1, 8), (1, 12),           # 1 divides all
        (2, 4), (2, 6), (2, 8), (2, 12),
        (3, 6), (3, 12),
        (4, 8), (4, 12),
        (6, 12)
    ]
    
    print("\nRunning example with divisibility poset...")
    print("Relations only provided - elements will be inferred")
    hasse = HasseDiagram(relations)
    hasse.print_summary()
    hasse.draw(title="Hasse Diagram: Divisibility Poset (Inferred Elements)")

    print("\nRunning same example with explicit elements...")
    elements = [1, 2, 3, 4, 6, 8, 12]
    hasse = HasseDiagram(relations, elements)
    hasse.print_summary()
    hasse.draw(title="Hasse Diagram: Divisibility Poset (Explicit Elements)")


def main():
    print("HASSE DIAGRAM GENERATOR".center(60))
    print("="*60)
    
    while True:
        print("\nOptions:")
        print("1. Enter your own poset (relations only)")
        print("2. Enter your own poset (relations + elements)")
        print("3. Run example")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            relations, elements = get_user_input()
            try:
                hasse = HasseDiagram(relations)
                hasse.print_summary()
                hasse.draw(title="Hasse Diagram of Your Poset")
            except ValueError as e:
                print(f"\nError: {e}\nPlease try again with valid poset input.")
        elif choice == '2':
            relations, elements = get_user_input()
            try:
                hasse = HasseDiagram(relations, elements)
                hasse.print_summary()
                hasse.draw(title="Hasse Diagram of Your Poset")
            except ValueError as e:
                print(f"\nError: {e}\nPlease try again with valid poset input.")
        elif choice == '3':
            example_usage()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()