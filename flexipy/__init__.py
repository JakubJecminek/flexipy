# -*- coding: utf-8 -*-

"""
Knihovna flexipy pro snadnou praci s REST API systemu Flexibee.
Ukazka pouziti:
>>>> import flexipy
>>>> flexipy.create_invoice(data)
it will return tuple consisting of (success, result, error_message)
where success = Tre/False
result = id of invoice in FLexibee
error_message = Error message if success=False else erorr_message=''

The other functions are supported - see `flexipy.api`. Full documentation
is at <TODO>.

:copyright: (c) 2012 Jakub Ječmínek.
:license: BSD, soubor LICENSE obsahuje kopii license.
"""
from .api import create_issued_invoice, get_all_bank_items, get_all_issued_invoices, \
get_all_received_invoices, create_received_invoice, delete_issued_invoice, \
delete_received_invoice, get_issued_invoice, get_received_invoice,\
get_template_dict, create_address_book_item,\
get_address_book_item, update_issued_invoice, __initialize_config_file,\
get_bank_item, get_banka_by_code, get_address_book_by_code, get_received_invoice_by_code,\
get_issued_invoice_by_code


#tato funkce se vola pouze pri importovani knihovny flexipy,
#inicializuje nektere poloyky typu relation primo z Flexibee
__initialize_config_file()

