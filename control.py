# from seleniumwire import webdriver
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time
import datetime
import os
import json
import chromedriver_autoinstaller
import iris_mysteria_login
import iris_mysteria_access
import iris_mysteria_acedemy
import iris_mysteria_room
import iris_mysteria_daily
import iris_mysteria_expedition
import iris_mysteria_stamp
import iris_mysteria_weekly
import iris_mysteria_general
import iris_mysteria_event
import iris_mysteria_reward
import iris_mysteria_ordeal
import asyncio
import traceback
import sys
async def initialize():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    with open(os.path.abspath(os.path.dirname(__file__))+'\config.json','r+', encoding='UTF-8') as f:
        user_config=json.loads(f.read())
        if(iris_mysteria_general.current_week()
           !=datetime.datetime.strptime(user_config["weekly"]["last_date"], '%Y-%m-%d %H:%M:%S').isocalendar().week):
            for i in user_config["weekly"]:
                if(i == "material" or i == "gem" or i == "present"):
                    for j in user_config["weekly"][i]:
                        user_config["weekly"][i][j] = 0
            print("iris mysteria reset weekly quest status for new week", iris_mysteria_general.current_week())
        else:
            print("iris mysteria today is in the same week of last time")
        if(iris_mysteria_general.current_month()
           !=datetime.datetime.strptime(user_config["ordeal"]["last_date"], '%Y-%m-%d %H:%M:%S').month):
            user_config["ordeal"]["palvin"] = 0
            user_config["ordeal"]["amniacorum"] = 0
            user_config["ordeal"]["bilvgarden"] = 0
            print("iris mysteria reset monthly ordeal for new month", iris_mysteria_general.current_month())
        else:
            print("iris mysteria today is in the same month of last time")
        f.seek(0)
        json.dump(user_config, f, indent=4)
        f.truncate()
            
        
    if(user_config["proxy"]["abide_system"]==True):
        print("iris mysteria abide system proxy config")
    else:
        print("user proxy config", user_config["proxy"]["ip_address"])
        options.add_argument('--proxy-server='+user_config["proxy"]["ip_address"])
    # options.add_argument(f"--disk-cache-dir={os.path.abspath(os.path.dirname(__file__))}"+r'\userdata\Default\Cache')
    options.add_argument(f"--user-data-dir={os.path.abspath(os.path.dirname(__file__))}"+r'\userdata')
    options.add_argument("--disk-cache-size=1073741824")
    options.binary_location = f"{os.path.abspath(os.path.dirname(__file__))}"+r'\Chrome\Application\chrome.exe'
    options.add_argument('--mute-audio')
    options.add_argument("--disable-infobars")
    # options.add_argument("--disable-extensions")
    # 使用 /tmp 而非 /dev/shm 作為暫存區
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    if(user_config["headless"]== True):
        options.add_argument("--headless")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--allow-insecure-localhost')
    # close the notifiction of automatic pop
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    count = 0
    while(count < user_config["maximum_retry"]):
        try:
            count = count + 1
            # driver = webdriver.Chrome(options=options, seleniumwire_options=user_config["seleniumwire_options"])
            driver = webdriver.Chrome(options = options)
            driver.set_window_size(1500, 1000)
            driver.set_window_position(0, 0)
            async with asyncio.timeout(1800):
                await iris_mysteria_login.login(user_config["account"], user_config["password"], driver)
                await iris_mysteria_access.access(driver)
            count = count - 1
            return driver
        except TimeoutError:
            print(count, "times exceed maximum delay")
            driver.quit()
            time.sleep(10)
        except Exception as e:
            logging.error(time.strftime('%y-%m-%d %H:%M:%S')+traceback.format_exc() + '-------------- \n')
            print(e)
            driver.quit()
            time.sleep(10)
    if(count >= user_config["maximum_retry"]):
        driver.quit()
        raise Exception('iris mysteria login error')



def loop_wrapper(fun, count_down = 600):
    async def wrapper(*args, **kwargs):
        #avoid "tuple object does not support item assignment" error
        args = list(args)
        count = 0
        while(1):
            try:
                async with asyncio.timeout(count_down):
                    return await fun(*args, **kwargs)
            except Exception as e:
                count = count + 1
                logging.error(time.strftime('%y-%m-%d %H:%M:%S')+traceback.format_exc() + '-------------- \n')
                print(e)
                args[0].quit()
                await asyncio.sleep(10)
                if(count > 5):
                    raise Exception('iris mysteria error',fun.__name__)
                args[0] = await initialize()
    return wrapper



