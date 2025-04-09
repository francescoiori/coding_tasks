# 🧠 Hierarchical Resource Access Control System

## ✨ Overview

You are building a **resource access control system** for a company that manages users’ access to a **geographical hierarchy** (like world → country → state → city). This hierarchy is modeled as a **tree**.

Users can be **granted** or **revoked** access to nodes. Access is inherited down the tree unless explicitly revoked. The most **recent operation** (grant or revoke) on a node or any of its ancestors determines whether the user currently has access to the node.


## 🏗️ Tree Structure Example

```
world 
└── usa 
    ├── california 
    │ └── san_francisco 
    └── new_york
``` 

## 🔐 Access Rules

- A **grant** gives a user access to that node and all its descendants.
- A **revoke** removes access to that node and all its descendants unless access is explicitly granted again lower in the tree.
- **Access is determined by the most recent operation** (grant or revoke) for a user when traversing from the node up to the root.

---

## ✅ Your Task

Implement the class `AccessControl` with the following methods:

### `grantAccess(userId: str, nodeId: str, timestamp: int)`
Grants the user access to the specified node at a given timestamp.

### `revokeAccess(userId: str, nodeId: str, timestamp: int)`
Revokes the user’s access to the specified node at the given timestamp.

### `hasAccess(userId: str, nodeId: str) -> bool`
Returns `True` if the **latest access-related operation** (grant or revoke) for the user on the node or any ancestor was a **grant**.

---

## 🧪 Example Walkthrough

### Step 1: Grant access at a parent node
```
world 
└── usa 
    ├── california 
    │ └── san_francisco 
    └── new_york
``` 

```python
ac.grantAccess("alice", "usa", 1)
```

✅ Result:

```python
hasAccess("alice", "usa") → True
hasAccess("alice", "california") → True
hasAccess("alice", "san_francisco") → True
```

### Step 2: Revoke access deeper in the tree

```python
ac.revokeAccess("alice", "california", 2)
```

✅ Result:

```python
hasAccess("alice", "california") → False
hasAccess("alice", "san_francisco") → False
hasAccess("alice", "new_york") → True
```

### Step 3: Grant access again, even deeper

```python
ac.grantAccess("alice", "san_francisco", 3)
```

✅ Result:

```python
hasAccess("alice", "san_francisco") → True
hasAccess("alice", "california") → False
```

### 🚫 Naive Approach (What Not To Do)
A naive solution might:

- Store a set of all nodes a user currently has access to.
- On grantAccess, traverse the entire subtree of the target node and add all nodes to the user's access set.
- On revokeAccess, do the same to remove access from all descendants.

This leads to:

❌ O(n) time per grant or revoke operation (where n is the size of the subtree).
❌ High memory usage per user.


### ⚙️ Optimal solution 

By using a timestamped log of grant/revoke actions per user and node:

- We don’t need to store the full access set.
- Each node for a user only stores the latest operation.

During hasAccess, we walk up the tree, comparing timestamps to find the most recent grant/revoke affecting access.

This enables:

- grantAccess and revokeAccess in O(1) (simple dictionary insert).
- hasAccess in O(depth) with efficient timestamp comparison.
- No redundant storage — each user-node pair only keeps the latest operation.

Timestamps are the key to enabling efficient, conflict-free resolution of overlapping grant/revoke operations across the tree hierarchy.

Timestamps are monotonically increasing — every grantAccess or revokeAccess is called with a strictly increasing timestamp for a given user.

### Space / Time complexity 

- grantAccess in O(1) time
- revokeAccess in O(1) time
- hasAccess in O(depth) time — where depth is the number of ancestors from the node to the root.

Minimal memory usage: store only the most recent operation (timestamp + action) per user-node.

Assume the tree is static (i.e., the structure doesn't change after initialization).

