from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

print(time.ctime())

chrome_options = Options()
chrome_options.add_argument("--disable-infobars")  # Disable infobars that may affect zooming
chrome_options.add_argument("--disable-extensions")  # Disable extensions
chrome_options.add_argument("--force-device-scale-factor=1.0")  # Set the initial zoom level

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://revenue.kerala.gov.in/")
time.sleep(3)

driver.maximize_window()
time.sleep(2)
iframe = driver.find_element_by_xpath('//*[@id="mainFrame"]')

driver.switch_to.frame(iframe)
element = driver.find_element_by_xpath("/html/body/form/div[2]/div/div[2]/div[1]/div/div/div/div[3]/nav/ul[2]/li[1]")
driver.execute_script("arguments[0].click();", element)
time.sleep(1)

driver.find_element_by_xpath('//*[@id="main-content"]/div[6]/div/div[1]/div/ul/li[3]/a').click()
time.sleep(1)

wait=WebDriverWait(driver, 30)
wait.until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="districtwise"]/option[6]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="talukwise"]/option[3]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="villagewise"]/option[4]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="svrvwisesrch"]/option[3]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="blockwise"]/option[2]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="oldsurno"]'))).send_keys(23)
wait.until(EC.element_to_be_clickable((By.XPATH,f'//*[@id="oldreslt"]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH,f'(//input[@name="get4"])[6]'))).click()
time.sleep(3)

# Table screenshot and extracting data
table_element = driver.find_element_by_xpath("//*[@id='datas']")
print(table_element.text)
table_element.screenshot("table_screenshot.png")

time.sleep(2)
driver.close()
print(time.ctime())


# database = []
# dis_db = []
# dis = driver.find_element_by_id('districtwise')
# dis_db.extend(dis.text.split('\n'))
# try:
#     for i in range(2,len(dis_db)):
#         dis = driver.find_element_by_xpath(f'//*[@id="districtwise"]/option[{i}]')
#         dis.click()
#         time.sleep(3)

#         teh_db = []
#         teh = driver.find_element_by_id('talukwise')
#         time.sleep(3)
#         teh_db.extend(teh.text.split('\n'))
#         for j in range(2,len(teh_db)):
#             teh = driver.find_element_by_xpath(f'//*[@id="talukwise"]/option[{j}]')
#             teh.click()
#             time.sleep(3)

#             vil_db = []
#             vil = driver.find_element_by_id('villagewise')
#             time.sleep(4)
#             vil_db.extend(vil.text.split('\n'))
#             for k in range(2,len(vil_db)):
#                 database.append(dis_db[i-1]+'%'+teh_db[j-1]+'%'+vil_db[k-1])
#                 print(dis_db[i-1]+'%'+teh_db[j-1]+'%'+vil_db[k-1])

#     a = [i.split('%') for i in  database]
#     df = pd.DataFrame(a,columns=['District','Taluka' ,'Village'])
#     df.to_excel('Kerala.xlsx',index=True,  engine='xlsxwriter')
      
# except Exception as e:
#     print(str(e))
#     a = [i.split('%') for i in  database]
#     df = pd.DataFrame(a,columns=['District','Taluka' ,'Village'])
#     df.to_excel('Kerala_1.xlsx',index=True,  engine='xlsxwriter')
#     driver.quit()