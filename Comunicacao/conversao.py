# 01 = ima
# 10 = motor lanca
# 11 = motor giro
# c1 = '11'

# se ima
#   0 desliga
#   1 liga
# se motor
#   256 em 9bits

def converter(s):
    print("0x%i" % int(s, 2))

def prefacio(s):
    print(bin((s & 1536) >> 9))

def posfacio(s):
    print(bin(s & 511))

print ('motor lanca, 180 graus')
s = '10' + '010110100'
print(s)
converter(s)
prefacio(1204)
posfacio(1204)

print ('motor giro, 10 graus')
s = '11' + '000001010'
print(s)
converter(s)
prefacio(1546)
posfacio(1546)

print ('ligar ima')
s = '01' + '000000001'
print(s)
converter(s)
prefacio(513)
posfacio(513)



