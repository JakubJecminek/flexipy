from setuptools import setup

setup(
    name='flexipy',
    version=0.0.3,
    description='A library for communication with accounting system Flexibee.',
    packages=['flexipy'],
    license='BSD',
    author='Jakub Ječmínek',
    author_email='jecmijak@gmail.com',
    keywords='flexibee accounting invoices',
    url='https://www.assembla.com/spaces/flexipy/wiki',
    include_package_data=True,

    install_requires=(
         'setuptools>=0.6b1',
         'Paver==1.0.5',
         'requests',         
     ),
)
