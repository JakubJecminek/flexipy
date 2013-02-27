# -*- coding: utf-8 -*-

import requests
import json
import config
import re

class FlexipyException(Exception):
	pass


def __send_request(method, endUrl, payload=''):
	"""Privatni funkce pro posilani requestu. Cast url se bere z nastaveni v config, 
	zbytek se doplni dle pozadavku. Tato funkce chyta nejzavaznejsi vyjimky definovane
	v knihovne Requests a vraci Response objekt pro dalsi zpracovani.
	:param method: Typ HTTP metody, mozne hodnoty:(get,put,post,delete)
	:param endUrl: koncova cast url, zavisla na konkretnim requestu 
	:param payload: Data v requestu
	"""
	try:
		r = requests.request(method=method, url=config.url+endUrl, data=payload, auth=(config.username,config.password))	
		if r.status_code == 401:
			raise FlexipyException("Nemate opravneni provest tuto operaci.")
		elif r.status_code == 402:
			raise FlexipyException("Platba vyzadovana, REST API neni aktivni.")
		elif r.status_code == 403:
			raise FlexipyException("Zakazana operace. Vase licence zrejme neumoznuje tuto operaci.")	
		elif r.status_code == 500:
			raise FlexipyException("Server error, zrejme je neco spatne se serverem na kterem je Flexibee.")							
	except requests.exceptions.ConnectionError:
		raise FlexipyException("Connection error")
	else:
		return r

def __prepare_data(evidence, data):
	'''Tato funkce pripravuje data na odeslani. Prida casti vyzadovane komunikacnim formatem 
	Flexibee a vrati JSON k odeslani. 
	'''		
	winstrom = {'winstrom':{evidence:[data]}}
	return json.dumps(winstrom)


def __get_all_records(evidence, query=None, detail='summary'):
	'''Vytvori a odesle pozadavek k ziskani vsech zaznamu z pozadovane evidence.
	Returns :list: contatining all records

	:param evidence: podporovane evidence se nachazi v config.evidence_list
	:param query: dotaz ktey filtruje zaznamy
	:param detail: uroven zobrazeni detailu(kolik polozek daneho zaznamu se vypise)
	defaultni hodnota je summary. Dalsi moznosi je id(vypise pouze id zaznamu) a full(kompletni vypis)
	'''
	re.sub(r'\s', '', evidence) #remove all wihtespaces	
	if query == None:
		r = __send_request(method='get', endUrl=evidence+'.json?detail='+detail)
	else:
		#pouzij query pro filtrovani
		#TODO: nejakym zpusobem zvaliduj query
		r = __send_request(method='get', endUrl=evidence+'/('+query+').json?detail='+detail)	
	return __process_response(r, evidence)

def __get_evidence_property_list(evidence):
	"""Tato funkce vraci seznam polozek danne evidence. Tyto polozky jsou 
	parsovane z Flexibee.
	:param evidence: identifikuje evidenci jejiz seznam polozek chceme stahnout
	"""
	result = {}
	r = r = __send_request(method='get', endUrl=evidence+'/properties.json')
	d = r.json()	
	return d['properties']['property']		

def __prepare_error_messages(e):	
	"""Pomocna funkce pro vytvareni chybovych zprav.
	Tyto chybove zpravy se se prebiraji z odpovedi kterou
	posila v pripade neuspechu Flexibee.
	"""
	error_messages = []
	for error in e:
		error_messages.append(error['message'])
	return error_messages	

def __process_response(response, evidence=None):
	"""Pote co Flexibee vytvori novy zaznam v nejake evidenci, vrati
	odpoved obsahujici urcite informace. Tato funkce zpracuje odpoved a vratu 
	jeji obsah jako dictionary.	Odstrani take nepotrebne casti. 
	:param response: Response objekt vraceny z Flexibee
	"""
	if evidence == None:
		d = response.json()
		dictionary = d['winstrom']
		return dictionary
	else:
		d = response.json()
		if len(d['winstrom'][evidence])==1:
			dictionary = d['winstrom'][evidence][0]	
			return dictionary
		else:
			list_of_items = d['winstrom'][evidence]
			return list_of_items	

def __delete_item(id, evidence):
	"""Smaze zaznam v evidenci na zaklade id.
	:param id: identifikuje zaznam(Flexibee identifikator nebo pripadne kod)
	:param evidence: identifikuje v ktere evidenci se zaznam nachazi
	"""
	r = __send_request(method='delete', endUrl=evidence+'/'+str(id)+'.json')
	if r.status_code not in (200,201):
		if r.status_code == 404:
			raise FlexipyException("Zaznam s id="+str(id)+" nebyl nalezen.")			
		else:
			raise FlexipyException("Neznama chyba.")								

