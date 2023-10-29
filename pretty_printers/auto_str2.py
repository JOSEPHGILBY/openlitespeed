import gdb.printing
class AutoStr2Printer:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        # Get the pointer and length
        ptr = self.val['ptr']
        len = self.val['len']

        # Create a string from the pointer and length
        string = ptr.lazy_string(length=len)

        return string

    # def children(self):
    #     yield 'ptr', self.val['ptr']
    #     yield 'len', self.val['len']

    # def display_hint(self):
    #     return 'string'

def build_pretty_printer():
    return AutoStr2Printer
