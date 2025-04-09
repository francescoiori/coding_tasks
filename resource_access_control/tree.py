class TreeNode:
  def __init__(self, id: str):
      self.id = id
      self.children = []
      self.parent = None

  def add_child(self, child: 'TreeNode'):
      child.parent = self
      self.children.append(child)
