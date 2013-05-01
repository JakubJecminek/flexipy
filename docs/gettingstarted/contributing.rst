Doporučení pro přispěvatele
===========================

V této části dokumentace uvádím návody a doporučení pro ty, kteří by měli zájem o rozšíření knihovny flexipy. Za každou pomoc 
budu jen rád :) a jsem otevřen jakýmkoliv návrhům na zlepšení. Navíc když jsem začal tuto knihovnu psát, bylo mi jasné, že nebudu schopen v krátké době implementovat podporu pro práci se všemi evidencemi a využívání všech možností Flexibe. Proto budu vděčný za pomoc s implementací dalších funkcionalit. 


.. _contributing-coding-style:

Coding style
------------

Doporučuji dodržovat `Django coding style <https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/>`_.

`PEP8`_ je oficiální přiručka pro psaní Python kódu a proto doporučuji všem potenciálním přispěvate si ji alespoň zběžně pročíst.

.. _PEP8: http://www.python.org/dev/peps/pep-0008/


.. _contributing-add-evidence:

Přídaní nové evidence
---------------------

Pokus chcete přidat funkcionalitu do flexipy, která bude sloužit k obsluze evidence ve Flexibee, která jesšte není zde implementovaná dodržujte prosím následující pravidla.

1. Všechny funkce, které nějakým způsobem souvisí s danou evidencí umístěte do souboru <jmeno_evidence>.py. Například pro adresář je to adresar.py.

2. Snažte se maximálně využívat jiř připravených generických funckí z modulu main.py. Například pro získání instance evidence zavolejte z modulu main funkci 
__get_evidence_item a pouze ošetřete nebo upravte věci, které vyžadujte pro danou evidenci.

3. Pro ošetřování chyb doporučuji používat systém, který je vidět v modulu invoice, kde se vyhazuje vyjímka FlexipyException v případě chyby nebo neočekávaného stavu. Případně do modulu exceptions přidejte vlastní vyjímku, která bude dědit FlexipyException.

4. Obecně by se dalo říci, že ideálně se stačí podívat na již implementovaný modul invoice a z něj vyjít při implementaci vlastního modulu.


.. _contributing-testing:

Testování
---------

Flexipy využívá `pytest <http://pytest.org/>`_ proto doporučuji projít si dokumentaci, která je na oficiálních stránkách projektu. Testy jsou izolovány pro každý modul, tzn. že pro modul invoice je testovací modul test_invoice. Pro psaní testů lze z výhodou použít knihovnu requests, kterou flexipy využívá. Pro spouštění testů je vytvořen paver task, takže stačí zavolat z rootu projektu příkaz::

	$ paver test