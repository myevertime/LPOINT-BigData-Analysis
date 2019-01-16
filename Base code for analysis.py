import pandas as pd

# Read data
data1 = pd.read_csv("Lpoint/01Product.csv", encoding = "cp949")
data2 = pd.read_csv("Lpoint/02Search1.csv")
data4 = pd.read_csv("Lpoint/04Custom.csv")
data5 = pd.read_csv("Lpoint/05Session.csv")
data6 = pd.read_csv("Lpoint/06Master.csv")

data1 = pd.DataFrame(data1)
data2 = pd.DataFrame(data2)
data5 = pd.DataFrame(data5)
data6 = pd.DataFrame(data6)

data = data1.merge(data2, how = 'inner')
data = data.merge(data4, how = 'inner')
data = data.merge(data5, how = 'inner')
data = data.merge(data6, how = 'inner')

# Data Preprocessing - Fill n/a

import numpy as np
data= data.fillna(0)

# Data Preprocessing

data["CLNT_GENDER"].replace({"F":2,"M":1}, inplace = True)

# Data Preprocessing - string data type to numeric type

data['TOT_SESS_HR_V'] = data['TOT_SESS_HR_V'].str.replace(',', '')
data['TOT_SESS_HR_V'] = pd.to_numeric(data['TOT_SESS_HR_V'])


# Group data by product_code and product_brand_name and count

result = data.groupby(['PD_C', 'PD_BRA_NM']).size().reset_index(name='counts')
result = result.sort_values(by=['counts'], ascending=False)

result["PD_BRA_NM"] # list of most sold (product code & brand name)

output = data.merge(result) # merge count column to original data

output.to_csv("output.csv")


# # 빈도분석 (Frequency Analysis)

d = output.groupby('PD_BRA_NM')[['PD_NM','KWD_NM']].apply(lambda g: g.values.tolist()).to_dict()
d # {brand name : (Product name, keyword)}

# Return the list containing unique brand names

unique_brand_lst = list(output.PD_BRA_NM.unique())

# Return a list sorted as the most searched keywords for each brand name

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

output_d = analyzer(unique_brand_lst, d)
output_d # {brand name : [(search keyword 1 , search count), (search keyword 2, search count)...]}

output_d.save("Brand_Link")

