Provable secure collision resistant hash function using Merkle-Damgard Transform

Take n,key,x as input.

Algorithm:
Let L be the length of x. Padd x with 0's to make L, multiple of n. 
Divide the x into B=ceil(L/n) partitions. They are x1,x2,..
x B+1 = L encoded in binary in n bits.
z0 = IV
compute zi = hash(zi-1,xi) for i = 1,2,...B+1.
output z B+1.