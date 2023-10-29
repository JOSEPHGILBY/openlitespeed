import gdb.printing

class LsStrPrinter:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        return self.val['ptr'].string(length=self.val['len'])

def build_pretty_printer():
    return LsStrPrinter