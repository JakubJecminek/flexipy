# -*- coding: utf-8 -*-

"""
This module contains utilites that are usefull for flexipy.


:copyright: (c) 2012 by Jakub Ječmínek.
:license: BSD, see LICENSE for more details.
"""

import requests
import config

def underscore_to_camelcase(value):
	"""Transforms string with underscores to camelcase.
	Found on stackoverflow 
	http://stackoverflow.com/questions/4303492/how-can-i-simplify-this-conversion-from-underscore-to-camelcase-in-python
	"""
	def camelcase(): 
		yield str.lower
		while True:
			yield str.capitalize

	c = camelcase()
	return "".join(c.next()(x) if x else '_' for x in value.split("_"))


def dash_to_camelcase(value):
	"""Same function as above with my additions 
	but this transoforms dashes to camelcase.	
	"""
	def camelcase():
		yield str.lower
		while True:
			yield str.capitalize
	c = camelcase()

	return "".join(c.next()(x) if x else '-' for x in value.split("-"))

def create_model_definition(evidence):
	"""This function helps to add new model definitions of evidence
	items, exactly how they are dedined in Flexibee. Except if item contains
	other items. Like for example Invoice contains Invoice items. It parse properties
	files that are provided by Flexibee.
	Returns string which contains formatted class definition.
	"""

	r = requests.get(url=config.url+evidence+'/properties.json', auth=(config.username,config.password))
	d = r.json
	classDef = ''
	#take the name of tme evidence item and transform it
	#to typical form of name for class
	name_of_class = str(d['properties']['tagName'])	
	name_of_class = dash_to_camelcase(name_of_class)
	#capitalize first letter
	name_of_class=name_of_class[0].capitalize()+name_of_class[1:]
	classDef += 'class '+name_of_class+'(micromodels.Model):\n'
	#start to parse fields
	propertiesList=d['properties']['property']
	for p in propertiesList:
		#dont write fields which are not writeable
		if p['isWritable']=='false':
			continue
		classDef +="    "+p['propertyName']+" = "
		if p['type']=='integer':
			classDef+="micromodels.IntegerField()\n"
		elif p['type']=='datetime':
			classDef+="micromodels.DateTimeField()\n"
		elif p['type']=='date':
			classDef+="micromodels.DateField()\n"	
		elif p['type']=='logic':
			classDef+="micromodels.BooleanField()\n"
		elif p['type'] in ('numeric','money'):
			classDef+="micromodels.FloatField()\n"
		else:
			classDef+="micromodels.CharField()\n"

	return classDef		
			

def create_all_model_definitions():
	"""It automaticly creates all model definitions
	used in FLexibee. It should be runned from time to time,
	if Flexibee changes something. In config.py there is evidence_list
	which contains all evidences that are supported by flexipy. If Flexibee
	add or remove some evidence, evidence_list has to be updated.
	"""
	f = open('models.py', 'w')
	f.write("# -*- coding: utf-8 -*-")
	f.write("\n\n")
	f.write("import micromodels")
	f.write("\n\n")
	for evidence in config.evidence_list:
		f.write(create_model_definition(evidence))
		#insert two empty lines between every class
		f.write("\n\n")
	f.close()


