# -*- coding: utf-8 -*-

import requests
import json
import config
from main import FlexipyException, __create_evidence_item, __delete_item, __update_evidence_item, __get_all_records, __get_evidence_item,\
__get_evidence_item_by_code, __validate_params

def get_all_issued_invoices(query=None, detail='summary'):
	"""Funkce vrati vsechny vydane faktury z Flexibee.
	:param query: Pokud je uveden dotaz ve formatu jaky podporuje 
	Flexibee(viz dokumentace), vrati vyfiltrovane zaznamy na zaklade 
	dotazu.
	"""
	d = __get_all_records('faktura-vydana', query, detail)
	return d

def get_all_received_invoices(query=None, detail='summary'):
	"""Funkce vrati vsechny prijate faktury z Flexibee.
	:param query: Pokud je uveden dotaz ve formatu jaky podporuje 
	Flexibee(viz dokumentace), vrati vyfiltrovane zaznamy na zaklade 
	dotazu.
	"""
	d = __get_all_records('faktura-prijata', query, detail)
	return d


def create_issued_invoice(kod, var_sym, datum_vyst, zdroj_pro_sklad=False, 
	typ_dokl=config.typ_faktury_vydane[0], dalsi_param=None, polozky_faktury=None):
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
	#doplneni vyzadovano flexibee
	typ_dokl = 'code:'+typ_dokl 
	invoice = {'kod':kod, 'varSym':var_sym, 'datVyst':datum_vyst,'zdrojProSkl':zdroj_pro_sklad, 'typDokl':typ_dokl}
	if dalsi_param != None:
		__validate_params(dalsi_param, 'faktura-vydana')
		for k,v in dalsi_param.iteritems():
			invoice[k] = v			
	if polozky_faktury != None:		
		invoice['bezPolozek'] = False
		inv_items = []
		for it in polozky_faktury:
			inv_items.append(it)
		invoice['polozkyFaktury']= inv_items
	return __create_evidence_item('faktura-vydana',invoice)
	

def create_received_invoice(kod, var_sym, cislo_dosle, datum_splat, 
	datum_vyst, zdroj_pro_sklad=False, typ_dokl=config.typ_faktury_prijate[0], 
	dalsi_param=None, polozky_faktury=None):
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
	typ_dokl = 'code:'+typ_dokl 
	invoice = {'datSplat': datum_splat, 'kod': kod, 'zdrojProSkl': zdroj_pro_sklad, 'datVyst': datum_vyst, 'varSym': var_sym, 'cisDosle': cislo_dosle, 'typDokl': typ_dokl}
	if dalsi_param != None:
		__validate_params(dalsi_param, 'faktura-prijata')
		for k,v in dalsi_param.iteritems():
			invoice[k] = v			
	if polozky_faktury != None:		
		invoice['bezPolozek'] = False
		inv_items = []
		for it in polozky_faktury:
			inv_items.append(it)
		invoice['polozkyFaktury']= inv_items
	return __create_evidence_item('faktura-prijata',invoice)
	

def update_issued_invoice(id, invoice):
	"""This function update issued invoice that is already in the Flexibee.
	For usage example see documentation.
	Returns :tuple consisting of (success, result, error_message)
	:param: id: id of invoice which you want to change
	:param invoice: dictionary that contains changed data
	"""
	return __update_evidence_item(id, 'faktura-vydana', invoice)

def delete_issued_invoice(id):
	"""Delete issued invoice specifeid by id.
	:param id: identifies invoice	
	"""
	__delete_item(id, 'faktura-vydana')

def delete_received_invoice(id):
	"""Delete received invoice specifeid by id
	:param id: identifies invoice	
	"""
	__delete_item(id, 'faktura-prijata')	

def get_issued_invoice(id, detail='summary'):
	return __get_evidence_item(id, 'faktura-vydana', detail)

def get_issued_invoice_by_code(code, detail='summary'):
	return __get_evidence_item_by_code(code, 'faktura-vydana', detail)
		
def get_received_invoice(id, detail='summary'):
	return __get_evidence_item(id, 'faktura-prijata', detail)

def get_received_invoice_by_code(code, detail='summary'):
	return __get_evidence_item_by_code(code, 'faktura-prijata', detail)		
