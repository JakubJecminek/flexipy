# -*- coding: utf-8 -*-

from flexipy import invoice
import requests

def test_get_all_vydane_faktury():
	r = requests.get('https://demo.flexibee.eu/c/demo/faktura-vydana.json',auth=('winstrom','winstrom'))
	d = r.json()
	list_of_invoices_expected = d['winstrom']['faktura-vydana']
	list_of_invoices_actual = invoice.get_all_vydane_faktury()
	assert list_of_invoices_expected == list_of_invoices_actual

def test_get_all_prijate_faktury():
	r = requests.get('https://demo.flexibee.eu/c/demo/faktura-prijata.json',auth=('winstrom','winstrom'))
	d = r.json()
	list_of_invoices_expected = d['winstrom']['faktura-prijata']
	list_of_invoices_actual = invoice.get_all_prijate_faktury()
	assert list_of_invoices_expected == list_of_invoices_actual

