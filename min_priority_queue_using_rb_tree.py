from rb_tree import rb_tree
import sys

class min_priority_queue(rb_tree):
    def heap_minimum(self):
        return self.minimum()
    def heap_extract_min(self):
        x = self.minimum()
        self.delete(x)
        return x
    def heap_decrease_key(self, node, key):
        if key > node.key:
            sys.exit("new key is larger than current key")
        self.delete(node)
        node.key = key
        self.insert(node)
    def min_heap_insert(self, node):
        self.insert(node)
