#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("prefer_index.csv")


# In[3]:


del data['Unnamed: 0']


# In[4]:


data


# In[5]:


summarize_data=data.describe()


# In[6]:


summarize_data_mead = summarize_data.loc['mean']


# In[7]:


summarize_data_mead_df=pd.DataFrame(summarize_data_mead)


# In[8]:


summarize_data_mead_df


# In[9]:


clnt_data = pd.read_csv("04Custom.csv")


# In[10]:


clnt_data


# In[11]:


data_merge=pd.merge(data, clnt_data, on="CLNT_ID",how="left")


# In[12]:


data_merge


# In[13]:


data_merge_1=data_merge[data_merge['가구']>=5.887168e-01]


# In[14]:


data_merge_1


# In[15]:


aa=data_merge_1['CLNT_GENDER'].describe()


# In[16]:


data_merge_1['CLNT_AGE'].describe()


# In[17]:


aa


# In[18]:


col=data.columns


# In[19]:


col_list = []
for factor in range(1,38):
    col_list.append(col[factor])


# In[20]:


col_list


# In[21]:


summarize_data_mead_df.loc['가구'][0]


# In[22]:


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


# In[23]:


clac1_clnt_prop_data_df = pd.DataFrame(clac1_clnt_prop_data)


# In[24]:


clac1_clnt_prop_data_df['CLAC1']=col_list


# In[25]:


clac1_clnt_prop_data_df


# In[26]:


ddata=clac1_clnt_prop_data_df[['CLAC1','gen_1','gen_1_count','gen_total','age_mean']]


# In[27]:


ddata


# In[65]:


ddata.to_csv("iiiiiiiiiii.csv")


# In[28]:


summarize_data


# In[ ]:





# In[29]:


summarize_data_mead = summarize_data.loc['75%']


# In[30]:


data_merge


# In[31]:


summarize_data_mead_df=pd.DataFrame(summarize_data_mead)


# In[32]:


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


# In[33]:


clac1_clnt_prop_data_df = pd.DataFrame(clac1_clnt_prop_data)


# In[34]:


clac1_clnt_prop_data_df['CLAC1']=col_list


# In[35]:


ddata=clac1_clnt_prop_data_df[['CLAC1','gen_1','gen_1_count','gen_total','age_75up']]


# In[36]:


ddata


# In[85]:


ddata.to_csv("ttttttttttt.csv")


# In[37]:


summarize_data


# In[38]:


summarize_data_50 = summarize_data.loc['50%']
summarize_data_75 = summarize_data.loc['75%']


# In[39]:


summarize_data_50_df=pd.DataFrame(summarize_data_50)
summarize_data_75_df=pd.DataFrame(summarize_data_75)


# In[40]:


summarize_data_75_df


# In[41]:


col_list


# In[50]:


ddddata = pd.read_csv("Final_2.csv")


# In[43]:


del ddddata['Unnamed: 0']
ddddata.head()


# In[52]:


ddddata_need = ddddata[['CLNT_ID','CLAC1_NM','HITS_SEQ','PD_BUY_CT','SESS_SEQ','TOT_PAG_VIEW_CT','TOT_SESS_HR_V','SESS_DT']]


# In[53]:


ddddata_need.head()


# In[45]:


colcol_list=['HITS_SEQ','SESS_SEQ','TOT_PAG_VIEW_CT','TOT_SESS_HR_V']


# In[46]:


import numpy as np
import matplotlib.pyplot as plt


# In[130]:


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


# In[47]:


dfdf = pd.DataFrame()


# In[48]:


dfdf['CLAC1']=col_list


# In[128]:


dfdf.to_csv("index_clac1.csv")


# In[131]:


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


# In[132]:


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


# In[54]:


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


# In[55]:


ddd_list_df=pd.DataFrame(ddd_list)


# In[56]:


ddd_list_df['CLAC1']=col_list


# In[150]:


ddd_list_df.to_csv("range_session.csv")


# In[ ]:





# In[57]:


data = ddddata_need[ddddata_need['CLAC1_NM']=='가구']


# In[58]:


data_des=data.describe()


# In[59]:


data_des.loc['25%']


# In[61]:


ddd_list = {"HITS_SEQ_mean":[],"SESS_SEQ_mean":[],"TOT_PAG_VIEW_CT_mean":[],"TOT_SESS_HR_V_mean":[]}
for col in col_list:
    data = ddddata_need[ddddata_need['CLAC1_NM']==col]
    data_des = data.describe()
    ddd_list['HITS_SEQ_mean'].append(data_des.loc['mean']['HITS_SEQ'])
    ddd_list['SESS_SEQ_mean'].append(data_des.loc['mean']['SESS_SEQ'])
    ddd_list['TOT_PAG_VIEW_CT_mean'].append(data_des.loc['mean']['TOT_PAG_VIEW_CT'])
    ddd_list['TOT_SESS_HR_V_mean'].append(data_des.loc['mean']['TOT_SESS_HR_V'])


# In[63]:


ddd_list_df = pd.DataFrame(ddd_list)


# In[65]:


ddd_list_df['CLAC1']=col_list


# In[66]:


ddd_list_df


# In[67]:


ddd_list_df.to_csv("logdata_mean.csv")


# In[ ]:





# In[ ]:




