from distutils.core import setup, Extension

module = Extension('lookup3',
                    define_macros = [('MAJOR_VERSION', '0'),
                                     ('MINOR_VERSION', '1')],
                    include_dirs = ['lib/'],
                    sources = ['lib/lookup3.c', 'src/py-lookup3.c'])

setup (name = 'py-lookup3',
       version = '0.1',
       description = 'Python bindings for fast hashing with lookup3',
       author = 'Siavash Ghorbani',
       author_email = 'siavashg@gmail.com',
       url = 'https://github.com/siavashg/py-lookup3',
       long_description = 'Python bindings for fast hashing with lookup3',
       ext_modules = [module])
