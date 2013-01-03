# -*- coding: utf-8 -*-

import requests
import json
import config
import re

from .models import FakturaVydana, Banka, FakturaPrijata, FakturaVydanaPolozka, FakturaPrijataPolozka

class FlexipyException(Exception):
	pass


def __send_request(method, endUrl, payload=''):
	"""Top level function for sending requests. It takes configuration from config and creates
	request which is further defined by arguments of this function. It catches the most problematic 
	exceptions defined by library Requests and returns response object for further proccessing.
	:param method: Type of HTTP method, possible values:(get,put,post,delete)
	:param endUrl: ending part of target url 
	:param payload: Data in request
	"""
	try:
		r = requests.request(method=method, url=config.url+endUrl, data=payload, auth=(config.username,config.password))	
		if r.status_code == 401:
			raise FlexipyException("You're not authorized for this operation, you must be authenticated.")
		elif r.status_code == 402:
			raise FlexipyException("Payment required, the REST API is not active.")
		elif r.status_code == 403:
			raise FlexipyException("Forbidden operation. You're license probably do not allow this operation.")	
		elif r.status_code == 500:
			raise FlexipyException("Server error, something went wrong in Flexibee. Please check the state of Flexibee server.")							
	except requests.exceptions.ConnectionError:
		raise FlexipyException("Connection error")
	else:
		return r

def __prepare_data(evidence, data):
	'''This function will add importent parts to data that 
	are required by Flexibee protocol and then returns them as JSON.
	'''		
	winstrom = {'winstrom':{evidence:[data]}}
	return json.dumps(winstrom)


def __get_all_records(evidence):
	'''Construct and send request for list of all records in specific evidence.
	Returns :list: contatining all records

	:param evidence: valid values of evidence are in config.evidence_list

	'''
	re.sub(r'\s', '', evidence) #remove all wihtespaces
	if evidence not in config.evidence_list:
		raise ValueError('evidence arg is valid only for' +str(config.evidence_list))		
	r = __send_request(method='get', endUrl=evidence+'.json')
	return __process_response(r, evidence)

def __prepare_error_messages(e):	
	error_messages = []
	for error in e:
		error_messages.append(error['message'])
	return error_messages	

def __process_response(response, evidence=None):
	"""After Flexibee created new evidence item it returns response with 
	certain informations. This function process this response and returns it 
	as dictionary.	And removes unnecessary parts. With parametr evidence it 
	als serve for processing returned evidence item. If response contains only 
	one item(one specific evidence item) than it returns clean dictionary
	containing only information of that item. It response contains mote irems 
	it will return list of evidence item.
	:param response: Response object returned from Flexibee
	"""
	if evidence == None:
		d = response.json
		dictionary = d['winstrom']
		return dictionary
	else:
		d = response.json
		if len(d['winstrom'][evidence])	== 1:	
			dictionary = d['winstrom'][evidence][0]	
			return dictionary
		else:
			list_of_items = d['winstrom'][evidence]
			return list_of_items	

def __delete_item(id, evidence):
	"""Delte item defined by id and evidence
	:param id: identifies item to delete
	:param evidence: identifies what type of item to delete
	"""
	r = __send_request(method='delete', endUrl=evidence+'/'+str(id)+'.json')
	if r.status_code not in (200,201):
		if r.status_code == 404:
			raise FlexipyException("The record with id="+str(id)+" was not found")			
		else:
			raise FlexipyException("Uknown error")								

def __get_evidence_item(id, evidence):
	"""Get item from evidence and return it as dictionary.
	Returns dictionary for further proccessing
	:param id: id of item(Flexibee identificator)
	:param evidence: type of evidence	
	"""		
	r = __send_request(method='get', endUrl=evidence+'/'+str(id)+'.json')
	if r.status_code not in (200,201):
		if r.status_code == 404:
			raise FlexipyException("The record with id="+str(id)+" was not found")			
		else:
			raise FlexipyException("Uknown error")	
	else:		
		dictionary = __process_response(r, evidence=evidence)
		return dictionary


