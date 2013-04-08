# -*- coding: utf-8 -*-

import requests
import json
from .exceptions import FlexipyException
from main import __create_evidence_item, __delete_item, __update_evidence_item,\
__get_all_records, __get_evidence_item, __get_evidence_item_by_code
try:	
	import config
except ImportError:
	raise FlexipyException("Pred samotnym pouzitim knihovny musite vytvorit config - viz docs.")

def get_adresar(id, detail='summary'):
	return __get_evidence_item(id, 'adresar', detail)

def get_adresar_by_code(code, detail='summary'):
	return __get_evidence_item_by_code(code, 'adresar', detail)			

def update_adresar(id, adresar):
	"""
	Tato funkce slouzi k udpatovani obsahu polozky v adresari
	viz dokumentace
	:param id: id polozky
	:parma adresar: dictionary obsahujici zmenene polozky adresare	
	:return tuple obsahujici (success, result, error_message)
	"""
	return main.__update_evidence_item(id, 'adresar', adresar)

def delete_adresar(id):
	__delete_item(id, 'adresar')		

def create_adresar(kod, nazev, dalsi_param=None):
	"""Vytvori novy kontakt v adresari Flexibee. Definice evidence se 
	nachazi zde:
	http://demo.flexibee.eu/c/demo/adresar/properties
	:param kod: kod adresare
	:param dalsi_param: dalsi nepovinne parametry
	"""	
	return __create_evidence_item('adresar',address_item)

def create_adresar_bank_ucet(firma, cislo_uctu, kod_banky, dalsi_parametry=None):
	"""Vytvori pro firmu v adresari bankovni spojeni.
	:param firma: kod firmy pro kterou vytvarime bankovni spojeni
	:param cislo_uctu: cislo bankovniho uctu
	:param kod_banky: code banky 
	:dalsi_parametry: dalsi mozne parametry viz dokumentace
	"""
	#TODO#
	return __create_evidence_item('adresar-bankovni-ucet')	