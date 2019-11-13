class Graph:
  verts = []
  edges = []
  relation = {}
  def __init__(self,vertices,edges):
    self.vertices = vertices
    self.edges = edges
    self.genRelation(vertices,edges)

  def genRelation(verts,edges):
    for vert in verts:
      self.relation[vert] = []
    for edge in edges:
      self.relation[edge.start].append(edge)
      self.realtion[edge.end].append(edge)

  def addVertex(self,vertex):
    self.vertices.append(vertex)
    self.relation[vertex] = []

  def addEdge(self,edge):
    if not edge.start in self.verts or not edge.end in self.verts:
      return
    self.edges.append(edge)
    self.relation[edge.start].append(TruncEdge(edge,0))
    self.relation[edge.end].append(TruncEdge(edge,1))
