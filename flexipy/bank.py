# -*- coding: utf-8 -*-

import requests
import json
from .exceptions import FlexipyException
from main import Flexipy
from config import Config

class Banka(Flexipy):

	def __init__(self, conf=Config()):
		Flexipy.__init__(self, config=conf)

	def create_bank_doklad(self, kod, datum_vyst, typ_dokl=None, typ_pohybu=None, 
		bank_ucet=None, dalsi_param=None):
		"""Metoda vytvori novy bankovni doklad.
		:param kod: cislo dokladu
		:param dat_vyst: datum vystaveni
		:param typ_dokl: typ bankovniho dokladu moznosti jsou definovany v configu
		:param bank_ucet: ucet uvedeny v dokladu(moznosti v konfigu) 	
		"""
		if typ_dokl == None:
			typ_dokl = self.conf.get_typ_bank_dokladu()[0]			
		typ_dokl = 'code:'+typ_dokl 
		if typ_pohybu == None:
			typ_pohybu = self.conf.get_typ_pohybu()[0]
		if bank_ucet == None:
			bank_ucet = self.conf.get_bankovni_ucty()[0]	
		bank_ucet = 'code:'+bank_ucet
		b_item = {'kod': kod, 'datVyst': datum_vyst, 'typDokl': typ_dokl, 'typPohybuK': typ_pohybu, 'banka':bank_ucet}
		if dalsi_param != None:
			self.validate_params(dalsi_param, 'banka')
			for k,v in dalsi_param.iteritems():
				b_item[k] = v
		return self.create_evidence_item('banka',b_item)


	def get_all_bank_doklady(self, query=None, detail='summary'):
		"""Metoda vrati vsechny bankovni doklady z Flexibee.
		:param query: Pokud je uveden dotaz ve formatu jaky podporuje 
		Flexibee(viz dokumentace), vrati vyfiltrovane zaznamy na zaklade 
		dotazu.
		"""
		d = self.get_all_records('banka', query, detail)
		return d

	def get_bank_doklad(self, id, detail='summary'):
		return self.get_evidence_item(id, 'banka', detail)

	def get_bank_doklad_by_code(self, code, detail='summary'):
		return self.get_evidence_item_by_code(str(code), 'banka', detail)		

	def delete_bank_doklad(self, id):
		self.delete_item(id, 'banka')

	def update_bank_doklad(self, id, bank_item):
		"""Tato metoda provede update hodnot bankovniho dokladu ve Flexibee.
		Pro ukazku pouziti viz dokuentace
		Returns :tuple skladajici se z (success, result, error_message)
		:param: id: id zaznamu ktery bude zmenen
		:param bank_item: dictionary obsahujici zmeny
		"""
		return self.update_evidence_item(id, 'banka', bank_item)	