# -*- coding: utf-8 -*-

from flexipy import main
import pytest

def test_validate_item():	
	invalid_params = {'doprava':'','duzpaPuv':'','zaveTxt':''}	
	pytest.raises(main.FlexipyException,main.__validate_params, invalid_params, 'faktura-vydana') 


