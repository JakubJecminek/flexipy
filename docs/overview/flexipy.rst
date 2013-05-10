=========
O flexipy
=========

Flexipy je knihovna v jazyce Python, jejíž účelem je ulehčit práci s REST API účetního systému Flexibee.

Systém Flexibee nabízí velmi propracované API pro vývojáře, kteří chtějí napojit Flexibee k nějakému jinému systému, 
nebo potřebují nějakým způsobem získávat z Flexibee data. 
API je ale velmi podrobné a práce s ním může ze začátku činit problémy. Z tohoto důvodu jsem se rozhodl napsat 
knihovnu v jazyku Python, která bude zjednodušovat práci s Flexibee. Další motivací bylo to, že díky této knihovně 
bude možné znovu použít části kódu, které se opakují. Knihovna také odchytává základní vyjímky a má jeden jednoduchý konfigurační soubor. 
Knihovna flexipy je vyvíjena v rámci mé bakalářské práce, která se zabývá implementací účetní komponenty(modulu) 
pro podporu sdílení aut(carsharing). Tento projekt je vyvíjen pod názvem Autonapůl.cz(dříve Metrocar) a jeho dokumentaci lze nalézt na `http://autonapul.cz/docs/`.

Pro více informací o REST API systému Flexibee doporučuji podrobnou `oficiální dokumentaci <http://www.flexibee.eu/api/>`_

.. note:: *Změna API knihovny od verze 0.4.0*
	
	Od verye 0.4.0 došlo ke změně API a kompletně byl přepracován systém knihovny a to jak pracuje. Hlavním důvodem pro tuto změnu byla zkušenost s 
	integrací fexipy do projektu Metrocar a hlavně fakt, že flexipy bylo poměrně obtížné testovat a konfigurovat ve spojení s jiným systémem. Proto nyní 
	nová verze je více flexibilnější a dá se mnohem snadněji konfigurovat. Pokud někoho zasáhla změna API tak se omlouvám, ale tato změna mi pomohla lépe integorvat flexipy 
	do mého projektu. Nebráním se žádné debatě či radě, ohledně vývoje, proto prosím v případě zájmu mi zašlete mail.