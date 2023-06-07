# 유가 스크래핑

1. scrapper.py를 실행하여 다운로드 폴더에 엑셀 파일을 다운로드 받습니다.
2. preprocessor 내 모든 코드를 실행하여 데이터 전처리를 진행합니다. data 폴더에 파일을 생성합니다.
    - base.csv: 다운로드한 엑셀 파일을 모두 합친 csv파일입니다.
    - processed.csv: base.csv에서 불필요한 데이터를 지운 파일입니다.
    - geo_info.json: folium choropleth를 위한 JSON 파일입니다. (출처: https://github.com/PinkWink)
3. visualator 코드를 실행하여 시각화 & 핵심 데이터를 봅니다.