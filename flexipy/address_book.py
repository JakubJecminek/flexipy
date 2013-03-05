# -*- coding: utf-8 -*-

import requests
import json
import config
from main import FlexipyException, __create_evidence_item, __delete_item, __update_evidence_item, __get_all_records, __get_evidence_item,\
__get_evidence_item_by_code

def get_address_book_item(id, detail='summary'):
	return __get_evidence_item(id, 'adresar', detail)

def get_address_book_by_code(code, detail='summary'):
	return __get_evidence_item_by_code(code, 'adresar', detail)			

def create_address_book_item(address_item):
	"""Creates new contact in address book, can be good for suppliers and
	subscribers. Definition of all fields is here 
	http://demo.flexibee.eu/c/demo/adresar/properties
	"""	
	return __create_evidence_item('adresar',address_item)

def create_address_book_bank_account(firma, cislo_uctu, kod_banky, dalsi_parametry):
	"""Vytvori pro firmu v adresari bankovni spojeni.
	:param firma: kod firmy
	:dalsi_parametry: dalsi mozne parametry viz dokumentace
	"""
	return __create_evidence_item('adresar-bankovni-uce')	