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


def main():
    seed = input('Enter the seed in binary number system: ')

    # or instead u can ask to input message here
    msg_bits = input('Input random message binary bits to see how PRF is working: ')

    if len(seed) <= 1:
        print('The seed length should be greater than 1')
        sys.exit(1)

    answer = prf(seed,msg_bits)
    print('The generated bit string(viz used as encryption key) is: ',answer)


if __name__ == '__main__':
    main()

