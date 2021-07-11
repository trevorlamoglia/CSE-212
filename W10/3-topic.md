# Data Structures outline

[Go Back](0-welcome.md)

## Tree

Similar to linked lists, **Trees** are connected to multiple different nodes and are connected together by pointers. We will look at the following types of trees: **binary trees**, **binary search trees**, and **balanced binary search trees**

### Binary Tree

**Binary Tree**, a tree that links to no more than two **nodes**. In the picture below, the top node(red) is called the **root** node. The bottom nodes, nodes that do not connect to other nodes(green) are called **leaf** nodes. The node that has connected nodes (top blue) is called **parent** node. The node connected to the parent (bottom blue) are called **child** nodes.

Nodes that are left and right of any parent node form a **subtree**. There is always one root node in a tree.

![Binary tree](binary.png)

### Binary Search Tree

**Binary Search Tree (BST)**, also called an *ordered binary tree* or *sorted binary tree*, is a type of non-linear data structure in which the nodes are arranged in a particular order. BST has the following properties: 

* The left subtree of a node has nodes which are only lesser than that node’s root.
* The right subtree of a node has nodes which are only greater than that node’s root.
* The left and right subtree must also be a binary search tree.

![Binary Search Tree](bst.jpg)

Non-linear data structure - data items that are not organized sequentially

## Common BST Operation:

* insert(value) - Insert 'value' into the tree
* remove(value) - Remove 'value' from the tree
* contains(value) - Determine if 'value is in the tree
* traverse_forward - Visit all objects from smallest to largest
* traverse_reverse - Visit all objects from largest to smallest
* height(node) - Determine the height of node.
* size() - Return the size of BST
* empty() - Returns true if root node is empty. 

## Time Complexity / Performance

Most BST operations above are in the **Logarithmic Time** Complexity except for the last two. A logarithmic time is an O(log n). An algorithm is said to have a logarithmic time complexity when it reduces the size of the input data in each step. It doesn't need to look at all values of the input data.

## Recursion

**Recursion** is a technique where a function calls itself. When using recursion, we follow two important rules:

* Smaller Problem - we need to make sure we are calling the function on a **smaller problem**. Without this rule, our function will run forever.
* As we continue to call the function on a smaller problem, we need a place to stop. We must define a scenario in which recursion is not required. This is called the **base case**.

## Example Code in Python

### Inserting into a BST



### Traversing a BST





## Problem to Solve

```python
# Problem 1



```

Click here

```python
# Problem 2



```

Click here








[Go Back](0-welcome.md)