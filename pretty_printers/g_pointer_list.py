import gdb.printing

class GPointerListPrinter:
    def __init__(self, val):
        self.val = val

    def display_hint(self):
        return 'array'

    def to_string(self):
        return "GPointerList with {} elements".format(self.val['pend'] - self.val['pstore'])
    
    def children(self):
        result = ["ayooooo", "yeeeep"]
        return iter(result)
        # current = gdb.parse_and_eval(to_cast_string(self.val) + ".begin()")
        # end = gdb.parse_and_eval(to_cast_string(self.val) + ".end()")
        # while current != end:
        #     data = gdb.parse_and_eval("*((void**)({}))".format(current))
        #     result.append((str(current), data))
        #     current = gdb.parse_and_eval("((void**)({})) + 1".format(current))
        # return iter(result)

def build_pretty_printer():
    return GPointerListPrinter

def to_cast_string(gdb_val):
    if gdb_val.type.code != gdb.TYPE_CODE_PTR:
        addr = gdb_val.address
        return "(*({}*)({}))".format(gdb_val.type, addr)
    else:
        return "(({})({}))".format(gdb_val.type, gdb_val)