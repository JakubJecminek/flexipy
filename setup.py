from setuptools import setup

setup(
    name='flexipy',
    version='0.3.1',
    description='A library for communication with accounting system Flexibee.',
    packages=['flexipy'],
    license='BSD',
    author='Jakub Jecminek',
    author_email='jecmijak@gmail.com',
    keywords='flexibee accounting invoices',
    url='https://www.assembla.com/code/flexipy/git/nodes',
    include_package_data=True,
    package_data={'flexipy':['flexipy.conf']},
    install_requires=(
         'setuptools>=0.6b1',
         'Paver==1.0.5',
         'requests',
     ),
)
