from priority_queue import min_priority_queue 
class Min_priority_queue(min_priority_queue):
    def min_heap_insert(self, key):
        if self.heap_size >= self.length:
            sys.exit("heap overflow")
        self.heap_size = self.heap_size + 1
        self.heap[self.heap_size - 1] = node(None, None, float("Inf"))
        self.heap_decrease_key(self.heap_size - 1, key)
class character(object):
    def __init__(self, char, freq, sibling = None):
        self.char = char
        self.freq = freq
        self.sibling = sibling
    def __eq__(self, y):
        if self.freq == y.freq:
            return True
    def __gt__(self, y):
        if self.freq > y.freq:
            return True
    def __ge__(self, y):
        if self.freq >= y.freq:
            return True
    def __le__(self, y):
        if self.freq <= y.freq:
            return True
    def __lt__(self, y):
        if self.freq < y.freq:
            return True
class node(object):
    def __init__(self, left, right, freq):
        self.left = left
        self.right =right
        self.freq = freq
    def __eq__(self, y):
        if self.freq == y.freq:
            return True
    def __gt__(self, y):
        if self.freq > y.freq:
            return True
    def __ge__(self, y):
        if self.freq >= y.freq:
            return True
    def __le__(self, y):
        if self.freq <= y.freq:
            return True
    def __lt__(self, y):
        if self.freq < y.freq:
            return True
class tenary_node(object):
    def __init__(self, freq, child = None, sibling = None):
        self.freq = freq
        self.child = child
        self.sibling = sibling
    def __eq__(self, y):
        if self.freq == y.freq:
            return True
    def __gt__(self, y):
        if self.freq > y.freq:
            return True
    def __ge__(self, y):
        if self.freq >= y.freq:
            return True
    def __le__(self, y):
        if self.freq <= y.freq:
            return True
    def __lt__(self, y):
        if self.freq < y.freq:
            return True
def huffman(chars, freqs):
    n = len(chars)
    c = [0] * n
    for i in range(0, n):
        c[i] = character(chars[i], freqs[i])
    q = Min_priority_queue(c)
    for i in range(0, n - 1):
        x = q.heap_extract_min()
        y = q.heap_extract_min()
        q.min_heap_insert(node(x, y, x.freq + y.freq))
    return q.heap_extract_min()
def print_code(root):
    print_code_aux(root, '')
def print_code_aux(node, s):
    if hasattr(node, "left"):
        print_code_aux(node.left, s + '0')
        print_code_aux(node.right, s + '1')
    else:
        print "character: {}\tfrequency: {}\tcode: {}".format(node.char, node.freq, s)
def compact_store_prefix_code(root):
    store = []
    compact_store_prefix_code_aux(root, store, '')
    return store
def compact_store_prefix_code_aux(node, store, string):
    if hasattr(node, "left"):
        compact_store_prefix_code_aux(node.left, store, string + '0')
        compact_store_prefix_code_aux(node.right, store, '1')
    else:
        store.append((node.char, string))
def decode_compact_prefix_code(store):
    code = ''
    pos = 0
    for i in range(0, len(store)):
        last_len = len(code)
        char = store[i][1][0]
        for pos in range(last_len - 1, -1, -1):
            if code[pos] != char:
                break
        if pos <= 0:
            code = store[i][1]
        else:
            code = code[0:pos] + store[i][1]
        print "char: {}, code: {}".format(store[i][0], code)
def huffman_tenary(chars, freqs, m):
    ''' generalize Huffman's algorithm to tenary codewords
    the parameter m is the number of symbols we use, eg, in
    original huffman algorithm, we use 0 and 1, so m = 2'''
    n = len(chars)
    c = [0] * n
    for i in range(0, n):
        c[i] = character(chars[i], freqs[i])
    q = Min_priority_queue(c)
    while q.heap_size >= m:
        x = q.heap_extract_min()
        z = tenary_node(x.freq, x)
        for j in range(1, m):
            y = q.heap_extract_min()
            x.sibling = y
            z.freq = z.freq + y.freq
            x = y
        q.min_heap_insert(z)
    if q.heap_size == 1:
        return q.heap_extract_min()
    x = q.heap_extract_min()
    z = tenary_node(x.freq, x)
    while q.heap_size > 0:    
        y = q.heap_extract_min()
        x.sibling = y
        z.freq = z.freq + y.freq
        x = y
    q.min_heap_insert(z)
    return q.heap_extract_min()
def print_huffman_tenary(root):
    print_huffman_tenary_aux(root, '', '')
def print_huffman_tenary_aux(node, string, sibling):
    if hasattr(node, "child"):
        print_huffman_tenary_aux(node.child, string + str(sibling),  0)
    else:
        print "character: {}\tfrequency: {}\tcode: {}".format(node.char, node.freq, string + str(sibling))
    if node.sibling != None:
        print_huffman_tenary_aux(node.sibling, string, sibling + 1)
