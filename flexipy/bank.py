# -*- coding: utf-8 -*-

import requests
import json
import config
from main import FlexipyException, __create_evidence_item, __delete_item, __update_evidence_item, __get_all_records, __get_evidence_item,\
__get_evidence_item_by_code

def create_bank_item(kod, dat_vyst, typ_dokl=config.typ_bank_dokladu[0], typ_pohybu=config.typ_pohybu[0], bank_ucet=config.bankovni_ucet[0]):
	"""Funkce vytvori novy bankovni doklad.
	:param kod: cislo dokladu
	:param dat_vyst: datum vystaveni
	:param typ_dokl: typ bankovniho dokladu moznosti jsou definovany v configu
	:param bank_ucet: ucet uvedeny v dokladu(moznosti v konfigu) 	
	"""


def get_all_bank_items(query=None, detail='summary'):
	"""Funkce vrati vsechny bankovni doklady z Flexibee.
	:param query: Pokud je uveden dotaz ve formatu jaky podporuje 
	Flexibee(viz dokumentace), vrati vyfiltrovane zaznamy na zaklade 
	dotazu.
	"""
	d = __get_all_records('banka', query, detail)
	return d

def get_bank_item(id, detail='summary'):
	return __get_evidence_item(id, 'banka', detail)

def get_banka_by_code(code, detail='summary'):
	return __get_evidence_item_by_code(code, 'banka', detail)		
