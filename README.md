# Demand Forcasting Competition
participated as a team named LBIG

# 1. Analysis
Required to conduct three topics below :
1) Develop online preference index(온라인 선호 지수 개발)
2) Develop demand forcasting model per product categories (상품군별 수요예측모델 설계)
3) Suggest new service based on the results of 1 and 2  (1), 2) 를 이용한 신규 서비스 제안)

We suggested the renovation of Lpoint homepage which was working as a simple advertisement system providing recommendation based on age.
We designed absolute curation service by targeting every single customer.

1. Development of online preference index
2. Interpretion of online preference index 
	- Examined relationship between "Sess_hr" & "Hit_sq",  "Sess_hr" & "Total_page_view_count"
3. Development of demand forcasting model
4. Analysis of Brand interconnectivity 
	- substituable or preferrable relationship
	- connectivity of brands 



# 2. Data Info

provided 6 types of data

01 Transaction Data (상품)
>CLNT_ID ; ClientID ■ 방문자(Visitors)의 쿠키에 랜덤으로 부여된 고유 ID
>
>SESS_ID ; SessionID ■ Web/App에 접속 후 세션이 시작될 때 부여된 고유 ID
>
>HITS_SEQ ; Hit Seq ■ Web/App에서 방문자의 행위에 대해 순서대로 배열된 일련번호
>
>PD_C ; ProductId ■ 구매한 상품의 코드(최소단위)
>
>PD_ADD_NM ; Product Additional Info ■ 구매한 상품의 추가 정보
>
>PD_BRA_NM ; Product Brand ■ 구매한 상품의 브랜드
>
>PD_BUY_AM ; Product order amount ■ 구매한 상품 1개의 금액
>
>PD_BUY_CT ; Product order count ■ 구매한 상품의 수량	

02 Search1 (검색어1)
>CLNT_ID ; Client ID
>
>SESS_ID ; Session ID
>
>KWD_NM	; Search Keyword	■ 검색창에 입력한 검색 키워드
>
>SEARCH_CNT ; Search count ■ 세션 내 해당 검색어 검색량	
				
03 Search2 (검색어2)
>SESS_DT ; Session Time ■ 세션일자 (YYYYMMDD 형식으로 표시)
>
>KWD_NM ; Search Keyword
>
>SEARCH_CNT ; Search Count ■ 세션 내 해당 검색어 검색량	

04 Customer (Custom, 회원)
>CLNT_ID ; ClientID
>
>CLNT_GENDER ; Gender ■ 성별정보 [남자 : M / 여자 : F]
>
>CLNT_AGE ; Client Age ■ 연령대 정보 [10대 : 10 / 20대 : 20 / 30대 : 30 ...]	

05 Session (세션)
>CLNT_ID ; 
>
>SESS_ID ;
>
>SESS_SEQ ;
>
>SESS_DT ;
>
>TOT_PAG_VIEW_CT ; Total Page View Count ■ 세션 내의 총 페이지(화면) 뷰 수
>
>TOT_SESS_HR_V ; Total Session Time in sec ■ 세션 내 총 시간(단위: 초)
>
>DVC_CTG_NM ; Device type ■ 기기 유형(1: desktop , 2: mobile, 3.tablet )
>
>ZON_NM ; Region Category1 ■ 세션기준 발생 대분류 지역명 (대분류IP 주소 또는 지역 ID 기준)
>
>CITY_NM ; Region Category2 ■ 세션기준 발생 중분류 지역명 (중분류IP 주소 또는 지역 ID 기준)
>
>CLNT_ID ;
				
06 Product Meta (Master, 상품분류)
>PD_C ; ProductID ■ 상품의 코드(최소단위)
>
>PD_NM ; Product name
>
>CLAC1_NM ; Product Category1
>
>CLAC2_NM ; Product Category2
>
>CLAC3_NM ; Product Category3
