#!/usr/bin/env python3
# -*- coding:utf -8 -*-
# !/usr/bin/env python3
# -*- coding:utf -8 -*-
import shelve

import selenium
from selenium import webdriver
# import webbrowser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestBrowser():
    def setup_method(self):
        # 复用浏览器
        # options = Options()
        # options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        # self.driver.quit()
        pass

    def test_testchrome(self):
        self.driver.get("https://www.baidu.com")

    def test_weixin(self):
        self.driver.find_element(By.ID, "menu_contacts").click()

    def test_cookie(self):
        # 通过get_cookies()可以获取当前页面的cookiesx信息
        # add_cookies()可以把添加到当前页面中去
        cookies = self.driver.get_cookies()
        print(cookies)
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688851197686367'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': '_xeteOUW-JgLf4n_vNm0_Tuwxw2zyJEQ4dgDk6cY3AjwwG8-9fzOnIh3CqOxGs0O2YctOz7XJzJQ-t3eMKsz-tNjETNK5aJcCzfQLpYyOqQvgRF4OS1bFz91km5eTS5CI1pdVO73G999XMCBApoe_F9cluNpx1vI3EdkOabzcln9J4Uon_blryPi2W3pcjctBLD6QGIKVBBglHtILzB9uyxmM30yWyzKEUWC40l0VoAIOy6QPvrHT_k37IN10rB1GqvjY4kQU1SPxeWyGkfsQA'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970325016163252'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '186707059261430'},
        #     {'domain': '.qq.com', 'expiry': 1603784628, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.555762051.1603637393'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1603712957, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '8s18kc5'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'iSM8bvjWDeaTXx5rb9eodYJrztx6Zahw_4dvQE6V1VtBFZ6FDlSIbUpZ--LHviIW'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1634968500, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': True, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1634981733, 'httpOnly': False,
        #      'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True,
        #      'value': '1603432503,1603445733'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1606290231, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a1831122'},
        #     {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
        #      'value': 'mMrQ8SxWFw'},
        #     {'domain': '.qq.com', 'expiry': 1666770228, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.125183880.1603432505'},
        #     {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
        #      'value': 'f8528b57e2d6bb43839ef7317b3726f392a759a2f738d7181cca74240b52662d'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688851197686367'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1603712957, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': True, 'value': '8s18kc5'},
        #     {'domain': '.qq.com', 'expiry': 2147731200, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': True, 'value': '1061033452281286'}]
        # shelve内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库
        # 可以通过key,value 来把数据保shelve中

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")

    def test_shelve(self):
        # cookies = [
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
        #      'value': '1688851197686367'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
        #      'value': '_xeteOUW-JgLf4n_vNm0_Tuwxw2zyJEQ4dgDk6cY3AjwwG8-9fzOnIh3CqOxGs0O2YctOz7XJzJQ-t3eMKsz-tNjETNK5aJcCzfQLpYyOqQvgRF4OS1bFz91km5eTS5CI1pdVO73G999XMCBApoe_F9cluNpx1vI3EdkOabzcln9J4Uon_blryPi2W3pcjctBLD6QGIKVBBglHtILzB9uyxmM30yWyzKEUWC40l0VoAIOy6QPvrHT_k37IN10rB1GqvjY4kQU1SPxeWyGkfsQA'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
        #      'value': '1970325016163252'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
        #      'value': '186707059261430'},
        #     {'domain': '.qq.com', 'expiry': 1603784628, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.555762051.1603637393'},
        #     {'domain': 'work.weixin.qq.com', 'expiry': 1603712957, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': False, 'value': '8s18kc5'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
        #      'value': 'iSM8bvjWDeaTXx5rb9eodYJrztx6Zahw_4dvQE6V1VtBFZ6FDlSIbUpZ--LHviIW'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1634968500, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
        #      'path': '/', 'secure': True, 'value': '0'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1634981733, 'httpOnly': False,
        #      'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True,
        #      'value': '1603432503,1603445733'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1606290231, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
        #      'path': '/', 'secure': False, 'value': 'zh'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
        #      'value': '1'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
        #      'value': 'direct'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
        #      'value': 'a1831122'},
        #     {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True,
        #      'value': 'mMrQ8SxWFw'},
        #     {'domain': '.qq.com', 'expiry': 1666770228, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
        #      'value': 'GA1.2.125183880.1603432505'},
        #     {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True,
        #      'value': 'f8528b57e2d6bb43839ef7317b3726f392a759a2f738d7181cca74240b52662d'},
        #     {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
        #      'value': '1688851197686367'},
        #     {'domain': '.work.weixin.qq.com', 'expiry': 1603712957, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
        #      'secure': True, 'value': '8s18kc5'},
        #     {'domain': '.qq.com', 'expiry': 2147731200, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
        #      'secure': True, 'value': '1061033452281286'}]

        # shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库#可以通过 key，value 来把数据保存到shelve中
        # 读取cookies
        db = shelve.open("cookies")
        # db['cookies'] = cookies
        # 利用读取的cookies完成登陆操作
        cookies = db['cookies']

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        db.close()

        # 找到倒入联系人按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "/Users/melot/Downloads/通讯录批量导入模板.xlsx")
        # 验证上传文件
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "通讯录批量导入模板.xlsx" == filename

        # self.driver.find_element(By.CSS_SELECTOR,".qui_btn ww_btn ww_btn_Large ww_btn_Blue ww_fileImporter_submit").click
