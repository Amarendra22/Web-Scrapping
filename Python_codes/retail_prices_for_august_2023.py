from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class FindElementByID():
    def locate_by_id(self):

        global downloaded_files
        website = 'https://fcainfoweb.nic.in/reports/report_menu_web.aspx'

        driver = webdriver.Chrome()

        driver.get(website)
        # This will open the website in chrome browser

        driver.maximize_window()

        time.sleep(2)

        retail = Select(driver.find_element(By.ID, 'ctl00_MainContent_Ddl_Rpt_type'))
        retail.select_by_visible_text("Retail")
        time.sleep(2)

        price = driver.find_element(By.XPATH, "//input[@id='ctl00_MainContent_Rbl_Rpt_type_0']")
        price.click()
        time.sleep(2)

        daily_prices = Select(driver.find_element(By.ID, 'ctl00_MainContent_Ddl_Rpt_Option0'))
        daily_prices.select_by_visible_text("Daily Prices")
        time.sleep(2)

        date_input = driver.find_element(By.ID, 'ctl00_MainContent_Txt_FrmDate')
        date_input.click()

        month_select = driver.find_element(By.XPATH, "//div[@id='ctl00_MainContent_CalendarExtender_frmdate_title']")
        month_select.click()
        time.sleep(2)

        month_select_august = driver.find_element(By.ID, f'ctl00_MainContent_CalendarExtender_frmdate_month_1_3')
        month_select_august.click()
        time.sleep(2)

        for day_id_firstrow in range(2, 7):
            date_select = driver.find_element(By.ID, f'ctl00_MainContent_CalendarExtender_frmdate_day_0_{day_id_firstrow}')
            date_select.click()
            time.sleep(2)

            get_data = driver.find_element(By.ID, 'ctl00_MainContent_btn_getdata1')
            get_data.click()
            time.sleep(2)

            get_excel_data = driver.find_element(By.ID, 'btnsave')
            get_excel_data.click()
            time.sleep(2)

            go_back = driver.find_element(By.ID, 'btn_back')
            go_back.click()
            time.sleep(2)

            driver.get(website)
            time.sleep(2)

            retail = Select(driver.find_element(By.ID, 'ctl00_MainContent_Ddl_Rpt_type'))
            retail.select_by_visible_text("Retail")
            time.sleep(2)

            price = driver.find_element(By.XPATH, "//input[@id='ctl00_MainContent_Rbl_Rpt_type_0']")
            price.click()
            time.sleep(2)

            daily_prices = Select(driver.find_element(By.ID, 'ctl00_MainContent_Ddl_Rpt_Option0'))
            daily_prices.select_by_visible_text("Daily Prices")
            time.sleep(2)

            date_input = driver.find_element(By.ID, 'ctl00_MainContent_Txt_FrmDate')
            date_input.click()

            month_select = driver.find_element(By.XPATH, "//div[@id='ctl00_MainContent_CalendarExtender_frmdate_title']")
            month_select.click()
            time.sleep(2)

            month_select_august = driver.find_element(By.ID, f'ctl00_MainContent_CalendarExtender_frmdate_month_1_3')
            month_select_august.click()
            time.sleep(2)

        for row_id in range(1, 4):
            for day_id in range(0, 7):
                month_select_august_1 = driver.find_element(By.ID, f'ctl00_MainContent_CalendarExtender_frmdate_day_{row_id}_{day_id}')
                month_select_august_1.click()
                time.sleep(2)

                get_data = driver.find_element(By.ID, 'ctl00_MainContent_btn_getdata1')
                get_data.click()
                time.sleep(2)

                get_excel_data = driver.find_element(By.ID, 'btnsave')
                get_excel_data.click()
                time.sleep(2)

                go_back = driver.find_element(By.ID, 'btn_back')
                go_back.click()
                time.sleep(2)

                driver.get(website)
                time.sleep(2)

                retail = Select(driver.find_element(By.ID, 'ctl00_MainContent_Ddl_Rpt_type'))
                retail.select_by_visible_text("Retail")
                time.sleep(2)

                price = driver.find_element(By.XPATH, "//input[@id='ctl00_MainContent_Rbl_Rpt_type_0']")
                price.click()
                time.sleep(2)

                daily_prices = Select(driver.find_element(By.ID, 'ctl00_MainContent_Ddl_Rpt_Option0'))
                daily_prices.select_by_visible_text("Daily Prices")
                time.sleep(2)

                date_input = driver.find_element(By.ID, 'ctl00_MainContent_Txt_FrmDate')
                date_input.click()

                month_select = driver.find_element(By.XPATH, "//div[@id='ctl00_MainContent_CalendarExtender_frmdate_title']")
                month_select.click()
                time.sleep(2)

                month_select_august = driver.find_element(By.ID, f'ctl00_MainContent_CalendarExtender_frmdate_month_1_3')
                month_select_august.click()
                time.sleep(2)

        for day_id in range(0, 5):
            month_select_august_1 = driver.find_element(By.ID, f'ctl00_MainContent_CalendarExtender_frmdate_day_4_{day_id}')
            month_select_august_1.click()
            time.sleep(2)

            get_data = driver.find_element(By.ID, 'ctl00_MainContent_btn_getdata1')
            get_data.click()
            time.sleep(2)

            get_excel_data = driver.find_element(By.ID, 'btnsave')
            get_excel_data.click()
            time.sleep(2)

            go_back = driver.find_element(By.ID, 'btn_back')
            go_back.click()
            time.sleep(2)

            driver.get(website)
            time.sleep(2)

            retail = Select(driver.find_element(By.ID, 'ctl00_MainContent_Ddl_Rpt_type'))
            retail.select_by_visible_text("Retail")
            time.sleep(2)

            price = driver.find_element(By.XPATH, "//input[@id='ctl00_MainContent_Rbl_Rpt_type_0']")
            price.click()
            time.sleep(2)

            daily_prices = Select(driver.find_element(By.ID, 'ctl00_MainContent_Ddl_Rpt_Option0'))
            daily_prices.select_by_visible_text("Daily Prices")
            time.sleep(2)

            date_input = driver.find_element(By.ID, 'ctl00_MainContent_Txt_FrmDate')
            date_input.click()

            month_select = driver.find_element(By.XPATH, "//div[@id='ctl00_MainContent_CalendarExtender_frmdate_title']")
            month_select.click()
            time.sleep(2)

            month_select_august = driver.find_element(By.ID, f'ctl00_MainContent_CalendarExtender_frmdate_month_1_3')
            month_select_august.click()
            time.sleep(2)

# Initialize the code
finder = FindElementByID()
finder.locate_by_id()
