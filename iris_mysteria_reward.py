import asyncio
import aircv
import os
from iris_mysteria_img_compare import img_appear
from iris_mysteria_img_compare import img_compare
from iris_mysteria_img_compare import img_group_compare
from selenium.webdriver.common.action_chains import ActionChains

async def reward(driver):
    # WARNING: click position of reward receive button is little lower than button exactly appear. this is deliberate for close the receive result menu
    # return 0 when compeleted
    await asyncio.sleep(5)
    canvas = driver.find_element("xpath", '//*[@id="unity-canvas"]')
    canvas_x = canvas.rect['width']
    canvas_y = canvas.rect['height']
    await asyncio.sleep(1)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.953-0.5)), int(canvas_y*(0.917-0.5))).click().perform()
    print('''iris mysteria click menu for entry gift''')
    await asyncio.sleep(3)
    canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    await asyncio.sleep(2)
    if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                      aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\reward\gift_indicator.png"))
                      == None):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.883-0.5))).click().perform()
        print('''iris mysteria gift no reward''')
        await asyncio.sleep(2)
    else:
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.125-0.5)), int(canvas_y*(0.572-0.5))).click().perform()
        print('''iris mysteria click gift in menu''')
        await asyncio.sleep(7)
        await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\reward\gift_title.png")
        await asyncio.sleep(1)
        await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\reward\gift_complete.png",driver,0.400,0.975)
        await asyncio.sleep(2)
    print('''iris mysteria gift complete''')
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.953-0.5)), int(canvas_y*(0.917-0.5))).click().perform()
    print('''iris mysteria click menu for entry mission''')
    await asyncio.sleep(3)
    canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    await asyncio.sleep(2)
    if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                      aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\reward\mission_indicator.png"))
                      == None):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.883-0.5))).click().perform()
        print('''iris mysteria mission no reward''')
        await asyncio.sleep(2)
    else:
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.125-0.5)), int(canvas_y*(0.423-0.5))).click().perform()
        print('''iris mysteria click mission in menu''')
        await asyncio.sleep(7)
        await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\reward\mission_title.png")
        await asyncio.sleep(2)
        canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
        await asyncio.sleep(1)
        img_group = img_group_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\reward\reward_indicator.png"))
        for i in img_group:
            ActionChains(driver).move_to_element_with_offset(canvas, int(i["result"][0]-(canvas_x*0.5)), int(i["result"][1]-(canvas_y*0.5))).click().perform()
            await asyncio.sleep(3)
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.975-0.5))).click().perform()
            await asyncio.sleep(5)
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.975-0.5))).click().perform()
            await asyncio.sleep(5)
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.975-0.5))).click().perform()
            await asyncio.sleep(5)
    print('''iris mysteria mission receive complete''')
    await asyncio.sleep(2)
    return 0