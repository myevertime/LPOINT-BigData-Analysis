# load data
import pandas as pd

output = pd.read_csv("output.csv")


# # 빈도분석 (Frequency Analysis)

d = output.groupby('PD_BRA_NM')[['PD_NM','KWD_NM']].apply(lambda g: g.values.tolist()).to_dict()
# {brand name : (Product name, keyword)}

unique_brand_lst = list(output.PD_BRA_NM.unique())
unique_brand_lst.remove("무료배송")
unique_brand_lst.remove("여성")

# return list of tuples sorted by most common searched keywords for each brand name

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

output_d = analyzer(unique_brand_lst, d)
# {brand name : [searched another brands]}


# return only brand names not count values

def make_analyze_lst(d):
    analyze_lst = []
    for item in d.items():
        lst = list(item)
        element_lst = [lst[0]]
        element_lst.extend(lst[1])
        analyze_lst.append(element_lst)
    return analyze_lst

analyze_lst = make_analyze_lst(output_d)

analyze_lst[:5] # show head of analyze_lst to check


# # Association Analysis

from pip._internal import main as pipmain
pipmain(['install', 'mlxtend'])

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_ary = te.fit(analyze_lst).transform(analyze_lst)
df = pd.DataFrame(te_ary, columns=te.columns_)

from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df, min_support = 0.001, use_colnames=True)

from mlxtend.frequent_patterns import association_rules

rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 0.01, support_only=False)
rules

# lines 76~80 can be deleted if you don't care the itemset length bigger than 1
rules['length'] = rules['antecedents'].apply(lambda x: len(x))
rules['length2'] = rules['consequents'].apply(lambda x: len(x))
rules2 = rules [ (rules['length'] == 1) & (rules['length2'] == 1) ]
rules2

rules.to_csv("Brands interconnectivity(rank10).csv")

