# -*- coding: utf-8 -*-

#this is configuration module for global settings
#here you have to set certain variables
#this is canonical way to share information across modules within a single program

#server running flexibee configuration
host='https://demo.flexibee.eu'
firma='demo'

#url for requests
url=host+'/c/'+firma+'/'

#authentication settings
username='winstrom'
password='winstrom' 

#tuple contains all evidences which are supported by flexipy
evidence_list = ('faktura-vydana', 'banka', 'interni-doklad','pohledavka',
	'adresar','cenik','interni-doklad')