def c(op, signal, arg):
    total = (op << 10) + (signal << 9) + arg
    return bytearray([total >> 8, total & 255])


op = 3
signal = 0
arg = 180

# print(bytes([]))
#print(c(op, signal, arg))

op = 1
#print(op << 10)
#print(op << 5)
#print((op << 10) | (op << 5))
print(1<<5)
