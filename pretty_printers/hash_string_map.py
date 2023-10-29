import gdb.printing
class HashStringMapPrinter:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        return "a string"
        # result = 'HashStringMap:\n'
        # begin = self.val'begin'
        # end = self.val'end'
        # while begin != end:
        #     key = begin.dereference()'first'
        #     data = begin.dereference()'second'
        #     result += 'Key: {}, Value: {}\n'.format(key, data)
        #     begin = self.val'next'
        # return result

def build_pretty_printer():
    return HashStringMapPrinter