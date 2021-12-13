

import pandas as pd 
import seaborn as sns


df = pd.read_csv("out.csv")


for i in range(len(df['Width'].index)):
    val = df['Width'].iloc[i]
    val = str(val)
    maxNum = 0
    nl = [i for i,c in enumerate(val) if c.isdigit()]
    if len(nl) == 0: 
        df['Width'].iloc[i] = 0
        continue
    fnum = min(nl)
    enum = max(nl)
    val = val[fnum:enum+1]
    if len(val.split(' ')) == 1:
        if '/' in val:
            num = float(val.split(' ')[0].split('/')[0]) / float(val.split(' ')[0].split('/')[1])
        else:
            num = int(val)
    else:
        num = int(val.split(' ')[0])
        frac = val.split(' ')[-1]
        if '/' in frac:
            num += float(frac.split('/')[0]) / float(frac.split('/')[-1])
    df['Width'].iloc[i] = num



for i in range(len(df['Height'].index)):
    val = df['Height'].iloc[i]
    val = str(val)
    maxNum = 0
    nl = [i for i,c in enumerate(val) if c.isdigit()]
    if len(nl) == 0: 
        df['Height'].iloc[i] = 0
        continue
    fnum = min(nl)
    enum = max(nl)
    val = val[fnum:enum+1]
    if len(val.split(' ')) == 1:
        if '/' in val:
            num = float(val.split(' ')[0].split('/')[0]) / float(val.split(' ')[0].split('/')[1])
        else:
            num = int(val)
    else:
        num = int(val.split(' ')[0])
        frac = val.split(' ')[-1]
        if '/' in frac:
            num += float(frac.split('/')[0]) / float(frac.split('/')[-1])
    df['Height'].iloc[i] = num





for i in range(len(df['Height'].index)):
    val = df['Height'].iloc[i]
    val = str(val)
    maxNum = 0
    nl = [i for i,c in enumerate(val) if c.isdigit()]
    if len(nl) == 0: 
        df['Height'].iloc[i] = 0
        continue
    fnum = min(nl)
    enum = max(nl)
    val = val[fnum:enum+1]
    if len(val.split(' ')) == 1:
        if '/' in val:
            num = float(val.split(' ')[0].split('/')[0]) / float(val.split(' ')[0].split('/')[1])
        else:
            num = int(val)
    else:
        num = int(val.split(' ')[0])
        frac = val.split(' ')[-1]
        if '/' in frac:
            num += float(frac.split('/')[0]) / float(frac.split('/')[-1])
    df['Height'].iloc[i] = num



print(df)
df.to_csv("out3.csv")