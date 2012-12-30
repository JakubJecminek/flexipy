VERSION = (0, 0, 1)

__version__ = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

"""
flexipy library for working with REST API of accounting ststem FLexibee
Basic usage:
>>>> import flexipy
>>>> flexipy.create_invoice(data)
it will return tuple consisting of (success, result, error_message)
where success = Tre/False
result = id of invoice in FLexibee
error_message = Error message if success=False else erorr_message=''

The other functions are supported - see `flexipy.api`. Full documentation
is at <TODO>.

:copyright: (c) 2012 by Jakub Ječmínek.
:license: BSD, see LICENSE for more details.
"""
from .api import 
