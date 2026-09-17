import networkx as nx
import matplotlib.pyplot as plt

# Criando o grafo
G = nx.Graph()

# Vértices
v1 = "V1"
v2 = "V2"
v3 = "V3"
v4 = "V4"

# Arestas
G.add_edge(v1, v2)
G.add_edge(v2, v3)
G.add_edge(v3, v4)
G.add_edge(v4, v2)

# Pesos das arestas
G[v1][v2]["peso"] = 5
G[v2][v3]["peso"] = 2
G[v2][v4]["peso"] = 7
G[v3][v4]["peso"] = 1

# Rótulos das arestas
edge_labels = {
    (v1, v2): 5,
    (v2, v3): 2,
    (v2, v4): 7,
    (v3, v4): 1
}

# Posição dos vértices
pos = nx.spring_layout(G)

# Desenhando os vértices
nx.draw_networkx(
    G,
    pos,
    node_size=5000,
    font_size=25,
    node_color="yellow",
    with_labels=True
)

# Desenhando os pesos das arestas
nx.draw_networkx_edge_labels(
    G,
    pos,
    font_size=20,
    font_color="blue",
    edge_labels=edge_labels
)

# Título
plt.title("Grafo de exemplo")

# Exibir
plt.show()

