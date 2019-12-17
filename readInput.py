import Graph, Edge

def readInput(filename):
    with open(filename,'r') as f:
        lines = f.readlines()
    lines = [line[:-1] for line in lines]
    return createGraph(lines)

def createGraph(lines):
    verts = []
    edges = []
    for line in lines:
        lineverts = line.split(' ')
        if not lineverts[0] in verts:
            verts.append(lineverts[0])
        if not lineverts[1] in verts:
            verts.append(lineverts[1])
        if len(lineverts) == 2:
            edges.append(Edge.Edge(lineverts[0],lineverts[1]))
        else:
            edges.append(Edge.Edge(lineverts[0],lineverts[1],lineverts[2]))
    return Graph.Graph(verts,edges)
