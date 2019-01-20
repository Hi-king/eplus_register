import selenium.webdriver
from selenium.webdriver.support.ui import Select
import time

class Eplus(object):
    def __init__(self, config):
        self.driver = selenium.webdriver.Chrome()
        self.login_id = config["loginId"]
        self.login_password = config["loginPassword"]
        self.card_selector = config["cardSelectorDOM"]
        self.card_cvc = config["cardCVC"]

    def run(self, serial, num_date):
        self.driver.get("http://eplus.jp/million6th-cd")

        # select
        buttons = self.driver.find_elements_by_class_name("ticket-area")
        buttons[num_date+2].click()

        # serial
        form = self.driver.find_element_by_class_name("input_form")
        form.find_element_by_id("idFreeItem1").send_keys(serial)
        form.find_element_by_id("idFreeItem1").submit()

        # select
        self.driver.find_element_by_class_name("bt-area").click()

        #login
        self.driver.find_element_by_class_name("login-bt").find_element_by_tag_name("a").click()

        # fill and login
        # print("fill")
        for i in range(30):
            try:
                time.sleep(5)
                self.driver.find_element_by_id("loginId").send_keys(self.login_id)
                self.driver.find_element_by_id("loginPassword").send_keys(self.login_password)

                self.driver.find_element_by_id("idPwLogin").click()
                break

                # time.sleep(5)
                # self.driver.find_element_by_id("loginId").submit()
            except Exception:
                time.sleep(5)

        # pull down
        for i in range(30):
            try:
                hope_area = self.driver.find_element_by_class_name("hope-area")
                selects = hope_area.find_elements_by_tag_name("select")
                print("slecgs", selects)
                Select(selects[0]).select_by_index(1)
                Select(selects[1]).select_by_index(1)
                Select(selects[2]).select_by_index(2)
                # self.driver.find_element_by_name("uji.model.1963585.combo").select_by_index(0)
                # self.driver.find_element_by_name("uji.model.1963592.combo").select_by_index(0)
                # self.driver.find_element_by_name("uji.model.1963593.combo").select_by_index(1)
                self.driver.find_element_by_class_name("enter-bt").click()
                break
            except Exception as e:
                print(e)
                time.sleep(5)

        # buy
        for i in range(30):
            try:
                self.driver.find_element_by_id("i2").click()
                self.driver.find_element_by_id("i6").click()
                self.driver.find_element_by_id("sm-menu-card").click()
                self.driver.find_element_by_id(self.card_selector).click()

                trs = self.driver.find_element_by_class_name("i-input-area").find_elements_by_tag_name("tr")
                inputs = trs[3].find_elements_by_tag_name("input")
                inputs[0].send_keys(self.card_cvc)

                self.driver.find_element_by_class_name("enter-bt").click()
                break
            except Exception as e:
                print(e)
                time.sleep(5)

        for i in range(30):
            try:
                # self.driver.find_elements_by_tag_name("input")[0].click()
                self.driver.find_elements_by_xpath("//input[@type='radio']")[0].click()
                self.driver.find_element_by_class_name("enter-bt").click()
                break
            except Exception as e:
                print(e)
                time.sleep(5)


