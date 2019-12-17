import Edge
import copy
import printing

class Graph:
  verts = []
  edges = []
  relation = {}
  def __init__(self,vertices,edges):
    self.verts = vertices
    self.edges = edges
    self.genRelation(vertices,edges)

  def __str__(self):
    string = ""
    for vert in self.verts:
      string = string + str(vert) + ": " + self.edgeListToString(self.relation[vert]) + "\n" 
    return string

  def edgeListToString(self,edges):
    string = ""
    for edge in edges:
      string = string + str(edge) + " "
    return string

  def genRelation(self,verts,edges):
    for vert in verts:
      self.relation[vert] = []
    for edge in edges:
      self.relation[edge.start].append(Edge.TruncEdge(edge=edge,head=True))
      self.relation[edge.end].append(Edge.TruncEdge(edge=edge,head=False))

  def addVertex(self,vertex):
    self.vertices.append(vertex)
    self.relation[vertex] = []

  def addEdge(self,edge):
    if not edge.start in self.verts or not edge.end in self.verts:
      return
    self.edges.append(edge)
    self.relation[edge.start].append(Edge.TruncEdge(edge=edge,head=True))
    self.relation[edge.end].append(Edge.TruncEdge(edge=edge,head=False))

  def cut(self,S):
    cutEdges = []
    for vert in S:
      for edge in self.relation[vert]:
        if not edge.vert in S:
          cutEdges.append(edge.full(vert))
    return cutEdges

  def contract(self,verts):
    newEdges = []
    newVerts = copy.deepcopy(self.verts)
    newVert = ' '.join(verts)
    newVerts.append(newVert)
#   print(newVerts)
    for vert in verts:
#     print(vert)
      newVerts.remove(vert)
    cutEdges = self.cut(verts)
#   printing.printEdges(cutEdges)
    nonCutEdges = copy.deepcopy(self.edges)
    for cutedge in cutEdges:
      for edge in nonCutEdges:
        if cutedge == edge:
          nonCutEdges.remove(edge)
          break
    used = []
    for edge in cutEdges:
      if not edge.end in used:
        newEdges.append(edge.newStart(newVert))
        used.append(edge.end)
    for edge in nonCutEdges:
      if not edge.start in verts:
        newEdges.append(edge)
    return Graph(newVerts,newEdges)
