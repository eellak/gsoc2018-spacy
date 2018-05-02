from __future__ import unicode_literals


# These exceptions are used to add NORM values based on a token's ORTH value.


# Norms are only set if no alternative is provided in the tokenizer exceptions.


_exc={
	'αδερφός': 'αδελφός',
	'αδερφή': 'αδελφή',
	'αδέρφια': 'αδέλφια',
	'αδερφοί': 'αδελφοί',
	'ξάδερφος': 'ξάδελφος',
	'ξαδέρφη': 'ξαδέλφη',
	'ξαδέρφια': 'ξαδέλφια',
	'ξάδερφοι': 'ξάδελφοι',

}

BASE_NORMS = {
   
}