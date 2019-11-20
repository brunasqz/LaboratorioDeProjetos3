def c(op, signal, arg):
    total = (op << 10) + (signal << 9) + arg
    return bytearray([total >> 8, total & 255])


op = 3
signal = 0
arg = 180

# print(bytes([]))
print(c(op, signal, arg))
