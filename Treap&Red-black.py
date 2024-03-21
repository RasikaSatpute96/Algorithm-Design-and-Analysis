import time
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, key, priority=0):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        self.color = 'red'  # Red-Black Tree color

class Treap:
    def __init__(self):
        self.root = None
        self.nodes = 0

    def insert(self, root, key, priority):
        if not root:
            self.nodes += 1
            return TreeNode(key, priority)
        if key < root.key:
            root.left = self.insert(root.left, key, priority)
            if root.left.priority > root.priority:
                root = self.rightRotate(root)
        else:
            root.right = self.insert(root.right, key, priority)
            if root.right.priority > root.priority:
                root = self.leftRotate(root)
        return root

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def rightRotate(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        return x

class RedBlackTree:
    def __init__(self):
        self.root = None
        self.nodes = 0

    def insert(self, root, key):
        if not root:
            self.nodes += 1
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root = self.fixViolation(root, key)
        return root

    def fixViolation(self, root, key):
        if not root:
            return None

        # If the newly inserted node is at the root
        if not root.left and not root.right:
            root.color = 'black'
            return root

        # If the parent is black, no violation, so return
        if root.left and root.left.color == 'black' and root.right and root.right.color == 'black':
            return root

        # Violation exists
        # Get the parent and grandparent
        parent = self.findParent(root, key)
        grandparent = self.findParent(root, parent.key)

        # Case 1: Parent is red and uncle is red
        if parent.color == 'red' and self.getUncle(root, parent.key).color == 'red':
            parent.color = 'black'
            self.getUncle(root, parent.key).color = 'black'
            grandparent.color = 'red'
            return self.fixViolation(grandparent, grandparent.key)

        # Case 2: Parent is red and uncle is black, and new node is right child
        if parent.color == 'red' and self.getUncle(root, parent.key).color == 'black' and key > parent.key:
            root = self.leftRotate(grandparent)
            parent.color = 'black'
            grandparent.color = 'red'
            return root

        # Case 3: Parent is red and uncle is black, and new node is left child
        if parent.color == 'red' and self.getUncle(root, parent.key).color == 'black' and key < parent.key:
            root = self.rightRotate(grandparent)
            parent.color = 'black'
            grandparent.color = 'red'
            return root

        return root

    def findParent(self, root, key):
        if not root or (not root.left and not root.right):
            return None
        if (root.left and root.left.key == key) or (root.right and root.right.key == key):
            return root
        if key < root.key:
            return self.findParent(root.left, key)
        else:
            return self.findParent(root.right, key)

    def getUncle(self, root, key):
        parent = self.findParent(root, key)
        grandparent = self.findParent(root, parent.key)
        if grandparent.left == parent:
            return grandparent.right
        else:
            return grandparent.left

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        y.color = x.color
        x.color = 'red'
        return y

    def rightRotate(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        x.color = y.color
        y.color = 'red'
        return x

# Define the nodes list before using it in the function call
nodes = [
   (50, 100), (25, 75), (75, 125), (12, 60), (37, 80),
    (63, 110), (87, 130), (6, 55), (18, 65), (31, 77),
    (43, 85), (56, 105), (68, 115), (81, 120), (93, 135), 
    (106, 140), (118, 149), (131, 76), (147, 190),
    (163, 160), (176, 170), (187, 195), (197, 198),
    (210, 180), (223, 200), (234, 169), (245, 210),
    (257, 220), (267, 235), (279, 199), (284, 180), (300, 400), (400, 500), (500, 600), (600, 700), (700, 800), 
    (800, 900), (900, 1000), (1000, 1100), (1200, 1300), (1400, 1500),
    (1600, 1700), (1800, 1900), (2000, 2100), (2200, 2300), (2400, 2500),
    (2600, 2700), (2800, 2900), (3000, 3100), (3200, 3300), (3400, 3500),
    (3600, 3700), (3800, 3900), (4000, 4100), (4200, 4300), (4400, 4500),
    (4600, 4700), (4800, 4900), (5000, 5100), (5200, 5300), (5400, 5500),
    (5600, 5700), (5800, 5900), (6000, 6100), (6200, 6300), (6400, 6500),
    (6600, 6700), (6800, 6900), (7000, 7100), (7200, 7300), (7400, 7500),
    (7600, 7700), (7800, 7900)
]

def insertNodes(treeType, nodes):
    start_time = time.time()
    if treeType == 'Treap':
        tree = Treap()
        for key, priority in nodes:
            tree.root = tree.insert(tree.root, key, priority)
    else:
        tree = RedBlackTree()
        for key in nodes:
            tree.root = tree.insert(tree.root, key)
    end_time = time.time()
    return tree, (end_time - start_time)

treap, treap_time = insertNodes('Treap', nodes)
rbt, rbt_time = insertNodes('RBT', [node[0] for node in nodes])

def calculate_height(root):
    if not root:
        return 0
    return 1 + max(calculate_height(root.left), calculate_height(root.right))

treap_height = calculate_height(treap.root)
rbt_height = calculate_height(rbt.root)

metrics = {
    'Insertion Time (s)': [treap_time, rbt_time],
    'Height': [treap_height, rbt_height],
    'Nodes': [treap.nodes, rbt.nodes]
}

labels = list(metrics.keys())
treap_metrics = [metrics[label][0] for label in labels]
rbt_metrics = [metrics[label][1] for label in labels]

x = range(len(labels))
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x, treap_metrics, width=0.4, label='Treap', align='center')
ax.bar(x, rbt_metrics, width=0.4, label='Red-Black Tree', align='edge')
ax.set_ylabel('Values')
ax.set_title('Treap vs Red-Black Tree Performance Comparison')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)
ax.legend()

# Generate nodes with varying sizes
node_sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200, 7400, 7600, 7800]

treap_times = []
rbt_times = []

for size in node_sizes:
    nodes_subset = nodes[:size]

    treap, treap_time = insertNodes('Treap', nodes_subset)
    rbt, rbt_time = insertNodes('RBT', [node[0] for node in nodes_subset])

    treap_times.append(treap_time)
    rbt_times.append(rbt_time)

# Plotting the time graph
plt.figure(figsize=(10, 6))
plt.plot(node_sizes, treap_times, marker='o', label='Treap')
plt.plot(node_sizes, rbt_times, marker='s', label='Red-Black Tree')
plt.xlabel('Number of Nodes')
plt.ylabel('Insertion Time (s)')
plt.title('Insertion Time Comparison for Treap and Red-Black Tree')
plt.legend()
plt.grid(True)
plt.show()