def __create_evidence_item(evidence, data):
	"""Function for creating evidence item, 
	created for purpose of refactoring
	Returns :tuple consisting of (success, result, error_message)
	:param evidence: evidence for new item
	:param data: JSON representation of data of created item
	"""	
	data = __prepare_data(evidence, data)
	r = __send_request(method='put', endUrl=evidence+'.json', payload=data)
	d = __process_response(r)
	if d['success'] == 'true':
		invoice_id = int(d['results'][0]['id'])
		return (True, invoice_id, None)
	else:
		e = d['results'][0]['errors']
		error_messages = __prepare_error_messages(e)
		return (False, None, error_messages) 

def __update_evidence_item(id, evidence, data):
	"""Function for updating already created evidence item.
	"param id: id(Flexibee identificator) of item to be changed
	:param evidence: evidence containing item which we want to update
	:param data: dictionary containing fields which we want to update
	"""
	data = __prepare_data(evidence, data)
	r = __send_request(method='put', endUrl=evidence+'/'+id+'.json', payload=data)


def get_all_bank_items():
	d = __get_all_records('banka')
	list_of_items = __process_response(d)
	return list_of_items

def get_all_issued_invoices():
	d = __get_all_records('faktura-vydana')
	return d

def get_all_received_invoices():
	d = __get_all_records('faktura-prijata')
	return d


def create_issued_invoice(invoice, invoice_items):
	"""This function creates new issued invoice in Flexibee. 
	Returns :tuple consisting of (success, result, error_message)
	where success = True/False
	result = id of invoice in FLexibee or None if success = False
	error_message = List of error messages if success=False else error_message=None
	"""	
	faktura = FakturaVydana.from_dict(invoice)
	inv_items = []
	for it in invoice_items:
		item = FakturaVydanaPolozka.from_dict(it)
		inv_items.append(item.to_dict())
	d = faktura.to_dict()
	d['polozkyFaktury']= inv_items
	return __create_evidence_item('faktura-vydana',d)
	

def create_received_invoice(invoice, invoice_items):
	"""This function creates new received invoice in Flexibee. 
	Returns :tuple consisting of (success, result, error_message)
	where success = True/False
	result = id of invoice in FLexibee or None if success = False
	error_message = Error message if success=False else error_message=None
	"""	
	faktura = FakturaVydana.from_dict(invoice)
	inv_items = []
	for it in invoice_items:
		item = FakturaPrijataPolozka.from_dict(it)
		inv_items.append(item.to_dict())
	d = faktura.to_dict()
	d['polozkyFaktury']= inv_items
	return __create_evidence_item('faktura-prijata',d)

def delete_issued_invoice(id):
	"""Delete issued invoice specifeid by id.
	:param id: identifies invoice	
	"""
	__delete_item(id, 'faktura-vydana')

def delete_received_invoice(id):
	"""Delete received invoice specifeid by id
	:param id: identifies invoice	
	"""
	__delete_item(id, 'faktura-prijata')	

def get_issued_invoice(id):
	return __get_evidence_item(id, 'faktura-vydana')
		

def get_received_invoice(id):
	return __get_evidence_item(id, 'faktura-prijata')		

def create_address_book_item(kod, nazev, nazevA=None, nazevB=None, nazevC=None, 
	poznam=None, popis=None, platiOd=None, platiDo=None, ulice=None, mesto=None,
	psc=None,tel=None,mobil=None,fax=None,email=None,www=None,stat=None,eanKod=None,
	ic=None,dic=None,postovniShodna=None,faEanKod=None,faJmenoFirmy=None,faUlice=None,
	faMesto=None,faPsc=None,splatDny=None,limitFak=None,limitPoSplatDny=None,
	limitPoSplatZakaz=None,platceDph=None,formExportK=None,typVztahuK=None,kodPojistovny=None,
	nazevPojistovny=None,osloveni=None,slevaDokl=None,obpAutomHotovo=None,stitky=None,
	skupFir=None,stredisko=None,faStat=None,zodpOsoba=None,skupCen=None):
	"""Creates new contact in address book, can be good for suppliers and
	subscribers. Definition of all fields is here 
	http://demo.flexibee.eu/c/demo/adresar/properties
	"""	
	return __create_evidence_item('adresar',data)

	