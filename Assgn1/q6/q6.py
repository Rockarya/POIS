generator = 7919
modulus = 9223372036854775783

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


def main():
    n = int(input('Enter n in range:[4,64]: '))
    q = find_q(n)
    x1 = int(input('Enter x1 and length should be in range:[1,{}]: '.format(q)))
    x2 = int(input('Enter x2 and length should be in range:[1,{}]: '.format(q)))

    hashed_value = hash(n,x1,x2,q)
    x1_bin = bin(x1).replace('0b','')
    x2_bin = bin(x2).replace('0b','')

    print('original length: {} \nhashed length: {}'.format(len(x1_bin)+len(x2_bin),len(hashed_value)))

if __name__ == '__main__':
    main()