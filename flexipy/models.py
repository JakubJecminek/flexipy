# -*- coding: utf-8 -*-

"""
In this file are definitions of models which are used by Flexibee. This module is 
using great library micromodels which makes extremely easy to work with json and serialize
python objects.
:copyright: (c) 2012 by Jakub Ječmínek.
:license: BSD, see LICENSE for more details.
"""

import micromodels

doklTyp = ('code:FAKTURA','code:ZDD',u"code:ZÁLOHA")
stavUhrVal = ('stavUhr.castUhr','stavUhr.uhrazenö́','stavUhr.uhrazenoRucne')
stavMailVal = {'neodesilat':'stavMail.neodesilat','odeslat':'stavMail.odeslat','odeslat':'stavMail.odeslano'}

class Adresar(micromodels.Model):
	kod = micromodels.CharField()
	nazev = micromodels.CharField()
	nazevA = micromodels.CharField()
	nazevB = micromodels.CharField()
	nazevC = micromodels.CharField()
	poznam = micromodels.CharField()
	popis = micromodels.CharField()
	platiOd = micromodels.IntegerField()	
	platiDo = micromodels.IntegerField()

class Faktura(micromodels.Model):
	"""Trida popisujici fakturu, nejsou uvedeny
	vsechny polozky viz 
	https://demo.flexibee.eu/c/demo/faktura-vydana/properties
	Polozky ktere nejsou uvedeny jsou automaticky spocteny z polozek.
	Dale nejsou uvedeny polozky ktere se vztahuji k firme, staci 
	uvest referenci na firmu a jsou vygenerovany automaticky.(z adresare)
	"""
	kod = micromodels.CharField()
	cisDosle = micromodels.CharField()
	varSym = micromodels.CharField()
	cisSml = micromodels.CharField()
	cisObj = micromodels.CharField()
	datObj = micromodels.DateField()
	cisDodak = micromodels.CharField()	
	doprava = micromodels.CharField()
	datVyst = micromodels.DateField()
	duzpPuv = micromodels.DateField()
	duzpUcto = micromodels.DateField()
	datSplat = micromodels.DateField()
	datTermin = micromodels.DateField()
	datReal = micromodels.DateField()
	popis = micromodels.CharField()
	poznam = micromodels.CharField()
	uvodTxt = micromodels.CharField()
	zavTxt = micromodels.CharField()
	sumOsv = micromodels.FloatField()
	#Celkova sleva na dokladu, ktera se aplikuje na vyslednou cenu.
	slevaDokl = micromodels.FloatField()
	#cislo bank. uctu
	buc = micromodels.CharField()
	iban = micromodels.CharField()
	bic = micromodels.CharField()
	bezPolozek = micromodels.BooleanField()
	#Snizena sazba DPH
	szbDphSniz = micromodels.FloatField()
	#zakladni sazba DPH
	szbDphZakl = micromodels.FloatField()
	#misto plneni tuzemsko
	uzpTuzemsko = micromodels.BooleanField()
	#datum zauctovani
	datUcto = micromodels.DateField()
	vyloucitSaldo = micromodels.BooleanField()
	#poviny field muze nabyvat pouze hodnot v doklTyp
	typDokl = micromodels.CharField()
	mena = micromodels.CharField()
	konSym = micromodels.CharField()
	#dulezita relace, nutne uvest pro idealni vypleni ost. polozek
	firma = micromodels.CharField()
	stat = micromodels.CharField()
	faStat = micromodels.CharField()
	mistUrc = micromodels.CharField()
	#ucet odberatele
	banSpojDod = micromodels.CharField()
	bankovniUcet = micromodels.CharField()
	#nasleduji dalsi relace pro provazani s ostatnimi evidencemi
	statDph = micromodels.CharField()
	stredisko = micromodels.CharField()
	cinnost = micromodels.CharField() 
	zakazka = micromodels.CharField()
	dodPodm = micromodels.CharField()
	#relace:obchodni transakce 
	obchTrans = micromodels.CharField()
	#relace na kontaktni osobu z firmy firma
	#vyplni se jeji jmeno, email atd
	kontaktOsoba = micromodels.CharField()
	#nasledujici tri fieldy jsou relace tykajici se dph
	sazbaDphOsv = micromodels.CharField()
	sazbaDphSniz = micromodels.CharField()
	sazbaDphZakl = micromodels.CharField()
	#realce tykajici se smlouvy
	smlouva = micromodels.CharField()
	#datum upominky 1 a 2
	datUp1 = micromodels.DateField()
	datUp2 = micromodels.DateField()
	#datum smiru a penalizace
	datSmir = micromodels.DateField()
	datPenale = micromodels.DateField()
	#forma uhrady
	formaUhradyCis = micromodels.CharField()
	#stav uhrady
	#mozne hodnoty jsou v stavUhrVal
	stavUhrK = micromodels.CharField()
	#jiz uhrazeno preplatky
	juhSumPp = micromodels.CharField()
	#stav mailu mozne hodnoty v stavMailVal
	stavMailK = micromodels.CharField()
	#muze byt nekolik polozek faktury
	#polozkyFaktury = micromodels.ModelCollectionField(PolozkaFaktury)


class PolozkaFaktury(micromodels.Model):
	pass