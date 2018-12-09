# -*- coding: utf-8 -*-

"""'_synthesis' module contains _synthesis functional interfaces."""

__author__ = "Yuan Chang"
__copyright__ = "Copyright (C) 2016-2018"
__license__ = "AGPL"
__email__ = "pyslvs@gmail.com"

from .collections import Collections, CollectionsDialog
from .structure_synthesis import StructureSynthesis
from .dimensional_synthesis import DimensionalSynthesis

__all__ = [
    'StructureSynthesis',
    'Collections',
    'CollectionsDialog',
    'DimensionalSynthesis'
]
