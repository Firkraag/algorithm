from typing import Any, Optional
import gdb


class LinkedListNode:
    def __init__(self, key: Any):
        self.key: Any = key
        self.prev: Optional[LinkedListNode] = None
        self.next: Optional[LinkedListNode] = None


class LinkedList:
    def __init__(self):
        self.head: Optional[LinkedListNode] = None
        self.size: int = 0

    def empty(self) -> bool:
        return self.size == 0

    def search(self, key: Any) -> Optional[LinkedListNode]:
        node = self.head
        while node and node.key != key:
            node = node.next
        return node

    def insert(self, node: LinkedListNode) -> None:
        self.size = self.size + 1
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        node.prev = None

    def delete(self, node: LinkedListNode) -> None:
        self.size = self.size - 1
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev

    def extract(self, node: LinkedListNode) -> LinkedListNode:
        self.delete(node)
        return node
