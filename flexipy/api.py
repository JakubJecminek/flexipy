# -*- coding: utf-8 -*-

"""
This module implements the flexipy API.

:copyright: (c) 2012 by Jakub Ječmínek.
:license: BSD, see LICENSE for more details.
"""
from . import main

def create_issued_invoice(data):
	"""This function creates new issued invoice in Flexibee. 
	Returns :tuple consisting of (success, result, error_message)
	where success = True/False
	result = id of invoice in FLexibee or None if success = False
	error_message = List of error messages if success=False else error_message=None
	:param kwargs: dictionary that contains data for new invoice. The schema of invoice is 
	in models.Faktura. 
	"""	
	return main.create_issued_invoice(data)

def create_received_invoice(data):
	"""This function creates new issued invoice in Flexibee. 
	Returns :tuple consisting of (success, result, error_message)
	where success = True/False
	result = id of invoice in FLexibee or None if success = False
	error_message = Error message if success=False else error_message=None
	:param kwargs: dictionary that contains data for new invoice. The schema of invoice is 
	in models.Faktura. 
	"""	
	return main.create_received_invoice(data)

def get_all_bank_items():
	return main.get_all_bank_items()

def get_all_issued_invoices():
	return main.get_all_issued_invoices()

def get_all_received_invoices():
	return main.get_all_received_invoices()

def delete_issued_invoice(id):
	pass

def delete_received_invoice(id):	
	pass