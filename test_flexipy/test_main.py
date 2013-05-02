# -*- coding: utf-8 -*-

from flexipy import main, config, faktura
import requests
import pytest
import json


def setup_module(self):
	#create some items in flexibee
	faktura.create_vydana_faktura(kod='flex11', var_sym='11235484', datum_vyst='2013-02-28', zdroj_pro_sklad=False)
	dalsiParams = {'specSym':48152342}
	#tyto dve jsou pro testovani get all records
	faktura.create_vydana_faktura(kod='flex12', var_sym='11235494', datum_vyst='2013-03-14', zdroj_pro_sklad=False,dalsi_param=dalsiParams)
	faktura.create_vydana_faktura(kod='flex13', var_sym='11235495', datum_vyst='2013-02-17', zdroj_pro_sklad=False,dalsi_param=dalsiParams)
def teardown_module(self):
	inv1 = faktura.get_vydana_faktura_by_code('flex11')
	inv2 = faktura.get_vydana_faktura_by_code('flex12')
	inv3 = faktura.get_vydana_faktura_by_code('flex13')
	faktura.delete_vydana_faktura(inv1['id'])
	faktura.delete_vydana_faktura(inv2['id'])
	faktura.delete_vydana_faktura(inv3['id'])

def test_validate_item():	
	invalid_params = {'doprava':'','duzpaPuv':'','zaveTxt':''}	
	pytest.raises(main.FlexipyException,main.__validate_params, invalid_params, 'faktura-vydana') 

def test_get_template_dict():
	expected_result = {u'kod': '', u'nazev': ''}
	assert expected_result == main.get_template_dict('adresar')

def test_send_request():
	url = str(config.conf.get("server","url"))
	url += 'faktura-vydana.json'
	expected_resp = requests.get(url=url,auth=(str(config.conf.get("server","username")),str(config.conf.get("server","password"))),verify=False)
	actual_resp = main.__send_request(method='get', endUrl='faktura-vydana.json')
	assert expected_resp.status_code == actual_resp.status_code
	assert expected_resp.json() == actual_resp.json()

def test_prepare_date():
	data = {'kod':'inv1','nazev':'mojeFaktura'}
	expected_result = json.dumps({'winstrom':{'faktura-vydana':[data]}})
	actual_result = main.__prepare_data('faktura-vydana', data)
	assert expected_result == actual_result

def test_get_all_records_without_query():
	url = str(config.conf.get("server","url"))
	url += 'faktura-vydana.json'
	r = requests.get(url=url,auth=(str(config.conf.get("server","username")),str(config.conf.get("server","password"))),verify=False)
	expected_result = r.json()['winstrom']['faktura-vydana']
	actual_result = main.__get_all_records('faktura-vydana')
	assert expected_result == actual_result

def test_get_all_records_with_query():	
	url = str(config.conf.get("server","url"))
	#get all records with specSym = 48152342
	url += 'faktura-vydana/(specSym="48152342").json'
	r = requests.get(url=url,auth=(str(config.conf.get("server","username")),str(config.conf.get("server","password"))),verify=False)
	expected_result = r.json()['winstrom']['faktura-vydana']
	actual_result = main.__get_all_records('faktura-vydana',query="specSym='"+str(48152342)+"'")
	assert len(expected_result) == len(actual_result)
	assert expected_result == actual_result

def test_get_evidence_property_list():
	pass