Designing CCA-secure encryption scheme

Take the encryption-decryption seed(in binary) and authentication seed(in binary) and text message as input.

Algorithm:
Generate the encryption-decryption key using encryption-decryption seed and authentication key using authentication seed using PRF.
Encrypt the message(as discussed in previous questions) using the enc-dec key.
Generate the MAC tag for the sender using this message and auth key. This is sender's tag
Now generate tag for the reciver's binary message, This is reciver's tag.
Pass both the tags to Verify function. 
If the veridct is 'Accept', then use the enc-dec key to decrypt the message and output the final decrypted text message.
If the verdict is 'Reject', then output '⊥'.
