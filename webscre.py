from selenium import webdriver
import chromedriver_binary
import time
import pandas as pd

USER = "test_user"
PASS = "test_pw"

#Chromeを起動
browser = webdriver.Chrome()
browser.implicitly_wait(3)

#ログインページへアクセス
url_login = "https://kino-code.work/membership-login"
browser.get(url_login)
time.sleep(3)
print("ログインページにアクセスしました")

#テキストボックス入力
element = browser.find_element_by_id('swpm_user_name')
element.clear()
element.send_keys(USER)
element = browser.find_element_by_id('swpm_password')
element.clear()
element.send_keys(PASS)
print('フォームを送信')

#入力したデータをクリック
browser_form = browser.find_element_by_name('swpm-login')
time.sleep(3)
browser_form.click()
print("情報を入力してログインボタンを押しました。")

#ウェブサイトへアクセス
url = "https://kino-code.work/member-only/"
time.sleep(3)
browser.get(url)
print(url,":アクセス完了")

#ダウンロードボタンをクリック
frm = browser.find_element_by_xpath('/html/body/div/div[3]/div/main/article/div/p[2]/button')
time.sleep(1)
frm.click()
print("ダウンロードボタンをクリック")
