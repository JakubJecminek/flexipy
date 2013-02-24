# -*- coding: utf-8 -*-

"""
Zde se nachazi globalni nastaveni modulu.
Je treba zde nastavit nektere parametry(viz dokumentace).
Nektere promene se automaticky naplni pri importu modulu.
Pro spravne nastaveni konfigurace je nutne byt pripojeny k systemu Flexibee.
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
	'faktura-prijata-polozka','typ-faktury-vydane')

#nasleduji listy a dictionaries ktere obsahuji polozky typu relation, ktere se nacitaji z flexibee

#dict ktery se inicializuje pri nacteni knihovny, obsahuje vsechny moznosti
#tato polozka se vyuziva u faktura-prijata, oznaceni typDokl
typ_faktury_prijate = []

typ_faktury_vydane = []

#typDokl u banka
typ_bank_dokladu = []

#tento dict se nainicalizuje pri importu knihovny dynamicky ze serveru na kterem je umisteno flexibee
#key je odkaz na evidenci(url) ktera obsahuje list moznych hodnot
#value je list, ktery obsahuje vsechny polozky kod, ktere muze nabyvat typDokl danne evidence
#kod je faktickym odkazem ktery se pak umistuje do typDokl
typDokl = {'typ-faktury-vydane':typ_faktury_vydane, 'typ-faktury-prijate':typ_faktury_prijate,'typ-banka':typ_bank_dokladu}

#select u banky, pevne dano, pouze dve moznosti
typPohybuK = {'prijem':'typPohybu.prijem','vydej':'typPohybu.vydej'}

