import time
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, key, priority=0):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
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

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and key < root.left.key:
            return self.rightRotate(root)
        if balance < -1 and key > root.right.key:
            return self.leftRotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        x.height = 1 + max(self.getHeight(x.left), self.getHeight(x.right))
        return x

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
    if treeType == 'AVL':
        tree = AVLTree()
        for key, _ in nodes:
            tree.root = tree.insert(tree.root, key)
    else:
        tree = Treap()
        for key, priority in nodes:
            tree.root = tree.insert(tree.root, key, priority)
    end_time = time.time()
    return tree, (end_time - start_time)

avl_tree, avl_time = insertNodes('AVL', nodes)
treap, treap_time = insertNodes('Treap', nodes)

def calculate_height(root):
    if not root:
        return 0
    return 1 + max(calculate_height(root.left), calculate_height(root.right))

avl_height = calculate_height(avl_tree.root)
treap_height = calculate_height(treap.root)

metrics = {
    'Insertion Time (s)': [avl_time, treap_time],
    'Height': [avl_height, treap_height],
    'Nodes': [avl_tree.nodes, treap.nodes]
}

labels = list(metrics.keys())
avl_metrics = [metrics[label][0] for label in labels]
treap_metrics = [metrics[label][1] for label in labels]

x = range(len(labels))
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(x, avl_metrics, width=0.4, label='AVL', align='center')
ax.bar(x, treap_metrics, width=0.4, label='Treap', align='edge')
ax.set_ylabel('Values')
ax.set_title('AVL Tree vs Treap Performance Comparison')
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45)
ax.legend()

# Generate nodes with varying sizes
node_sizes = [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600, 6800, 7000, 7200, 7400, 7600, 7800]

avl_times = []
treap_times = []

for size in node_sizes:
    nodes_subset = nodes[:size]

    avl_tree, avl_time = insertNodes('AVL', nodes_subset)
    treap, treap_time = insertNodes('Treap', nodes_subset)

    avl_times.append(avl_time)
    treap_times.append(treap_time)

# Plotting the time graph
plt.figure(figsize=(10, 6))
plt.plot(node_sizes, avl_times, marker='o', label='AVL')
plt.plot(node_sizes, treap_times, marker='s', label='Treap')
plt.xlabel('Number of Nodes')
plt.ylabel('Insertion Time (s)')
plt.title('Insertion Time Comparison for AVL Tree and Treap')
plt.legend()
plt.grid(True)
plt.show()

