Jak používat flexipy
====================

Flexipy je především určeno k usnadnění napojení informačního systému(napsaného například v Djangu nebo Flask frameworku) na REST API systému Flexibee. Flexibee je poměrně komplexní nástroj ve kterém se dá mnoho věcí nastavit a případně upravit dle požadavků. 
Flexipy se naopak snaží odstínit tuto komplexitu a poskytnout maximální možný komfort pro programátora. Momentálně flexipy nepodporuje všechny evidence a všechny možnosti Flexibee, ale přes to základní práce s fakturami a dalšími položkami je téměř hotová. 
Flexipy je navrhnuto tak, aby bylo maximálně konfigurovatelné a přizpůsobívé konkrétním potřebám. Zde uvedu základní postupy jak si flexipy natavit a na které věci je třeba dát pozor. 

.. _config-file:

Nastavení konfiguračního souboru flexipy
========================================

Flexipy využívá konfigruační soubor config.py, který obsahuje všechna nastavení potřebná pro správnou práci flexipy. 
Flexipy obsahuje šablonu konfiguračního souboru flexipy/config_example.py která obsahuje všechny možná nastavení. 
Nastavení odpovídají demo instalaci Flexibee serveru na demo.flexibee.eu. Je nutné před samotným použitím flexipy si vytvořit ve 
složce flexipy/ vlastní soubor config.py takovým způsobem, že skopírujete config-example.py a pouze upravíte hodnoty, které potřebujete 
dle Vaší situace::
	
	$ cp config_example.py cofig.py 	#nutné být ve složce flexipy/


Základní použití knihovny
=========================

Knihovna je strukturovaná podobným způsobem jako známá knihovna requests. Pro práci s flexipy tedy stačí pouze 
importovat knihovnu a dále pracovat už jen s api::

	>>> import flexipy
	>>> flexipy.delete_vydana_faktura(id=1)

Kompletní api se nachází v api.py. 	

Systém vnitřních vazeb
======================

Systém vniřních vazeb, který používá Flexibee je podrobně vysvětlen v oficiální `http://www.flexibee.eu/api/doc/ref/internal-dependencies dokumentaci`. V podstatě jde o to, že pokud například vytvářím fakturu, tak musím uvést informace o odběrateli(jméno firmy, adresa atd.). Flexibee ale umožňuje tento proces zjednodušit kdy si firmu zadefiunuju v adresáři a přiřadím ji nějaký unikátní kód. Poté pouze při vytváření faktury uvedu 'firma':'code:<kodirmy>' a ostatni polozky se automaticky doplni z adresare. Takových to položek je ve Flexibee více a snahou při vývoji flexipy bylo začlenit toto usnadnění do knihovny. Proto v config.py se nachází několik listů, které je třeba doplnit o Vámi vytvořené typy dokladů, firem atd. Komentáře nad každým tímto seznamem Vám napoví o kterou položku se jedná a jak ji vyplnit. V config-example.py se nachází pouze u každé položky defaultní hodnoty které najdete v čisté instalaci Flexibee serveru(například pouze základní faktura), zbytek je třeba doplnit dle Vašich konkrétních potřeb a stavu Flexibee.

Jak použit config soubor::


	>>> import flexipy
	>>> from flexipy import config
	>>> flexipy.create_vydana_faktura(kod='flex11', var_sym='11235484', datum_vyst='2013-02-28', zdroj_pro_sklad=False, typ_dokl=config.typ_faktury_vydane[0], dalsi_param=dalsi_param)