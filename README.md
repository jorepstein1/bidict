# bidict
A bi-directional dictionary implemented in Python based on built-in functions.

Supports all normal dict features such as retrieving an entry by
   sample_bidict['key'],

as well as iterating through the keys or values via
   iter(sample_bidict.keys())
   iter(sample_bidict.values())

Reverse use accessible by calling
   sample_bidict.get_key('value')
which returns a list of keys with values 'value'
