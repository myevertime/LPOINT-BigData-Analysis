category = '화장품/뷰티케어' # Categories of products

import os
import sys
import urllib.request
import json
import pandas as pd
import pickle
import matplotlib.pyplot as plt


file=open("Brand_Link_4","rb") # dictionary with key as brand name and value as keywords
data=pickle.load(file)

CLAC1_BRAND=pd.read_csv("CLAC1_BRAND_RANK_10.csv")
del CLAC1_BRAND['Unnamed: 0']

def get_brand(CLAC1):
    brand_list=[]
    for factor in CLAC1_BRAND[CLAC1]:
        brand_list.append(factor)
    return brand_list

def get_link(brand, start_date, end_date):
    link = '{"startDate":"' + start_date + '","endDate":"' + end_date + '","timeUnit":"date","keywordGroups":['+str(data[brand])+']}'
    return link

def get_trend_data(brand, start_date, end_date):
    client_id = "hpWo_SdiiUaB1_tBYdnc"
    client_secret = "REJjj6veyZ"
    url = "https://openapi.naver.com/v1/datalab/search";
    link = get_link(brand, start_date, end_date)
    body = link;
    
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    request.add_header("Content-Type","application/json")
    response = urllib.request.urlopen(request, data=body.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
    else:
        print("Error Code:" + rescode)
    data = json.loads(response_body)
    return data

def get_ratio_data(CLAC, start_date, end_date):
    BR_LIST = get_brand(CLAC)
    result_data = pd.DataFrame({"0":[],"1":[],"2":[],"3":[],"4":[], "5":[], "6":[], "7":[], "8":[], "9":[]})
    result_data.columns=BR_LIST
    for brand in BR_LIST:
        data = get_trend_data(brand, start_date, end_date)
        DF_data = pd.DataFrame(data)
        DF_results_data=DF_data['results']
        factor_data=DF_results_data[0]['data']
        ratio_data=[]
        for factor in range(len(factor_data)):
            ratio_data.append(factor_data[factor]['ratio'])
        
        result_data[brand]=ratio_data
    return result_data



CLAC_BUTCT = pd.read_csv("SESSDT_CLAC1_BUYCT_qq.csv")          #판매량 데이터 불러오기
del CLAC_BUTCT['Unnamed: 0']


# # 회귀분석


import statsmodels.api as sm #선형회귀 라이브러리


def save_linear_summary(x_df,y_df): #OLS 방법으로 선형회귀
    model_boston2 = sm.OLS(y_df, x_df)
    result_boston2 = model_boston2.fit()
    result_boston2.save("data")

    
def read_rsquared(start_date, end_date):
    df = get_ratio_data(category, start_date, end_date)
    save_linear_summary(df,CLAC_BUTCT[category])
    file=open("data","rb")
    data2=pickle.load(file)
    rsquared = data2.rsquared
    return rsquared


def get_highest_model():
    import datetime
    start_month = 2
    start_day = 1
    end_month = 8
    end_day = 2
    highest_r_score = 0

    for i in range(30): # shift days for 31 times (stop at 2018-04-01)
        date = datetime.datetime(2018, start_month, start_day)
        start = date + datetime.timedelta(hours=24)
        date2 = datetime.datetime(2018, end_month, end_day)
        end = date2 + datetime.timedelta(hours=24)
        start_date = start.strftime('%Y-%m-%d')
        end_date = end.strftime('%Y-%m-%d')
        
        new_r_score = read_rsquared(start_date, end_date)
        if new_r_score > highest_r_score:
            highest_r_score = new_r_score
            highest_day = start_date
            highest_end_day = end_date
        
        start_month = start.month
        start_day = start.day
        end_month = end.month
        end_day = end.day
    return (highest_r_score, highest_day)

r_score, highest_day = get_highest_model() # got the date when the model gets highest R2


# # Visualization

import datetime
d0 = datetime.datetime(2018, 3, 1)
d1 = datetime.datetime(2018, 8, 30)
delta = d1 - d0
# calculate period

month = int(highest_day[5:7])
day = int(highest_day[8:])

end_date = (datetime.datetime(2018, month, day) + datetime.timedelta(days=delta.days)).strftime('%Y-%m-%d')


from sklearn.decomposition import PCA #PCA

def PCA_BUYCT_SCATTER(x_df,y_df):                   #pca한 x와 y 점 그래프
    x_pca=get_PCA(x_df)
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(1,1,1)
    ax.scatter(x_pca,y_df)
    plt.show()

df = get_ratio_data(category, highest_day, end_date)

def get_PCA(DataFrame):
    pca= PCA(n_components=1)
    w_1 = pca.fit_transform(DataFrame)
    result_list=[]
    for factor in w_1:
        result_list.append(factor[0])
    return result_list

pca_data = get_PCA(df)

PCA_BUYCT_SCATTER(df,CLAC_BUTCT[category])