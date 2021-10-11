from keyword import iskeyword
from Global import data
import pytest

def test_attr():
	for x in data:
		assert x.isidentifier() and not iskeyword(x)

def test_data():
	for x in data.values():
		assert x.data