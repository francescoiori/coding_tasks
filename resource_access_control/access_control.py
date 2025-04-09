from typing import Dict, Tuple
from tree import TreeNode

class AccessControl:
    def __init__(self, root: TreeNode):
        self.root = root
        # Maps nodeId to TreeNode for lookup
        self.node_map: Dict[str, TreeNode] = {}
        self._index_tree(root)

        # userId -> { nodeId -> (timestamp, isGrant) }
        self.access_log: Dict[str, Dict[str, Tuple[int, bool]]] = {}

    def _index_tree(self, node: TreeNode):
        self.node_map[node.id] = node
        for child in node.children:
            self._index_tree(child)

    def grantAccess(self, userId: str, nodeId: str, timestamp: int):
        if userId not in self.access_log:
            self.access_log[userId] = {}
        self.access_log[userId][nodeId] = (timestamp, True)

    def revokeAccess(self, userId: str, nodeId: str, timestamp: int):
        if userId not in self.access_log:
            self.access_log[userId] = {}
        self.access_log[userId][nodeId] = (timestamp, False)

    def hasAccess(self, userId: str, nodeId: str) -> bool:
        # This is the function to be implemented
      
        if userId not in self.access_log:
            return False

        node = self.node_map.get(nodeId)
        if not node:
            return False

        latest_op = (-1, False)  # timestamp, isGrant

        while node:
            if node.id in self.access_log[userId]:
                op = self.access_log[userId][node.id]
                if op[0] > latest_op[0]:
                    latest_op = op
            node = node.parent

        return latest_op[1]
