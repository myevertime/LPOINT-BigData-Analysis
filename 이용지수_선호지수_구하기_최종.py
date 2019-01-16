#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
data_1=pd.read_csv("01Product.csv")
data_2=pd.read_csv("02Search1.csv")  
data_3=pd.read_csv("03Search2.csv")
data_4=pd.read_csv("04Custom.csv")
data_5=pd.read_csv("05Session.csv")
data_6=pd.read_csv("06Master.csv")


# 세션 데이터 부분

# In[2]:


import numpy as np


# In[3]:


a_data = data_1[['CLNT_ID','HITS_SEQ','SESS_ID','PD_C']]
b_data = data_5[['CLNT_ID','SESS_ID','TOT_PAG_VIEW_CT','TOT_SESS_HR_V']]
c_data = data_6[['PD_C','CLAC1_NM']]


# In[4]:


data = a_data.merge(b_data, on=['CLNT_ID','SESS_ID'], how='inner')
data=data.merge(c_data, on=['PD_C'], how='inner')


# In[5]:


data['HITS_SEQ']=data['HITS_SEQ'].astype(float)
data['TOT_PAG_VIEW_CT']=data['TOT_PAG_VIEW_CT'].astype(float)
data['TOT_SESS_HR_V']=data['TOT_SESS_HR_V'].astype(str)
data['TOT_SESS_HR_V']=data['TOT_SESS_HR_V'].str.replace(',', '')
data['TOT_SESS_HR_V']=data['TOT_SESS_HR_V'].astype(float)
data['TOT_PAG_VIEW_CT']=data['TOT_PAG_VIEW_CT'].astype(str)
data['TOT_PAG_VIEW_CT']=data['TOT_PAG_VIEW_CT'].str.replace(',', '')
data['TOT_PAG_VIEW_CT']=data['TOT_PAG_VIEW_CT'].astype(float)


# In[6]:


pivot_1=pd.pivot_table(data,index=['CLNT_ID','CLAC1_NM'],values=['HITS_SEQ','TOT_PAG_VIEW_CT','TOT_SESS_HR_V'],aggfunc=np.sum,fill_value=0)


# In[7]:


pivot_2=pd.pivot_table(data,index=['CLAC1_NM'],values=['HITS_SEQ','TOT_PAG_VIEW_CT','TOT_SESS_HR_V'],aggfunc=np.sum,fill_value=0)


# In[8]:


pivot_1_1=pivot_1.reset_index()


# In[9]:


pivot_2_1=pivot_2.reset_index()


# In[10]:


pivot_2_1_rename = pivot_2_1.rename(columns = {'HITS_SEQ': 'HITS_SEQ_CLAC','TOT_PAG_VIEW_CT':'TOT_PAG_VIEW_CT_CLAC','TOT_SESS_HR_V':'TOT_SESS_HR_V_CLAC'})


# In[11]:


merge_1 = pd.merge(pivot_1_1,pivot_2_1_rename,on='CLAC1_NM',how = 'left')


# In[12]:


merge_1['HITS_SEQ_index']=merge_1['HITS_SEQ'].div(merge_1['HITS_SEQ_CLAC'])
merge_1['TOT_PAG_VIEW_CT_index']=merge_1['TOT_PAG_VIEW_CT'].div(merge_1['TOT_PAG_VIEW_CT_CLAC'])
merge_1['TOT_SESS_HR_V_index']=merge_1['TOT_SESS_HR_V'].div(merge_1['TOT_SESS_HR_V_CLAC'])


# In[13]:


merge_1['SESS_INDEX_SUM']=merge_1['HITS_SEQ_index'].add(merge_1['TOT_PAG_VIEW_CT_index'])


# In[14]:


merge_1['SESS_INDEX_SUM_2']=merge_1['SESS_INDEX_SUM'].add(merge_1['TOT_SESS_HR_V_index'])


# In[15]:


merge_1['SESS_INDEX_SUM_2_aa']=merge_1['SESS_INDEX_SUM_2'].mul(1000)


# In[16]:


merge_1_INDEX=merge_1[['CLNT_ID','CLAC1_NM','SESS_INDEX_SUM_2_aa']]


# In[74]:


merge_1_INDEX


# 구매수량 부분

# In[17]:


a_data_1 = data_1[['CLNT_ID','PD_BUY_CT','SESS_ID','PD_C']]
c_data_1 = data_6[['PD_C','CLAC1_NM']]


# In[18]:


data_11=a_data_1.merge(c_data_1, on=['PD_C'], how='inner')


# In[19]:


data_11_need = data_11[['CLNT_ID','CLAC1_NM','PD_BUY_CT']]


# In[24]:


data_11_need['PD_BUY_CT']=data_11_need['PD_BUY_CT'].astype(str)
data_11_need['PD_BUY_CT']=data_11_need['PD_BUY_CT'].str.replace(',', '')
data_11_need['PD_BUY_CT']=data_11_need['PD_BUY_CT'].astype(float)


# In[25]:


CLAC_sum=data_11_need.PD_BUY_CT.groupby(data_11_need.CLAC1_NM).sum()


# In[27]:


CLAC_sum_df=pd.DataFrame(CLAC_sum)


# In[30]:


CLAC_sum_df_1=CLAC_sum_df.reset_index()


# In[32]:


CLNT_CLAC_sum=data_11_need.PD_BUY_CT.groupby([data_11_need['CLNT_ID'],data_11_need['CLAC1_NM']]).sum()


# In[34]:


CLNT_CLAC_sum_df=pd.DataFrame(CLNT_CLAC_sum)


# In[37]:


CLNT_CLAC_sum_df_1=CLNT_CLAC_sum_df.reset_index()


# In[40]:


CT_data=pd.merge(CLNT_CLAC_sum_df_1,CLAC_sum_df_1,on=['CLAC1_NM'],how='left')


# In[42]:


CT_data['CT_index']=CT_data['PD_BUY_CT_x'].div(CT_data['PD_BUY_CT_y'])


# In[44]:


CT_data['CT_index_1']=CT_data['CT_index'].mul(1000)


# In[46]:


CT_data_need=CT_data[['CLNT_ID','CLAC1_NM','CT_index_1']]


# In[49]:


final_index=pd.merge(CT_data_need,merge_1_INDEX,on=['CLNT_ID','CLAC1_NM'],how='inner')


# In[51]:


final_index['Total_index']=final_index['CT_index_1'].add(final_index['SESS_INDEX_SUM_2_aa'])


# In[53]:


final_index_need=final_index[['CLNT_ID','CLAC1_NM','Total_index']]


# In[80]:


final_index


# In[ ]:





# 최종 이용지수

# In[54]:


final_index_need


# 선호지수 구하기

# In[55]:


ddata_1 = pd.pivot_table(final_index_need, index = 'CLNT_ID',values='Total_index',columns='CLAC1_NM',aggfunc='mean')


# In[58]:


ddata_1.reset_index()


# In[59]:


collist=[]
for factor in ddata_1.columns:
    collist.append(factor)


# In[61]:


ddata_1['total']=ddata_1.loc[:,collist].sum(axis=1)


# In[63]:


ddata_1_copy = ddata_1.copy()


# In[64]:


for col in collist:
    ddata_1_copy[col]=ddata_1_copy[col].div(ddata_1_copy['total'])


# In[65]:


dfdf=pd.DataFrame(ddata_1_copy)


# In[68]:


prefer_index_df=dfdf.reset_index()


# 최종 선호지수

# In[69]:


prefer_index_df


# In[70]:


prefer_index_df.to_csv("prefer_index.csv")


# In[81]:


prefer_index_df.fillna(0)


# In[ ]:




