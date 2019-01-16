# Coded by another team mem

# Load data
import pandas as pd

data = pd.read_csv("prefer_index.csv")
del data['Unnamed: 0']

# Summarization of data

summarize_data=data.describe()

# mean
summarize_data_mead = summarize_data.loc['mean']

summarize_data_mead_df=pd.DataFrame(summarize_data_mead)

summarize_data_mead_df

# load data of session date, session seq...
clnt_data = pd.read_csv("04Custom.csv")

data_merge=pd.merge(data, clnt_data, on="CLNT_ID",how="left")

# remove outliers
data_merge_1=data_merge[data_merge['가구']>=5.887168e-01]

aa=data_merge_1['CLNT_GENDER'].describe()

data_merge_1['CLNT_AGE'].describe()

# make a column list
col=data.columns

col_list = []
for factor in range(1,38):
    col_list.append(col[factor])

summarize_data_mead_df.loc['가구'][0]

clac1_clnt_prop_data={"gen_1":[],"gen_1_count":[],"gen_total":[],"age_mean":[]}
for col in col_list:
    mean_value = summarize_data_mead_df.loc[col][0]
    data_merge_1=data_merge[data_merge[col]>=mean_value]
    gender=data_merge_1['CLNT_GENDER'].describe()
    age=data_merge_1['CLNT_AGE'].describe()
    clac1_clnt_prop_data["gen_1"].append(gender[2])
    clac1_clnt_prop_data["gen_1_count"].append(gender[3])
    clac1_clnt_prop_data["gen_total"].append(gender[0])
    clac1_clnt_prop_data['age_mean'].append(age[1])

clac1_clnt_prop_data_df = pd.DataFrame(clac1_clnt_prop_data)

clac1_clnt_prop_data_df['CLAC1']=col_list

ddata=clac1_clnt_prop_data_df[['CLAC1','gen_1','gen_1_count','gen_total','age_mean']]

ddata.to_csv("result.csv")



# # Data above 75%

summarize_data_mead = summarize_data.loc['75%']
summarize_data_mead_df=pd.DataFrame(summarize_data_mead)

clac1_clnt_prop_data={"gen_1":[],"gen_1_count":[],"gen_total":[],"age_75up":[]}
for col in col_list:
    up75_value = summarize_data_mead_df.loc[col][0]
    data_merge_1=data_merge[data_merge[col]>=up75_value]
    gender=data_merge_1['CLNT_GENDER'].describe()
    age=data_merge_1['CLNT_AGE'].describe()
    clac1_clnt_prop_data["gen_1"].append(gender[2])
    clac1_clnt_prop_data["gen_1_count"].append(gender[3])
    clac1_clnt_prop_data["gen_total"].append(gender[0])
    clac1_clnt_prop_data['age_75up'].append(age[1])

clac1_clnt_prop_data_df = pd.DataFrame(clac1_clnt_prop_data)

clac1_clnt_prop_data_df['CLAC1']=col_list

ddata=clac1_clnt_prop_data_df[['CLAC1','gen_1','gen_1_count','gen_total','age_75up']]

ddata.to_csv("result_above_75.csv")


# # Result btw 50% and 75%

summarize_data_50 = summarize_data.loc['50%']
summarize_data_75 = summarize_data.loc['75%']

summarize_data_50_df=pd.DataFrame(summarize_data_50)
summarize_data_75_df=pd.DataFrame(summarize_data_75)

ddddata = pd.read_csv("Final_2.csv")
del ddddata['Unnamed: 0']

ddddata_need = ddddata[['CLNT_ID','CLAC1_NM','HITS_SEQ','PD_BUY_CT','SESS_SEQ','TOT_PAG_VIEW_CT','TOT_SESS_HR_V','SESS_DT']]
colcol_list=['HITS_SEQ','SESS_SEQ','TOT_PAG_VIEW_CT','TOT_SESS_HR_V']



# # Visualization


import numpy as np
import matplotlib.pyplot as plt


df = pd.DataFrame()
i=0
for col in col_list:
    up50_value = summarize_data_50_df.loc[col][0]
    up75_value = summarize_data_75_df.loc[col][0]
    data_merge_1=data_merge[(data_merge[col]>=up50_value)&(data_merge[col]>=up75_value)]
    need_clnt_list=data_merge_1['CLNT_ID']
    need_clnt_list_df = pd.DataFrame(need_clnt_list)
    ddddata_need_1=ddddata_need[ddddata_need['CLAC1_NM']==col]
    qqdata = pd.merge(need_clnt_list_df,ddddata_need_1,on=['CLNT_ID'],how='left')
    pivot_2=pd.pivot_table(qqdata,index=['SESS_DT'],values=['HITS_SEQ','PD_BUY_CT','SESS_SEQ','TOT_PAG_VIEW_CT','TOT_SESS_HR_V'],aggfunc='mean',fill_value=0)
    dd_reset=pivot_2.reset_index()
    i_str=str(i)
    for colcol in colcol_list:
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(1,1,1)
        ax.scatter(dd_reset[colcol],dd_reset['PD_BUY_CT'])
        plt.savefig('C:\\Users\\user\\Desktop\\aaa\\'+i_str+'_'+colcol)
        i+=1

dfdf = pd.DataFrame()
dfdf['CLAC1']=col_list
dfdf.to_csv("index_clac1.csv")


