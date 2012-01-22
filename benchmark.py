import sys
import timeit
import uuid

versions = {
    'lookup3': """\
        import lookup3
        for str in strings:
            x = lookup3.hashlittle(str)
    """,
    'md5': """\
        import hashlib
        for str in strings:
            a = hashlib.md5(str).hexdigest()
    """,
    'sha1': """\
        import hashlib
        for str in strings:
            a = hashlib.sha1(str).hexdigest()
    """,
}

def run(version, times=1000):
    bench = timeit.Timer(versions[version],
         "from __main__ import get_strings; strings = get_strings(%d)" % times)
    print 'Ran %s %s times in %s' % (version, times,
                                     bench.timeit(number=times))

def get_strings(times):
    strings = []
    for i in xrange(times):
        strings.append(uuid.uuid4().hex)
    return strings

def main():
    try:
        times = int(sys.argv[1])
    except (IndexError, ValueError):
        times = 1000

    run('sha1', times)
    run('md5', times)
    run('lookup3', times)

if __name__ == '__main__':
    main()
