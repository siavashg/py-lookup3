##py-lookup3##
Python bindings for lookup3 ("A hash function for hash table lookup that is faster and more thorough than 
the one you are using now.").

**Install:**

    python setup.py install

**Usage:**

    import lookup3
    hash = lookup3.hashlittle('String to hash')`

**Benchmark:**

    python benchmark.py
    Ran md5 1000 times in 2.27848410606
    Ran lookup3 1000 times in 0.56174492836
    Ran murmur3 1000 times in 0.399135112762
    Ran python 1000 times in 0.208546161652