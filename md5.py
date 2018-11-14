import math
from urllib import parse
from html import unescape
from my_function import *


class MyMD5(object):
    def __init__(self, string):
        self._hash = {
            'sigBytes': 16,
            'words': [1732584193, 4023233417, 2562383102, 271733878]
        }
        self.md5 = ""
        self._data = {}
        self._nDataBytes = 0
        self.u = []
        self.blockSize = 16
        self.string = string

    def init(self):
        self.u = [0] * 64
        for e in range(0, 64):
            self.u[e] = ctypes_cov(int(abs(math.sin(e + 1)) * 4294967296)) | 0

    def _start(self):
        self.init()
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
        self.md5 = "".join(r)

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
        n = e['words']
        r = self._nDataBytes * 8
        i = e['sigBytes'] * 8
        gap = 16 - len(n)
        later_t_len = len(n)
        if gap:
            n.extend([0] * gap)
            later_t_len += gap
        n[rshift(i, 5)] = ctypes_cov(n[rshift(i, 5)]) | ctypes_cov(
            lshift(128, 24 - i % 32))
        s = 0
        o = r
        n[lshift(rshift(i + 64, 9), 4) + 15] = 0

        n[lshift(rshift(i + 64, 9), 4) + 14] = ctypes_cov(
            (ctypes_cov(lshift(o, 8)) | ctypes_cov(rshift(0, 24))) & 16711935
        ) | ctypes_cov((ctypes_cov(lshift(o, 24))
                        | ctypes_cov(rshift(0, 8))) & 4278255360)
        self._data['sigBytes'] = (later_t_len + 1) * 4
        self._data['words'] = n
        self._process()
        u = self._hash
        a = u['words']
        for f in range(0, 4):
            l = a[f]
            a[f] = ctypes_cov(
                ctypes_cov(
                    (ctypes_cov(lshift(l, 8)))
                    | ctypes_cov(rshift(l, 24))) & 16711935) | ctypes_cov(
                        ctypes_cov((ctypes_cov(lshift(l, 24)))
                                   | ctypes_cov(rshift(l, 8))) & 4278255360)
        self._hash['words'] = a

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
        h = r[:f]
        self._data['sigBytes'] -= l

    def _doProcessBlock(self, e, t):
        for n in range(0, 16):
            r = t + n
            i = e[r]
            e[r] = ctypes_cov(
                ctypes_cov(
                    (ctypes_cov(lshift(i, 8)))
                    | ctypes_cov(rshift(i, 24))) & 16711935) | ctypes_cov(
                        ctypes_cov((ctypes_cov(lshift(i, 24)))
                                   | ctypes_cov(rshift(i, 8))) & 4278255360)
        s = self._hash['words']
        o = e[t + 0]
        a = e[t + 1]
        p = e[t + 2]
        d = e[t + 3]
        v = e[t + 4]
        m = e[t + 5]
        g = e[t + 6]
        y = e[t + 7]
        b = e[t + 8]
        w = e[t + 9]
        E = e[t + 10]
        S = e[t + 11]
        x = e[t + 12]
        N = e[t + 13]
        C = e[t + 14]
        k = e[t + 15]
        L = s[0]
        A = s[1]
        O = s[2]
        M = s[3]
        L = self.f(L, A, O, M, o, 7, self.u[0])
        M = self.f(M, L, A, O, a, 12, self.u[1])
        O = self.f(O, M, L, A, p, 17, self.u[2])
        A = self.f(A, O, M, L, d, 22, self.u[3])
        L = self.f(L, A, O, M, v, 7, self.u[4])
        M = self.f(M, L, A, O, m, 12, self.u[5])
        O = self.f(O, M, L, A, g, 17, self.u[6])
        A = self.f(A, O, M, L, y, 22, self.u[7])
        L = self.f(L, A, O, M, b, 7, self.u[8])
        M = self.f(M, L, A, O, w, 12, self.u[9])
        O = self.f(O, M, L, A, E, 17, self.u[10])
        A = self.f(A, O, M, L, S, 22, self.u[11])
        L = self.f(L, A, O, M, x, 7, self.u[12])
        M = self.f(M, L, A, O, N, 12, self.u[13])
        O = self.f(O, M, L, A, C, 17, self.u[14])
        A = self.f(A, O, M, L, k, 22, self.u[15])
        L = self.l(L, A, O, M, a, 5, self.u[16])
        M = self.l(M, L, A, O, g, 9, self.u[17])
        O = self.l(O, M, L, A, S, 14, self.u[18])
        A = self.l(A, O, M, L, o, 20, self.u[19])
        L = self.l(L, A, O, M, m, 5, self.u[20])
        M = self.l(M, L, A, O, E, 9, self.u[21])
        O = self.l(O, M, L, A, k, 14, self.u[22])
        A = self.l(A, O, M, L, v, 20, self.u[23])
        L = self.l(L, A, O, M, w, 5, self.u[24])
        M = self.l(M, L, A, O, C, 9, self.u[25])
        O = self.l(O, M, L, A, d, 14, self.u[26])
        A = self.l(A, O, M, L, b, 20, self.u[27])
        L = self.l(L, A, O, M, N, 5, self.u[28])
        M = self.l(M, L, A, O, p, 9, self.u[29])
        O = self.l(O, M, L, A, y, 14, self.u[30])
        A = self.l(A, O, M, L, x, 20, self.u[31])
        L = self.c(L, A, O, M, m, 4, self.u[32])
        M = self.c(M, L, A, O, b, 11, self.u[33])
        O = self.c(O, M, L, A, S, 16, self.u[34])
        A = self.c(A, O, M, L, C, 23, self.u[35])
        L = self.c(L, A, O, M, a, 4, self.u[36])
        M = self.c(M, L, A, O, v, 11, self.u[37])
        O = self.c(O, M, L, A, y, 16, self.u[38])
        A = self.c(A, O, M, L, E, 23, self.u[39])
        L = self.c(L, A, O, M, N, 4, self.u[40])
        M = self.c(M, L, A, O, o, 11, self.u[41])
        O = self.c(O, M, L, A, d, 16, self.u[42])
        A = self.c(A, O, M, L, g, 23, self.u[43])
        L = self.c(L, A, O, M, w, 4, self.u[44])
        M = self.c(M, L, A, O, x, 11, self.u[45])
        O = self.c(O, M, L, A, k, 16, self.u[46])
        A = self.c(A, O, M, L, p, 23, self.u[47])
        L = self.h(L, A, O, M, o, 6, self.u[48])
        M = self.h(M, L, A, O, y, 10, self.u[49])
        O = self.h(O, M, L, A, C, 15, self.u[50])
        A = self.h(A, O, M, L, m, 21, self.u[51])
        L = self.h(L, A, O, M, x, 6, self.u[52])
        M = self.h(M, L, A, O, d, 10, self.u[53])
        O = self.h(O, M, L, A, E, 15, self.u[54])
        A = self.h(A, O, M, L, a, 21, self.u[55])
        L = self.h(L, A, O, M, b, 6, self.u[56])
        M = self.h(M, L, A, O, k, 10, self.u[57])
        O = self.h(O, M, L, A, g, 15, self.u[58])
        A = self.h(A, O, M, L, N, 21, self.u[59])
        L = self.h(L, A, O, M, v, 6, self.u[60])
        M = self.h(M, L, A, O, S, 10, self.u[61])
        O = self.h(O, M, L, A, p, 15, self.u[62])
        A = self.h(A, O, M, L, w, 21, self.u[63])
        self._hash['words'][0] = ctypes_cov(self._hash['words'][0] + L) | 0
        self._hash['words'][1] = ctypes_cov(self._hash['words'][1] + A) | 0
        self._hash['words'][2] = ctypes_cov(self._hash['words'][2] + O) | 0
        self._hash['words'][3] = ctypes_cov(self._hash['words'][3] + M) | 0

    def f(self, e, t, n, r, i, s, o):
        u = ctypes_cov(e) + (ctypes_cov(t) & ctypes_cov(n) | ~ctypes_cov(t) &
                             ctypes_cov(r)) + ctypes_cov(i) + ctypes_cov(o)
        return (lshift(u, s) | rshift(u, 32 - s)) + t

    def l(self, e, t, n, r, i, s, o):
        u = ctypes_cov(e) + (
            ctypes_cov(t) & ctypes_cov(r)
            | ctypes_cov(n) & ~ctypes_cov(r)) + ctypes_cov(i) + ctypes_cov(o)
        return (lshift(u, s) | rshift(u, 32 - s)) + t

    def c(self, e, t, n, r, i, s, o):
        u = ctypes_cov(e) + (ctypes_cov(t) ^ ctypes_cov(n) ^ ctypes_cov(r)) + \
        ctypes_cov(i) + ctypes_cov(o)
        return (lshift(u, s) | rshift(u, 32 - s)) + t

    def h(self, e, t, n, r, i, s, o):
        u = ctypes_cov(e) + (
            ctypes_cov(n) ^
            (ctypes_cov(t) | ~ctypes_cov(r))) + ctypes_cov(i) + ctypes_cov(o)
        return (lshift(u, s) | rshift(u, 32 - s)) + t


if __name__ == '__main__':
    x = MyMD5('tc_385577b5faf07cd6_166ee91e8db_3ea51541762745203')
    x.start()