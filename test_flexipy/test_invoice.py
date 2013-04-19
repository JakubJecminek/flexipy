# -*- coding: utf-8 -*-

from flexipy import invoice
from flexipy import main, config
import requests
import json

def test_get_all_vydane_faktury():
	username = str(config.conf.get("server","username"))
	password = str(config.conf.get("server","password"))
	r = requests.get(str(config.conf.get("server","url"))+'faktura-vydana.json' ,auth=(username,password), verify=False)
	d = r.json()
	if len(d['winstrom']['faktura-vydana']):
		list_of_invoices_expected = d['winstrom']['faktura-vydana'][0]
	else:
		list_of_invoices_expected = d['winstrom']['faktura-vydana']
	list_of_invoices_actual = invoice.get_all_vydane_faktury()
	assert list_of_invoices_expected == list_of_invoices_actual

def test_get_all_prijate_faktury():
	username = str(config.conf.get("server","username"))
	password = str(config.conf.get("server","password"))
	r = requests.get(str(config.conf.get("server","url"))+'faktura-prijata.json' ,auth=(username,password), verify=False)
	d = r.json()
	if(len(d['winstrom']['faktura-prijata']) == 1):
		list_of_invoices_expected = d['winstrom']['faktura-prijata'][0]
	else:	
		list_of_invoices_expected = d['winstrom']['faktura-prijata']
	list_of_invoices_actual = invoice.get_all_prijate_faktury()
	assert list_of_invoices_expected == list_of_invoices_actual

def test_create_vydana_faktura():
	expected_data = {'kod':'flex11','typDokl':'code:FAKTURA','firma':'code:201','popis':'Flexipy test invoice', 'sumDphZakl':'0.0','bezPolozek':'true', 'varSym':'11235484','zdrojProSkl':'false'}
	dalsi_param = {'popis':'Flexipy test invoice','firma':'code:201'}
	result = invoice.create_vydana_faktura(kod='flex11', var_sym='11235484', datum_vyst='2013-02-28', zdroj_pro_sklad=False, typ_dokl=config.get_typy_faktury_vydane()[0], dalsi_param=dalsi_param)
	assert result[0] == True #expected True
	id = result[1]
	actualData = invoice.get_vydana_faktura(id, detail='full') 
	assert actualData['kod'].lower() == expected_data['kod'].lower()
	assert actualData['typDokl'] == expected_data['typDokl']
	assert actualData['firma'] == expected_data['firma']
	assert actualData['popis'] == expected_data['popis']
	assert actualData['sumDphZakl'] == expected_data['sumDphZakl']	
	#uklid po sobe
	invoice.delete_vydana_faktura(id)

def test_create_vydana_faktura_polozky():
	polozky = [{'typPolozkyK':config.get_typ_polozky_vydane()[0],'zdrojProSkl':False,'nazev':'vypujceni auta','ucetni':True,'cenaMj':'4815.0'}]	
	expected_data = {'kod':'flex12','typDokl':'code:FAKTURA','firma':'code:201','popis':'Flexipy test invoice', 
	'varSym':'11235484','zdrojProSkl':'false','polozkyFaktury':polozky}
	expected_polozky = [{'typPolozkyK':'typPolozky.obecny','zdrojProSkl':'false','nazev':'vypujceni auta','ucetni':'true','cenaMj':'4815.0'}]
	dalsi_param = {'popis':'Flexipy test invoice','firma':'code:201','typUcOp':u'code:TRŽBA SLUŽBY'}
	result = invoice.create_vydana_faktura(kod='flex12', var_sym='11235484', datum_vyst='2013-02-28', 
	zdroj_pro_sklad=False, typ_dokl=config.get_typy_faktury_vydane()[0], dalsi_param=dalsi_param, polozky_faktury=polozky)
	assert result[0] == True #expected True
	id = result[1]
	actualData = invoice.get_vydana_faktura(id, detail='full') 
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
	invoice.delete_vydana_faktura(id)	