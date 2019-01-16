# Load data

import pandas as pd

data = pd.read_csv("output.csv")

d = output.groupby('PD_BRA_NM')[['PD_NM','KWD_NM']].apply(lambda g: g.values.tolist()).to_dict()
# d shaped like {brand name : (Product name, keyword)}


# extract top 100 common brand names

brand_list = data.PD_BRA_NM.tolist()
from collections import Counter
cnt = Counter(brand_list)
top_100 = cnt.most_common(100)

top_100_2 = [] 
for top in top_100:
    top_100_2.append(top[0])


# find the most common searched keywords for each brand name

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

# extract unique brand list from data

unique_brand_lst = list(output.PD_BRA_NM.unique())
unique_brand_lst.remove("무료배송") # preprocessing
unique_brand_lst.remove("여성") # preprocessing

output_d = analyzer(unique_brand_lst, d)


# extract only brand names from counter function result

def make_analyze_lst(d):
    analyze_lst = []
    for item in d.items():
        lst = list(item)
        element_lst = [lst[0]]
        element_lst.extend(lst[1])
        analyze_lst.append(element_lst)
    return analyze_lst

analyze_lst = make_analyze_lst(output_d)


# result only for top 100 common brands

unique_brand_lst2 = []
for brand in unique_brand_lst:
    if brand in top_100_2:
        unique_brand_lst2.append(brand)

dic = {}
for brand in unique_brand_lst2:
    CLAC1 = output.iloc[output.index[output['PD_BRA_NM'] == brand]].CLAC1_NM.tolist()
    from collections import Counter
    cnt = Counter(CLAC1)
    CLAC1 = cnt.most_common(1)[0][0]
    dic[brand] = CLAC1


# ## 보완관계(Complement)

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


# ## 대체관계 (Substitute)

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
