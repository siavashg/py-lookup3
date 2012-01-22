A hash function for hash table lookup that is faster and more thorough than 
the one you are using now.

Install:
python setup.py install

Usage:
import lookup3
hash = lookup3.hashlittle('String to hash')

Benchmark:
Ran sha1 1000 times in 2.52090787888
Ran md5 1000 times in 2.30922293663
Ran lookup3 1000 times in 0.572417974472
