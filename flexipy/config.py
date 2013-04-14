# -*- coding: utf-8 -*-

"""
Zde se nachazi globalni nastaveni modulu.
Je treba zde nastavit nektere parametry(viz dokumentace).
Nektere promene je treba doplnit na zaklade faktickeho 
stavu z Flexibee. Napriklad doplnit typy faktur.
"""

from ConfigParser import SafeConfigParser
from pkg_resources import Requirement, resource_filename
import codecs


conf = SafeConfigParser()
#use resource management api to find flexipy.conf, see docs
filename = resource_filename(Requirement.parse("flexipy"),"flexipy/flexipy.conf")
# Open the file with the correct encoding	
with codecs.open(filename, 'r', encoding='utf-8') as f:
		conf.readfp(f)




def __get_section_list(section_name):
	"""
	Tato privatni funkce ypracuje vsechny sekce v config filu 
	na zaklade jmena sekce a vrati list obsahujici vsechny polozky.
	"""	
	result_list = []

	try:
		section_content = conf.items(section_name)
		for key, val in section_content:
			result_list.append(val)
	except ConfigParser.NoSectionError:
		raise ValueError("Config file neobsahuje sekci "+section_name)		
	return result_list

def get_evidence_list():
	return __get_section_list('evidence')	

def get_typy_faktury_prijate():
	return __get_section_list('typ_faktury_prijate')

def get_typy_faktury_vydane():
	return __get_section_list('typ_faktury_vydane')	

def get_typ_bank_dokladu():
	return __get_section_list('typ_bank_dokladu')

def get_typ_pohybu():
	return __get_section_list('typ_pohybu')	

def get_bankovni_ucty():
	return __get_section_list('bankovni_ucty')	

def get_typ_polozky_vydane():
	return __get_section_list('typ_polozky_vydane')

def get_typ_ucetni_operace():
	return __get_section_list('typ_ucetni_operace')	