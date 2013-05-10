# -*- coding: utf-8 -*-

import requests
import json
from .exceptions import FlexipyException
from main import Flexipy
from config import Config


class Adresar(Flexipy):

	def __init__(self, conf=Config()):
		Flexipy.__init__(self, config=conf)

	def get_adresar(self, id, detail='summary'):
		return self.get_evidence_item(id, 'adresar', detail)

	def get_adresar_by_code(self, code, detail='summary'):
		return self.get_evidence_item_by_code(code, 'adresar', detail)			

	def update_adresar(self, id, adresar):
		"""
		Tato metoda slouzi k udpatovani obsahu polozky v adresari
		viz dokumentace
		:param id: id polozky
		:parma adresar: dictionary obsahujici zmenene polozky adresare	
		:return tuple obsahujici (success, result, error_message)
		"""
		return self.update_evidence_item(id, 'adresar', adresar)

	def delete_adresar(self, id):
		self.delete_item(id, 'adresar')		

	def create_adresar(self, kod, nazev, dalsi_param=None):
		"""Vytvori novy kontakt v adresari Flexibee. Definice evidence se 
		nachazi zde:
		http://demo.flexibee.eu/c/demo/adresar/properties
		:param kod: kod adresare
		:param dalsi_param: dalsi nepovinne parametry
		"""	
		return self.create_evidence_item('adresar',address_item)

	def create_adresar_bank_ucet(self, firma, cislo_uctu, kod_banky, dalsi_parametry=None):
		"""Vytvori pro firmu v adresari bankovni spojeni.
		:param firma: kod firmy pro kterou vytvarime bankovni spojeni
		:param cislo_uctu: cislo bankovniho uctu
		:param kod_banky: code banky 
		:dalsi_parametry: dalsi mozne parametry viz dokumentace
		"""
		#TODO#
		return self.create_evidence_item('adresar-bankovni-ucet')	