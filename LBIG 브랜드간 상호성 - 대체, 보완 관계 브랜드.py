#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data1 = pd.read_csv("Lpoint/01Product.csv", encoding = 'utf-8')
data2 = pd.read_csv("Lpoint/02Search1.csv", encoding = 'utf-8')
data4 = pd.read_csv("Lpoint/04Custom.csv", encoding = 'utf-8')
data5 = pd.read_csv("Lpoint/05Session.csv", encoding = 'utf-8')
data6 = pd.read_csv("Lpoint/06Master.csv", encoding = 'utf-8')


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


import numpy as np
data= data.fillna(0)


# In[6]:


data["CLNT_GENDER"].replace({"F":2,"M":1}, inplace = True)


# In[7]:


data['TOT_SESS_HR_V'] = data['TOT_SESS_HR_V'].str.replace(',', '')
data['TOT_SESS_HR_V'] = pd.to_numeric(data['TOT_SESS_HR_V'])


# In[8]:


data = data.sort_values(by=['CLAC2_NM'], ascending=False)


# In[9]:


result = data.groupby(['PD_C', 'PD_BRA_NM']).size().reset_index(name='counts')
result = result.sort_values(by=['counts'], ascending=False)


# In[10]:


output = data.merge(result) # merge count column to original data


# In[11]:


output = output.sort_values(by=['counts'], ascending=False)


# # 대체/연관관계 분석

# In[12]:


d = output.groupby('PD_BRA_NM')[['PD_NM','KWD_NM']].apply(lambda g: g.values.tolist()).to_dict()
# {brand name : (Product name, keyword)}


# In[13]:


brand_list = data.PD_BRA_NM.tolist()
from collections import Counter
cnt = Counter(brand_list)
top_100 = cnt.most_common(100)


# In[14]:


top_100_2 = [] 
for top in top_100:
    top_100_2.append(top[0])


# In[15]:


def analyzer(brand_lst, dic):
    d = {}
    from collections import Counter
    for brand in brand_lst:
        lst = []
        for search in dic[brand]:
            lst.extend(search[1].split(" "))
        cnt = Counter(lst)
        keywords = cnt.most_common(10)
        lst2 = []
        for keyword in keywords:
            if keyword[0] in unique_brand_lst:
                if brand != keyword[0]:
                    lst2.append(keyword[0])
        if lst2 != []:
            d.update({brand : lst2})
    return d


# In[16]:


unique_brand_lst = list(output.PD_BRA_NM.unique())
unique_brand_lst.remove("무료배송")


# In[20]:


output_d = analyzer(unique_brand_lst, d)


# In[18]:


def make_analyze_lst(d):
    analyze_lst = []
    for item in d.items():
        lst = list(item)
        element_lst = [lst[0]]
        element_lst.extend(lst[1])
        analyze_lst.append(element_lst)
    return analyze_lst


# In[21]:


analyze_lst = make_analyze_lst(output_d)


# In[22]:


unique_brand_lst2 = []
for brand in unique_brand_lst:
    if brand in top_100_2:
        unique_brand_lst2.append(brand)


# In[23]:


dic = {}
for brand in unique_brand_lst2:
    CLAC1 = output.iloc[output.index[output['PD_BRA_NM'] == brand]].CLAC1_NM.tolist()
    from collections import Counter
    cnt = Counter(CLAC1)
    CLAC1 = cnt.most_common(1)[0][0]
    dic[brand] = CLAC1


# ## 보완관계

# In[43]:


# make complement brands list
Complement_lst = []
for item in analyze_lst:
    different_lst = []
    if item[0] in dic.keys():
        clac1 = dic[item[0]]
        for brand in item:
            if brand in dic.keys():
                clac2 = dic[brand]
                if clac1 != clac2:
                    different_lst.append(item[0])
                    different_lst.append(brand)
            if different_lst != []:
                Complement_lst.append(different_lst)

Complement_lst


# ## 대체관계

# In[41]:


# make substitute brands list
Substitute_lst = []
for item in analyze_lst:
    same_lst = []
    if item[0] in dic.keys():
        clac1 = dic[item[0]]
        for brand in item:
            if brand in dic.keys():
                clac2 = dic[brand]
                if clac1 == clac2:
                    same_lst.append(item[0])
                    same_lst.append(brand)
            if same_lst != []:
                Substitute_lst.append(same_lst)

for i in range(len(Substitute_lst)):
    Substitute_lst[i] = list(set(Substitute_lst[i])) # remove duplicated brands
    
Substitute_lst = [sub_lst for sub_lst in Substitute_lst if len(sub_lst) != 1] # remove nested list that contains only 1 brand

Substitute_lst


# In[ ]:




