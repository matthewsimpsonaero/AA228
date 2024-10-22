import networkx as nx
import matplotlib.pyplot as plt

# Define the nodes and edges of the Bayesian network
nodes = ["age", "portembarked", "fare", "numparentschildren", 
         "passengerclass", "sex", "numsiblings", "survived"]

edges = [
    ("age", "numparentschildren"),
    ("numparentschildren", "numsiblings"),
    ("numparentschildren", "survived"),
    ("passengerclass", "fare"),
    ("passengerclass", "portembarked"),
    ("passengerclass", "survived"),
    ("passengerclass", "age"),
    ("sex", "survived"),
    ("sex", "numparentschildren"),
    ("sex", "passengerclass"),
    ("numsiblings", "portembarked"),
    ("survived", "portembarked"),
]

# Create a directed graph from the edges
G = nx.DiGraph()
G.add_edges_from(edges)

# Calculate the number of parents and children for each node
num_parents = {node: 0 for node in nodes}
num_children = {node: 0 for node in nodes}

for parent, child in edges:
    num_parents[child] += 1
    num_children[parent] += 1

# Assign colors based on the number of parents and children
colors = []
alphas = [1] * len(nodes)  # Set all alphas to 1
for node in nodes:
    parent_count = num_parents[node]
    child_count = num_children[node]

    # Total parents and children
    total_count = parent_count + child_count

    if total_count > 0:
        # Calculate the ratio of children to total (for gradient)
        ratio = child_count / total_count

        # Interpolate color between red (1, 0, 0) and blue (0, 0, 1)
        color = (
            1 - ratio,  # Red component decreases with more children
            0,          # Green component stays 0
            ratio       # Blue component increases with more children
        )
    else:
        color = (0.5, 0.5, 0.5)  # Grey for neutral nodes with no children or parents

    colors.append(color)

# Draw the graph
plt.figure(figsize=(12, 10))  # Adjust the figure size
pos = nx.spring_layout(G, k=1.3)  # Increased k to spread out the nodes further

# Draw each node individually with alpha=1
for i, node in enumerate(nodes):
    nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color=[colors[i]], node_size=3500, alpha=0.5)

# Draw the edges
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20, edge_color='black')  # Draw edges separately

# Draw the labels with smaller black bold text inside the nodes
for node, (x, y) in zip(nodes, pos.values()):
    plt.text(x, y, node, fontsize=8, fontweight='bold', ha='center', va='center', color='black', alpha=1.0)  # Smaller font size

plt.axis('off')  # Turn off the axis
plt.show()
