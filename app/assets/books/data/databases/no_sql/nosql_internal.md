## INDEXING STRUCTURES FOR NOSQL DATABASES

Indexing is the process of associating a key with the location of a corresponding data record in a DBMS. There are many indexing data structures used in NoSQL databases. 

### B-Tree Indexing

B-Tree is one of the most common index structures in DBMS’s.
In B-trees, internal nodes can have a variable number of child nodes within some predefined range.
One major difference from other tree structures, such as AVL, is that B-Tree allows nodes to have a variable number of child nodes, meaning less tree balancing but more wasted space.
The B+-Tree is one of the most popular variants of B-Trees. The B+-Tree is an improvement over B-Tree that requires all keys to reside in the leaves.

### T-Tree Indexing

The data structure of T-Trees was designed by combining features from AVL-Trees and B-Trees.
AVL-Trees are a type of self-balancing binary search trees, while B-Trees are unbalanced, and each node can have a different number of children.
In a T-Tree, the structure is very similar to the AVL-Tree and the B-Tree.
Each node stores more than one {key-value, pointer} tuple. Also, binary search is utilized in combination with the multiple-tuple nodes to produce better storage and performance.
A T-Tree has three types of nodes: A T-Node that has a right and left child, a leaf node with no children, and a half-leaf node with only one child.

It is believed that T-Trees have better overall performance than AVL-Trees.

### O2-Tree Indexing

The O2-Tree is basically an improvement over Red-Black trees, a form of a Binary-Search tree, in which the leaf nodes contain the {key value, pointer} tuples.
O2-Tree was proposed to enhance the performance of current indexing methods. An O2-Tree of order m (m ≥ 2), where m is the minimum degree of the tree, satisfies the following properties:
Every node is either red or black. The root is black.
Every leaf node is colored black and consists of a block or page that holds “key value, record-pointer” pairs.
If a node is red, then both its children are black.
For each internal node, all simple paths from the node to descendant leaf-nodes contain the same number of black nodes. Each internal node holds a single key value.
Leaf-nodes are blocks that have between ⌈m/2⌉ and m “key-value, record-pointer” pairs.
If a tree has a single node, then it must be a leaf, which is the root of the tree, and it can have between 1 to m key data items.
Leaf nodes are double-linked in forward and backward directions.

