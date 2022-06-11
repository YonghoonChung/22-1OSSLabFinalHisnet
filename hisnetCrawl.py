from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import telegram
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

print("Please type your Hisnet ID")
hisId = input()
print("Please type your Hisnet PW")
hisPw = input()
token = '5330943457:AAG9amFSl-40UdET1FmUznXj2za7FLqb_Yw'
id = 5112724408
 
bot = telegram.Bot(token)
bot.sendMessage(chat_id=id, text="Initializing...")

timestampStart = time.time()

f = open("data.txt",'w')
now = datetime.now()
hour = now.hour
min = now.minute

options = Options()
options.headless = True
s = Service('/usr/lib/chromium-browser/chromedriver') #linking to the chromedriver
driver = webdriver.Chrome(service = s,options = options)
# driver = webdriver.Chrome(service = s)
driver.implicitly_wait(3)
print("Welcome to hisnet.handong.edu")
driver.get('https://hisnet.handong.edu/')
driver.maximize_window()

search = driver.find_element(By.XPATH,"/html/frameset/frame[1]") #which frame
driver.switch_to.frame(search)

EmailField = driver.find_element(By.XPATH,"//tbody/tr[1]/td[2]/span[1]/input[1]")#login
EmailField.clear()
EmailField.send_keys(hisId)
Password = driver.find_element(By.XPATH,"//tbody/tr[3]/td[2]/input[1]")
Password.clear()
Password.send_keys(hisPw)
EmailField.send_keys(Keys.RETURN)
print("Successfully logged in! ")
#time.sleep(2)

driver.find_element(By.XPATH, "//tbody/tr[2]/td[3]/a[1]/img[1]").click()
search = driver.find_element(By.XPATH,"/html[1]/frameset[1]/frame[1]") #which frame
driver.switch_to.frame(search)
driver.find_element(By.XPATH, "//tbody/tr[2]/td[1]/div[1]/a[3]/img[1]").click()
driver.find_element(By.XPATH, "//body[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[3]/table[1]/tbody[1]/tr[3]/td[1]/table[2]/tbody[1]/tr[1]/td[2]/a[1]/img[1]").click()
driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
if(5 < hour < 24):
    search = driver.find_element(By.XPATH,"/html/frameset/frame[1]") #which frame
    driver.switch_to.frame(search)
    driver.find_element(By.XPATH, "//a[contains(text(),'Coding Talk')]").click()
    search = driver.find_element(By.XPATH,'//*[@id="calFrame"]') #switch frame
    # time.sleep(5)
    if(min<45):
        hour -= 4
    else:
        hour -= 3
    if min < 15:
        m1 = 1
        m2 = 3
    elif min < 30:
        m1 = 3
        m2 = 1
    elif min < 45:
        m1 = 3
        m2 = 3
    else:
        m1 = 1
        m2 = 1

    xpath_now = "/html/body/form/table[3]/tbody/tr/td[3]/table/tbody/tr["+str(hour)+"]/td/table/tbody/tr["+str(m1)+"]/td["+str(m2)+"]"
