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
for folder in (clean_air, polluted_air):
    for i, image in enumerate(folder.list_paths_in_partition()):
        image_labels_df.iloc[i] = [image[1:], folder]


# Write recipe outputs
image_labels = dataiku.Dataset("image_labels")
image_labels.write_with_schema(image_labels_df)
