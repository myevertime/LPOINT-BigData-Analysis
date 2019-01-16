# 2018-Lpoint BigData Competition
participated as a team named LBIG

**1. 데이터 정보**

총 6가지 데이터를 제공받았습니다.

01 상품구매(Product)
>CLNT_ID 클라이언트ID ■ 방문자(Visitors)의 쿠키에 랜덤으로 부여된 고유 ID
>
>SESS_ID 세션ID ■ Web/App에 접속 후 세션이 시작될 때 부여된 고유 ID
>
>HITS_SEQ 히트일련번호 ■ Web/App에서 방문자의 행위에 대해 순서대로 배열된 일련번호
>
>PD_C 상품코드 ■ 구매한 상품의 코드(최소단위)
>
>PD_ADD_NM 상품추가정보 ■ 구매한 상품의 추가 정보
>
>PD_BRA_NM 상품브랜드 ■ 구매한 상품의 브랜드
>
>PD_BUY_AM 단일상품금액 ■ 구매한 상품 1개의 금액
>
>PD_BUY_CT 구매건수 ■ 구매한 상품의 수량	

02 검색어1 (Search1)
>CLNT_ID 클라이언트ID
>
>SESS_ID 세션ID
>
>KWD_NM	검색키워드명	■ 검색창에 입력한 검색 키워드
>
>SEARCH_CNT 검색건수 ■ 세션 내 해당 검색어 검색량	
				
03 검색어2(Search2)
>SESS_DT 세션일자 ■ 세션일자 (YYYYMMDD 형식으로 표시)
>
>KWD_NM 검색키워드명
>
>SEARCH_CNT 검색건수 ■ 세션 내 해당 검색어 검색량	

04 회원(Custom)
>CLNT_ID 클라이언트ID
>
>CLNT_GENDER 성별 ■ 성별정보 [남자 : M / 여자 : F]
>
>CLNT_AGE 연령대 ■ 연령대 정보 [10대 : 10 / 20대 : 20 / 30대 : 30 ...]	

05 세션(Session)
>CLNT_ID 클라이언트ID
>
>SESS_ID 세션ID
>
>SESS_SEQ 세션일련번호
>
>SESS_DT 세션일자
>
>TOT_PAG_VIEW_CT 총페이지조회건수 ■ 세션 내의 총 페이지(화면) 뷰 수	
>TOT_SESS_HR_V 총세션시간값 ■ 세션 내 총 시간(단위: 초)	
>DVC_CTG_NM 기기유형 ■ 기기 유형(1: desktop , 2: mobile, 3.tablet )	
>ZON_NM 지역대분류 ■ 세션기준 발생 대분류 지역명 (대분류IP 주소 또는 지역 ID 기준)	
>CITY_NM 지역중분류 ■ 세션기준 발생 중분류 지역명 (중분류IP 주소 또는 지역 ID 기준)	
>CLNT_ID 클라이언트ID 
				
06 상품분류(Master)
>PD_C 상품코드 ■ 상품의 코드(최소단위)
>PD_NM 상품명
>CLAC1_NM 상품 대분류명	
>CLAC2_NM 상품 중분류명	
>CLAC3_NM 상품 소분류명	


**2. 분석**
주최측에서 전달받은 주제는 총 3가지 였습니다.
1) 온라인 선호지수 개발
2) 상품군별 수요예측모델 설계
3) 1), 2) 를 이용한 신규 서비스 제안

저희는 분석을 통해 Lpoint의 홈페이지 혁신을 제안했습니다. 단순히 연령대/나이별로 맞춤형 추천 또는 광고 시스템이 아니라, 소비자 개개별로 타겟팅한 홈페이지(Absolute Curation Service)를 구상했습니다.

진행된 분석은 다음과 같습니다:
