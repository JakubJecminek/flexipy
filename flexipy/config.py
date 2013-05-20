# -*- coding: utf-8 -*-

"""
Zde se nachazi globalni nastaveni modulu.
Je treba zde nastavit nektere parametry(viz dokumentace).
Nektere promene je treba doplnit na zaklade faktickeho 
stavu z Flexibee. Napriklad doplnit typy faktur.
"""

import ConfigParser
from pkg_resources import Requirement, resource_filename
import codecs


class Config(object):
	"""
	Base config class definuje zakladni metody pro praci s konfiguracnim souborem.	
	"""

	def __init__(self, config_name="flexipy/flexipy.conf"):
		self.conf = ConfigParser.SafeConfigParser()
		#use resource management api to find flexipy.conf, see docs
		filename = resource_filename(Requirement.parse("flexipy"), config_name)
		# Open the file with the correct encoding	
		try:
			with codecs.open(filename, 'r', encoding='utf-8') as f:
				self.conf.readfp(f)
		except IOError:
			raise ValueError('Konfiguracni soubor '+config_name+' neexistuje nebo jste uvedli spatnou cestu.')		

	def get_section_list(self, section_name):
		"""
		Tato privatni metoda spracuje vsechny sekce v config filu 
		na zaklade jmena sekce a vrati list obsahujici vsechny polozky.
		"""	
		result_list = []
		try:
			section_content = self.conf.items(section_name)
			for key, val in section_content:
				result_list.append(val)
		except ConfigParser.NoSectionError:
			raise ValueError("Config file neobsahuje sekci "+section_name)		
		return result_list

	def get_server_config(self):
		"""
		Tato metoda vrati dict obsahujici vsechna nastaveni tykajici se serveru. 		
		"""
		result = {}
		try:
			section_content = self.conf.items("server")
			for key, val in section_content:
				result[key]=val			
		except ConfigParser.NoSectionError:
			raise ValueError("Config file neobsahuje sekci server")		
		return result

	def get_evidence_list(self):
		return self.get_section_list('evidence')	

	def get_typy_faktury_prijate(self):
		return self.get_section_list('typ_faktury_prijate')

	def get_typy_faktury_vydane(self):
		return self.get_section_list('typ_faktury_vydane')	

	def get_typ_bank_dokladu(self):
		return self.get_section_list('typ_bank_dokladu')

	def get_typ_pohybu(self):
		return self.get_section_list('typ_pohybu')	

	def get_bankovni_ucty(self):
		return self.get_section_list('bankovni_ucty')	

	def get_typ_polozky_vydane(self):
		return self.get_section_list('typ_polozky_vydane')

	def get_typ_ucetni_operace(self):
		return self.get_section_list('typ_ucetni_operace')	

	def get_typ_pokladni_pohyb(self):
		return self.get_section_list('typ_pokladni_pohyb')		

	def get_typ_pokladna(self):
		return self.get_section_list('typ_pokladna')				



class TestingConfig(Config):
	"""
	Pro testovani staci vytvorit instanci teto tridy.
	"""

	def __init__(self):
		Config.__init__(self, config_name="flexipy/test_flexipy.conf")

class DemoConfig(Config):
	"""
	Pouzijte tento config pro praci s demo instalaci Flexibee na demo.flexibee.eu
	Vhodne pro testovani nejnovejsich verzi systemu Flexibee.
	"""		
	def __init__(self):
		Config.__init__(self, config_name="flexipy/demo_flexibee.conf")	