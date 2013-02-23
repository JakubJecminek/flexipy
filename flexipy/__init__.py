# -*- coding: utf-8 -*-

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
from .api import create_issued_invoice, get_all_bank_items, get_all_issued_invoices, \
get_all_received_invoices, create_received_invoice, delete_issued_invoice, \
delete_received_invoice, get_issued_invoice, get_received_invoice,\
get_template_dict, create_address_book_item,\
get_address_book_item, update_issued_invoice


