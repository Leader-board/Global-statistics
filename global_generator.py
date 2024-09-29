from pushtowiki import return_csv
from os import listdir
import pandas as pd

def concat_csv(folderloc):
    files = listdir(folderloc)
    ll = []
    for f in files:
        filename = folderloc + "/" + str(f)
        page_name = str(f)[:-4]
        df = return_csv(filename, page_name)
        ll.append(df)

    new_df = pd.concat(ll, ignore_index = True)

    return new_df.to_csv('/statdata/processed_csv/globalcontribs.csv', index=False, sep='|')