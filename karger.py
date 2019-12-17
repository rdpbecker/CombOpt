import random, printing
import readInput as read

def pickEdge(edges):
  total = sum([x.weight for x in edges])
  pick = total*random.random()
  partial = 0
  for edge in edges:
    if partial >= pick:
      return edge
    partial = partial + edge.weight
  return edges[-1]
 
def karger(graph):
  while len(graph.verts) > 2:
    print("Current Graph")
    print(graph)
    print("Current Edges")
    printing.printEdges(graph.edges)
    edge = pickEdge(graph.edges)
    graph = graph.contract([edge.start,edge.end])
  return graph.verts[0]

def main():
  graph1 = read.readInput("testInput/test1.txt")
  cut = karger(graph1)
  print(cut)

if __name__ == "__main__":
  main()