df = pd.DataFrame()
i=0
for col in col_list:
    up50_value = summarize_data_50_df.loc[col][0]
    up75_value = summarize_data_75_df.loc[col][0]
    data_merge_1=data_merge[(data_merge[col]>=up50_value)&(data_merge[col]>=up75_value)]
    need_clnt_list=data_merge_1['CLNT_ID']
    need_clnt_list_df = pd.DataFrame(need_clnt_list)
    ddddata_need_1=ddddata_need[ddddata_need['CLAC1_NM']==col]
    qqdata = pd.merge(need_clnt_list_df,ddddata_need_1,on=['CLNT_ID'],how='left')
    pivot_2=pd.pivot_table(qqdata,index=['SESS_DT'],values=['HITS_SEQ','PD_BUY_CT','SESS_SEQ','TOT_PAG_VIEW_CT','TOT_SESS_HR_V'],aggfunc='mean',fill_value=0)
    dd_reset=pivot_2.reset_index()
    i_str=str(i)
    for colcol in colcol_list:
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(1,1,1)
        ax.hist(dd_reset[colcol],bins=500)
        plt.savefig('C:\\Users\\user\\Desktop\\bbb\\'+i_str+'_'+colcol)
        i+=1


df = pd.DataFrame()
i=0
for col in col_list:
    up50_value = summarize_data_50_df.loc[col][0]
    up75_value = summarize_data_75_df.loc[col][0]
    data_merge_1=data_merge[(data_merge[col]>=up50_value)&(data_merge[col]>=up75_value)]
    need_clnt_list=data_merge_1['CLNT_ID']
    need_clnt_list_df = pd.DataFrame(need_clnt_list)
    ddddata_need_1=ddddata_need[ddddata_need['CLAC1_NM']==col]
    qqdata = pd.merge(need_clnt_list_df,ddddata_need_1,on=['CLNT_ID'],how='left')
    pivot_2=pd.pivot_table(qqdata,index=['SESS_DT'],values=['HITS_SEQ','PD_BUY_CT','SESS_SEQ','TOT_PAG_VIEW_CT','TOT_SESS_HR_V'],aggfunc='mean',fill_value=0)
    dd_reset=pivot_2.reset_index()
    i_str=str(i)
    for colcol in colcol_list:
        fig = plt.figure(figsize=(10,10))
        ax = fig.add_subplot(1,1,1)
        ax.hist(dd_reset[colcol],bins=100)
        plt.savefig('C:\\Users\\user\\Desktop\\ccc\\'+i_str+'_'+colcol)
    i+=1

ddd_list = {"HITS_SEQ_25":[],"HITS_SEQ_75":[],"SESS_SEQ_25":[],"SESS_SEQ_75":[],"TOT_PAG_VIEW_CT_25":[],"TOT_PAG_VIEW_CT_75":[],"TOT_SESS_HR_V_25":[],"TOT_SESS_HR_V_75":[]}
for col in col_list:
    data = ddddata_need[ddddata_need['CLAC1_NM']==col]
    data_des = data.describe()
    ddd_list['HITS_SEQ_25'].append(data_des.loc['25%']['HITS_SEQ'])
    ddd_list['HITS_SEQ_75'].append(data_des.loc['75%']['HITS_SEQ'])
    ddd_list['SESS_SEQ_25'].append(data_des.loc['25%']['SESS_SEQ'])
    ddd_list['SESS_SEQ_75'].append(data_des.loc['75%']['SESS_SEQ'])
    ddd_list['TOT_PAG_VIEW_CT_25'].append(data_des.loc['25%']['TOT_PAG_VIEW_CT'])
    ddd_list['TOT_PAG_VIEW_CT_75'].append(data_des.loc['75%']['TOT_PAG_VIEW_CT'])
    ddd_list['TOT_SESS_HR_V_25'].append(data_des.loc['25%']['TOT_SESS_HR_V'])
    ddd_list['TOT_SESS_HR_V_75'].append(data_des.loc['75%']['TOT_SESS_HR_V'])


ddd_list_df=pd.DataFrame(ddd_list)
ddd_list_df['CLAC1']=col_list
ddd_list_df.to_csv("range_session.csv")


data = ddddata_need[ddddata_need['CLAC1_NM']=='가구']

data_des=data.describe()


# # Data below 25%

data_des.loc['25%']

ddd_list = {"HITS_SEQ_mean":[],"SESS_SEQ_mean":[],"TOT_PAG_VIEW_CT_mean":[],"TOT_SESS_HR_V_mean":[]}
for col in col_list:
    data = ddddata_need[ddddata_need['CLAC1_NM']==col]
    data_des = data.describe()
    ddd_list['HITS_SEQ_mean'].append(data_des.loc['mean']['HITS_SEQ'])
    ddd_list['SESS_SEQ_mean'].append(data_des.loc['mean']['SESS_SEQ'])
    ddd_list['TOT_PAG_VIEW_CT_mean'].append(data_des.loc['mean']['TOT_PAG_VIEW_CT'])
    ddd_list['TOT_SESS_HR_V_mean'].append(data_des.loc['mean']['TOT_SESS_HR_V'])

ddd_list_df = pd.DataFrame(ddd_list)

ddd_list_df['CLAC1']=col_list

ddd_list_df.to_csv("logdata_mean.csv")
