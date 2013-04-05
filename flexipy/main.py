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
		r = requests.request(method=method, url=config.url+endUrl, data=payload, auth=(config.username,config.password), verify=config.verify_ssl)	
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
		try:
			r = __send_request(method='get', endUrl=evidence+'.json?detail='+detail)
		except FlexipyException:
			print 		
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

def __validate_params(params, evidence):
	"""Tato funkce validuje parametry ktere zadal uzivatel jako dodatecne polozky 
	evidence.
	V pripade chybi vyhodi FlexipyException
	:param params: dictionary obsahujici dodatecne polozky
	:param evidence: typ evidence pro ktery se ma provest validace
	"""
	template_dict = get_template_dict(evidence, True)
	invalid_params = ''
	for key in params:
		if key not in template_dict:
			invalid_params += key + ', '			
	if len(invalid_params) > 0:
		raise FlexipyException('Dalsi parametry: '+invalid_params+'nejsou validni')

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