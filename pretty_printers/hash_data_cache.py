import gdb.printing
class HashDataCachePrinter:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        return "a string"
        # result = 'HashDataCache:\n'
        # result += 'Expire: {}, MaxSize: {}\n'.format(self.val['m_iCacheExpire'], self.val['m_iMaxCacheSize'])
        # begin = self.val'begin'
        # end = self.val'end'
        # while begin != end:
        #     key = begin.dereference()'first'
        #     data = begin.dereference()'second' # Assumes KeyData has an overloaded stream insertion operator
        #     result += 'Key: {}, Value: {}\n'.format(key, data)
        #     begin = self.val'next'
        # return result

def build_pretty_printer():
    return HashDataCachePrinter
