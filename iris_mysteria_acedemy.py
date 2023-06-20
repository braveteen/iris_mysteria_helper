import asyncio
import os
import aircv
from iris_mysteria_img_compare import img_appear
from selenium.webdriver.common.action_chains import ActionChains

async def acedemy(driver):
    await asyncio.sleep(5)
    canvas = driver.find_element("xpath", '//*[@id="unity-canvas"]')
    canvas_x = canvas.rect['width']
    canvas_y = canvas.rect['height']
    await asyncio.sleep(1)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.953-0.5)), int(canvas_y*(0.917-0.5))).click().perform()
    print('''iris mysteria click menu for entry acedemy''')
    await asyncio.sleep(2)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.238-0.5)), int(canvas_y*(0.305-0.5))).click().perform()
    print('''iris mysteria click acedemy in menu''')
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\acedemy\acedemy_title.png")
    await asyncio.sleep(5)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.328-0.5)), int(canvas_y*(0.875-0.5))).click().perform()
    print('''iris mysteria click the train start''')
    await asyncio.sleep(3)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.441-0.5)), int(canvas_y*(0.532-0.5))).click().perform()
    print('''iris mysteria max train times''')
    await asyncio.sleep(3)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.601-0.5)), int(canvas_y*(0.833-0.5))).click().perform()
    print('''iris mysteria click confirm the train start''')
    await asyncio.sleep(10)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.937-0.5)), int(canvas_y*(0.049-0.5))).click().perform()
    print('''iris mysteria skip train animation''')
    await asyncio.sleep(4)
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\general\menu.png", driver, 0.961, 0.930)
    print('''iris mysteria finish train''')
    await asyncio.sleep(3)