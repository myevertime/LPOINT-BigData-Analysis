#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data1 = pd.read_csv("Lpoint/01Product.csv", encoding = "cp949")
data2 = pd.read_csv("Lpoint/02Search1.csv")
data4 = pd.read_csv("Lpoint/04Custom.csv")
data5 = pd.read_csv("Lpoint/05Session.csv")
data6 = pd.read_csv("Lpoint/06Master.csv")


# In[3]:


data1 = pd.DataFrame(data1)
data2 = pd.DataFrame(data2)
data5 = pd.DataFrame(data5)
data6 = pd.DataFrame(data6)


# In[4]:


data = data1.merge(data2, how = 'inner')
data = data.merge(data4, how = 'inner')
data = data.merge(data5, how = 'inner')
data = data.merge(data6, how = 'inner')


# In[5]:


data


# In[6]:


import numpy as np
data= data.fillna(0)


# In[7]:


data.head()


# In[8]:


data["CLNT_GENDER"].replace({"F":2,"M":1}, inplace = True)


# In[9]:


data['TOT_SESS_HR_V'] = data['TOT_SESS_HR_V'].str.replace(',', '')
data['TOT_SESS_HR_V'] = pd.to_numeric(data['TOT_SESS_HR_V'])


# In[10]:


data = data.sort_values(by=['CLAC2_NM'], ascending=False)


# In[11]:


result = data.groupby(['PD_C', 'PD_BRA_NM']).size().reset_index(name='counts')
result = result.sort_values(by=['counts'], ascending=False)


# In[12]:


result["PD_BRA_NM"] # list of most sold (product code & brand name)


# In[13]:


output = data.merge(result) # merge count column to original data


# In[14]:


output = output.sort_values(by=['counts'], ascending=False)


# In[15]:


output.to_csv("output.csv")


# In[22]:


output.head()


# # 빈도분석 (Frequency Analysis)

# In[17]:


d = output.groupby('PD_BRA_NM')[['PD_NM','KWD_NM']].apply(lambda g: g.values.tolist()).to_dict()
d # {brand name : (Product name, keyword)}


# In[18]:


unique_brand_lst = list(output.PD_BRA_NM.unique())


# In[19]:


def analyzer(brand_lst, dic):
    d = {}
    from collections import Counter
    for brand in brand_lst:
        lst = []
        for search in dic[brand]:
            lst.extend(search[1].split(" "))
        cnt = Counter(lst)
        d.update({brand : cnt.most_common()})
    return d


# In[20]:


output_d = analyzer(unique_brand_lst, d)
output_d # {brand name : [(search keyword 1 , search count), (search keyword 2, search count)...]}


# In[ ]:


output_d.save("Brand_Link_4")

