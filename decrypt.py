'''----------------------------------------------------------------------
  Function: Descrypts a ciphered text with a given key using caesar cipher
   
  Returns:  Plain Text

  Arguments: None   
-------------------------------------------------------------------------'''

def decryptCaesarCipher():
    cipherText = input("Enter text to be decrypted here:")
    key = getKey()
    print (key)
    plainText = ''
    for letter in cipherText.upper():
        if letter.isalpha():
             plainText += I2L[ (L2I[letter] - key)%26 ]
        else: 
            plainText += letter
    return plainText
