# VigenereCipher
# Implemented by Aaron Aikman
# https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

import subprocess

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)


# Core
alphabet = 'abcdefghijklmnopqrstuvwxyz'
keydict = dict([ (x[1],x[0]) for x in enumerate(alphabet) ])

# For Testing
# plainText = 'ATTACKATDAWN'
# cipherKey = 'LEMON'
# cipherTex = 'lxfopvefrnhr'

def doVigenere(toConvert, cKey, mode = 0):
    '''
    Mode 0 = decrypt
    Mode 1 = encrypt
    '''
    # Lengthening cipher if needed
    if len(toConvert) > len(cKey):
        multiplier = len(toConvert) / len(cKey)
        cKey *= (multiplier + 1)
        cKey = cKey[:len(toConvert)]
    if not mode:
        mode = -1

    # Formatting inputs
    toConvert = toConvert.lower()
    cKey = cKey.lower()

    # Cipher
    temp = ''
    for ind, val in enumerate(toConvert):
        # Adding or subtracting to compensate by mode
        indexToFind = keydict[val] + (keydict[cKey[ind]] * mode)
        # looping indices
        if indexToFind > 25:
            indexToFind -= 26
        if indexToFind < 0:
            indexToFind += 26
        temp += alphabet[indexToFind]
    return cKey.upper(), temp.upper()

# For testing
# print doVigenere(cipherTex, cipherKey, mode = 0)
# print doVigenere(plainText, cipherKey, mode = 1)

while True:
    print 'Welcome to the VigenereCipher Program'
    z = raw_input('Please enter a mode (1 to encrypt, 0 to decrypt):\n')

    # Processing Z
    if z == '':
        z = 1

    try:
        z = int(z)
    except:
        z = 1

    if z > 0:
        z = 1
    else:
        z = 0

    messages = [['\nSet to Decrypt',
                 'Please enter the text to decrypt.\n',
                 'Please enter the cipher text \n(its length will be formatted if necessary)\n',
                 'PlainText:  '
                 ],
                ['\nSet to Encrypt',
                 'Please enter the text to encrypt without spaces.\n',
                 'Please enter the cipher text (its length will be formatted if necessary).\n',
                 'Encrypted:  '
                 ]
                 ]

    # Handling modes
    print messages[z][0]
    x = (raw_input(messages[z][1])).replace(' ', '')
    x = filter(lambda i: i.isalpha(), x)
    y = raw_input(messages[z][2])
    y = filter(lambda j: j.isalpha(), y)
    if len(y) > len(x):
        print 'Error: The source text length was shorter than the cipher text length'
    else:
        result = doVigenere(x, y, z)
        print '\n'
        resultText = "CipherText: {}\n{}{}".format(result[0], messages[z][3], result[1])
        copy2clip(result[1])
        print resultText

    print '\n'

