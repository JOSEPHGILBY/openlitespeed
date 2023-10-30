import gdb.printing
class HashStringMapPrinter:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        return str(self.val.type)
        # result = 'HashStringMap:\n'
        # begin = self.val'begin'
        # end = self.val'end'
        # while begin != end:
        #     key = begin.dereference()'first'
        #     data = begin.dereference()'second'
        #     result += 'Key: {}, Value: {}\n'.format(key, data)
        #     begin = self.val'next'
        # return result

    # def display_hint(self):
    #     return 'map'

    # def children(self):
    #     count = 0
    #     result = []
    #     for it in self.val:
    #         count += 1
    #         result.append(('Key %d' % count, it['first']))
    #         result.append(('Value %d' % count, it['second']))
    #     return iter(result)

def build_pretty_printer():
    return HashStringMapPrinter