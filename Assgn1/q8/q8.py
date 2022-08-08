import math
import sys

generator = 7919
modulus = 9223372036854775783
opad = 54
ipad = 92


n_to_prime = {4: 7,
 5: 13,
 6: 31,
 7: 61,
 8: 127,
 9: 251,
 10: 509,
 11: 1021,
 12: 2039,
 13: 4093,
 14: 8191,
 15: 16381,
 16: 32749,
 17: 65521,
 18: 131071,
 19: 262139,
 20: 524287,
 21: 1048573,
 22: 2097143,
 23: 4194301,
 24: 8388593,
 25: 16777213,
 26: 33554393,
 27: 67108859,
 28: 134217689,
 29: 268435399,
 30: 536870909,
 31: 1073741789,
 32: 2147483647,
 33: 4294967291,
 34: 8589934583,
 35: 17179869143,
 36: 34359738337,
 37: 68719476731,
 38: 137438953447,
 39: 274877906899,
 40: 549755813881,
 41: 1099511627689,
 42: 2199023255531,
 43: 4398046511093,
 44: 8796093022151,
 45: 17592186044399,
 46: 35184372088777,
 47: 70368744177643,
 48: 140737488355213,
 49: 281474976710597,
 50: 562949953421231,
 51: 1125899906842597,
 52: 2251799813685119,
 53: 4503599627370449,
 54: 9007199254740881,
 55: 18014398509481951,
 56: 36028797018963913,
 57: 72057594037927931,
 58: 144115188075855859,
 59: 288230376151711717,
 60: 576460752303423433,
 61: 1152921504606846883,
 62: 2305843009213693951,
 63: 4611686018427387847,
 64: 9223372036854775783}

def prf(seed,msg_bits):
    n = len(seed)
    for i in range(n):
        str = prg(seed,2*n)
        if msg_bits[i] == '0':
            seed = str[:len(str)//2]
        else:
            seed = str[len(str)//2:]

    return seed

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


def find_q(n):
    global n_to_prime,generator
    p = n_to_prime[n+1]
    G = set()
    i = 1
    while 1:
        val = pow(generator,i,p)
        if val in G:
            break
        G.add(val)
        i += 1

    q = len(G)
    return q


def hash(n,x1,x2,q):
    global n_to_prime,generator
    p = n_to_prime[n+1]
    bin_generator = bin(generator).replace('0b', '')
    str = prg(bin_generator,len(bin_generator))
    val = int(str,2)
    ind = val%q
    h = pow(generator,ind+1,p)
    hashed_val = (pow(generator,x1,p)*pow(h,x2,p))%p
    return bin(hashed_val).replace('0b', '')


def MDT(n,key,x,z0):
    L = len(x)
    # L < pow(2,n)
    if L >= pow(2,n):
        print('The length of x  should be less than 2^n')
        sys.exit(1)

    B = math.ceil(L/n)
    padded_x = ''
    for i in range(n-(L%n)):
        padded_x += '0'
    padded_x += x

    arr_x = []
    for i in range(0,len(padded_x),n):
        arr_x.append(padded_x[i:i+n])

    arr_x.append(bin(L).replace('0b','').zfill(n))

    # finding Z (B+1)
    z = z0
    q = find_q(n)
    for i in range(B+1):
        z = hash(n,int(z,2),int(arr_x[i],2),q)

    return z


def hmac(n,key,msg):
    IV = ''
    for i in range(n):
        IV += '0'

    q = find_q(n)

    ipad_bin = bin(ipad).replace('0b','')
    val1 = ''
    for i in range(max(len(ipad_bin),len(key))):
        if i < len(ipad_bin) and i < len(key):
            if ipad_bin[i]!=key[i]:
                val1 += '1'
            else:
                val1 += '0'
        elif i < len(ipad_bin):
            val1 += ipad_bin[i]
        else:
            val1 += key[i]

    val1 = hash(n,int(val1,2),int(IV,2),q)
    val1 = MDT(n,key,msg,val1)

    opad_bin = bin(opad).replace('0b','')
    val2 = ''
    for i in range(max(len(opad_bin),len(key))):
        if i < len(opad_bin) and i < len(key):
            if opad_bin[i]!=key[i]:
                val2 += '1'
            else:
                val2 += '0'
        elif i < len(opad_bin):
            val2 += opad_bin[i]
        else:
            val2 += key[i]

    val2 = hash(n,int(val2,2),int(IV,2),q)
    hmac_tag = hash(n,int(val1,2),int(val2,2),q)

    return hmac_tag


def Verify(sender_tag,receiver_tag):
    if sender_tag == receiver_tag:
        return 'Accept'
    else:
        return 'Reject'
    


def main():
    n = int(input('Enter n in range:[4,64]: '))
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

    sender_hmac_tag = hmac(n,auth_key,encrypted_msg)

    print('HMAC tag: ',sender_hmac_tag)

    receiver_msg = encrypted_msg
    receiver_hmac_tag = hmac(n,auth_key,receiver_msg)

    verdict = Verify(sender_hmac_tag,receiver_hmac_tag)

    if verdict == 'Accept':
        decrypted_msg = decryption(encrypted_msg,enc_key)
        print('Decrypted Message is: ',decrypted_msg)
    else:
        print('⊥')


if __name__ == '__main__':
    main()