def __get_evidence_item(id, evidence, detail='summary'):
	"""Ziskej zaznam z evidence na zaklade id.
	Vraci zaznam jako dictionary pro dalsi zpracovani.
	:param id: id zaznamu(Flexibee identifikator nebo pripadne kod)
	:param evidence: identifikuje v ktere evidenci se zaznam nachazi
	:param detail: uroven zobrazeni detailu(kolik polozek daneho zaznamu se vypise)
	defaultni hodnota je summary. Dalsi moznosi je id(vypise pouze id zaznamu) a full(kompletni vypis)		
	"""		
	r = __send_request(method='get', endUrl=evidence+'/'+str(id)+'.json?detail='+detail)
	if r.status_code not in (200,201):
		if r.status_code == 404:
			raise FlexipyException("Zaznam s id="+str(id)+" nebyl nalezen.")			
		else:
			raise FlexipyException("Neznama chyba.")	
	else:		
		dictionary = __process_response(r, evidence=evidence)
		return dictionary

def __get_evidence_item_by_code(kod, evidence, detail='summary'):
	"""Ziskej zaznam z evidence na zaklade polozky kod.
	Vraci zaznam jako dictionary pro dalsi zpracovani.
	:param kod: kod zaznamu(Flexibee polozka kod)
	:param evidence: identifikuje v ktere evidenci se zaznam nachazi	
	:param detail: uroven zobrazeni detailu(kolik polozek daneho zaznamu se vypise)
	defaultni hodnota je summary. Dalsi moznosi je id(vypise pouze id zaznamu) a full(kompletni vypis)	
	"""		
	r = __send_request(method='get', endUrl=evidence+"/(kod='"+kod+"').json?detail="+detail)
	if r.status_code not in (200,201):
		if r.status_code == 404:
			raise FlexipyException("Zaznam s kodem="+kod+" nebyl nalezen.")			
		else:
			raise FlexipyException("Neznama chyba.")	
	else:		
		dictionary = __process_response(r, evidence=evidence)
		return dictionary

def __create_evidence_item(evidence, data):
	"""Privatni funkce pro vytvareni novych zaznamu v evidenci.
	Returns :tuple skladajici se z (success, result_id, error_message)
	:param evidence: evidence for new item
	:param data: JSON reprezebtace dat vytvareneho zaznamu
	"""	
	data = __prepare_data(evidence, data)
	r = __send_request(method='put', endUrl=evidence+'.json', payload=data)
	d = __process_response(r)
	if d['success'] == 'true':
		id = int(d['results'][0]['id'])
		return (True, id, None)
	else:
		e = d['results'][0]['errors']
		error_messages = __prepare_error_messages(e)
		return (False, None, error_messages) 

def __update_evidence_item(id, evidence, data):
	"""Function for updating already created evidence item.
	Returns :tuple consisting of (success, result, error_message)
	:param id: id(Flexibee identificator) of item to be changed
	:param evidence: evidence containing item which we want to update(change)
	:param data: dictionary containing fields which we want to update
	"""
	data = __prepare_data(evidence, data)
	r = __send_request(method='put', endUrl=evidence+'/'+str(id)+'.json', payload=data)
	d = __process_response(r)
	if d['success'] == 'true':
		id = int(d['results'][0]['id'])
		return (True, id, None)
	else:
		e = d['results'][0]['errors']
		error_messages = __prepare_error_messages(e)
		return (False, None, error_messages) 

def __initialize_config_file():
	for odkaz, typ_list in config.typDokl.iteritems():	
		d = __get_all_records(odkaz)
		for dictPolozka in d:
			kod = dictPolozka['kod']
			typ_list.append(kod)

def get_template_dict(evidence, complete=False):
	"""This function creates tepmlate dictionary for evidence.
	This is usefull for creation of evidence items.
	:param evidence: evidence for which will be created template
	:param complete: if True return dict with all params
	"""
	if evidence not in config.evidence_list:
		raise ValueError('evidence arg is valid only for' +str(config.evidence_list))
	#start parsing properties
	property_list = __get_evidence_property_list(evidence)
	result={}
	if complete == False:
		for property in property_list:
		#every property is dictionary
			if property['isWritable'] == 'true' and property['mandatory']=='true':
				property_name = property['propertyName']	
				result[property_name] = ''
	else:		
		for property in property_list:
			#every property is dictionary
			if property['isWritable'] == 'true':
				property_name = property['propertyName']	
				result[property_name] = ''

	return result	


