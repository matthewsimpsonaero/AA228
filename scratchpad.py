#create a random bayes net to check our scoring algorithm
num_edges = random.randint(len(nodes), len(nodes) * (len(nodes) - 1) // 2)  # Random number of edges

for _ in range(num_edges):
    u, v = random.sample(list(nodes), 2)  # Pick two random nodes
    bayes_net.add_edge(u, v)  # Add edge
    
    # If adding the edge creates a cycle, remove it
    if not networkx.is_directed_acyclic_graph(bayes_net):
        bayes_net.remove_edge(u, v)

draw_network(bayes_net)