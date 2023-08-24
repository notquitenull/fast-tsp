import sys
import os
import io

try:
    from skbuild import setup
except ImportError:
    print(
        'Please update pip, you need pip 10 or greater,\n'
        ' or you need to install the PEP 518 requirements in pyproject.toml yourself',
        file=sys.stderr,
    )
    raise

from setuptools import find_packages

DIR = os.path.abspath(os.path.dirname(__file__))
DESCRIPTION = "A fork from shmulvad's fast TSP solver with Python bindings, which also accepts a list of 2D points as an input."

# Import the README and use it as the long-description.
try:
    with io.open(os.path.join(DIR, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


setup(
    name='fast_tsp',
    version='0.1.2.5',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Søren Mulvad',
    author_email='shmulvad@gmail.com',
    url='http://github.com/shmulvad/fast-tsp',
    license='MIT',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    cmake_install_dir='src/fast_tsp',
    package_data={'src': ['py.typed']},
    include_package_data=True,
    python_requires='>=3.8',
    install_requires=['numpy>=1.0.0'],
    extras_require={
        'test': ['pytest', 'numpy'],
        'docs': ['sphinx', 'sphinx-rtd-theme', 'sphinx-autodoc-typehints'],
    },
)
