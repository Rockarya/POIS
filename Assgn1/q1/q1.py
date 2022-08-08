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

def main():
    seed = input('Enter the seed in binary number system: ')
    new_length = input('Enter the length of the random number you want to generate: ')
    answer = prg(seed,new_length)
    print('The generated bit string is: ',answer)


if __name__ == '__main__':
    main()

