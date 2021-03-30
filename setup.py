from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

extension = Extension(
    "lwan_demo",
    sources=["src/lwan_demo.pyx"],
    # For Mac OS ?
    # include_dirs=["./vendor/lwan/src/lib/", "./vendor/lwan/src/lib/missing/"],
    include_dirs=["./vendor/lwan/src/lib/"],
    library_dirs=["./vendor/lwan/build/src/lib/"],
    runtime_library_dirs=["./vendor/lwan/build/src/lib/"],
    libraries=["lwan"],
)

setup(ext_modules=cythonize([extension], language_level="3"))
