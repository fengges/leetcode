#最正确的版本，但是在没有搜索词的时候鼠标不会移动，应给是句柄位置的关系
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,ElementNotVisibleException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import calendar
import time
import pyautogui
import xlwt
import os
from selenium.webdriver.common.keys import Keys
#登录，输入关键词，最大化界面，选择全部日期
def init_spider(keyword):
    '''
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")#设置chrome为headless模式
    chrome_options.add_argument("--disable-gpu")
    '''
    url = 'http://index.baidu.com/'
    chromePath = 'chromedriver.exe'  # Chromedriver的路径
    #driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=chromePath)  # 打开浏览器
    driver = webdriver.Chrome(executable_path=chromePath)  # 打开浏览器
    driver.get(url)  # 打开网站
    cookieList = [{'domain': '.index.baidu.com', 'httpOnly': False, 'name': 'Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc',
                   'path': '/', 'secure': False, 'value': '1550887201'},
                  {'domain': '.baidu.com', 'expiry': 1582423184.563163, 'httpOnly': False, 'name': 'BAIDUID',
                   'path': '/', 'secure': False, 'value': '50C5105A44FDAF8B13979DA6BD118AFF:FG=1'},
                  {'domain': '.index.baidu.com', 'expiry': 1582423201, 'httpOnly': False,
                   'name': 'Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc', 'path': '/', 'secure': False,
                   'value': '1550887185'},
                  {'domain': '.baidu.com', 'expiry': 1810087199.519391, 'httpOnly': True, 'name': 'BDUSS', 'path': '/',
                   'secure': False,
                   'value': 'XY0SEw0Rmxjb2RLSXFLVVZlWElMVnlvRWFESERGaW1Va1NUVnczaHU1Z3ZOcGhjQVFBQUFBJCQAAAAAAAAAAAEAAACiCMtSaG91c2XB1rLosugAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC-pcFwvqXBca'},
                  {'domain': 'index.baidu.com', 'expiry': 1550973600.889628, 'httpOnly': False, 'name': 'CHKFORREG',
                   'path': '/', 'secure': False, 'value': '12d9ff823e2f294c2c403f8f6b435ca5'}]
    for cookie in cookieList:
        driver.add_cookie(cookie)
    driver.get(url)
    time.sleep(1)
    driver.refresh()
    # 第一次登录，将这两行取消注释，后三行进行注释
    # 输入关键词并最大化界面
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class='search-input']")))
    driver.find_element_by_xpath("//input[@class='search-input']").send_keys(keyword)
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='search-input-cancle']")))
    driver.find_element_by_xpath("//span[@class='search-input-cancle']").click()
    driver.maximize_window()

    HTMLdata = driver.page_source  # 获得页面代码
    return driver



#清除搜索框的值，并输入关键词，点击确定，得到关键词的搜索指数页面
def second(driver,keyword):
    time.sleep(0.05)
    #将搜索框全选
    driver.find_element_by_xpath('//*[@id="search-input-form"]/input[3]').send_keys(Keys.CONTROL,'a')
    #将搜索框清除
    driver.find_element_by_xpath('//*[@id="search-input-form"]/input[3]').send_keys(Keys.BACKSPACE)
    #在关键词框框里输入关键词
    driver.find_element_by_xpath('//*[@id="search-input-form"]/input[3]').send_keys(keyword)
    #点击确定class="keyword-group__ok"
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div/div[1]/div/span/span')))
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[1]/div/span/span').click()
    # 打开页面后，将日期选为全部
    time.sleep(0.5)
    #for handle in driver.window_handles:  # 方法二，始终获得当前最后的窗口，操纵句柄
        #driver.switch_to.window(handle)
    # 点击日期选项按钮
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//div[@class="index-dropdown-list"]/button/span[contains(text(), "近30天")] | //div[@class="index-dropdown-list"]/button/span[contains(text(), "全部")]')))
    driver.find_element_by_xpath('//div[@class="index-dropdown-list"]/button/span[contains(text(), "近30天")] | //div[@class="index-dropdown-list"]/button/span[contains(text(), "全部")]').click()
    # 点击选择全部日期
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[6]")))
    driver.find_element_by_xpath("/html/body/div[3]/div/div/div[6]").click()
    time.sleep(0.5)
    #driver.refresh()
    # 选中搜索指数图形区域，同时鼠标在上面显示出来
    WebDriverWait(driver, 10, 0.5).until(
        EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[1]/canvas")))
    driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[1]/canvas").click()
    time.sleep(0.05)
    return driver



firstword='北汽新能源'
driver = init_spider(firstword)
#创建要写入的EXCEL
file='奥迪1'+'.xls'
f=xlwt.Workbook()
sheet1=f.add_sheet(u'sheet1',cell_overwrite_ok=True)#创建sheet
#写入日期
#获取每个车型
#brand_url = 'D:/Python/pythonproject/SpiderbaiduIndex-python-master/car-brand-chinese/' + '奥迪' + '.txt'
#fileOfBrand = open(brand_url, 'r').read()
#brand_list = fileOfBrand.split(',')
#brand_list = list(brand_list)#获取了每个车型的名字的列表
brand_list=['奥迪','宝马','奔驰','大众']
j=1
for car in range(0, len(brand_list)):
            #开始访问每个车型
            if len(brand_list[car]) != 0:#如果这个名字不为空，就继续以下步骤
                keyword=brand_list[car]
                i = 0
                browser = second(driver, keyword)  # 在页面输入关键词
                # for handle in browser.window_handles:  # 方法二，始终获得当前最后的窗口，操纵句柄
                #     browser.switch_to.window(handle)
                for x in range(400, 500, 2):  # 移动鼠标,最左边开始是63，最右边结束是1261
                    i = i + 1
                    # time.sleep(2)
                    pyautogui.moveTo(x, 600)  # 鼠标滑动到这个位置
                    # browser.refresh()
                    time.sleep(0.01)
                    if j == 1:
                        title1 = 'data'
                        sheet1.write(0, 0, title1)
                        # 获取时间，数据类型为字符串
                        date = browser.find_element_by_xpath(
                                "/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[2]/div[1]").get_attribute('textContent')
                        sheet1.write(i, 0, date)
                            # print(data)
                            # 获取搜索量，数据类型为字符串
                    search = browser.find_element_by_xpath("html/body/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div[1]/div/div[2]/div[2]/div[2]").get_attribute('textContent')
                    search = search.strip()
                    ##print('--------------')
                    sheet1.write(i, j, search)
                #except TimeoutException:
                    #print('---------------------------' + keyword + '未能读取信息')
                sheet1.write(0, j, str(keyword))#写入标题
                f.save(file)  # 保存文件
                j = j + 1
                print('-------------------' + keyword + '已爬完')
                #browser.delete_all_cookies()
