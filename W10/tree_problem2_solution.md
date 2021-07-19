```python
def _traverse_backward(self, node):
    if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)
```

Back to [Tree](3-topic.md)