async def main():
    logging.basicConfig(level='INFO',
                        # level='WARNING',
                        format='%(levelname)s %(filename)s %(funcName)s\n[line:%(lineno)d]%(message)s',
                        datefmt='%y-%m-%d',
                        filename=f"{os.path.abspath(os.path.dirname(__file__))}"+"\log\\"+time.strftime('%y-%m-%d')+r".log",
                        filemode='a+')
    try: 
        chromedriver_path = chromedriver_autoinstaller.install(path=f"{os.path.abspath(os.path.dirname(__file__))}"+r'\chromedriver')
        print(chromedriver_path)
        with open(os.path.abspath(os.path.dirname(__file__))+'\config.json','r', encoding='UTF-8') as f:
            user_config=json.loads(f.read())
        #WARNING: after initialize, the driver returned was the driver of original game canvas, do not switch frame again
        game_driver = await initialize()
        stamina = 0
        await loop_wrapper(iris_mysteria_acedemy.acedemy)(game_driver)
        await loop_wrapper(iris_mysteria_room.room)(game_driver)
        stamina = await loop_wrapper(iris_mysteria_daily.daily)(game_driver)
        await loop_wrapper(iris_mysteria_expedition.expedition)(game_driver)
        await loop_wrapper(iris_mysteria_stamp.stamp)(game_driver)
        if(user_config["weekly"]["enable"]==True):
            with open(os.path.abspath(os.path.dirname(__file__))+'\config.json','r+', encoding='UTF-8') as f:
                user_config=json.loads(f.read())
                user_config["weekly"]["last_date"] = iris_mysteria_general.standard_time().strftime('%Y-%m-%d %H:%M:%S')
                f.seek(0)
                json.dump(user_config, f, indent=4)
                f.truncate()
            print("iris mysteria weekly gather quest is available")
            if(stamina != -1):
                stamina = await loop_wrapper(iris_mysteria_weekly.weekly_material,3600)(game_driver)
            if(stamina != -1):
                stamina = await loop_wrapper(iris_mysteria_weekly.weekly_gem,2400)(game_driver)
            if(stamina != -1):  
                stamina = await loop_wrapper(iris_mysteria_weekly.weekly_present,3600)(game_driver)
        else:
            print("iris mysteria weekly gather quest is disabled")
        if(user_config["event"]["enable"]==True and stamina != -1):
            await loop_wrapper(iris_mysteria_event.event,7200)(game_driver)
        if(user_config["ordeal"]["enable"]==True):
            with open(os.path.abspath(os.path.dirname(__file__))+'\config.json','r+', encoding='UTF-8') as f:
                user_config=json.loads(f.read())
                user_config["ordeal"]["last_date"] = iris_mysteria_general.standard_time().strftime('%Y-%m-%d %H:%M:%S')
                f.seek(0)
                json.dump(user_config, f, indent=4)
                f.truncate()
            await loop_wrapper(iris_mysteria_ordeal.ordeal,1200)(game_driver)
        await loop_wrapper(iris_mysteria_reward.reward)(game_driver)
    except Exception as e:
        print(e)
        logging.error(time.strftime('%y-%m-%d %H:%M:%S')+traceback.format_exc() + '-------------- \n')
    print("iris mysteria all thread finished")
    await asyncio.sleep(10)
    game_driver.quit()

if(__name__ == "__main__"):
    with open(os.path.abspath(os.path.dirname(__file__))+'\config.json','r+', encoding='UTF-8') as f:
        user_config=json.loads(f.read())
    if(user_config["loop"]["enable"]==False):
        print("execute iris mysteria thread without loop")
        asyncio.run(main())
        sys.exit()
    else:
        print(f"execute iris mysteria using loop in {user_config['loop']['trigger_hour']} hours unitll user voluntary cancel")
        while(1):
            print(datetime.datetime.now().hour,"is current hour")
            if(int(datetime.datetime.now().hour) in user_config['loop']['trigger_hour']):
                print("appropriate time for execute iris mysteria")
                asyncio.run(main())
            time.sleep(1800)
