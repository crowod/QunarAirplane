from urllib import parse
from html import unescape
from my_function import *

class MySHA(object):
    def __init__(self, string):
        self._hash = {
            'sigBytes': 20,
            'words':
            [1732584193, 4023233417, 2562383102, 271733878, 3285377520]
        }
        self._data = {}
        self._nDataBytes = 0
        self.blockSize = 16
        self.sha = ''
        self.string = string
    
    def _start(self):
        self._append()
        self._doFinalize()
        self.decrypt()

    def start(self):
        self._start()

    def toString(self,number):
        return hex(number).replace('0x', '')

    def decrypt(self):
        t = self._hash['words']
        n = self._hash['sigBytes']
        r = []
        for i in range(n):
            s = ctypes_cov(rshift(t[rshift(i, 2)], ctypes_cov(24 - i % 4 * 8))) & 255
            r.append(self.toString(rshift(s, 4)))
            r.append(self.toString(ctypes_cov(s) & 15))
        self.sha = "".join(r)

    def _append(self):
        self.string = unescape(parse.quote(self.string))
        n = [0] * 25
        for r in range(len(self.string)):
            n[rshift(r, 2)] = ctypes_cov(n[rshift(r, 2)]) | ctypes_cov(
                lshift((ord(self.string[r]) & 255), 24 - (r % 4 * 8)))
        n = list(filter(lambda x: x != 0, n))
        self._data['sigBytes'] = len(self.string)
        self._data['words'] = n
        self._nDataBytes += len(self.string)

    def _doFinalize(self):
        e = self._data
        t = e['words']
        n = self._nDataBytes * 8
        r = e['sigBytes'] * 8
        gap = 16 - len(t)
        later_t_len = len(t)
        if gap:
            t.extend([0] * gap)
            later_t_len += gap
        t[rshift(r, 5)] = ctypes_cov(t[rshift(r, 5)]) | ctypes_cov(
            lshift(128, 24 - r % 32))
        t[lshift(rshift(r + 64, 9), 4) + 14] = 0
        t[lshift(rshift(r + 64, 9), 4) + 15] = n
        self._data['sigBytes'] = later_t_len * 4
        self._data['words'] = t
        self._process()

    def _process(self):
        n = self._data
        r = n['words']
        i = n['sigBytes']
        s = self.blockSize
        u = s * 4
        a = i / u
        a = int(a)
        f = a * s
        l = min(f * 4, i)
        if f:
            for c in range(0, f, s):
                self._doProcessBlock(r, c)

    def _doProcessBlock(self, e, t):
        o = [0] * 80
        n = self._hash['words']
        r = n[0]
        i = n[1]
        s = n[2]
        u = n[3]
        a = n[4]
        gap = 80 - len(e)
        e.extend([0] * gap)
        for f in range(0, 80):
            if f < 16:
                o[f] = ctypes_cov(e[t + f]) | 0
            else:
                l = ctypes_cov(o[f - 3]) ^ ctypes_cov(o[f - 8]) ^ ctypes_cov(
                    o[f - 14]) ^ ctypes_cov(o[f - 16])
                o[f] = lshift(ctypes_cov(l), 1) | ctypes_cov(rshift(l, 31))
            c = (ctypes_cov(lshift(r, 5))
                 | ctypes_cov(rshift(r, 27))) + a + o[f]
            if f < 20:
                c += (ctypes_cov(i) & ctypes_cov(s)
                      | ~ctypes_cov(i) & ctypes_cov(u)) + 1518500249
            elif f < 40:
                c += (
                    ctypes_cov(i) ^ ctypes_cov(s) ^ ctypes_cov(u)) + 1859775393
            elif f < 60:
                c += (ctypes_cov(i) & ctypes_cov(s)
                      | ctypes_cov(i) & ctypes_cov(u)
                      | ctypes_cov(s) & ctypes_cov(u)) - 1894007588
            else:
                c += (
                    ctypes_cov(i) ^ ctypes_cov(s) ^ ctypes_cov(u)) - 899497514
            a = u
            u = s
            s = ctypes_cov(lshift(i, 30)) | ctypes_cov(rshift(i, 2))
            i = r
            r = c
        self._hash['words'][0] = ctypes_cov(self._hash['words'][0] + r) | 0
        self._hash['words'][1] = ctypes_cov(self._hash['words'][1] + i) | 0
        self._hash['words'][2] = ctypes_cov(self._hash['words'][2] + s) | 0
        self._hash['words'][3] = ctypes_cov(self._hash['words'][3] + u) | 0
        self._hash['words'][4] = ctypes_cov(self._hash['words'][4] + a) | 0

if __name__ == '__main__':
    x = MySHA('tc_385577b5faf07cd6_166ee91e8db_3ea51541753268802')
    x.start()
