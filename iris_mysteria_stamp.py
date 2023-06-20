import asyncio
import aircv
import os
from iris_mysteria_img_compare import img_appear
from iris_mysteria_img_compare import img_compare
from selenium.webdriver.common.action_chains import ActionChains

async def stamp(driver):
    # WARNING: click position of stamp receive button is little lower than button exactly appear. this is deliberate for close the receive result menu
    # return 1 when do not find the stamp indicator image
    # return 0 when compeleted
    await asyncio.sleep(5)
    canvas = driver.find_element("xpath", '//*[@id="unity-canvas"]')
    canvas_x = canvas.rect['width']
    canvas_y = canvas.rect['height']
    await asyncio.sleep(1)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.953-0.5)), int(canvas_y*(0.917-0.5))).click().perform()
    print('''iris mysteria click menu for entry stamp''')
    await asyncio.sleep(3)
    canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    await asyncio.sleep(2)
    if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                      aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\stamp\stamp_indicator.png"))
                      == None):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.883-0.5))).click().perform()
        print('''iris mysteria stamp has no reward''')
        await asyncio.sleep(2)
        return 1
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.449-0.5)), int(canvas_y*(0.666-0.5))).click().perform()
    print('''iris mysteria click stamp in menu''')
    await asyncio.sleep(7)
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\stamp\stamp_title.png")
    await asyncio.sleep(1)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.975-0.5))).click().perform()
    await asyncio.sleep(5)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.975-0.5))).click().perform()
    await asyncio.sleep(5)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.975-0.5))).click().perform()
    await asyncio.sleep(5)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.304-0.5)), int(canvas_y*(0.069-0.5))).click().perform()
    print('''iris mysteria click stamp book mission button''')
    await asyncio.sleep(5)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.975-0.5))).click().perform()
    await asyncio.sleep(5)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.975-0.5))).click().perform()
    await asyncio.sleep(5)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.975-0.5))).click().perform()
    await asyncio.sleep(5)
    print('''iris mysteria receive daily stamp completed''')
    canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    await asyncio.sleep(1)
    if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                      aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\stamp\weekly_stamp.png"))
                      != None):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.151-0.5)), int(canvas_y*(0.414-0.5))).click().perform()
        await asyncio.sleep(5)
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.975-0.5))).click().perform()
        await asyncio.sleep(5)
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.975-0.5))).click().perform()
        await asyncio.sleep(5)
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.975-0.5))).click().perform()
        print('''iris mysteria receive weekly stamp completed''')
    await asyncio.sleep(2)
    return 0