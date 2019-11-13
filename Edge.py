class Edge:
  start = 0
  end = 1
  reverse = False
  weight = 1
  
  def __init__(self,start,end,weight=1,reverse=False):
    self.start = start
    self.end = end
    self.weight = weight

  def __str__(self):
    return "("+str(self.start)+","+str(self.end)+","+str(self.weight)+")"

  def reverse(self):
    return Edge(self.end,self.start,self.weight,not self.reverse)

  def invert(self):
    return Edge(self.end,self.start,-1*self.weight,self.reverse)

class TruncEdge:
  vert = 0
  weight = 1
  
  def __init__(self,vert=None,weight=1,edge=None,end=False):
    if edge:
      if start:
        self.vert = edge.end
      else:
        self.vert = edge.start
    else:
      self.vert = vert
    self.weight = weight

  def __str__(self):
    return "("+str(self.vert)+","+str(self.weight)+")"

  def full(self,start):
    return Edge(start,self.vert,self.weight)
