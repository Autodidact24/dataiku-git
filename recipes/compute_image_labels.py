# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
clean_air = dataiku.Folder("ep3MDqmT")
polluted_air = dataiku.Folder("EP5fW8G4")


# Compute recipe outputs
# TODO: Write here your actual code that computes the outputs
# NB: DSS supports several kinds of APIs for reading and writing data. Please see doc.



image_labels_df = pd.DataFrame(columns=['image', 'label'])
for folder in (clean_air, polluted_air):
    for i, image in enumerate(folder.list_paths_in_partition()):
        image_labels_df.loc[i] = [image[1:], folder.get_name()]


# Write recipe outputs
image_labels = dataiku.Dataset("image_labels")
image_labels.write_with_schema(image_labels_df)
