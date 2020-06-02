class Node:
  "Common base class for all nodes"
  def __init__(self, node_type: str, position: list, color: str, isVisited: bool = False):
    self.type = node_type
    self.position = position
    self.color = color
    self.isVisited = isVisited
