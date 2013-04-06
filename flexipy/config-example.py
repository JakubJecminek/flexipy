# -*- coding: utf-8 -*-

"""
Zde se nachazi globalni nastaveni modulu.
Je treba zde nastavit nektere parametry(viz dokumentace).
Nektere promene je treba doplnit na zaklade faktickeho 
stavu z Flexibee či vlastních potřeb. Napriklad doplnit typy faktur.
TOTO JE POUZE UKAZKOVY CONFIG FILE!!! JE NUTNE SKOPIROVAT A VYTVORIT 
VLASTNI. 
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
	'adresar','faktura-prijata','faktura-vydana-polozka',
	'faktura-prijata-polozka','typ-faktury-vydane','adresar-bankovni-ucet')

#nasleduji listy, ktere obsahuji polozky typu relation, ktere se nachazeji ve flexibee

#tato polozka se vyuziva u faktura-prijata, oznaceni typDokl
typ_faktury_prijate = ['FAKTURA']

#tato polozka se vyuziva u faktura-vydana, oznaceni typDokl
typ_faktury_vydane = ['FAKTURA']

#typDokl u banka
typ_bank_dokladu = ['STANDARD']

#select u banky, pevne dano, pouze dve moznosti
typ_pohybu = ['typPohybu.prijem','typPohybu.vydej']

#relace u bank dokladu je to evidence bankovni-ucet
bankovni_ucet = ['BANKA_1']

#typy polozek u faktury vydane
#toto je typ select, tyto hodnoty jsou by default ve flexibee
#polozka ma oznaceni typPolozkyK
typ_polozky_vydane=['typPolozky.obecny','typPolozky.katalog','typPolozky.ucetni','typPolozky.text']

#polozka typUcOp u faktur
#zde jen uvedeny ty ktere konkretne potrebuji ja
typ_ucetni_operace = [u'TRŽBA SLUŽBY',u'NÁKUP SLUŽBY']

#zde je vhodne uvest seznam firem s kterymi pracujte ve Flexibee, pote lze snadneji
#vytvaret faktury pomoci vnitrnich vazeb. Viz dokumentace.
#firmy musi byt ve formatu 'code:<kodFirmy>' kde kodFirmy je kod ktery jste danne firme priradili
firmy = []

#nastaveni zda requests maji kontrolovat https certifikat
#na lokalni instalaci jsem mel s timto problem, proto pro lokalni instalaci
#doporucuji nastavit na False. Default je na True
verify_ssl = True