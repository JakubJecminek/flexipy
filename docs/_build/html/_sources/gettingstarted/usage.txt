Jak používat flexipy
====================

Flexipy je především určeno k usnadnění napojení informačního systému(napsaného například v Djangu nebo Flask frameworku) na REST API systému Flexibee. Flexibee je poměrně komplexní nástroj ve kterém se dá mnoho věcí nastavit a případně upravit dle požadavků. 
Flexipy se naopak snaží odstínit tuto komplexitu a poskytnout maximální možný komfort pro programátora. Momentálně flexipy nepodporuje všechny evidence a všechny možnosti Flexibee, ale přes to základní práce s fakturami a dalšími položkami je téměř hotová. 
Flexipy je navrhnuto tak, aby bylo maximálně konfigurovatelné a přizpůsobívé konkrétním potřebám. Zde uvedu základní postupy jak si flexipy natavit a na které věci je třeba dát pozor. 

.. _config-file:

Nastavení konfiguračního souboru flexipy
========================================

Flexipy využívá defaultně konfigruační soubor flexipy.conf, který obsahuje všechna nastavení potřebná pro správnou práci flexipy. K tomuto 
konfiguračnímu souboru knihovna přistupuje skrze třídu Config z modulu config.py, který využívá standartní třídu ConfigParser pro práci s flexipy.conf.
Flexipy defaultně obsahuje ještě další konfigurační soubory, například test_flexipy.conf je konfigurační soubor určen pro testování. demo_flexibee.conf obsahuje 
nastavení pro komunikaci s demo isntalací Flexibee na serveru demo.flexibee.eu. Jakékoliv třídě, která reprezentuje nějakou evidenci můžete při inicializaci vložit 
svoji konfiguraci. Stačí pokud vytvoříte podle defaultního konfiguračního souboru svoji konfiguraci. Můžete tajé vytvořit potomka třídy Config jakým je například třída TestingConfig. 
Pro takto vzniklého potomka si můžete definovat vlastní metody, které potřebujete nebo pouze překrýt již existující metody z předka. Objekt zakto vzniklé třídy poté vložte jako argument konstruktoru dané třídy.::
	
	>>> from flexipy import config, Faktura
	>>> my_conf = config.TestingConfig()
	>>> faktura = Faktura(my_conf)

Konstruktor třídy Config obsahuje nepovinný parametr, který specifikujeme cestu ke konfiguračnímu souboru. Defaultně je vždy nastaven na konfigurační soubor, který je pro danou třídu jako default. Například pro rodičovskou(defaultní) třídu Config je to flexipy.cong pro TestingConfig je to test_flexipy.conf. 
 
Nastavení ve flexipy.conf odpovídají instalaci Flexibee serveru na mém stroji, proto je nutné si vytvořit vlastní konfigurační soubor dle Vaší situace. To můžete provést buď tak, že přímo editujete danný soubor(který je ve formátu INI odpovídajícího RFC 822), nebo můžete 
využít metod třídy ConfigParser a měnit flexipz.conf přímo z shellu::
	
	>>> from ConfigParser import SafeConfigParser
	>>> from pkg_resources import Requirement, resource_filename	
	>>> import codecs #nektera nastaveni vyzaduji unicode
	>>> conf = SafeConfigParser()
	>>> filename = resource_filename(Requirement.parse("flexipy"),"flexipy/flexipy.conf") #vyuziva resource management api 
	>>> with codecs.open(filename, 'a+', encoding='utf-8') as f: conf.readfp(f)
	>>> conf.add_section('moje_sekce') #pridani sekce [moje_sekce]
	>>> conf.set('moje_sekce', 'popisek', 'hodnota') # vlozi do sekce moje_sekce par klic/hodnota popisek=hodnota
	>>> conf.write(filename) # ulozime zmeny


Základní použití knihovny
=========================

Knihovna je strukturovaná způsobem kdy každá evidence ve Flexibee je reprezentována třídou, která zapouzdřuje funkcionalitu pro danou evidenci. Pro práci s flexipy tedy stačí pouze 
importovat knihovnu a dále pracovat už jen s třídami, které jsou definovány v api::

	>>> import flexipy
	>>> faktura = flexipy.Faktura()
	>>> faktura.delete_vydana_faktura(id=1)

Kompletní seznam tříd, které momentálně flexipy nabízí se nachází v api.py. 	

Systém vnitřních vazeb
======================

Systém vniřních vazeb, který používá Flexibee je podrobně vysvětlen v oficiální `http://www.flexibee.eu/api/doc/ref/internal-dependencies dokumentaci`. V podstatě jde o to, že pokud například vytvářím fakturu, tak musím uvést informace o odběrateli(jméno firmy, adresa atd.). Flexibee ale umožňuje tento proces zjednodušit kdy si firmu zadefiunuju v adresáři a přiřadím ji nějaký unikátní kód. Poté pouze při vytváření faktury uvedu 'firma':'code:<kodfirmy>' a ostatní položky se automaticky doplní z adresáře. Takových to položek je ve Flexibee více a snahou při vývoji flexipy bylo začlenit toto usnadnění do knihovny. Proto v flexipy.conf se nachází několik listů, které je třeba doplnit o Vámi vytvořené typy dokladů, firem atd. Komentáře nad každým tímto seznamem Vám napoví o kterou položku se jedná a jak ji vyplnit. V config-example.py se nachází pouze u každé položky defaultní hodnoty které najdete v čisté instalaci Flexibee serveru(například pouze základní faktura), zbytek je třeba doplnit dle Vašich konkrétních potřeb a stavu Flexibee.

Jak použit config soubor::


	>>> import flexipy
	>>> from flexipy import config
	>>> c = config.Config('mojeKonfigurace.conf') #vlozim vlastni conf soubor
	>>> faktura = flexipy.Faktura(c) #objekt faktura nainicializuji svym konfiguracnim souborem
	>>> #faktura nyni obsahuje instanci tridy Config a muzu k ni pristupovat prez faktura.conf
	>>> faktura.create_vydana_faktura(kod='flex11', var_sym='11235484', datum_vyst='2013-02-28', zdroj_pro_sklad=False, typ_dokl=faktura.conf.get_typy_faktury_vydane()[0], dalsi_param=dalsi_param)