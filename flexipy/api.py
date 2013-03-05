# -*- coding: utf-8 -*-

"""
This module implements the flexipy API.

:copyright: (c) 2012 by Jakub Ječmínek.
:license: BSD, see LICENSE for more details.
"""
from . import main, invoice, bank, address_book

def create_issued_invoice(kod, var_sym, datum_vyst, **kwargs):
	"""Tato funkce vytvori novou vydanou fakturu ve Flexibee 
	:param kod: interni cislo
	:param var_sym: variabilni symbol faktury
	:param datum_vyst: datum vystaveni faktury format datumu(2013-02-28+01:00)
	:param zdroj_pro_sklad: True nebo False zda je zdrojem pro skladove zaznamy 
	:param typ_dokl: mozne hodnoty se nachazi v config.typ_faktury_vydane
	:param dalsi_param:  dalsi nepovinne paramerty viz dokumentace Flexibee
	:param polozky_faktury: polozky fakturz jsou list obsahujici jednotlive polozky
	Returns :tuple skladajici se z (success, result, error_message)
	"""	
	return invoice.create_issued_invoice(kod=kod, var_sym=var_sym, datum_vyst=datum_vyst, **kwargs)

def create_received_invoice(kod, var_sym, cislo_dosle, datum_splat, 
	datum_vyst, **kwargs):
	"""Tato funkce zaznamena novou prijatou fakturu ve Flexibee 
	:param kod: interni cislo
	:param var_sym: variabilni symbol faktury
	:param datum_splat: datum splatnosti faktury format datumu(2013-02-28+01:00)
	:param datum_vyst: datum vystaveni faktury format datumu(2013-02-28+01:00)
	:param zdroj_pro_sklad: True nebo False zda je zdrojem pro skladove zaznamy 
	:param typ_dokl: mozne hodnoty se nachazi v config.typ_faktury_prijate
	:param dalsi_param:  dalsi nepovinne paramerty viz dokumentace Flexibee
	:param polozky_faktury: polozky fakturz jsou list obsahujici jednotlive polozky
	Returns :tuple skladajici se z (success, result, error_message)
	kde success = True/False
	"""	
	return invoice.create_received_invoice(kod=kod, var_sym=var_sym, cislo_dosle=cislo_dosle, datum_splat=datum_splat, 
	datum_vyst=datum_vyst, **kwargs)

def update_issued_invoice(id, invoice):
	return invoice.update_issued_invoice(id, invoice)	


def get_all_issued_invoices(query=None, detail='summary'):
	"""This function obtains all issued invoices form Flexibee. 
	Returns :dictionary that contains all issued invoices.
	"""	
	return invoice.get_all_issued_invoices(query, detail)

def get_all_received_invoices(query=None, detail='summary'):
	return invoice.get_all_received_invoices(query, detail)

def delete_issued_invoice(id):
	invoice.delete_issued_invoice(id)

def delete_received_invoice(id):	
	invoice.delete_received_invoice(id)

def get_issued_invoice(id, detail='summary'):
	return invoice.get_issued_invoice(id, detail)

def get_issued_invoice_by_code(code, detail='summary'):
	return invoice.get_issued_invoice_by_code(code, detail)

def get_received_invoice(id, detail='summary'):
	return invoice.get_received_invoice(id, detail)	

def get_received_invoice_by_code(code, detail='summary'):
	return invoice.get_received_invoice_by_code(code, detail)	

def create_address_book_item(address_item):
	return address_book.create_address_book_item(address_item)
	

def get_all_bank_items(query=None, detail='summary'):
	"""This function obtains all bank items form Flexibee. 
	Returns :dictionary that contains all bank items.
	"""	
	return bank.get_all_bank_items(query, detail)

def get_bank_item(id, detail='summary'):
	return bank.get_bank_item(id, detail)

def get_banka_by_code(code, detail='summary'):
	return bank.get_banka_by_code(code, detail)		
	

def get_address_book_item(id, detail='summary'):
	return main.get_address_book_item(id, detail)		

def get_address_book_by_code(code, detail='summary'):
	return main.get_address_book_by_code(code, detail)


def get_template_dict(evidence, complete=False):
	return main.get_template_dict(evidence, complete)
