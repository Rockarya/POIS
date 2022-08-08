Using collsion resistant hash fuctions to build H-MAC's

Take n, encryption_seed, authentication_seed, sender_message as input.

Algorithm:
Generate authentication key from authentication_seed.
Take XOR of key and ipad and pass this value as one argument in hash function whose another would be IV.
Run MDT fuction, the value is val1
Take XOR of key and opad and pass this value as one argument in hash function whose another would be IV. This value is val2
Pass val1 and val2 in hash function, and this generated bit string is our HMAC tag.
Similarly generate HMAC tag for receiver's output and pass the tags to the Verify function.
If the verdict of the Verify function is 'Accept', then decrypt the message otherwise output ⊥.