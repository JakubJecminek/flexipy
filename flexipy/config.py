# -*- coding: utf-8 -*-

"""
Zde se nachazi globalni nastaveni modulu.
Je treba zde nastavit nektere parametry(viz dokumentace).
Nektere promene je treba doplnit na zaklade faktickeho 
stavu z Flexibee. Napriklad doplnit typy faktur.
"""

#parametry pro nastaveni serveru na kterem bezi Flexibee
host='https://192.168.56.1:5434'
firma='autonapul'

#zaklad url pro requesty
url=host+'/c/'+firma+'/'

#autorizacni udaje k Flexibee
username='jecmijak'
password='Abyss17gabs=' 

#tuple obsahujici podporavene evidence se kterymi knihovna umi pracovat
evidence_list = ('faktura-vydana', 'banka', 'interni-doklad',
	'adresar','faktura-prijata','faktura-vydana-polozka',
	'faktura-prijata-polozka','typ-faktury-vydane','adresar-bankovni-ucet')

#nasleduji listy, ktere obsahuji polozky typu relation, ktere se nachazeji ve flexibee

#tato polozka se vyuziva u faktura-prijata, oznaceni typDokl
typ_faktury_prijate = ['FAKTURA', 'PR\xcdJEMKA','Z\xc1LOHA','ZDD']

#tato polozka se vyuziva u faktura-vydana, oznaceni typDokl
typ_faktury_vydane = ['FAKTURA','FAKT\xdaRA ESHOP','PREDFAKT\xdaRA','Z\xc1LOHA','ZDD']

#typDokl u banka
typ_bank_dokladu = ['BANKOVN\xcd \xda\u010cET 2','STANDARD']

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

#nastaveni zda requests maji kontrolovat https certifikat
verify_ssl = False