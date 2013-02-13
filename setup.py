from setuptools import setup

setup(
    name='flexipy',
    version=0.1,
    description='A library for communication with accounting system Flexibee',
    packages=['flexipy'],
    license='BSD',
    url='',
    include_package_data=True,

    install_requires=(
         'setuptools>=0.6b1',
         'Paver==1.0.5',
         'requests',
     ),
)
