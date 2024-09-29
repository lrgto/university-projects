import os
dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def getMode():
    print('Do you wish to encrypt or decrypt a message?')
    mode = input()
#
    if mode in 'E Encrypt e encrypt'.split():
        print(Encryption())
        return mode
    elif mode in 'D Decrypt d decrypt'.split():
        print(Decryption())
        return mode
    else:
        print('For Encryption, enter either "E", "Encrypt", "e", "encrypt".') 
        print('For Decryption, enter either "D", "Decrypt", "d", "decrypt".')

def Encryption():
    print('Enter message to be encrypted!')
    ERead = input()
    print('Please enter unique key for Encryption!')
    Ekey = input()
    EMessage = len(ERead)
    EKey = Ekey * (1 + EMessage//len(Ekey))
    EWrite = open(dir+'/plaintext.txt.enc.txt', 'w')
    for i in range(EMessage):
        EPi = ord(ERead[i])
        Eki = ord(EKey[i]) - 32
        ECi = EPi + Eki
        if ECi > 126:
            ECi = ECi - 95
        E = chr(ECi)
        print(EPi, Eki, ECi, E)
        EWrite.write(E)
    EWrite.close()
    print('System Message: Encryption Complete')


def Decryption():
    print('Enter message to be encrypted!')
    DRead = input()
    print('Please enter unique key for Encryption!')
    Dkey = input()
    DMessage = len(DRead)
    DKey = Dkey * (1 + DMessage//len(Dkey))
    DWrite = open(dir+'/plaintext.txt.enc.dec.txt', 'w')
    for i in range(DMessage):
        DPi = ord(DRead[i])
        Dki = ord(DKey[i]) - 32
        DCi = DPi - Dki
        if DCi < 32:
            DCi = DCi + 95
        D = chr(DCi)
        print(DPi, Dki, DCi, D)
        DWrite.write(D)
    DWrite.close()
    print('System Message: Decryption Complete')

Cipher = getMode()
print(Cipher)