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
                self._rules[chuck] = substrings


    def __call__(self, string):
    	if len(string) >= (2 ** 30):
            raise ValueError(Errors.E025.format(length=len(string)))
        tokens = tokenize(self,string)
        return Doc(self.vocab, tokens)

    def tokenize(self,text):
		tokens = []
	    for substring in text.split(' '):
	        suffixes = []
	        while substring:
	            if substring in self._rules:
	                tokens.extend(self._rules[substring])
	                substring = ''
	            elif find_prefix(substring) is not None:
	                split = find_prefix(substring)
	                tokens.append(substring[:split])
	                substring = substring[split:]
	            elif find_suffix(substring) is not None:
	                split = find_suffix(substring)
	                suffixes.append(substring[split:])
	                substring = substring[:split]
	            elif find_infix(substring):
	                infixes = find_infix(substring)
	                offset = 0
	                for match in infixes:
	                    tokens.append(substring[offset : match.start()])
	                    tokens.append(substring[match.start() : match.end()])
	                    offset = match.end()
	                substring = substring[offset:]
	            else:
	                tokens.append(substring)
	                substring = ''
	        tokens.extend(reversed(suffixes))
	    return tokens


    def find_infix(self, unicode string):
        """Find internal split points of the string, such as hyphens.

        string (unicode): The string to segment.
        RETURNS (list): A list of `re.MatchObject` objects that have `.start()`
            and `.end()` methods, denoting the placement of internal segment
            separators, e.g. hyphens.
        """
        if self.infix_finditer is None:
            return 0
        return list(self.infix_finditer(string))

    def find_prefix(self, unicode string):
        """Find the length of a prefix that should be segmented from the
        string, or None if no prefix rules match.

        string (unicode): The string to segment.
        RETURNS (int): The length of the prefix if present, otherwise `None`.
        """
        if self.prefix_search is None:
            return 0
        match = self.prefix_search(string)
        return (match.end() - match.start()) if match is not None else 0

    def find_suffix(self, unicode string):
        """Find the length of a suffix that should be segmented from the
        string, or None if no suffix rules match.

        string (unicode): The string to segment.
        Returns (int): The length of the suffix if present, otherwise `None`.
        """
        if self.suffix_search is None:
            return 0
        match = self.suffix_search(string)
        return (match.end() - match.start()) if match is not None else 0
