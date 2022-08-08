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


def Verify(sender_tag,receiver_tag):
    if sender_tag == receiver_tag:
        return 'Accept'
    else:
        return 'Reject'


def main():
    seed = input('Enter the seed in binary number system: ')
    sender_msg = input('Enter the message to be encrypted: ')
    sender_msg_binary = "".join(format(ord(i),'0b').zfill(8) for i in sender_msg)
    
    # as per argument the key length should be 2n
    if len(sender_msg_binary) < 2*len(seed):
        print('Key length exceeds the message length')
        sys.exit(1)

    # the MAC tag
    sender_tag = prf(seed,sender_msg_binary)
    print('The sender\'s tag is: ',sender_tag)

    # u can write the receiver msg as your convineince. For now it's equal to sender's msg
    receiver_msg_binary = sender_msg_binary
    receiver_tag = prf(seed,receiver_msg_binary)
    print('The receiver\'s tag is: ',receiver_tag)

    verdict = Verify(sender_tag,receiver_tag)
    print('The verdict of tag matching is: ',verdict)

if __name__ == '__main__':
    main()

