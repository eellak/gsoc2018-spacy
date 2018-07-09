from __future__ import unicode_literals
from ...errors import Errors, Warnings, deprecation_warning
from ..tokens import Doc
import regex as re

class GreekTokenizer:
	def __init__(self, vocab, rules=None, prefix_search=None, suffix_search=None, infix_finditer=None, token_match=None):
		self.token_match = token_match
		self.prefix_search = prefix_search
		self.suffix_search = suffix_search
		self.infix_finditer = infix_finditer
		self.vocab = vocab
		self._rules = {}
		if rules is not None:
			for chunk, substrings in sorted(rules.items()):
				self._rules[chunk] = substrings
	def __call__(self, string):
		if (len(string) >= (2**30)):
			raise ValueError(Errors.E025.format(length=len(string)))
		tokens = self.tokenize(string)
		return Doc(self.vocab, tokens)
	def tokenize(self, text):
		tokens = []
		for substring in text.split(' '):
			suffixes = []
			while (substring):
				if substring in self._rules:
					tokens.extend(self._rules[substring])
					substring = ''
				elif self.find_prefix(substring) is not None:
					split = self.find_prefix(substring)
					tokens.append(substring[:split])
					substring = substring[split:]
				elif self.find_suffix(substring) is not None:
					split = self.find_suffix(substring)
					suffixes.append(substring[split:])
					substring = substring[:split]
				elif self.find_infix(substring):
					infixes = find_infix(substring)
					offset = 0
					for match in infixes:
						tokens.append(substring[offset : match.start()])
						tokens.append(substring[match.start() : match.end()])
						offset = match.end()
					substring = substring[offset:]
				else:
					tokens.append(substring)
					substring =  ''
			tokens.extend(reversed(suffixes))
		return tokens
	def find_infix(self, string):
		if self.infix_finditer is None:
			return 0
		return list(self.infix_finditer(string))
	def find_prefix(self, string):
		if (self.prefix_search is None):
			return 0
		match = self.prefix_search(string)
		return (match.end() - match.start()) if match is not None else 0
	def find_suffix(self, string):
		if (self.suffix_search is None):
			return 0
		match = self.suffix_search(string)
		return (match.end() - match.start()) if match is not None else 0
