import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import time
from PIL import Image
import datetime
import winapps
from io import BytesIO
import cv2
import numpy as np
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
requests.urllib3.disable_warnings()

def chrome_setup():
    """"
        A function for chrome setup and also check chrome is alreday installed
        or not in the machines

    Returns:
        driver and action object of a chrome setup
    """
    try:
        if winapps.search_installed('chrome'):
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--disable-notifications')
            options.add_argument("--disable-popup-blocking")
            options.add_argument('--ignore-ssl-errors')
            driver = webdriver.Chrome('./chromedriver.exe',chrome_options=options)
            action = ActionChains(driver)
            # maximize with maximize_window()
            driver.maximize_window()
            # Dismiss the popup alert
            driver.switch_to.alert.dismiss()
        else:
            raise ValueError("Chrome is not installed in the system")
    except ValueError as value_error:
        print("Observed Error - Chrome is not present in the given machine")
    except Exception as ex:
            print("Observed Error {0}".format(ex))
    
    return driver,action

driver,action = chrome_setup()

class KVM_Screen_Recorder():
    def __init__(self):
        self._bmc_ip = "10.45.132.207"
        self._bmc_login_password = '0penBmc1'
        self._bmc_login_username = 'debuguser'
        
        
    def open_bmc_login(self):
        """
            A function to open BMC Login Page
        """
        try:
            url = (r'https://{0}/#/login.'.format(self._bmc_ip))
            driver.get(url)
            username = driver.find_element(By.ID,"username")
            password = driver.find_element(By.ID,"password")

            username.send_keys(self._bmc_login_username)
            password.send_keys(self._bmc_login_password)

            # Explicit wait
            wait = WebDriverWait(driver, 5)
            element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[data-test-id = login-button-submit]")))
            
            # create action chain object
            element.submit()
            # click the item
            action.click(on_element = element)
            # perform the operation
            action.perform()
            driver.implicitly_wait(15)
            time.sleep(5)
            #self.capture_screenshot_alone(file_name="screenkvm")
            self.mount_image()
            driver.implicitly_wait(5)

        except Exception as ex:
            print("Failed to open the login page {0}".format(self._bmc_ip))
            print("Observed Error {0}".format(ex))

    def is_already_logged_in(self, driver):
        """
           A function for checking already logged in function

        Returns:
            True or False according to logged in or not
        """
        cookies = driver.get_cookies() # returns list of dicts
        login_status = False
        for cookie in cookies:
            if cookie['name'] == 'XSRF-TOKEN':
                login_status = True
                break
        if login_status:
            return True
        else:
            return False
        
    def capture_screenshot_alone(self , file_name = None):
        """
                A function to capture screenshots of the BMC page and save the screenshot
            return :
                  captured screenshot of the bmc page
        """
        # if already not login then first ,login
        if not self.is_already_logged_in(driver):
            self.open_bmc_login()
        # now that we have the preliminary stuff out of the way time to get that image :D
        driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/nav/ul/li[4]/button').click()
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,'//*[@id="operations"]/li/a[1]').click()
        element = driver.find_element(By.XPATH,"//*[@id='terminal-kvm']/div/canvas")
        sleep(20)
        # find part of the page you want image of
        location = element.location
        size = element.size
        png = driver.get_screenshot_as_png() # saves screenshot of entire page
        #driver.quit()
        im = Image.open(BytesIO(png)) # uses PIL library to open image in memory
        left = location['x']
        top = location['y']
        right = location['x'] + 1.5*size['width']
        bottom = location['y'] + 1.5*size['height']

        # save with date and time
        DateString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        if file_name == None:
            NewFolder = 'Screenshot_' + DateString
        else:
            NewFolder = file_name + DateString
        im = im.crop((left, top, right, bottom)) # defines crop points
        im.save(NewFolder +'.png') # saves new cropped image
        return im

    def screen_recorder(self, file_name , record_time_in_sec):
        """
                A function to record the screen of the BMC page
                and save the screenshot
        """
        # if already not login then first ,login
        if not self.is_already_logged_in(driver):
            self.open_bmc_login()

        element = driver.find_element(By.XPATH,"//*[@id='terminal-kvm']/div/canvas")
        location = element.location
        size = element.size
        left = location['x']
        top = location['y']
        right = location['x'] + 2*size['width']
        bottom = location['y'] + 2*size['height']
        # Specify resolution
        resolution = (2*size['width'], 2*size['height'])
        # Specify video codec
        codec = cv2.VideoWriter_fourcc(*'mp4v')
        # Specify name of Output file
        # save with date and time
        DateString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        if file_name == None:
            filename = DateString + 'Screen_recorder.avi'
        else:
            filename = DateString + file_name + '.avi'
        # Specify frames rate. We can choose any
        # value and experiment with it
        fps = 60.0
        # Creating a VideoWriter object
        out = cv2.VideoWriter(filename, codec, fps, resolution)
        # Create an Empty window
        cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
        # Resize this window
        cv2.resizeWindow("Live", 480, 270)
        for i in range(int(record_time_in_sec * fps)):
            # Take screenshot using PyAutoGUI
            png = pyautogui.screenshot()
            img = png.crop((left, top, right, bottom))
            # Convert the screenshot to a numpy array
            frame = np.array(img)
            # Convert it from BGR(Blue, Green, Red) to
            # RGB(Red, Green, Blue)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Write it to the output file
            out.write(frame)
            # Optional: Display the recording screen
            cv2.imshow('Live', frame)
            # Stop recording after fix time-
            # if the user clicks q, it exits
            if cv2.waitKey(1) == ord("q"):
                break
        # Release the Video writer
        out.release()
        # Destroy all windows
        cv2.destroyAllWindows()
        
    def mount_image(self):
        """
            select the image from specific location to system and then mounted
        """
        if not self.is_already_logged_in(driver):
            self.open_bmc_login()

        driver.find_element(By.XPATH,'//*[@id="app"]/div/div[2]/div/nav/ul/li[4]/button').click()
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH,'//*[@id="operations"]/li/a[6]').click()
        select_image = driver.find_element(By.ID, "slot_0")
        time.sleep(5)
        select_image.send_keys("C:\\Users\\AMARJEET\\OneDrive - Intel Corporation\\Desktop\\tasks\\image.iso")
        time.sleep(35)
        driver.find_element(By.XPATH, "//*[@id='main-content']/div/div[2]/div/div/div/div[2]/button").click()
        time.sleep(20)

    class Keystrokes_for_KVM:
        """
            Class for different key strokes
        """
        def send_up_keystrokes(self, no_of_times):
            """
                this function to send the up key strokes
            """
            
            # if already not login then first ,login
            if not KVM_Screen_Recorder.is_already_logged_in(self,driver):
                KVM_Screen_Recorder().open_bmc_login()
            time.sleep(5)
            WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='terminal-kvm']/div/canvas")))
            driver.find_element(By.XPATH, "//*[@id='terminal-kvm']/div/canvas").send_keys()
            driver.implicitly_wait(5)
            for i in range(no_of_times):
                action.key_down(Keys.ARROW_UP)
                action.key_up(Keys.ARROW_UP).perform()

        def send_down_keystrokes(self,no_of_times):
            """
                this function to send the down key strokes
            """
            # if already not login then first ,login
            if not KVM_Screen_Recorder.is_already_logged_in(self, driver):
                self.outer_instance.open_bmc_login()
                #KVM_Screen_Recorder.open_bmc_login()
            time.sleep(5)
            WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='terminal-kvm']/div/canvas")))
            driver.find_element(By.XPATH, "//*[@id='terminal-kvm']/div/canvas").send_keys()
            driver.implicitly_wait(5)
            for i in range(no_of_times):
                action.key_down(Keys.ARROW_DOWN)
                action.key_up(Keys.ARROW_DOWN).perform()
            
        def send_enter_keystrokes(self,no_of_times):
            """
                this function to send the enter key strokes
            """
            # if already not login then first ,login
            if not KVM_Screen_Recorder.is_already_logged_in(self, driver):
                KVM_Screen_Recorder.open_bmc_login()
            time.sleep(5)
            WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='terminal-kvm']/div/canvas")))
            driver.find_element(By.XPATH, "//*[@id='terminal-kvm']/div/canvas").send_keys()
            driver.implicitly_wait(5)
            for i in range(no_of_times):
                action.key_down(Keys.ENTER)
                action.key_up(Keys.ENTER).perform()
                
        def send_esc_keystrokes(self,no_of_times):
            """
                this function to send the esc key strokes
            """
            # if already not login then first ,login
            if not KVM_Screen_Recorder.is_already_logged_in(self, driver):
                KVM_Screen_Recorder().open_bmc_login()
            time.sleep(5)
            WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='terminal-kvm']/div/canvas")))
            driver.find_element(By.XPATH, "//*[@id='terminal-kvm']/div/canvas").send_keys()
            driver.implicitly_wait(5)
            for i in range(no_of_times):
                action.key_down(Keys.ESCAPE)
                action.key_up(Keys.ESCAPE).perform()

        def send_tab_keystrokes(self,no_of_times):
            """
                this function to send the TAB key strokes
            """
            # if already not login then first ,login
            if not KVM_Screen_Recorder.is_already_logged_in(self, driver):
                KVM_Screen_Recorder().open_bmc_login()
            time.sleep(5)
            WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='terminal-kvm']/div/canvas")))
            driver.find_element(By.XPATH, "//*[@id='terminal-kvm']/div/canvas").send_keys()
            driver.implicitly_wait(5)
            for i in range(no_of_times):
                action.key_down(Keys.TAB)
                action.key_up(Keys.TAB).perform()
                
        def send_F2_keystrokes(self,no_of_times):
            """
                this function to send the TAB key strokes
            """
            # if already not login then first ,login
            if not KVM_Screen_Recorder().is_already_logged_in(self, driver):
                KVM_Screen_Recorder().open_bmc_login()
            time.sleep(5)
            WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='terminal-kvm']/div/canvas")))
            driver.find_element(By.XPATH, "//*[@id='terminal-kvm']/div/canvas").send_keys()
            driver.implicitly_wait(5)
            for i in range(no_of_times):
                action.key_down(Keys.F2)
                action.key_up(Keys.F2).perform()
                
        def write_keystrokes(self,cmd):
            """
                this function to write key strokes and send the command
            """
            # if already not login then first ,login
            if not KVM_Screen_Recorder().is_already_logged_in(self, driver):
                KVM_Screen_Recorder().open_bmc_login()
            time.sleep(5)
            WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='terminal-kvm']/div/canvas")))
            driver.find_element(By.XPATH, "//*[@id='terminal-kvm']/div/canvas").send_keys()
            driver.implicitly_wait(5)
            action.key_down(Keys.COMMAND)
            action.send_keys(cmd)
            action.key_up(Keys.COMMAND).perform()


if __name__=="__main__":
    kvm_obj = KVM_Screen_Recorder()
    kvm_obj.open_bmc_login()
    #kvm_obj.Keystrokes_for_KVM().send_up_keystrokes(no_of_times=3)

