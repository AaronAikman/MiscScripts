# VernamCipher
# implemented by Aaron Aikman for binary
# http://www.cryptomuseum.com/crypto/vernam.htm
# NOTE May prove difficult to use in the console if a newline character is generated

import subprocess


def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)


# two functions below by tmthydvnprt on Stack Overflow, the rest is invented
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]


def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])


# for testing
# sourceText = 'hello world'
# cipherText = 'waitbutwhy?'

def doVernam(sText, cText):
    bSText = string2bits(sText)
    bCText = string2bits(cText)
    binEncryptedText = []
    for ind, val in enumerate(bSText):
        # compare binary (matching bytes = 0, mismatching = 1) aka XOR
        binEncryptedText.append(reduce(lambda x, y: str(x) + str(y), [(1 - int(s == c)) for s, c in zip(val, bCText[ind])]))
    result = bits2string(binEncryptedText)
    copy2clip(result)
    return result

# For testing
# encryptedText = doVernam(sourceText, cipherText)
# print encryptedText
# print doVernam(encryptedText, cipherText)


while True:
    print 'Welcome to the VernamCipher Program'
    x = raw_input('Please enter the source text:\n')
    y = raw_input('Please enter the cipher text of matching length:\n')
    if len(x) != len(y):
        print 'Error: Lengths do not match'
    else:
        print doVernam(x, y)
    print '\n'