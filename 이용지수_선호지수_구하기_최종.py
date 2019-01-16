# Load data

import pandas as pd
data_1=pd.read_csv("01Product.csv")
data_2=pd.read_csv("02Search1.csv")  
data_3=pd.read_csv("03Search2.csv")
data_4=pd.read_csv("04Custom.csv")
data_5=pd.read_csv("05Session.csv")
data_6=pd.read_csv("06Master.csv")


# Session data

import numpy as np

a_data = data_1[['CLNT_ID','HITS_SEQ','SESS_ID','PD_C']]
b_data = data_5[['CLNT_ID','SESS_ID','TOT_PAG_VIEW_CT','TOT_SESS_HR_V']]
c_data = data_6[['PD_C','CLAC1_NM']]

data = a_data.merge(b_data, on=['CLNT_ID','SESS_ID'], how='inner')
data=data.merge(c_data, on=['PD_C'], how='inner')

# Data preprocessing
data['HITS_SEQ']=data['HITS_SEQ'].astype(float)
data['TOT_PAG_VIEW_CT']=data['TOT_PAG_VIEW_CT'].astype(float)
data['TOT_SESS_HR_V']=data['TOT_SESS_HR_V'].astype(str)
data['TOT_SESS_HR_V']=data['TOT_SESS_HR_V'].str.replace(',', '')
data['TOT_SESS_HR_V']=data['TOT_SESS_HR_V'].astype(float)
data['TOT_PAG_VIEW_CT']=data['TOT_PAG_VIEW_CT'].astype(str)
data['TOT_PAG_VIEW_CT']=data['TOT_PAG_VIEW_CT'].str.replace(',', '')
data['TOT_PAG_VIEW_CT']=data['TOT_PAG_VIEW_CT'].astype(float)


# Pivot table
pivot_1=pd.pivot_table(data,index=['CLNT_ID','CLAC1_NM'],values=['HITS_SEQ','TOT_PAG_VIEW_CT','TOT_SESS_HR_V'],aggfunc=np.sum,fill_value=0)

pivot_2=pd.pivot_table(data,index=['CLAC1_NM'],values=['HITS_SEQ','TOT_PAG_VIEW_CT','TOT_SESS_HR_V'],aggfunc=np.sum,fill_value=0)

# reset index
pivot_1_1=pivot_1.reset_index()
pivot_2_1=pivot_2.reset_index()

# rename columns
pivot_2_1_rename = pivot_2_1.rename(columns = {'HITS_SEQ': 'HITS_SEQ_CLAC','TOT_PAG_VIEW_CT':'TOT_PAG_VIEW_CT_CLAC','TOT_SESS_HR_V':'TOT_SESS_HR_V_CLAC'})

merge_1 = pd.merge(pivot_1_1,pivot_2_1_rename,on='CLAC1_NM',how = 'left')

merge_1['HITS_SEQ_index']=merge_1['HITS_SEQ'].div(merge_1['HITS_SEQ_CLAC'])
merge_1['TOT_PAG_VIEW_CT_index']=merge_1['TOT_PAG_VIEW_CT'].div(merge_1['TOT_PAG_VIEW_CT_CLAC'])
merge_1['TOT_SESS_HR_V_index']=merge_1['TOT_SESS_HR_V'].div(merge_1['TOT_SESS_HR_V_CLAC'])

merge_1['SESS_INDEX_SUM']=merge_1['HITS_SEQ_index'].add(merge_1['TOT_PAG_VIEW_CT_index'])

merge_1['SESS_INDEX_SUM_2']=merge_1['SESS_INDEX_SUM'].add(merge_1['TOT_SESS_HR_V_index'])

merge_1['SESS_INDEX_SUM_2_aa']=merge_1['SESS_INDEX_SUM_2'].mul(1000)

merge_1_INDEX=merge_1[['CLNT_ID','CLAC1_NM','SESS_INDEX_SUM_2_aa']]

merge_1_INDEX


# Buy-Count data

a_data_1 = data_1[['CLNT_ID','PD_BUY_CT','SESS_ID','PD_C']]
c_data_1 = data_6[['PD_C','CLAC1_NM']]

data_11=a_data_1.merge(c_data_1, on=['PD_C'], how='inner')

data_11_need = data_11[['CLNT_ID','CLAC1_NM','PD_BUY_CT']]

data_11_need['PD_BUY_CT']=data_11_need['PD_BUY_CT'].astype(str)
data_11_need['PD_BUY_CT']=data_11_need['PD_BUY_CT'].str.replace(',', '')
data_11_need['PD_BUY_CT']=data_11_need['PD_BUY_CT'].astype(float)

CLAC_sum=data_11_need.PD_BUY_CT.groupby(data_11_need.CLAC1_NM).sum()

CLAC_sum_df=pd.DataFrame(CLAC_sum)

CLAC_sum_df_1=CLAC_sum_df.reset_index()

CLNT_CLAC_sum=data_11_need.PD_BUY_CT.groupby([data_11_need['CLNT_ID'],data_11_need['CLAC1_NM']]).sum()

CLNT_CLAC_sum_df=pd.DataFrame(CLNT_CLAC_sum)

CLNT_CLAC_sum_df_1=CLNT_CLAC_sum_df.reset_index()

CT_data=pd.merge(CLNT_CLAC_sum_df_1,CLAC_sum_df_1,on=['CLAC1_NM'],how='left')

CT_data['CT_index']=CT_data['PD_BUY_CT_x'].div(CT_data['PD_BUY_CT_y'])

CT_data['CT_index_1']=CT_data['CT_index'].mul(1000)

CT_data_need=CT_data[['CLNT_ID','CLAC1_NM','CT_index_1']]

final_index=pd.merge(CT_data_need,merge_1_INDEX,on=['CLNT_ID','CLAC1_NM'],how='inner')

final_index['Total_index']=final_index['CT_index_1'].add(final_index['SESS_INDEX_SUM_2_aa'])

final_index_need=final_index[['CLNT_ID','CLAC1_NM','Total_index']]

final_index


## Final Usage index

final_index_need


## Preference Index

ddata_1 = pd.pivot_table(final_index_need, index = 'CLNT_ID',values='Total_index',columns='CLAC1_NM',aggfunc='mean')

ddata_1.reset_index()

collist=[]
for factor in ddata_1.columns:
    collist.append(factor)

ddata_1['total']=ddata_1.loc[:,collist].sum(axis=1)

ddata_1_copy = ddata_1.copy()

for col in collist:
    ddata_1_copy[col]=ddata_1_copy[col].div(ddata_1_copy['total'])

dfdf=pd.DataFrame(ddata_1_copy)

prefer_index_df=dfdf.reset_index()

prefer_index_df



prefer_index_df.to_csv("prefer_index.csv")
