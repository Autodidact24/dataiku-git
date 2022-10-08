# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from fastdownload import download_url
from fastcore.all import *
from time import sleep

# Read recipe inputs
clean_air_or_not = dataiku.Folder("TPQ6w2ke")
clean_air_or_not_info = clean_air_or_not.get_info()

from duckduckgo_search import ddg_images
from fastcore.all import *
from fastai.vision.all import *

def search_images(term, max_images=200): return L(ddg_images(term, max_results=max_images)).itemgot('image')

searches = 'clean air skyline', 'polluted air skyline'
path = dataiku.Folder("Dv0sfj8P"), dataiku.Folder("rZHKyy2U")

print(dataiku.Folder("Dv0sfj8P").get_path())
for o, p in zip(searches, path):
    dest = (Path(p.get_path())/o)
    
    dest.mkdir(exist_ok=True, parents=True)
    download_images(dest, urls=search_images(f'{o} photo'))
    sleep(10)  # Pause between searches to avoid over-loading server
    download_images(dest, urls=search_images(f'{o} aqi'))
    sleep(10)
    download_images(dest, urls=search_images(f'{o} buildings'))
    sleep(10)
    resize_images(Path(p.get_path())/o, max_size=400, dest=Path(p.get_path())/o)

# Write recipe outputs
clean_air = dataiku.Folder("Dv0sfj8P")
clean_air_info = clean_air.get_info()
polluted_air = dataiku.Folder("rZHKyy2U")
polluted_air_info = polluted_air.get_info()