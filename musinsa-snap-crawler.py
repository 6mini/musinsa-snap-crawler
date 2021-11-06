from urllib.request import urlretrieve
from selenium import webdriver
import os

path = '/Users/6mini/musinsa-snap-crawler/chromedriver' # chromedriver의 절대경로
driver = webdriver.Chrome(path)

page_num = 1 # 크롤링 시작 페이지
last_page_num = 3 # 마지막 페이지 설정
styles = ['01', '02', '04', '09', '11', '12', '14'] # 크롤링 할 스타일 설정
'''
01: 스트릿/힙합
02: 심플/캐주얼
04: 포멀/클래식
09: 유니크/키치
11: 걸리시
12: 섹시/페미닌
14: 워크/밀리터리
'''

for style in styles:
    while page_num <= last_page_num: # 자동으로 페이지가 이동되게 while문 사용
        url = 'https://magazine.musinsa.com/index.php?m=street&style=0{}&_mon=&p={}#listStart'.format(style, page_num)
        driver.get(url) # url 접속

        img_num = 0
        while img_num < 2: # 60 고정: 무신사 스트릿 스냅 페이지의 이미지 수 60장
            driver.find_elements_by_css_selector('.articleImg')[img_num].click() # 이미지 접속
            img_url = driver.find_elements_by_css_selector('.lbox')[0].get_attribute('href') # url 파싱 

            if not os.path.isdir(style): # 기본적으로 스타일 번호를 폴더로 지정, 폴더 없으면 생성
                os.mkdir(style)

            urlretrieve(img_url, '{}/{}-{}.jpg'.format(style, page_num, img_num)) # img_url에서 이미지 다운로드, style 폴더에 'page_num-img_num.jpg' 형태로 저장
            driver.get(url) # 뒤로가기 대신 url 재접속을 사용(오류 최소화)
            img_num += 1
        page_num += 1
    page_num = 1 # 하나의 스타일에 대한 cycle이 다 돌고 재 설정