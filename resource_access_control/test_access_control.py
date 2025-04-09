from tree import TreeNode
from access_control import AccessControl

def build_sample_tree():
    root = TreeNode("world")
    usa = TreeNode("usa")
    ca = TreeNode("california")
    sf = TreeNode("san_francisco")
    ny = TreeNode("new_york")

    root.add_child(usa)
    usa.add_child(ca)
    ca.add_child(sf)
    usa.add_child(ny)

    return root

def test_access_control():
    root = build_sample_tree()
    ac = AccessControl(root)

    ac.grantAccess("alice", "usa", 1)
    assert ac.hasAccess("alice", "san_francisco") is True
    assert ac.hasAccess("alice", "new_york") is True

    ac.revokeAccess("alice", "california", 2)
    assert ac.hasAccess("alice", "san_francisco") is False
    assert ac.hasAccess("alice", "new_york") is True

    ac.grantAccess("alice", "san_francisco", 3)
    assert ac.hasAccess("alice", "san_francisco") is True

if __name__ == "__main__":
    test_access_control()
    print("All tests passed.")
