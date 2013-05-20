# -*- coding: utf-8 -*-

from .exceptions import FlexipyException
from main import Flexipy
from config import Config

class Faktura(Flexipy):

	def __init__(self, conf=Config()):
		Flexipy.__init__(self, config=conf)

	def get_all_vydane_faktury(self, query=None, detail='summary'):
		"""Metoda vrati vsechny vydane faktury z Flexibee.
		:param query: Pokud je uveden dotaz ve formatu jaky podporuje 
		Flexibee(viz dokumentace), vrati vyfiltrovane zaznamy na zaklade 
		dotazu.
		"""
		d = self.get_all_records('faktura-vydana', query, detail)
		return d

	def get_all_prijate_faktury(self, query=None, detail='summary'):
		"""Metoda vrati vsechny prijate faktury z Flexibee.
		:param query: Pokud je uveden dotaz ve formatu jaky podporuje 
		Flexibee(viz dokumentace), vrati vyfiltrovane zaznamy na zaklade 
		dotazu.
		"""
		d = self.get_all_records('faktura-prijata', query, detail)
		return d


	def create_vydana_faktura(self, kod, var_sym, datum_vyst, zdroj_pro_sklad=False, 
		typ_dokl=None, dalsi_param=None, polozky_faktury=None):
		"""Tato metoda vytvori novou vydanou fakturu ve Flexibee 
		:param kod: interni cislo
		:param var_sym: variabilni symbol faktury
		:param datum_vyst: datum vystaveni faktury format datumu(2013-02-28)
		:param zdroj_pro_sklad: True nebo False zda je zdrojem pro skladove zaznamy 
		:param typ_dokl: mozne hodnoty se nachazi v config.typ_faktury_vydane
		:param dalsi_param:  dalsi nepovinne paramerty viz dokumentace Flexibee
		:param polozky_faktury: polozky fakturz jsou list obsahujici jednotlive polozky
		Returns :tuple skladajici se z (success, result, error_message)
		"""	
		#doplneni vyzadovano flexibee
		if typ_dokl == None:
			typ_dokl = self.conf.get_typy_faktury_vydane()[0]
		typ_dokl = 'code:'+typ_dokl 
		#dopleni datumu na pozadovany format
		datum_vyst += '+01:00'
		invoice = {'kod':kod, 'varSym':var_sym, 'datVyst':datum_vyst,'zdrojProSkl':zdroj_pro_sklad, 'typDokl':typ_dokl}
		if dalsi_param != None:
			self.validate_params(dalsi_param, 'faktura-vydana')
			for k,v in dalsi_param.iteritems():
				invoice[k] = v			
		if polozky_faktury != None:		
			invoice['bezPolozek'] = False
			inv_items = []
			for it in polozky_faktury:
				self.validate_params(it, 'faktura-vydana-polozka')
				inv_items.append(it)
			invoice['polozkyFaktury']= inv_items
		return self.create_evidence_item('faktura-vydana',invoice)
		

	def create_prijata_faktura(self, kod, var_sym, cislo_dosle, datum_splat, 
		datum_vyst, zdroj_pro_sklad=False, typ_dokl=None, 
		dalsi_param=None, polozky_faktury=None):
		"""Tato metoda zaznamena novou prijatou fakturu ve Flexibee 
		:param kod: interni cislo
		:param var_sym: variabilni symbol faktury
		:param datum_splat: datum splatnosti faktury format datumu(2013-02-28)
		:param datum_vyst: datum vystaveni faktury format datumu(2013-02-28)
		:param zdroj_pro_sklad: True nebo False zda je zdrojem pro skladove zaznamy 
		:param typ_dokl: mozne hodnoty se nachazi v config.typ_faktury_prijate
		:param dalsi_param:  dalsi nepovinne paramerty viz dokumentace Flexibee
		:param polozky_faktury: polozky fakturz jsou list obsahujici jednotlive polozky
		Returns :tuple skladajici se z (success, result, error_message)
		kde success = True/False
		"""	
		if typ_dokl == None:
			typ_dokl = self.conf.get_typy_faktury_prijate()[0]
		typ_dokl = 'code:'+typ_dokl 
		datum_splat+= '+01:00'
		datum_vyst += '+01:00'
		invoice = {'datSplat': datum_splat, 'kod': kod, 'zdrojProSkl': zdroj_pro_sklad, 'datVyst': datum_vyst, 'varSym': var_sym, 'cisDosle': cislo_dosle, 'typDokl': typ_dokl}
		if dalsi_param != None:
			self.validate_params(dalsi_param, 'faktura-prijata')
			for k,v in dalsi_param.iteritems():
				invoice[k] = v			
		if polozky_faktury != None:		
			#TODO pouzij __validate_params na validaci polozek
			invoice['bezPolozek'] = False
			inv_items = []
			for it in polozky_faktury:
				self.validate_params(it, 'faktura-prijata-polozka')
				inv_items.append(it)
			invoice['polozkyFaktury']= inv_items
		return self.create_evidence_item('faktura-prijata',invoice)
		

	def update_vydana_faktura(self, id, invoice):
		"""Tato metoda slouzi k updatu hodnot vydane faktuy, ktera je jiz
		vedena ve Flexibee.
		Pro ukazku pouziti viz dokumentace.
		Returns :tuple consisting of (success, result, error_message)
		:param: id: id of invoice which you want to change
		:param invoice: dictionary that contains changed data
		"""
		return self.update_evidence_item(id, 'faktura-vydana', invoice)

	def update_prijata_faktura(self, id, invoice):
		return self.update_evidence_item(id, 'faktura-prijata', invoice)

	def delete_vydana_faktura(self, id):
		"""Smaze vydanou fakturu podle id.
		:param id: id faktury	
		"""
		self.delete_item(id, 'faktura-vydana')

	def delete_prijata_faktura(self, id):
		"""Smaze prijatou fakturu podle id.
		:param id: id faktury
		"""
		self.delete_item(id, 'faktura-prijata')	

	def get_vydana_faktura(self, id, detail='summary'):
		return self.get_evidence_item(id, 'faktura-vydana', detail)

	def get_vydana_faktura_by_code(self, code, detail='summary'):
		return self.get_evidence_item_by_code(code, 'faktura-vydana', detail)
			
	def get_prijata_faktura(self, id, detail='summary'):
		return self.get_evidence_item(id, 'faktura-prijata', detail)

	def get_prijata_faktura_by_code(self, code, detail='summary'):
		return self.get_evidence_item_by_code(code, 'faktura-prijata', detail)		

	def __get_faktura_pdf_url(self, faktura_typ, id):
		"""Vraci url odkaz na fakturu ve formatu pdf.
		:param faktura_typ: dve moznosti faktura-prijata, faktura-vydana
		:param id: id faktury
		"""
		server_settings = self.conf.get_server_config()
		url = str(server_settings['url'])
		return url+faktura_typ+'/'+id+'.pdf'

	def get_faktura_vydana_pdf_url(self, id):
		"""Vrati string obsahujici odkaz na pdf vydane faktury.
		:param id: Id vydane faktury
		"""
		return self.get_faktura_pdf_url('faktura-vydana',id)

	def get_faktura_prijata_pdf_url(self, id):
		"""Vrati string obsahujici odkaz na pdf prijate faktury.
		:param id: Id prijate faktury
		"""
		return self.get_faktura_pdf_url('faktura-prijata',id)	


	def get_faktura_vydana_pdf(self, id):
		"""
		Vraci pdf faktury vydane, ktera je ve Flexibee.
		:param id: id vydane faktury
		"""
		return self.get_evidence_pdf('faktura-vydana',id)
