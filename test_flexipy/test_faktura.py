# -*- coding: utf-8 -*-

from flexipy import Faktura
from flexipy import config
import requests
import json

class TestFaktura:

	def setup(self):
		self.conf = config.TestingConfig()
		server_settings = self.conf.get_server_config()
		self.username = str(server_settings['username'])
		self.password = str(server_settings['password'])
		self.url = str(server_settings['url'])
		self.faktura = Faktura(self.conf)

	def test_get_all_vydane_faktury(self):
		r = requests.get(self.url+'faktura-vydana.json' ,auth=(self.username,self.password), verify=False)
		d = r.json()
		if len(d['winstrom']['faktura-vydana']):
			list_of_invoices_expected = d['winstrom']['faktura-vydana'][0]
		else:
			list_of_invoices_expected = d['winstrom']['faktura-vydana']
		list_of_invoices_actual = self.faktura.get_all_vydane_faktury()
		assert list_of_invoices_expected == list_of_invoices_actual

	def test_get_all_prijate_faktury(self):
		r = requests.get(self.url+'faktura-prijata.json' ,auth=(self.username,self.password), verify=False)
		d = r.json()
		if(len(d['winstrom']['faktura-prijata']) == 1):
			list_of_invoices_expected = d['winstrom']['faktura-prijata'][0]
		else:	
			list_of_invoices_expected = d['winstrom']['faktura-prijata']
		list_of_invoices_actual = self.faktura.get_all_prijate_faktury()
		assert list_of_invoices_expected == list_of_invoices_actual

	def test_create_vydana_faktura(self):
		expected_data = {'kod':'flex11','typDokl':'code:FAKTURA','firma':'code:201','popis':'Flexipy test invoice', 'sumDphZakl':'0.0','bezPolozek':'true', 'varSym':'11235484','zdrojProSkl':'false'}
		dalsi_param = {'popis':'Flexipy test invoice','firma':'code:201'}
		result = self.faktura.create_vydana_faktura(kod='flex11', var_sym='11235484', datum_vyst='2013-02-28', zdroj_pro_sklad=False, typ_dokl=self.conf.get_typy_faktury_vydane()[0], dalsi_param=dalsi_param)
		assert result[0] == True #expected True
		id = result[1]
		actualData = self.faktura.get_vydana_faktura(id, detail='full') 
		assert actualData['kod'].lower() == expected_data['kod'].lower()
		assert actualData['typDokl'] == expected_data['typDokl']
		assert actualData['firma'] == expected_data['firma']
		assert actualData['popis'] == expected_data['popis']
		assert actualData['sumDphZakl'] == expected_data['sumDphZakl']	
		#uklid po sobe
		self.faktura.delete_vydana_faktura(id)

	def test_create_vydana_faktura_polozky(self):
		polozky = [{'typPolozkyK':self.conf.get_typ_polozky_vydane()[0],'zdrojProSkl':False,'nazev':'vypujceni auta','ucetni':True,'cenaMj':'4815.0'}]	
		expected_data = {'kod':'flex12','typDokl':'code:FAKTURA','firma':'code:201','popis':'Flexipy test invoice', 
		'varSym':'11235484','zdrojProSkl':'false','polozkyFaktury':polozky}
		expected_polozky = [{'typPolozkyK':'typPolozky.obecny','zdrojProSkl':'false','nazev':'vypujceni auta','ucetni':'true','cenaMj':'4815.0'}]
		dalsi_param = {'popis':'Flexipy test invoice','firma':'code:201','typUcOp':u'code:TRŽBA SLUŽBY'}
		result = self.faktura.create_vydana_faktura(kod='flex12', var_sym='11235484', datum_vyst='2013-02-28', 
		zdroj_pro_sklad=False, typ_dokl=self.conf.get_typy_faktury_vydane()[0], dalsi_param=dalsi_param, polozky_faktury=polozky)
		assert result[0] == True #expected True
		id = result[1]
		actualData = self.faktura.get_vydana_faktura(id, detail='full') 
		assert actualData['kod'].lower() == expected_data['kod'].lower()
		assert actualData['typDokl'] == expected_data['typDokl']
		assert actualData['firma'] == expected_data['firma']
		assert actualData['popis'] == expected_data['popis']
		#pocet polozek se musi rovnat
		assert len(actualData['polozkyFaktury']) == len(expected_polozky)
		actual_polozky = actualData['polozkyFaktury'][0]
		assert actual_polozky['typPolozkyK'] == expected_polozky[0]['typPolozkyK']
		assert actual_polozky['nazev'] == expected_polozky[0]['nazev']
		assert actual_polozky['cenaMj'] == expected_polozky[0]['cenaMj']
		#uklid po sobe
		self.faktura.delete_vydana_faktura(id)	