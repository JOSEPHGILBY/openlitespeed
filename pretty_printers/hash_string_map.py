import gdb.printing
from g_hash import GHashPrinter
class HashStringMapPrinter:
    def __init__(self, val):
        ghash_val = gdb.parse_and_eval("(*({}*)({}))".format("GHash", val.address))
        self.g_hash_printer = GHashPrinter(ghash_val)
        self.val = val
        self.template_type = str(val.type.template_argument(0))

    def to_string(self):
        return "it's a hashstringmap"

    def display_hint(self):
        return 'map'

    def children(self):
        result = []
        for key, value in self.g_hash_printer.children():
            casted_value = gdb.parse_and_eval("(*({})({}))".format(self.template_type, value.address))
            result.append((key, casted_value))
        return iter(result)
        

def build_pretty_printer():
    return HashStringMapPrinter