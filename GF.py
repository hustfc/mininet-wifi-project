primitive_polynomial_dict = {4: 0b10011,  # x**4  + x  + 1
                             8: (1 << 8) + 0b11101,  # x**8  + x**4  + x**3 + x**2 + 1
                             16: (1 << 16) + (1 << 12) + 0b1011,  # x**16 + x**12 + x**3 + x + 1
                             32: (1 << 32) + (1 << 22) + 0b111,  # x**32 + x**22 + x**2 + x + 1
                             64: (1 << 64) + 0b11011  # x**64 + x**4 + x**3 + x + 1
                             }
class GF:
    def __init__(self, w):
        self.w = w
        self.gflog = []
        self.gfilog = [1] # g(0) = 1
        self.make_gf_dict(self.w, self.gflog, self.gfilog)

    def make_gf_dict(self, w, gflog, gfilog):
        gf_element_total_number = 1 << w
        primitive_polynomial = primitive_polynomial_dict[w]
        for i in range(1, gf_element_total_number - 1):
            temp = gfilog[i - 1] << 1  # g(i) = g(i-1) * g
            if temp & gf_element_total_number:  # 如果溢出，那么异或primitive polynomial
                temp ^= primitive_polynomial  # mod primitive_polynomial in GF(2**w) == XOR
            gfilog.append(temp)

        assert (gfilog[gf_element_total_number - 2] << 1) ^ primitive_polynomial
        gfilog.append(None)

        for i in range(gf_element_total_number):
            gflog.append(None)

        for i in range(0, gf_element_total_number - 1):
            gflog[gfilog[i]] = i
        print(gflog)
        print(gfilog)

    def mul(self, a, b):
        total = (1 << self.w) - 1
        return self.gfilog[(self.gflog[a] + self.gflog[b]) % total]

    def div(self, a, b):
        total = (1 << self.w) - 1
        return self.gfilog[(self.gflog[a] - self.gflog[b]) % total]

gf = GF(4)
a = gf.mul(7, 9)
print(a)
b = gf.div(a, 9)
print(b)





