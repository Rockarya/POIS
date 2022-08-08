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


def main():
    seed = input('Enter the seed in binary number system: ')
    msg = input('Enter the message to be encrypted: ')
    binary_msg = "".join(format(ord(i),'0b').zfill(8) for i in msg)

    # as per argument the key length should be 2n
    if len(binary_msg) < 2*len(seed):
        print('Key length exceeds the message length')
        sys.exit(1)

    key = prf(seed,binary_msg)
    # making key and msg of equal lengths
    key = key.zfill(len(binary_msg))
    encrypted_msg = encryption(binary_msg,key)
    print('Encrypted Message is: ',encrypted_msg)
    decrypted_msg = decryption(encrypted_msg,key)
    print('Decrypted Message is: ',decrypted_msg)


if __name__ == '__main__':
    main()

