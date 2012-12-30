import requests
import json
import config
import re




def __send_request(method, endUrl, payload=''):
	try:
		r = requests.request(method=method, url=config.url+endUrl, data=payload, auth=(config.username,config.password))		
	except requests.exceptions.ConnectionError:
		print 'Problem with connection' 
	except requests.exceptions.Timeout :
		print 'Timeout for request'	
	else:
		return r

def __get_all_records(evidence):
	'''Construct and send request for list of all records in specific evidence.
	Returns :list: contatining all records

	:param evidence,valid values of evidence are: faktura-vydana, banka, interni-doklad,pohledavka	

	'''
	re.sub(r'\s', '', evidence) #remove all wihtespaces
	if evidence not in ('faktura-vydana', 'banka', 'interni-doklad','pohledavka'):
		raise ValueError("evidence arg is valid only for 'faktura-vydana', 'banka', 'interni-doklad','pohledavka'")		
	r = __send_request(method='get', endUrl=evidence+'.json')
	dictionary = r.json
	result = dictionary['winstrom'][evidence]
	return result

def __prepare_error_messages(e):
	error_messages = []
	for error in e:
		error_messages.append(e['message'])
	return error_messages	

def __process_response(r):
	"""After Flexibee created new evidence item it returns response with 
	certain informations. This function process this response and returns it 
	as dictionary.	
	:param r: Response object returned from Flexibee
	"""
	d = r.json
	return d

def __create_evidence_item(evidence, data):
	"""Function for creating evidence item, 
	created for purpose of refactoring
	Returns :tuple consisting of (success, result, error_message)
	:param evidence: evidence for new item
	:param data: data of created item
	"""
	r = __send_request(method='put', endUrl=evidence+'.json', payload=data)
	d = __process_response(r)
	if d['winstrom']['success'] == 'true':
		invoice_id = int(d['winstrom']['results'][0]['id'])
		return (True, invoice_id, None)
	else:
		e = d['winstrom']['results'][0]['errors']
		error_mesages = __prepare_error_messages(e)
		return (False, None, error_messages) 


def get_all_bank_():
	d = __get_all_records('banka')
	return d

def get_all_invoices():
	d = __get_all_records('faktura-vydana')
	return d



def create_issued_invoice(data):
	"""This function creates new issued invoice in Flexibee. 
	Returns :tuple consisting of (success, result, error_message)
	where success = True/False
	result = id of invoice in FLexibee or None if success = False
	error_message = List of error messages if success=False else error_message=None
	"""	
	return __create_evidence_item('faktura-vydana',data)
	

def create_received_invoice(data):
	"""This function creates new received invoice in Flexibee. 
	Returns :tuple consisting of (success, result, error_message)
	where success = True/False
	result = id of invoice in FLexibee or None if success = False
	error_message = Error message if success=False else error_message=None
	"""	
	return __create_evidence_item('faktura-vydana',data)	

def __delete_item(id, evidence):
	"""Delte item defined by id and evidence
	:param id: identifies item to delete
	:param evidence: identifies what type of item to delete
	"""
	__send_request(method='delete', endUrl=evidence+'/'+id+'.json')

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