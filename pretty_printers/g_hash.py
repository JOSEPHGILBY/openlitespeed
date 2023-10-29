import gdb.printing

class GHashPrinter:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        eval_string = "(*("+str(self.val.type)+"*)("+str(self.val.address)+")).method()"
        return "a string"
        # result = 'GHash:\n'
        # begin = self.val'begin'
        # end = self.val'end'
        # while begin != end:
        #     key = begin.dereference()'getKey'
        #     data = begin.dereference()'getData'
        #     result += 'Key: {}, Value: {}\n'.format(key, data)
        #     begin = self.val'next'
        # return result

def build_pretty_printer():
    return GHashPrinter