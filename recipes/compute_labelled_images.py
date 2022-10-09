# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
clean_air = dataiku.Folder("ep3MDqmT")
polluted_air = dataiku.Folder("EP5fW8G4")

paths = dataiku.Folder("ep3MDqmT").get_path(), dataiku.Folder("EP5fW8G4").get_path()
# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.


LABEL_0 = "clean_air"
LABEL_1 = "polluted_air"

image_labels_df = pd.DataFrame(columns=['path', 'label'])
for i,j in enumerate(paths):
    if LABEL_0 in j:
        image_labels_df.loc[i] = [j[1:], LABEL_0]
    if LABEL_1 in j:
        image_labels_df.loc[i] = [j[1:], LABEL_1]



# Write recipe outputs
image_labels = dataiku.Dataset("labelled_images")
image_labels.write_with_schema(image_labels_df)
