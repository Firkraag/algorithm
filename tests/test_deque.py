from unittest import TestCase

from Queue import FullException, EmptyException
from deque import Deque


class TestDeque(TestCase):
    def test_enqueue_tail_and_dequeue_head(self):
        deque = Deque(3)
        deque.enqueue_tail(1)
        deque.enqueue_tail(2)
        with self.assertRaises(FullException):
            deque.enqueue_tail(3)
        self.assertEqual(1, deque.dequeue_head())
        self.assertEqual(2, deque.dequeue_head())
        with self.assertRaises(EmptyException):
            deque.dequeue_head()

    def test_enqueue_head_and_dequeue_tail(self):
        deque = Deque(3)
        deque.enqueue_head(1)
        deque.enqueue_head(2)
        with self.assertRaises(FullException):
            deque.enqueue_head(3)
        self.assertEqual(1, deque.dequeue_tail())
        self.assertEqual(2, deque.dequeue_tail())
        with self.assertRaises(EmptyException):
            deque.dequeue_tail()

    def test_enqueue_tail_and_dequeue_tail(self):
        deque = Deque(3)
        deque.enqueue_tail(1)
        deque.enqueue_tail(2)
        self.assertEqual(2, deque.dequeue_tail())
        self.assertEqual(1, deque.dequeue_tail())
        with self.assertRaises(EmptyException):
            deque.dequeue_tail()
        with self.assertRaises(EmptyException):
            deque.dequeue_head()

    def test_enqueue_head_and_dequeue_head(self):
        deque = Deque(3)
        deque.enqueue_head(1)
        deque.enqueue_head(2)
        self.assertEqual(2, deque.dequeue_head())
        self.assertEqual(1, deque.dequeue_head())
        with self.assertRaises(EmptyException):
            deque.dequeue_tail()
        with self.assertRaises(EmptyException):
            deque.dequeue_head()
