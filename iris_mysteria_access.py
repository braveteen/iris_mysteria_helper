import asyncio
import os
import aircv
from iris_mysteria_img_compare import img_appear
from iris_mysteria_img_compare import img_compare
from selenium.webdriver.common.action_chains import ActionChains

async def access(driver):
    # url = "https://pc-play.games.dmm.co.jp/play/imys_r/"
    # driver.get(url)
    await asyncio.sleep(5)
    iframe = driver.find_element("xpath", '//*[@id="game_frame"]')
    driver.switch_to.frame(iframe)
    print('''iris mysteria switch to id="game_frame" frame success''')
    iframe = driver.find_element("xpath", '//*[@id="iframe"]')
    driver.switch_to.frame(iframe)
    print('''iris mysteria switch to id="iframe" frame success''')
    canvas = driver.find_element("xpath", '//*[@id="unity-canvas"]')
    canvas_x = canvas.rect['width']
    canvas_y = canvas.rect['height']
    print("iris mysteria canvas size "+str(canvas_x)+" "+str(canvas_y))
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\login\login_config.png")
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.752-0.5))).click().perform()
    await asyncio.sleep(13)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.752-0.5))).click().perform()
    print('''iris mysteria start menu click start botton''')
    await asyncio.sleep(20)
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\general\homepage_indicator.png", driver, 0.523, 0.944)
    print('''iris mysteria enter game home page successed''')
    return 0