# -*- coding: utf-8 -*-

"""
Zde se nachazi globalni nastaveni modulu.
Je treba zde nastavit nektere parametry(viz dokumentace).
Nektere promene je treba doplnit na zaklade faktickeho 
stavu z Flexibee. Napriklad doplnit typy faktur.
"""

#parametry pro nastaveni serveru na kterem bezi Flexibee
host='https://demo.flexibee.eu'
firma='demo'

#zaklad url pro requesty
url=host+'/c/'+firma+'/'

#autorizacni udaje k Flexibee
username='winstrom'
password='winstrom' 

#tuple obsahujici podporavene evidence se kterymi knihovna umi pracovat
evidence_list = ('faktura-vydana', 'banka', 'interni-doklad',
	'adresar','cenik','faktura-prijata','faktura-vydana-polozka',
	'faktura-prijata-polozka','typ-faktury-vydane','adresar-bankovni-ucet')

#nasleduji listy a dictionaries ktere obsahuji polozky typu relation, ktere se nacitaji z flexibee

#dict ktery se inicializuje pri nacteni knihovny, obsahuje vsechny moznosti
#tato polozka se vyuziva u faktura-prijata, oznaceni typDokl
typ_faktury_prijate = ['FAKTURA', 'PR\xcdJEMKA','Z\xc1LOHA','ZDD']

typ_faktury_vydane = ['FAKTURA','FAKT\xdaRA ESHOP','PREDFAKT\xdaRA','Z\xc1LOHA','ZDD']

#typDokl u banka
typ_bank_dokladu = ['BANKOVN\xcd \xda\u010cET 2','STANDARD']

#select u banky, pevne dano, pouze dve moznosti
typ_pohybu = ['typPohybu.prijem','typPohybu.vydej']

#relace u bank dokladu je to evidence bankovni-ucet
bankovni_ucet = ['BANKA_1']