def get_all_bank_items(query=None, detail='summary'):
	"""Funkce vrati vsechny bankovni doklady z Flexibee.
	:param query: Pokud je uveden dotaz ve formatu jaky podporuje 
	Flexibee(viz dokumentace), vrati vyfiltrovane zaznamy na zaklade 
	dotazu.
	"""
	d = __get_all_records('banka', query, detail)
	return d

def get_all_issued_invoices(query=None, detail='summary'):
	"""Funkce vrati vsechny vydane faktury z Flexibee.
	:param query: Pokud je uveden dotaz ve formatu jaky podporuje 
	Flexibee(viz dokumentace), vrati vyfiltrovane zaznamy na zaklade 
	dotazu.
	"""
	d = __get_all_records('faktura-vydana', query, detail)
	return d

def get_all_received_invoices(query=None, detail='summary'):
	"""Funkce vrati vsechny prijate faktury z Flexibee.
	:param query: Pokud je uveden dotaz ve formatu jaky podporuje 
	Flexibee(viz dokumentace), vrati vyfiltrovane zaznamy na zaklade 
	dotazu.
	"""
	d = __get_all_records('faktura-prijata', query, detail)
	return d


def create_issued_invoice(kod, var_sym, datum_vyst, zdroj_pro_sklad=False, 
	typ_dokl=config.typ_faktury_vydane[0], dalsi_param=None, polozky_faktury=None):
	"""This function creates new issued invoice in Flexibee. 
	Returns :tuple consisting of (success, result, error_message)
	"""	
	invoice = {'kod':kod, 'varSym':var_sym, 'datVyst':datum_vyst,'zdrojProSkl':zdroj_pro_sklad, 'typDokl':typ_dokl}
	if dalsi_param != None:
		for k,v in dalsi_param.iteritems():
			invoice[k] = v			
	if polozky_faktury != None:		
		invoice['bezPolozek'] = False
		inv_items = []
		for it in polozky_faktury:
			inv_items.append(it)
		invoice['polozkyFaktury']= inv_items
	return __create_evidence_item('faktura-vydana',invoice)
	

def create_received_invoice(kod, var_sym, cislo_dosle, datum_splat, 
	datum_vyst, zdroj_pro_sklad=False, typ_dokl=config.typ_faktury_prijate[0], 
	dalsi_param=None, polozky_faktury=None)):
	"""This function creates new received invoice in Flexibee. 
	Returns :tuple consisting of (success, result, error_message)
	where success = True/False
	"""	
	invoice = {'datSplat': datum_splat, 'kod': kod, 'zdrojProSkl': zdroj_pro_sklad, 'datVyst': datum_vyst, 'varSym': var_sym, 'cisDosle': cislo_dosle, 'typDokl': typ_dokl}
	inv_items = []
	for it in invoice_items:
		inv_items.append(it)
	d = faktura.to_dict()
	invoice['polozkyFaktury']= inv_items
	return __create_evidence_item('faktura-prijata',invoice)
	

def update_issued_invoice(id, invoice):
	"""This function update issued invoice that is already in the Flexibee.
	For usage example see documentation.
	Returns :tuple consisting of (success, result, error_message)
	:param: id: id of invoice which you want to change
	:param invoice: dictionary that contains changed data
	"""
	return __update_evidence_item(id, 'faktura-vydana', invoice)

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

def get_issued_invoice(id, detail='summary'):
	return __get_evidence_item(id, 'faktura-vydana', detail)

def get_issued_invoice_by_code(code, detail='summary'):
	return __get_evidence_item_by_code(code, 'faktura-vydana', detail)
		
def get_received_invoice(id, detail='summary'):
	return __get_evidence_item(id, 'faktura-prijata', detail)

def get_received_invoice_by_code(code, detail='summary'):
	return __get_evidence_item_by_code(code, 'faktura-prijata', detail)		

def get_address_book_item(id, detail='summary'):
	return __get_evidence_item(id, 'adresar', detail)

def get_address_book_by_code(code, detail='summary'):
	return __get_evidence_item_by_code(code, 'adresar', detail)			

def get_bank_item(id, detail='summary'):
	return __get_evidence_item(id, 'banka', detail)

def get_banka_by_code(code, detail='summary'):
	return __get_evidence_item_by_code(code, 'banka', detail)		

def create_address_book_item(address_item):
	"""Creates new contact in address book, can be good for suppliers and
	subscribers. Definition of all fields is here 
	http://demo.flexibee.eu/c/demo/adresar/properties
	"""	
	return __create_evidence_item('adresar',address_item)

	