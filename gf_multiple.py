def xtime(x):
    remainder = 0x1b if x & 0x80 else 0x00
    return (x << 1) ^ remainder
def multiply(a, b):
    temp = [a]
    for i in range(1, 8):
        temp.append(xtime(temp[-1]))
    result = (b & 0x01) * a
    for i in range(1, 8):
        result ^= ((b >> i) & 0x01) * temp[i]
    return hex(result & 0xff)
a = 7
b = 10
print(multiply(a, b))
