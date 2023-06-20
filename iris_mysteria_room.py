import asyncio
import os
from iris_mysteria_img_compare import img_appear
from selenium.webdriver.common.action_chains import ActionChains

async def room(driver):
    await asyncio.sleep(5)
    canvas = driver.find_element("xpath", '//*[@id="unity-canvas"]')
    canvas_x = canvas.rect['width']
    canvas_y = canvas.rect['height']
    await asyncio.sleep(1)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.953-0.5)), int(canvas_y*(0.917-0.5))).click().perform()
    print('''iris mysteria click menu for entry room''')
    await asyncio.sleep(2)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.234-0.5)), int(canvas_y*(0.666-0.5))).click().perform()
    print('''iris mysteria click room in menu''')
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\room\room_title.png")
    await asyncio.sleep(5)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.601-0.5)), int(canvas_y*(0.925-0.5))).click().perform()
    await asyncio.sleep(5)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.601-0.5)), int(canvas_y*(0.925-0.5))).click().perform()
    await asyncio.sleep(5)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.601-0.5)), int(canvas_y*(0.925-0.5))).click().perform()
    print('''iris mysteria gather all resouse in room''')
    await asyncio.sleep(2)