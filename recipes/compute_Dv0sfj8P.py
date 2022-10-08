# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
clean_air_or_not = dataiku.Folder("TPQ6w2ke")
clean_air_or_not_info = clean_air_or_not.get_info()

from duckduckgo_search import ddg_images
from fastcore.all import *

def search_images(term, max_images=200): return L(ddg_images(term, max_results=max_images)).itemgot('image')


# Write recipe outputs
clean_air = dataiku.Folder("Dv0sfj8P")
clean_air_info = clean_air.get_info()
polluted_air = dataiku.Folder("rZHKyy2U")
polluted_air_info = polluted_air.get_info()
