from unittest import TestCase
from queue import Queue, EmptyException, FullException


class TestQueue(TestCase):
    def test_enqueue_and_dequeue(self):
        queue = Queue(3)
        queue.enqueue(1)
        queue.enqueue(2)
        with self.assertRaises(FullException):
            queue.enqueue(3)
        self.assertEqual(1, queue.dequeue())
        self.assertEqual(2, queue.dequeue())
        with self.assertRaises(EmptyException):
            queue.dequeue()

    def test_empty(self):
        queue = Queue(2)
        self.assertTrue(queue.empty())

    def test_full(self):
        queue = Queue(2)
        queue.enqueue(1)
        self.assertTrue(queue.full())
        queue = Queue(1)
        self.assertTrue(queue.full())

    def test_capacity(self):
        queue = Queue(5)
        self.assertEqual(4, queue.capacity())