#     xpath_now = "/html/body/form/table[3]/tbody/tr/td[5]/table/tbody/tr[9]/td/table/tbody/tr[1]/td[1]"
    info = ["/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[2]/td[2]","/html[1]/body[1]/table[1]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[3]/td[2]"]

    driver.switch_to.frame(search)
    driver.find_element(By.XPATH, xpath_now).click()
    tabs = driver.window_handles
    if(len(tabs)==2):
        print("checking Coding Talk...")
        driver.switch_to.window(driver.window_handles[-1])
        f.writelines(driver.find_element(By.XPATH,info[0]).text+'\n')
        f.writelines(driver.find_element(By.XPATH,info[1]).text+'\n')
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    else:
        f.writelines("It is empty"+'\n')
        f.writelines("No phoneNo"+'\n')
    driver.switch_to.parent_frame()
    #time.sleep(3)
    for i in range(1,11):
        search = driver.find_element(By.XPATH,"/html/frameset/frame[1]") #which frame
        driver.switch_to.frame(search)
        link = "//a[contains(text(),'상상랩"+('0' if (i<10) else '')+str(i)+"')]"
        driver.find_element(By.XPATH, link).click()#LAB1
        search = driver.find_element(By.XPATH,'//*[@id="calFrame"]') #switch frame
        driver.switch_to.frame(search)
        driver.find_element(By.XPATH, xpath_now).click()
        tabs = driver.window_handles
        if i == 6:
            bot.sendMessage(chat_id=id, text="Almost...")
        if(len(tabs)==2):
            driver.switch_to.window(driver.window_handles[-1])
            print(f"checking 상상랩{i}...")
            f.writelines(driver.find_element(By.XPATH,info[0]).text+'\n')
            f.writelines(driver.find_element(By.XPATH,info[1]).text+'\n')
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        else:
            f.writelines("It is empty"+'\n')
            f.writelines("No phoneNo"+'\n')
        driver.switch_to.parent_frame()
else:
    print("please try between 05:00 and 24:00")
timestampEnd = time.time()
duration = round(timestampEnd- timestampStart)
print("Working Time : {} sec".format(duration))
#time.sleep(5)
f.close()
driver.quit()
print("Thank you~")

f = open("data.txt","r")
lists = []
while True:
    line = f.readline().strip()
    if not line : break
    lists.append(line)
j = 1
for i in range(len(lists)):
    if i == 0 :
        print("Coding Talk")
    if i != 0 and i%2 == 0:
        msg = "Conference Room 0" + str(j)
        if i == 20:
            msg = "Conference Room 10"
        print(msg)
        j += 1
    print(lists[i])
    



bot.sendMessage(chat_id=id, text="Ready to use!")
starting_msg ='Which conference room do you want?\n-codingTalk\n-conference01~10'
bot.sendMessage(chat_id=id, text=starting_msg)
updater = Updater(token=token, use_context=True)
dispatcher = updater.dispatcher
updater.start_polling()

def handler(update, context):
    user_text = update.message.text
    if user_text == "codingTalk": 
        bot.send_message(chat_id=id, text=lists[0])
        bot.send_message(chat_id=id, text=lists[1])
    elif user_text == "conference01":
        bot.send_message(chat_id=id, text=lists[2])
        bot.send_message(chat_id=id, text=lists[3])
    elif user_text == "conference02":
        bot.send_message(chat_id=id, text=lists[4])
        bot.send_message(chat_id=id, text=lists[5])
    elif user_text == "conference03":
        bot.send_message(chat_id=id, text=lists[6])
        bot.send_message(chat_id=id, text=lists[7])
    elif user_text == "conference04":
        bot.send_message(chat_id=id, text=lists[8])
        bot.send_message(chat_id=id, text=lists[9])
    elif user_text == "conference05":
        bot.send_message(chat_id=id, text=lists[10])
        bot.send_message(chat_id=id, text=lists[11])
    elif user_text == "conference06":
        bot.send_message(chat_id=id, text=lists[12])
        bot.send_message(chat_id=id, text=lists[13])
    elif user_text == "conference07":
        bot.send_message(chat_id=id, text=lists[14])
        bot.send_message(chat_id=id, text=lists[15])
    elif user_text == "conference08":
        bot.send_message(chat_id=id, text=lists[16])
        bot.send_message(chat_id=id, text=lists[17])
    elif user_text == "conference09":
        bot.send_message(chat_id=id, text=lists[18])
        bot.send_message(chat_id=id, text=lists[19])
    elif user_text == "conference10":
        bot.send_message(chat_id=id, text=lists[20])
        bot.send_message(chat_id=id, text=lists[21])
    else:
        bot.send_message(chat_id=id, text="Please type again")
echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)

# 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
