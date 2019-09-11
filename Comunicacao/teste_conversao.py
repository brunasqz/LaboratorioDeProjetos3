def generateChar(s):
    return ("0x%i" % int(s, 2))


def getPrefix(s):
    return (bin((s & 1536) >> 9))


def getPosfix(s):
    return (bin(s & 511))

# 2 bits para operacao
#   01, aciona ima
#   10, motor lanca
#   11, motor giro
# 9 bits para parametro
#   converter 360 em 9 bits

# motor lanca, 180 graus
assert generateChar('10' + '010110100') == '0x1204'
assert getPrefix(1204) == '0b10'
assert getPosfix(1204) == '0b10110100'

# motor giro, 10 graus
assert generateChar('11' + '000001010') == '0x1546'
assert getPrefix(1546) == '0b11'
assert getPosfix(1546) == '0b1010'

# ligar ima
assert generateChar('01' + '000000001') == '0x513'
assert getPrefix(513) == '0b1'
assert getPosfix(513) == '0b1'
