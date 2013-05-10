# -*- coding: utf-8 -*-

from flexipy.main import Flexipy
from flexipy import config
from flexipy import Faktura
from flexipy.exceptions import FlexipyException
import requests
import pytest
import json

class TestFlexipy:


	def setup(self):
		#use testing config
		self.conf = config.TestingConfig()
		server_settings = self.conf.get_server_config()
		self.username = str(server_settings['username'])
		self.password = str(server_settings['password'])
		self.url = str(server_settings['url'])
		self.flexipy = Flexipy(self.conf)
		self.faktura = Faktura(self.conf)
		#create some items in flexibee
		self.faktura.create_vydana_faktura(kod='flex11', var_sym='11235484', datum_vyst='2013-02-28', zdroj_pro_sklad=False)
		dalsiParams = {'specSym':48152342}
		#tyto dve jsou pro testovani get all records
		self.faktura.create_vydana_faktura(kod='flex12', var_sym='11235494', datum_vyst='2013-03-14', zdroj_pro_sklad=False,dalsi_param=dalsiParams)
		self.faktura.create_vydana_faktura(kod='flex13', var_sym='11235495', datum_vyst='2013-02-17', zdroj_pro_sklad=False,dalsi_param=dalsiParams)

	def teardown(self):
		inv1 = self.faktura.get_vydana_faktura_by_code('flex11')
		inv2 = self.faktura.get_vydana_faktura_by_code('flex12')
		inv3 = self.faktura.get_vydana_faktura_by_code('flex13')
		self.faktura.delete_vydana_faktura(inv1['id'])
		self.faktura.delete_vydana_faktura(inv2['id'])
		self.faktura.delete_vydana_faktura(inv3['id'])

	def test_validate_item(self):	
		invalid_params = {'doprava':'','duzpaPuv':'','zaveTxt':''}	
		pytest.raises(FlexipyException,self.flexipy.validate_params, invalid_params, 'faktura-vydana') 

	def test_get_template_dict(self):
		expected_result = {u'kod': '', u'nazev': ''}
		assert expected_result == self.flexipy.get_template_dict('adresar')

	def test_send_request(self):		
		expected_resp = requests.get(url=self.url+'faktura-vydana.json',auth=(self.username,self.password),verify=False)
		actual_resp = self.flexipy.send_request(method='get', endUrl='faktura-vydana.json')
		assert expected_resp.status_code == actual_resp.status_code
		assert expected_resp.json() == actual_resp.json()

	def test_prepare_date(self):
		data = {'kod':'inv1','nazev':'mojeFaktura'}
		expected_result = json.dumps({'winstrom':{'faktura-vydana':[data]}})
		actual_result = self.flexipy.prepare_data('faktura-vydana', data)
		assert expected_result == actual_result

	def test_get_all_records_without_query(self):
		r = requests.get(self.url+'faktura-vydana.json',auth=(self.username,self.password),verify=False)
		expected_result = r.json()['winstrom']['faktura-vydana']
		actual_result = self.flexipy.get_all_records('faktura-vydana')
		assert expected_result == actual_result

	def test_get_all_records_with_query(self):
		#get all records with specSym = 48152342
		url = self.url+'faktura-vydana/(specSym="48152342").json'
		r = requests.get(url=url,auth=(self.username,self.password),verify=False)
		expected_result = r.json()['winstrom']['faktura-vydana']
		actual_result = self.flexipy.get_all_records('faktura-vydana',query="specSym='"+str(48152342)+"'")
		assert len(expected_result) == len(actual_result)
		assert expected_result == actual_result

	def test_get_evidence_property_list(self):
		pass