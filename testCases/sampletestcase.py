from selenium.webdriver import Ie
import time
import sys

for n in range(5):
    print(sys.stdin.write('!',end=" "))

#specify where your chrome driver present in your pc
#PATH=r"C:\Users\educative\Documents\chromedriver\chromedriver.exe"
# PATH=r"C:\\Users\\Suresh Konni\\PycharmProjects\\Avaaomo\\msedgedriver.exe"
# print("Hi")
# input()
# #get instance of web driver
# driver = Ie(PATH)
#
#
# #provide website url here
# #driver.get("www.google.com")
# driver.maximize_window()
# driver.get("https://c6.avaamo.com/web_channels/c767654d-6709-43f6-bb0c-ce1d2c559f6a/demo.html?banner=true&demo=true&banner_text=%20&banner_title=This%20is%20how%20the%20chat%20agent%20shows%20up")
#
# driver.save_screenshot(".\\ScreenShots\\"+"test_homePageTitle.png")
# #sleep for 2 seconds
# time.sleep(2)
#
#
# #click on the link to get popup
# popup_link = driver.find_element("xpath", '/html[1]/body[1]/div[2]/div[3]/a[1]/img[1]').click()
#
# #get instance of first pop up  window
# whandle = driver.window_handles[1]
#
# #switch to pop up window
# driver.switch_to.window(whandle)
#
# # #get text of a element in pop window
# # print(driver.find_element("id","para1").text)
# #
# # #sleep for 1 second
# time.sleep(1)
#
# #closes current window
# driver.close()