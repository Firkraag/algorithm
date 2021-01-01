#!/usr/bin/env python

import b_tree as bt

a = bt.b_tree_node(3, True, 2)
a.key[0] = 'A'
a.key[1] = 'B'
b = bt.b_tree_node(3, True, 3)
b.key[0] = 'D'
b.key[1] = 'E'
b.key[2] = 'F'
c = bt.b_tree_node(3, True, 3)
c.key[0] = 'J'
c.key[1] = 'K'
c.key[2] = 'L'
d = bt.b_tree_node(3, True, 2)
d.key[0] = 'N'
d.key[1] = 'O'
x = bt.b_tree_node(3, True, 3)
x.key[0] = 'Q'
x.key[1] = 'R'
x.key[2] = 'S'
y = bt.b_tree_node(3, True, 2)
y.key[0] = 'U'
y.key[1] = 'V'
z = bt.b_tree_node(3, True, 2)
z.key[0] = 'Y'
z.key[1] = 'Z'
e = bt.b_tree_node(3, False, 3)
e.key[0] = 'C'
e.key[1] = 'G'
e.key[2] = 'M'
e.c[0] = a
e.c[1] = b
e.c[2] = c
e.c[3] = d
v = bt.b_tree_node(3, False, 2)
v.key[0] = 'T'
v.key[1] = 'X'
v.c[0] = x
v.c[1] = y
v.c[2] = z
t = bt.b_tree(3)
t.root.key[0] = 'P'
t.root.c[0] = e
t.root.c[1] = v
t.root.n = 1
t.root.leaf = False
t.root.delete(t, 'F')
t.root.print_child_first()
print()
t.root.delete(t, 'M')
t.root.print_child_first()
print()
t.root.delete(t, 'G')
t.root.print_child_first()
print()
t.root.delete(t, 'D')
t.root.print_child_first()
print()
t.root.delete(t, 'B')
t.root.print_child_first()
print()
t.root.delete(t, 'C')
t.root.print_child_first()
print()
t.root.delete(t, 'P')
t.root.print_child_first()
print()
t.root.delete(t, 'V')
t.root.print_child_first()
print()
