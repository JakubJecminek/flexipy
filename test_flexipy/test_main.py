# -*- coding: utf-8 -*-

from flexipy import main


def test_validate_item():	

	valid_params = {'doprava':'','duzpPuv':'','zavTxt':''}
	#valid_params by meli projit validaci a vrati (True,None)
	expected_valid = (True, None)
	assert main.__validate_params(valid_params, 'faktura-vydana') == expected_valid
	invalid_params = {'doprava':'','duzpaPuv':'','zaveTxt':''}
	expected_invalid = (False, ['duzpaPuv','zaveTxt'])
	assert main.__validate_params(invalid_params, 'faktura-vydana') == expected_invalid


