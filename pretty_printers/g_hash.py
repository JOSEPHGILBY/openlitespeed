import gdb.printing

class GHashPrinter:
    def __init__(self, val):
        self.val = val

    def display_hint(self):
        return 'map'

    def to_string(self):
        return "GHash with {} elements".format(self.val['sizenow'])
    
    def children(self):
        result = []
        current = gdb.parse_and_eval(to_cast_string(self.val) + ".begin()")
        end = gdb.parse_and_eval(to_cast_string(self.val) + ".end()")
        while current != end:
            key = current['pkey']
            data = current['pdata']
            result.append((str(key), data))
            current = gdb.parse_and_eval(to_cast_string(self.val) + ".next(" + to_cast_string(current) + ")" )
        return iter(result)

def build_pretty_printer():
    return GHashPrinter

def to_cast_string(gdb_val):
    if gdb_val.type.code != gdb.TYPE_CODE_PTR:
        addr = gdb_val.address
        return "(*({}*)({}))".format(gdb_val.type, addr)
    else:
        return "(({})({}))".format(gdb_val.type, gdb_val)