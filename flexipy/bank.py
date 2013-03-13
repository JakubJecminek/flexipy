# -*- coding: utf-8 -*-

import requests
import json
import config
from main import FlexipyException, __create_evidence_item, __delete_item,\
__update_evidence_item, __get_all_records, __get_evidence_item, __get_evidence_item_by_code,\
__validate_params

def create_bank_doklad(kod, dat_vyst, typ_dokl=config.typ_bank_dokladu[0], typ_pohybu=config.typ_pohybu[0], 
	bank_ucet=config.bankovni_ucet[0], dalsi_param=None):
	"""Funkce vytvori novy bankovni doklad.
	:param kod: cislo dokladu
	:param dat_vyst: datum vystaveni
	:param typ_dokl: typ bankovniho dokladu moznosti jsou definovany v configu
	:param bank_ucet: ucet uvedeny v dokladu(moznosti v konfigu) 	
	"""
	typ_dokl = 'code:'+typ_dokl 
	bank_ucet = 'code:'+bank_ucet
	b_item = {'kod': kod, 'datVyst': datum_vyst, 'typDokl': typ_dokl, 'typPohybuK': typ_pohybu, 'banka':bank_ucet}
	if dalsi_param != None:
		__validate_params(dalsi_param, 'banka')
		for k,v in dalsi_param.iteritems():
			b_item[k] = v
	return __create_evidence_item('banka',b_item)


def get_all_bank_doklady(query=None, detail='summary'):
	"""Funkce vrati vsechny bankovni doklady z Flexibee.
	:param query: Pokud je uveden dotaz ve formatu jaky podporuje 
	Flexibee(viz dokumentace), vrati vyfiltrovane zaznamy na zaklade 
	dotazu.
	"""
	d = __get_all_records('banka', query, detail)
	return d

def get_bank_doklad(id, detail='summary'):
	return __get_evidence_item(id, 'banka', detail)

def get_bank_doklad_by_code(code, detail='summary'):
	return __get_evidence_item_by_code(code, 'banka', detail)		

def delete_bank_doklad(id):
	__delete_item(id, 'banka')

def update_bank_doklad(id, bank_item):
	"""Tato funkce provede update hodnot bankovniho dokladu ve Flexibee.
	Pro ukazku pouziti viz dokuentace
	Returns :tuple skladajici se z (success, result, error_message)
	:param: id: id zaznamu ktery bude zmenen
	:param bank_item: dictionary obsahujici zmeny
	"""
	return __update_evidence_item(id, 'banka', bank_item)	