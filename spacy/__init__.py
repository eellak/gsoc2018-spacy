# coding: utf8
from __future__ import unicode_literals

from .cli.info import info as cli_info
from .glossary import explain
from .about import __version__
from .errors import Warnings, deprecation_warning
from . import util


def load(name, **overrides):
    depr_path = overrides.get('path')
    if depr_path not in (True, False, None):
        deprecation_warning(Warnings.W001.format(path=depr_path))
    return util.load_model(name, **overrides)


def blank(name, **kwargs):
    LangClass = util.get_lang_class(name)
    return LangClass(**kwargs)


<<<<<<< HEAD
def info(model=None, markdown=False):
    return cli_info(model, markdown)
=======
def info(model=None, markdown=False, silent=False):
    return cli_info(model, markdown, silent)
>>>>>>> 14d9007efd2ca457c6e6549d5599e460e198904c
