from collections import defaultdict


# Defaultdict é um contêiner como dicionários presentes nas coleções de módulos.
# Defaultdict é uma subclasse da classe de dicionário que retorna um objeto semelhante a um dicionário. 
# A funcionalidade de ambos os dicionários e defualtdict são quase as mesmas,
# exceto pelo fato de que defualtdict nunca gera um KeyErro

from graphviz import Digraph
from graphviz import Graph

#Graphviz é um software de visualização de gráficos de código aberto. 
# A visualização de gráficos é uma forma de representar informações estruturais 
# como diagramas de gráficos abstratos e redes. 
# Possui aplicações importantes em redes, bioinformática, engenharia de software, 
# banco de dados e web design, aprendizado de máquina e em interfaces visuais para outros domínios técnicos


class Grafo(object):
    """ Implementação básica de um grafo. """

    def __init__(self, arestas, direcionado=False):
        """Inicializa as estruturas base do grafo."""
        self.adj = defaultdict(set)
        self.direcionado = direcionado
        self.adiciona_arestas(arestas)

    def get_vertices(self):
        """ Retorna a lista de vértices do grafo. """
        return list(self.adj.keys())

    def get_arestas(self):
        """ Retorna a lista de arestas do grafo. """
        return [(k, v) for k in self.adj.keys() for v in self.adj[k]]


    def adiciona_arestas(self, arestas):
        """ Adiciona arestas ao grafo. """
        for u, v in arestas:
            self.adiciona_arco(u, v)


    def adiciona_arco(self, u, v):
        """ Adiciona uma ligação (arco) entre os nodos 'u' e 'v'. """
        self.adj[u].add(v)
        # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
        #if not self.direcionado:
          #  self.adj[v].add(u)


    def existe_aresta(self, u, v):
        """ Existe uma aresta entre os vértices 'u' e 'v'? """
        return u in self.adj and v in self.adj[u]


    def __len__(self):
        return len(self.adj)


    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.adj))


    def __getitem__(self, v):
        return self.adj[v]


    def desenha(self):

        if(self.direcionado):
           g = Digraph('G')
        else:
           g = Graph('G')

        
       #desenhando vertices
        for estado in self.get_vertices():
         g.node(estado) # um dos estados 

        #desenhando arestas
        arestas = self.get_arestas()
        for u, v in arestas:
          g.edge(u, v)

        return g

# Cria a lista de arestas.
arestas = [('A', 'A'),('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'B'), ('C', 'E'), ('D', 'A'), ('E', 'B')]

# Cria e imprime o grafo.
grafo = Grafo(arestas, direcionado=True)
print(grafo.adj)

print(grafo.get_vertices())

print(grafo.get_arestas())

print(grafo.existe_aresta('A', 'B'), grafo.existe_aresta('E', 'C'))

g=grafo.desenha();
g

