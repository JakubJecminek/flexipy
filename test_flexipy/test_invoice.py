# -*- coding: utf-8 -*-

from flexipy import invoice
import requests

def test_get_all_issued_invoices():
	r = requests.get('https://demo.flexibee.eu/c/demo/faktura-vydana.json?detail=full',auth=('winstrom','winstrom'))
	d = r.json()
	list_of_invoices_expected = d['winstrom']['faktura-vydana']
	list_of_invoices_actual = invoice.get_all_issued_invoices()
	assert list_of_invoices_expected == list_of_invoices_actual

	