# -*- coding: utf-8 -*-

"""
This module implements the flexipy API.

:copyright: (c) 2012 by Jakub Ječmínek.
:license: BSD, see LICENSE for more details.
"""
from . import main, invoice, bank, address_book

def create_vydana_faktura(kod, var_sym, datum_vyst, **kwargs):
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
	return invoice.create_vydana_faktura(kod=kod, var_sym=var_sym, datum_vyst=datum_vyst, **kwargs)

def create_prijata_faktura(kod, var_sym, cislo_dosle, datum_splat, 
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
	return invoice.create_prijata_faktura(kod=kod, var_sym=var_sym, cislo_dosle=cislo_dosle, datum_splat=datum_splat, 
	datum_vyst=datum_vyst, **kwargs)

def create_bank_doklad(kod, dat_vyst, **kwargs):
	return bank.create_bank_doklad(kod=kod, dat_vyst=dat_vyst, **kwargs)	

def create_adresar(kod, nazev, dalsi_param=None):
	return address_book.create_adresar(kod, nazev, dalsi_param)	

def get_all_vydane_faktury(query=None, detail='summary'):
	"""This function obtains all issued invoices form Flexibee. 
	Returns :dictionary that contains all issued invoices.
	"""	
	return invoice.get_all_vydane_faktury(query, detail)

def get_all_prijate_faktury(query=None, detail='summary'):
	return invoice.get_all_prijate_faktury(query, detail)

def get_vydana_faktura(id, detail='summary'):
	return invoice.get_vydana_faktura(id, detail)

def get_vydana_faktura_by_code(code, detail='summary'):
	return invoice.get_vydana_faktura_by_code(code, detail)

def get_prijata_faktura(id, detail='summary'):
	return invoice.get_prijata_faktura(id, detail)	

def get_prijata_faktura_by_code(code, detail='summary'):
	return invoice.get_prijata_faktura_by_code(code, detail)		

def get_all_bank_doklady(query=None, detail='summary'):
	"""This function obtains all bank items form Flexibee. 
	Returns :dictionary that contains all bank items.
	"""	
	return bank.get_all_bank_doklady(query, detail)

def get_bank_doklad(id, detail='summary'):
	return bank.get_bank_doklad(id, detail)

def get_bank_doklad_by_code(code, detail='summary'):
	return bank.get_bank_doklad_by_code(code, detail)			

def get_adresar(id, detail='summary'):
	return main.get_adresar(id, detail)		

def get_adresar_by_code(code, detail='summary'):
	return main.get_adresar_by_code(code, detail)

def get_template_dict(evidence, complete=False):
	return main.get_template_dict(evidence, complete)

def delete_adresar(id):
	address_book.delete_adresar(id)	

def delete_bank_doklad(id):
	bank.delete_bank_doklad(id)

def delete_vydana_faktura(id):
	invoice.delete_vydana_faktura(id)

def delete_prijata_faktura(id):	
	invoice.delete_prijata_faktura(id)

def update_vydana_faktura(id, invoice):
	return invoice.update_vydana_faktura(id, invoice)	

def update_prijata_faktura(id, invoice):
	return invoice.update_prijata_faktura(id, invoice)	

def update_bank_doklad(id, bank_item):
	return bank.update_bank_doklad(id, bank_item)	