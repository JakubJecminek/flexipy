# -*- coding: utf-8 -*-

"""
This module implements the flexipy API.

:copyright: (c) 2012 by Jakub Ječmínek.
:license: BSD, see LICENSE for more details.
"""
from . import main

def create_issued_invoice(invoice, invoice_items):
	"""This function creates new issued invoice in Flexibee. 
	Returns :tuple consisting of (success, result, error_message)
	where success = True/False
	result = id of invoice in FLexibee or None if success = False
	error_message = List of error messages if success=False else error_message=None
	:param invoice: dictionary that contains data for new invoice. The schema of invoice is 
	in models.FakturaVydana. 
	:param invoice_items: list of invoice items(every inv. item is dictionary). Schema of invoice item 
	is in models.FakturaVydanaPolozka
	"""	
	return main.create_issued_invoice(invoice, invoice_items)

def create_received_invoice(invoice, invoice_items):
	"""This function creates new issued invoice in Flexibee. 
	Returns :tuple consisting of (success, result, error_message)
	where success = True/False
	result = id of invoice in FLexibee or None if success = False
	error_message = Error message if success=False else error_message=None
	:param invoice: dictionary that contains data for new invoice. The schema of invoice is 
	in models.FakturaVydana. 
	:param invoice_items: list of invoice items(every inv. item is dictionary). Schema of invoice item 
	is in models.FakturaVydanaPolozka 
	"""	
	return main.create_received_invoice(invoice, invoice_items)

def get_all_bank_items():
	return main.get_all_bank_items()

def get_all_issued_invoices():
	return main.get_all_issued_invoices()

def get_all_received_invoices():
	return main.get_all_received_invoices()

def delete_issued_invoice(id):
	main.delete_issued_invoice(id)

def delete_received_invoice(id):	
	main.delete_received_invoice(id)

def get_issued_invoice(id):
	return main.get_issued_invoice(id)

def get_received_invoice(id):
	return main.get_received_invoice(id)		