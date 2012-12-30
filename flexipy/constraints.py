"""
This module implements constraints for certain fields.
I found it as elegant for checking input args if they comply
to Flexibee's constraints
:copyright: (c) 2012 by Jakub Ječmínek.
:license: BSD, see LICENSE for more details.
"""

def __constraint_string_size(name,min,max):
	"""Univerzalni constraint pro stringy, ktery
	kontroluje zda vstupni string ma odpovidajici delku
	:param name: name of arg to be checked
	:param min: minimum Size
	:param max: maximum size
	"""

	def closure(x):
		"""
		closure for actual checking
		:param x: input string 
		"""
		if len(x) < min or len(x) > max:
			raise ValueError('Size of string '+name+' must be in interval <'+min+';'+max+'>.')

	return closure	

#checking if kod is ok
kod_constraint_check = __constraint_string_size('kod',0,20)

common_string_constraint_check = __constraint_string_size('',0,255)