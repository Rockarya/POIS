import sys

modulus = 9223372036854775783
generator = 7919

def prg(seed, new_length):
    seed = int(seed,2)
    new_length = int(new_length)
    global modulus, generator
    ans = ''
    for i in range(new_length):
        seed_length = len(bin(seed)) - 2  #the binary string is padded with 0b so subtract 2 from it
        val = pow(generator,seed,modulus)
        str = bin(val).replace('0b', '').zfill(seed_length)
        ans += str[0]
        seed = int(str[1:],2)
    return ans

def prf(seed,msg_bits):
    n = len(seed)
    for i in range(n):
        str = prg(seed,2*n)
        if msg_bits[i] == '0':
            seed = str[:len(str)//2]
        else:
            seed = str[len(str)//2:]

    return seed


def encryption(msg,key):
    encrypted_msg = ''
    for i in range(len(msg)-1,-1,-1):
        if key[i]!=msg[i]:
            encrypted_msg += '1'
        else:
            encrypted_msg += '0'

    # because we started taking XOR from end in above for loop
    encrypted_msg = "".join(reversed(encrypted_msg))
    return encrypted_msg


def decryption(msg,key):
    # we need to take XOR of the message with the key
    msg = encryption(msg,key)

    decrypted_msg = ''
    for i in range(0,len(msg),8):
        bins = msg[i:i+8]
        decimal = int(bins,2)
        decrypted_msg += chr(decimal)

    return decrypted_msg


def Verify(sender_tag,receiver_tag):
    if sender_tag == receiver_tag:
        return 'Accept'
    else:
        return 'Reject'


def main():
    enc_seed = input('Enter the encryption-decryption seed in binary number system: ')
    auth_seed = input('Enter the authentication seed in binary number system: ')
    sender_msg = input('Enter the message to be encrypted: ')
    sender_msg_binary = "".join(format(ord(i),'0b').zfill(8) for i in sender_msg)

    # as per argument the key length should be 2n
    if (len(sender_msg_binary) < 2*len(enc_seed)) or (len(sender_msg_binary) < 2*len(auth_seed)):
        print('Key length exceeds the message length')
        sys.exit(1)

    enc_key = prf(enc_seed,sender_msg_binary)
    auth_key = prf(auth_seed,sender_msg_binary)

    # making enc_key and msg of equal lengths
    enc_key = enc_key.zfill(len(sender_msg_binary))
    encrypted_msg = encryption(sender_msg_binary,enc_key)
    print('Encrypted Message is: ',encrypted_msg)

    # generating MAC tag -> tag is generated on encrypted msg
    sender_tag = prf(auth_key,encrypted_msg)
    print('The sender\'s tag is: ',sender_tag)

    # u can write the receiver msg as your convineince. For now it's equal to sender's msg
    received_msg = encrypted_msg
    receiver_tag = prf(auth_key,received_msg)
    print('The receiver\'s tag is: ',receiver_tag)

    verdict = Verify(sender_tag,receiver_tag)
    print('The verdict of tag matching is: ',verdict)

    if verdict == 'Accept':
        decrypted_msg = decryption(encrypted_msg,enc_key)
        print('Decrypted Message is: ',decrypted_msg)
    else:
        print('⊥')


if __name__ == '__main__':
    main()

