import os
dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

def Decryption():
    DRead = open(dir+'/secret.txt', 'r').read()
#This opens the plaintext.txt.enc.txt file and reads it, if the user
#did not want to source form a txt file then the code can be replaced 
#in line 10 by;
             #print('Enter message to be Decrypted!')
             #ERead = input()
    print('Please enter unique key for Decryption!')
    Dkey = input()
#Line 16 & 17 allows the user to input a unique key that is the 
#important reference to which the code decrypts, thus typing the 
#key in has to be correct and has to be the same as the key set 
#during the encryption phase. For this the set key is
#"PH370 Python"
    DMessage = len(DRead)
    DKey = Dkey * (1 + DMessage//len(Dkey))
#Both the message and key in lines 23 & 24 are now broken down for
#their lengths.
    DWrite = open(dir+'/secret.txt.dec.txt', 'w')
#This is the location where the Decrypted text with outputted too.
#This allows the code to write into a .txt file.
    for i in range(DMessage):
        DPi = ord(DRead[i])
        Dki = ord(DKey[i]) - 32
        DCi = DPi - Dki
#The above sequences allow for the mathematical formula for 
#decrypting a message, its is the reverse method to encrypting a 
#file. Line 31 converts the individual letters of the message into 
#numbers that corresponds with ASCII 1967 defintions. Lines 32 Does 
#the following but with the key instead of the message, 32 is then 
#subtracted but the numbers the individual letters so that the key 
#is not greater than 126 which is the highest number in the ASCII 
#1967 defintions. The value of the letters in the message then is 
#taken away from the value of letters in the key to encrypt the 
#letter via a number.
        if DCi < 32:
            DCi = DCi + 95
#If the final value of DCi is greater than 126 (The max limit of the
#ASCII 1967 defintions), similiar what happens to the key in line 32.
        D = chr(DCi)
#Line 33 minus the key and the letter togehter to get a single number
#the muber is thus changed back into a letter in relation to the 
#ASCII 1967 defintions. This allows the message in line 80 to be 
#"encrypted" but replaces the orginal message with the encrypted 
#message. Which is saved in a .txt file named in line 27.
        print(DPi, Dki, DCi, D)
        DWrite.write(D)
    DWrite.close()
    print('System Message: Decryption Complete')
#The lines 55 & 56 writes the decrypted text into a seperate file
#labelled in line 27, and closes it, stops the writing to the file.

Cipher = Decryption()
print(Cipher)