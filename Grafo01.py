import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('Lins')
G.add_node('Guaiçara')
G.add_node('RioPreto')
G.add_node('Penápolis')
G.add_node('Promissão')
G.add_node('Avanhandava')

G.add_edge('Lins', 'Guaiçara', distancia=5)

G.add_edge('Guaiçara', 'Penápolis', distancia=40)

G.add_edge('Guaiçara', 'RioPreto', distancia=100)

G.add_edge('Penápolis', 'RioPreto', distancia=50)

G.add_edge('Guaiçara', 'Promissão', distancia=8)

G.add_edge('Guaiçara', 'Avanhandava', distancia=8)

G.add_edge('Avanhandava', 'Promissão', distancia=10)


rotulos = {
    ('Lins', 'Guaiçara'): 5,
    ('Guaiçara', 'Penápolis'): 40,
    ('Guaiçara', 'RioPreto'): 100,
    ('Penápolis', 'RioPreto'): 50,
    ('Guaiçara', 'Promissão'): 8,
    ('Guaiçara', 'Avanhandava'): 8,
    ('Avanhandava', 'Promissão'): 10
}


path = nx.shortest_path(G, 'Lins', 'RioPreto', weight='distancia')

print(path)


pos = nx.spring_layout(G)

nx.draw_networkx(
    G,
    pos,
    node_size=1110,
    font_color='w',
    font_size=7.5
)

nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=rotulos
)

plt.show()