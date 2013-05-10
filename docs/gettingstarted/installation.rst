=========
Instalace
=========

.. note:: *Rada*

    Pokud to je pro Vás možné, pracujte na projektu na Unix-based systému,
    protože to je systém, který nejvíce vývojářu používá a je nejméně 
    pravděpodobné, že by jste narazili na nějaké větší problémy při 
    instalaci knihovny. Pokus jste na Windows doporučuji navštívit stránky projektu 
    `Vagrant <http://www.vagrantup.com/>`_


.. highlight:: bash


1. Get the code
===============

Aktuální kód se nacházi v `git repozitáři <https://www.assembla.com/code/flexipy/git/nodes>`_

::

    $ git clone git@git.assembla.com:flexipy.git

``git@git.assembla.com:flexipy.git`` je hlavní rewpozitář. Požádejte 
:ref:`project-maintainer` pro získání přístupu. Mezitím, můžete získat kód
skrze Public clone URL:

``git://git.assembla.com/flexipy.git``


2. Vytvoření virtualenv(doporučený krok)
========================================

Virtualenv_ je nástroj pro vytváření oddělených python prostředí. Umožňuje Vám instalovat python package bez zanášení hlavního python prostředí Vašeho OS.

Nejdříve je nutné virtuaelnv nainstalovat_ na Váš systém, pokud jej již nemáte.

Poté vytvořte virtuální prostředí pro flexipy takto::

    $ virtualenv flexipy-env 

Kde ``flexipy-env`` je adresář, ve kterém virtualenv bude vytvořeno. Může se nacházet kdekoliv (ale nevytvářejte virtualenv uvnitř repozitáře, aby nedošlo náhodnému komitnutí).

Pro využívání virtuálního prostředí je nutné ho aktivovat::

    $ . flexipy-env/bin/activate

Pro deaktivaci zadejte::

    $ deactivate

(V jakékoliv složce)

.. note::

    Toto se liší pokud jste na Windows, viz `virtualenv
    documentation`_.



.. _Virtualenv: http://pypi.python.org/pypi/virtualenv
.. _install: http://pypi.python.org/pypi/virtualenv
.. _virtualenv documentation: http://pypi.python.org/pypi/virtualenv


3. Nainstalujte python balíčky
==============================

Běžte do repozitáře, které jste si stáhli(git clone) v prvním kroku (s virtualenv aktivovanám, pokud ho 
využíváte)::

    $ cd flexipy

Nainstalujte balíčky potřebné pro projekt::

    $ python setup.py develop

A nainstalujte další závislosti(tyto závislosti nejsou nutné pro používání knihovny ale jsou určeny pro vývoj a testování a dokumentaci)::

    $ paver install_dependencies


4. Update your development settings
===================================

Ve složce flexipy se nachazi soubor flexipy.conf. Tento soubor slouží jako ukázkový a zároveň defaultní konfigurační soubor(pokud nespecifikujete jinak načte se tento soubor), tento soubor si skopírujte a vytvořte podle něj svůj vlastní konfigurační soubor dle svých potřeb. Konfigurační soubor se dá upravit buď textovým editorem(je ve stadartním formátu ini), nebo lze interaktivně upravit pomocí metod, které nabízí třída ConfigParser. Více se dočtete v :ref:`config-file`.
Především je nutné nastavit proměnné host, firma, username a password, díky tomu bude knihovna schopn komunikovat s Vaším Flexibee serverem. 

5. Run the tests
================

Tento projekt používá knihovnu pytest pro testování, testy spustíte příkazem::

    $ paver test
    