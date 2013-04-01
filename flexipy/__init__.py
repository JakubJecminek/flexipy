# -*- coding: utf-8 -*-

"""
Knihovna flexipy pro snadnou praci s REST API systemu Flexibee.
Pro ukazku pouziti se podivejte do dokumentace ve slozce docs.

:copyright: (c) 2012 Jakub Ječmínek.
:license: BSD, soubor LICENSE obsahuje kopii license.
"""
from .api import create_vydana_faktura, create_prijata_faktura, create_bank_doklad\
,get_all_vydane_faktury, get_all_prijate_faktury, get_vydana_faktura, get_vydana_faktura_by_code\
,get_prijata_faktura, get_prijata_faktura_by_code, get_all_bank_doklady, get_bank_doklad\
,get_bank_doklad_by_code, get_adresar, get_adresar_by_code, get_template_dict, delete_adresar\
,delete_bank_doklad, delete_vydana_faktura, delete_prijata_faktura, update_vydana_faktura\
,update_prijata_faktura, update_bank_doklad, get_faktura_vydana_pdf_url, get_faktura_prijata_pdf_url

