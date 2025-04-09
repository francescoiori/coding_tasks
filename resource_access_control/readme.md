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

