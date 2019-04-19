
# A mapping from letter to integer
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26))) 
# A mapping from Interger to lettter
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

'''-------------------------------------------------------------------------------
  Function: Get the encryption or decryption key if it is in range between 1- 26 
   
  Returns:  Key

  Arguments: None   
----------------------------------------------------------------------------------'''
def getKey():
    while True:
        print('Enter the key for encryption (between 1 - 26)')
        key = int(input())
        if (key >= 1 and key <= 26):
            return key
    return key

'''----------------------------------------------------------------------
  Function: Encrypts a text input with a given key using caesar cipher
   
  Returns:  Ciphered Text

  Arguments: None   
-------------------------------------------------------------------------'''
def encryptCaesarCipher():
    plainText = input("Enter text to be encrypted here:")
    key = getKey()
    cipherText =''
    for letter in plainText.upper():
        if letter.isalpha(): 
            cipherText += I2L[ (L2I[letter] + key)%26 ]
        else: 
            cipherText += letter
    return cipherText
