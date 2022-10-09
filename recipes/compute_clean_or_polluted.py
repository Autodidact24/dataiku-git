# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

from duckduckgo_search import ddg_images
from fastcore.all import *
from fastdownload import download_url
from fastai.vision.all import *

from time import sleep
from os import path


def search_images(term, max_images=200):
    return L(ddg_images(term, max_results=max_images)).itemgot('image')


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.

searches = 'clean air skyline','polluted air skyline'

paths = dataiku.Folder('clean_air').get_path(), dataiku.Folder('polluted_air').get_path()
paths = (Path(path) for path in paths)

for o,path in zip(searches, paths):
    dest = (path/o)
    dest.mkdir(exist_ok=True, parents=True)
    download_images(dest, urls=search_images(f'{o} photo', max_images=1))
    #sleep(10)  # Pause between searches to avoid over-loading server
    #download_images(dest, urls=search_images(f'{o} aqi'))
    #sleep(10)
    #download_images(dest, urls=search_images(f'{o} buildings'))
    #sleep(10)
    resize_images(path/o, max_size=400, dest=path/o)

#clean_or_polluted_df = ... # Compute a Pandas dataframe to write into clean_or_polluted


# Write recipe outputs
#clean_or_polluted = dataiku.Dataset("clean_or_polluted")
#clean_or_polluted.write_with_schema(clean_or_polluted_df)