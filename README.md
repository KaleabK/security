## Cryptography (Caesar cipher)

Caesar cipher - is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 

The method is apparently named after Julius Caesar, who apparently used it to communicate with his officials.
Thus to cipher a given text we need an integer value, known as shift which indicates the number of position each letter of the text has been moved down.

The encryption can also be represented using modular arithmetic by first transforming the letters into numbers,according to the scheme, A → 0, B → 1, ..., Z → 25. Encryption of a letter x by a shift n can be described mathematically as

![Encryption Phase with shift n](https://github.com/KaleabK/security/master/data/encryption.svg)

Decryption is performed similarly,

![Decryption Phase with shift n](https://github.com/KaleabK/security/master/data/decryption.svg)

##
![Caesar cipher](https://github.com/KaleabK/security/master/data/ceaserCi.png)