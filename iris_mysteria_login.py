from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import asyncio




async def password_login(url, user_name, password, driver):
    try:
        await asyncio.sleep(1)
        driver.get(url)
        await asyncio.sleep(5)
        try:
            driver.find_element(By.CLASS_NAME, 'ntgnavi-item')
            print("cookies is not expired yet")
            print("DMM login success")
            return 0
        except:
            print("cookies is already expired")
            pass
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="loginbutton_script_on"]/span/input')))
        await asyncio.sleep(1)
        driver.find_element(By.ID, 'login_id').send_keys(user_name)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.XPATH, '//*[@id="loginbutton_script_on"]/span/input').click()
        await asyncio.sleep(1)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'ntgnavi-item')))
        print("DMM login success")
        return 0
    except Exception as e:
        await asyncio.sleep(1)
        print(e,'getlogin error, going to try again')
        await password_login(url, user_name, password, driver)


async def login(user_name, password, driver):
    result = -1
    while(result != 0):
        await asyncio.sleep(5)
        result = await password_login('https://pc-play.games.dmm.co.jp/play/imys_r/', user_name, password, driver)