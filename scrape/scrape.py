from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import psycopg2

# データベースに接続するための設定
conn = psycopg2.connect(
    dbname="ds_pro_final", 
    user="testuser", 
    password="test000", 
    host="localhost",
    port='5432'
)
cur = conn.cursor()

driver = webdriver.Chrome()
driver.get('https://cde.ucr.cjis.gov/LATEST/webapp/#/pages/explorer/crime/crime-trend')

# 'Show More' ボタンを探してクリックするまで待機
show_more_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.ID, "crime-trend-Offender Age-showmore"))
)
show_more_button.click()


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# 加害者のデータ
offender_age_number_0_9 = soup.find('p', id='crime-trend-Offender Age-number-0-9-value')
offender_age_number_10_19 = soup.find('p', id='crime-trend-Offender Age-number-10-19-value')
offender_age_number_20_29 = soup.find('p', id='crime-trend-Offender Age-number-20-29-value')
offender_age_number_30_39 = soup.find('p', id='crime-trend-Offender Age-number-30-39-value')
offender_age_number_40_49 = soup.find('p', id='crime-trend-Offender Age-number-40-49-value')
offender_age_number_50_59 = soup.find('p', id='crime-trend-Offender Age-number-50-59-value')
offender_age_number_60_69 = soup.find('p', id='crime-trend-Offender Age-number-60-69-value')
offender_age_number_70_79 = soup.find('p', id='crime-trend-Offender Age-number-70-79-value')
offender_age_number_80_89 = soup.find('p', id='crime-trend-Offender Age-number-80-89-value')
offender_age_90_older = soup.find('p', id='crime-trend-Offender Age-number-90-Older-value')
unknown = soup.find('p', id='crime-trend-Offender Age-number-Unknown-value')
# 被害者のデータ
victim_age_number_10_19 = soup.find('p', id='crime-trend-Victim Age-number-10-19-value')
victim_age_number_20_29 = soup.find('p', id='crime-trend-Victim Age-number-20-29-value')
victim_age_number_30_39 = soup.find('p', id='crime-trend-Victim Age-number-30-39-value')
victim_age_number_40_49 = soup.find('p', id='crime-trend-Victim Age-number-40-49-value')
victim_age_number_50_59 = soup.find('p', id='crime-trend-Victim Age-number-50-59-value')
# 犯行に用いた武器等（素手も含む）
personal_weapons = soup.find('p', id='crime-trend-Type of weapon involved by offense-number-Personal Weapons-value')
handgun = soup.find('p', id='crime-trend-Type of weapon involved by offense-number-Handgun-value')
knife_cutting_instrument = soup.find('p', id='crime-trend-Type of weapon involved by offense-number-Knife/Cutting Instrument-value')
firearm = soup.find('p', id='crime-trend-Type of weapon involved by offense-number-Firearm-value')
none = soup.find('p', id='crime-trend-Type of weapon involved by offense-number-None-value')
# トータルのデータ
offender_sum_total = soup.find('p', id='crime-trend-Offender Age-number-Total')
victim_sum_total = soup.find('p', id='crime-trend-Victim Age-number-Total')
type_of_weapons_sum_total = soup.find('p', id='crime-trend-Type of weapon involved by offense-number-Total')


# 文字列を整数に変換する関数
def convert_to_int(string):
    return int(string.replace(",", ""))
if all([offender_age_number_0_9, offender_age_number_10_19, offender_age_number_20_29, offender_age_number_30_39 ,offender_age_number_40_49,offender_age_number_50_59,offender_age_number_60_69,offender_age_number_70_79,offender_age_number_80_89,offender_age_90_older,unknown,
        victim_age_number_10_19, victim_age_number_20_29, victim_age_number_30_39, victim_age_number_40_49, victim_age_number_50_59, personal_weapons, handgun, knife_cutting_instrument, firearm, none, offender_sum_total, victim_sum_total, type_of_weapons_sum_total]):
    
    # 加害者
    offender_age_number_0_9 = convert_to_int(offender_age_number_0_9.text.strip())
    offender_age_number_10_19 = convert_to_int(offender_age_number_10_19.text.strip())
    offender_age_number_20_29 = convert_to_int(offender_age_number_20_29.text.strip())
    offender_age_number_30_39 = convert_to_int(offender_age_number_30_39.text.strip())
    offender_age_number_40_49 = convert_to_int(offender_age_number_40_49.text.strip())
    offender_age_number_50_59 = convert_to_int(offender_age_number_50_59.text.strip())
    offender_age_number_60_69 = convert_to_int(offender_age_number_60_69.text.strip())
    offender_age_number_70_79 = convert_to_int(offender_age_number_70_79.text.strip())
    offender_age_number_80_89 = convert_to_int(offender_age_number_80_89.text.strip())
    offender_age_90_older = convert_to_int(offender_age_90_older.text.strip())
    unknown = convert_to_int(unknown.text.strip())
    
    # 被害者
    victim_age_number_10_19 = convert_to_int(victim_age_number_10_19.text.strip())
    victim_age_number_20_29 = convert_to_int(victim_age_number_20_29.text.strip())
    victim_age_number_30_39 = convert_to_int(victim_age_number_30_39.text.strip())
    victim_age_number_40_49 = convert_to_int(victim_age_number_40_49.text.strip())
    victim_age_number_50_59 = convert_to_int(victim_age_number_50_59.text.strip())
    
    # 武器
    personal_weapons = convert_to_int(personal_weapons.text.strip())
    handgun = convert_to_int(handgun.text.strip())
    knife_cutting_instrument = convert_to_int(knife_cutting_instrument.text.strip())
    firearm = convert_to_int(firearm.text.strip())
    none = convert_to_int(none.text.strip())
    
    # トータル
    offender_sum_total = convert_to_int(offender_sum_total.text.strip())
    victim_sum_total = convert_to_int(victim_sum_total.text.strip())
    type_of_weapons_sum_total = convert_to_int(type_of_weapons_sum_total.text.strip())
    # データベースにデータを挿入
    cur.execute("INSERT INTO scrape_scrape (offender_age_number_0_9, offender_age_number_10_19, offender_age_number_20_29, offender_age_number_30_39, offender_age_number_40_49, offender_age_number_50_59, offender_age_number_60_69, offender_age_number_70_79, offender_age_number_80_89, offender_age_90_older,unknown,offender_sum_total,victim_age_number_10_19,victim_age_number_20_29, victim_age_number_30_39, victim_age_number_40_49, victim_age_number_50_59, victim_sum_total,personal_weapons, handgun, knife_cutting_instrument, firearm, none,type_of_weapons_sum_total) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                (offender_age_number_0_9, offender_age_number_10_19, offender_age_number_20_29, offender_age_number_30_39, offender_age_number_40_49, offender_age_number_50_59, offender_age_number_60_69, offender_age_number_70_79, offender_age_number_80_89, offender_age_90_older, unknown,offender_sum_total, victim_age_number_10_19, victim_age_number_20_29, victim_age_number_30_39, victim_age_number_40_49, victim_age_number_50_59,victim_sum_total, personal_weapons, handgun, knife_cutting_instrument, firearm, none, type_of_weapons_sum_total))
    # 変更をコミット
    conn.commit()
# ブラウザを閉じる
driver.quit()
# データベース接続を閉じる
cur.close()
conn.close()


# なお、ローカルデータに関してはターミナルでpostgreslに入力しているため、このファイルには記述しておりません