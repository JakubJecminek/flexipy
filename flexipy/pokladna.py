# -*- coding: utf-8 -*-

from .exceptions import FlexipyException
from main import Flexipy
from config import Config

class Pokladna(Flexipy):

	def __init__(self, conf=Config()):
		Flexipy.__init__(self, config=conf)

	def get_all_pokladni_doklady(self, query=None, detail='summary'):
		d = self.get_all_records('pokladni-pohyb', query, detail)		
		return d

	def delete_pokladni_doklad(self, id):
		"""Smaze vydanou fakturu podle id.
		:param id: id faktury	
		"""
		self.delete_item(id, 'pokladni-pohyb')

	def create_pokladni_doklad(self, kod, datum_vyst, typ_pohybu=None, typ_dokl=None, zdroj_pro_sklad=False, typ_pokladna=None):
		if typ_dokl == None:
			typ_dokl = self.conf.get_typ_bank_dokladu()[0]
		typ_dokl = 'code:'+typ_dokl 	
		if typ_pohybu == None:
			typ_pohybu = self.conf.get_typ_pokladni_pohyb()[0]
		if typ_pokladna == None:
			typ_pokladna = self.conf.get_typ_pokladna()[0]
		typ_pokladna = 'code:'+typ_pokladna 	
		datum_vyst += '+01:00'
		
