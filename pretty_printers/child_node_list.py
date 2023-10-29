import gdb.printing
class ChildNodeListPrinter:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        return "ChildNodeList"

    def children(self):
        # Create a callback function to yield key-value pairs
        def callback(key, value):
            yield 'key', key
            yield 'value', value

        # Use for_each2 to iterate over elements in the hash map
        self.val['m_pHash'].dereference().for_each2(callback)

def build_pretty_printer():
    return ChildNodeListPrinter

