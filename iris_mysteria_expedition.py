import asyncio
import aircv
import os
from iris_mysteria_img_compare import img_appear
from iris_mysteria_img_compare import img_compare
from selenium.webdriver.common.action_chains import ActionChains

async def expedition(driver):
    # WARNING: click position of depart button is little lower than button exactly appear. this is deliberate for close relationship increase menu
    # return 1 when expedition is not return
    # return 0 when compeleted
    await asyncio.sleep(5)
    canvas = driver.find_element("xpath", '//*[@id="unity-canvas"]')
    canvas_x = canvas.rect['width']
    canvas_y = canvas.rect['height']
    await asyncio.sleep(1)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.953-0.5)), int(canvas_y*(0.917-0.5))).click().perform()
    print('''iris mysteria click menu for entry expedition''')
    await asyncio.sleep(2)
    canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    await asyncio.sleep(1)
    if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                      aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\expedition\expedition_indicator.png"))
                      == None):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.883-0.5))).click().perform()
        print('''iris mysteria expedition is not return yet''')
        await asyncio.sleep(2)
        return 1
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.664-0.5)), int(canvas_y*(0.305-0.5))).click().perform()
    print('''iris mysteria click expedition in menu''')
    await asyncio.sleep(10)
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\expedition\expedition_depart.png", driver, 0.563, 0.964)
    await asyncio.sleep(1)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.691-0.5)), int(canvas_y*(0.871-0.5))).click().perform()
    print('''iris mysteria click depart expedtion party again button''')
    await asyncio.sleep(10)
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\general\menu.png")
    print('''iris mysteria depart expedtion party compeleted''')
    await asyncio.sleep(2)
    return 0