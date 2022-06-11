# 2022 OSS Final project
# Why Not Use This Place?
## Youtube Link: 

## What does this project do?
- This project uses the open-source selenium and chrome-driver to scrape the booker’s name and phone number from the Hisnet reservation page.
- It shows the data through the linux command line and telegram chat bot. 
<img width="759" alt="스크린샷 2022-06-11 오후 4 07 19" src="https://user-images.githubusercontent.com/96009062/173177562-bcdef021-1bf8-49b7-9f65-15543a54305e.png">
<img width="200" alt="스크린샷 2022-06-11 오후 4 07 28" src="https://user-images.githubusercontent.com/96009062/173177645-34befee4-34b5-4ec9-bc0d-4176dd5edf2d.png">
<img width="296" alt="스크린샷 2022-06-11 오후 4 19 50" src="https://user-images.githubusercontent.com/96009062/173177904-8678677d-575c-47ee-9ec9-c91d8fee2906.png">
* Telegram bot
<img width="372" alt="스크린샷 2022-06-11 오후 4 55 03" src="https://user-images.githubusercontent.com/96009062/173179025-c2113675-30e3-427a-991b-5e842b782dbd.png">
* Chats
<img width="420" alt="스크린샷 2022-06-11 오후 4 56 37" src="https://user-images.githubusercontent.com/96009062/173179082-71b2114d-9f02-410f-ba1d-21689ff1c085.png">
## Why is this project useful?
- During this semester, I realized that several people irresponsibly booked the conference room and did not show up. This leads to the waste of materials. I wondered how to solve this issue, then the answer did not easily pop up. What about we let the other people just use this room after getting permission. Therefore this program has come out.
- I thought it will be great if someone tells me the name and phone number of the booker, then I might be able to take an action on whether to use this room for a few minutes.
- This project is very useful to everyone. By using this program, students can find better places and efficient ways of using the conference room. Also, this program indicates the empty room at the time. Without using this program, a person had to visit every page of the conference room whether the room is empty or not. However, by waiting until the program is getting ready, the user can easily find which room is empty and which room it shouldn't be empty.


## How to get started?
<p float="left">
  <img width = "400" src ="https://user-images.githubusercontent.com/96009062/173178330-9f21c210-38e6-459b-bee5-6ec75a386423.png"/><img width = "200" src ="https://user-images.githubusercontent.com/96009062/173178380-cacc0931-be9e-4af2-99cb-d4e1ec2b62df.jpeg"/>
</p>

- Download these programs in raspberry pi
```
sudo apt-get update
sudo apt install python3 idle3
sudo apt install chromium-chromedriver
sudo pip3 intall selenium
```
You are ready to go!

* Go to its cloned repository and type `python3 hisnetCrawl.py` 
## Errors while you are installing
Once you started downloading and type these simple code, it might now work
```
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://automatetheboringstuff.com')
```
The error might looks like this.
```
"session not created: This version of ChromeDriver only supports Chrome version 101
Current browser version is 98.0.4758.106 with binary path /usr/bin/chromium-browser"
```

## Where can people get more help, if needed?

## Reference
* https://ivanderevianko.com/2020/01/selenium-chromedriver-for-raspberrypi
* https://stackoverflow.com/questions/64979042/how-to-run-seleniumchrome-on-raspberry-pi-4
* https://py-son.tistory.com/8?category=917185