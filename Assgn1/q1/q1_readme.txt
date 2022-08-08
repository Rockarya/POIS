Code implements the Pseudo Random Generator.
An input seed is taken in binary number system alongwith the number of bits required in generated random number.
G = (generator^seed % mod) is used to genrate the randmo bits, where generator and mod is fixed globally and are both prime numbers.
The value of mod should be high to create more randomness in output.

Algorithm:
Define an empty answer string. Let the seed length be l. If the length of o/p of G is less than l, then padd it with 0's. 
Take the MSB(rightmost) bit of this string and add it in the answer. Update the remaining string as your new seed and again pass it to the generator function.
We need to loop this till the required length(of output) times.
