#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


data1 = pd.read_csv("Lpoint/01Product.csv", encoding = 'utf-8')
data2 = pd.read_csv("Lpoint/02Search1.csv", encoding = 'utf-8')
data4 = pd.read_csv("Lpoint/04Custom.csv", encoding = 'utf-8')
data5 = pd.read_csv("Lpoint/05Session.csv", encoding = 'utf-8')
data6 = pd.read_csv("Lpoint/06Master.csv", encoding = 'utf-8')


# In[7]:


data1 = pd.DataFrame(data1)
data2 = pd.DataFrame(data2)
data5 = pd.DataFrame(data5)
data6 = pd.DataFrame(data6)


# In[8]:


data = data1.merge(data2, how = 'inner')
data = data.merge(data4, how = 'inner')
data = data.merge(data5, how = 'inner')
data = data.merge(data6, how = 'inner')


# In[9]:


import numpy as np
data= data.fillna(0)


# In[10]:


data["CLNT_GENDER"].replace({"F":2,"M":1}, inplace = True)


# In[11]:


data['TOT_SESS_HR_V'] = data['TOT_SESS_HR_V'].str.replace(',', '')
data['TOT_SESS_HR_V'] = pd.to_numeric(data['TOT_SESS_HR_V'])


# In[12]:


data = data.sort_values(by=['CLAC2_NM'], ascending=False)


# In[13]:


result = data.groupby(['PD_C', 'PD_BRA_NM']).size().reset_index(name='counts')
result = result.sort_values(by=['counts'], ascending=False)


# In[14]:


result["PD_BRA_NM"] # list of most sold (product code & brand name)


# In[15]:


output = data.merge(result) # merge count column to original data


# In[16]:


output = output.sort_values(by=['counts'], ascending=False)


# In[17]:


output.to_csv("output.csv")


# In[18]:


output.head()


# # 빈도분석 (Frequency Analysis)

# In[19]:


d = output.groupby('PD_BRA_NM')[['PD_NM','KWD_NM']].apply(lambda g: g.values.tolist()).to_dict()
# {brand name : (Product name, keyword)}


# In[35]:


unique_brand_lst = list(output.PD_BRA_NM.unique())
unique_brand_lst.remove("무료배송")


# In[36]:


unique_brand_lst.remove("여성")


# In[37]:


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


# In[38]:


output_d = analyzer(unique_brand_lst, d)
# {brand name : [searched another brands]}


# In[39]:


def make_analyze_lst(d):
    analyze_lst = []
    for item in d.items():
        lst = list(item)
        element_lst = [lst[0]]
        element_lst.extend(lst[1])
        analyze_lst.append(element_lst)
    return analyze_lst


# In[40]:


analyze_lst = make_analyze_lst(output_d)


# In[41]:


analyze_lst[:5] # show head of analyze_lst


# # Association Analysis

# In[42]:


from pip._internal import main as pipmain

pipmain(['install', 'mlxtend'])


# In[43]:


import pandas as pd
from mlxtend.preprocessing import TransactionEncoder


# In[44]:


te = TransactionEncoder()
te_ary = te.fit(analyze_lst).transform(analyze_lst)
df = pd.DataFrame(te_ary, columns=te.columns_)


# In[45]:


from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df, min_support = 0.001, use_colnames=True)


# In[46]:


from mlxtend.frequent_patterns import association_rules

rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 0.01, support_only=False)
rules


# In[47]:


rules['length'] = rules['antecedents'].apply(lambda x: len(x))
rules['length2'] = rules['consequents'].apply(lambda x: len(x))
rules2 = rules [ (rules['length'] == 1) & (rules['length2'] == 1) ]
rules2


# In[48]:


rules.to_csv("Brands interconnectivity(rank10).csv")


# In[49]:


rules2.to_csv("Brands interconnectivity(rank10 & 1 to 1).csv")

