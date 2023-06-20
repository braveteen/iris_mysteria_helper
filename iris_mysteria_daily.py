import asyncio
import os
import aircv
import sys
from iris_mysteria_img_compare import img_appear
from iris_mysteria_img_compare import img_compare
from iris_mysteria_skip import normal_skip
from selenium.webdriver.common.action_chains import ActionChains

async def daily(driver):
    # return 1 when already cleared
    # return 0 when clear success
    # return -1 when out of stamina
    await asyncio.sleep(5)
    canvas = driver.find_element("xpath", '//*[@id="unity-canvas"]')
    canvas_x = canvas.rect['width']
    canvas_y = canvas.rect['height']
    await asyncio.sleep(1)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.953-0.5)), int(canvas_y*(0.917-0.5))).click().perform()
    print('''iris mysteria click menu for daily battle''')
    await asyncio.sleep(2)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.449-0.5)), int(canvas_y*(0.305-0.5))).click().perform()
    print('''iris mysteria click quest in menu''')
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\quest\quest_home_title.png")
    await asyncio.sleep(7)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.883-0.5)), int(canvas_y*(0.472-0.5))).click().perform()
    print('''iris mysteria entry challenge quest''')
    await asyncio.sleep(3)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.258-0.5)), int(canvas_y*(0.472-0.5))).click().perform()
    print('''iris mysteria entry hunting of challenge quest''')
    await asyncio.sleep(6)
    canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    await asyncio.sleep(1)
    result = -99
    if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                      aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\quest\ancient_particle_quest.png"))
                      != None):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.172-0.5)), int(canvas_y*(0.333-0.5))).click().perform()
        print('''iris mysteria find today's ancient particle is not finished yet, going to skip''')
        result = await normal_skip(driver, canvas)
        await asyncio.sleep(2)
    if(result == -1):
        print('''iris mysteria out of stamina in daily ancient particle''')
    elif(result == 0):
        print('''iris mysteria clear ancient particle today''')
    else:
        print('''iris mysteria today ancient particle is already cleared''')
        result = 1
    await asyncio.sleep(2)
    return result
