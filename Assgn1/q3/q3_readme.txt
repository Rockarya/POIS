Using PRF in secure mode to obtain CPA-secure encryption scheme.

Take seed(as binary string) and message(text) as input.

Algorithm:
The encryption-decryption key is generated using PRF in same way discussed in q2.
Making the key length to be equal to the message length.
Convert the text message to ASCII characters and then to binary string representation. 8 bits for each character.
For encryption, take XOR of the message and key to get encrypted message.
For decryption, again take XOR with the same key to get the decrypted message.
The decrypted message is in binary string format, so take 8 bits at a time and convert them into decimal and then to ASCII.
The message is decrypted in text!