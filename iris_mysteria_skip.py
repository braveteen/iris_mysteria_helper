from selenium.webdriver.common.action_chains import ActionChains
from iris_mysteria_img_compare import img_appear
from iris_mysteria_img_compare import img_compare
from iris_mysteria_img_compare import img_group_compare
import os
import asyncio
import aircv

async def normal_skip(driver, canvas, times = 1):
    # due to the difference in UI design, this function can not skip weekly material gather quest
    # and increase skip times is ineffctive for some stages that without multiply ratio battle capability
    # retrun -1 when out of stamina
    # return 0 if skip successed
    canvas_x = canvas.rect['width']
    canvas_y = canvas.rect['height']
    await asyncio.sleep(3)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.851-0.5)), int(canvas_y*(0.921-0.5))).click().perform()
    print('''iris mysteria click skip button''')
    await asyncio.sleep(3)
    canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    await asyncio.sleep(1)
    if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                      aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\quest\can_multi_skip.png"))
                      != None):
        await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\quest\normal_counter.png", driver, 0.309, 0.622)
    for i in range(1,times):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.309-0.5)), int(canvas_y*(0.492-0.5))).click().perform()
        await asyncio.sleep(1)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.598-0.5)), int(canvas_y*(0.778-0.5))).click().perform()
    print(f'iris mysteria confirm normal skip for {times} times')
    await asyncio.sleep(9)
    canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    await asyncio.sleep(1)
    if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                      aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\quest\out_of_stamina.png"))
                      != None):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.825-0.5))).click().perform()
        await asyncio.sleep(2)
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.408-0.5)), int(canvas_y*(0.781-0.5))).click().perform()
        print(f'iris mysteria do not have enough stamina for normal skip')
        await asyncio.sleep(2)
        return -1
    while(1):
        if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\general\menu.png"))
                        != None):
            await asyncio.sleep(2)
            break
        if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\bonus_quest.png"))
                        != None):
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.406-0.5)), int(canvas_y*(0.680-0.5))).click().perform()
            print("iris mysteria normal skip close bonus quest")
            await asyncio.sleep(7)
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.894-0.5)), int(canvas_y*(0.942-0.5))).click().perform()
        await asyncio.sleep(7)
        canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    print(f'iris mysteria normal skip completed')
    await asyncio.sleep(2)
    return 0

async def weekly_skip(driver, canvas):
    # due to the difference in UI design, this function can not skip other quest except weekly material quest
    # increase skip times is not avialible in this function
    # retrun -1 when out of stamina
    # return 0 if skip successed or already cleared
    canvas_x = canvas.rect['width']
    canvas_y = canvas.rect['height']
    await asyncio.sleep(3)
    canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    await asyncio.sleep(2)
    img_group = img_group_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                      aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\quest\weekly_indicator.png"))
    if(len(img_group)==0):
        print(f'iris mysteria this weekly stage list is all cleared')
        await asyncio.sleep(2)
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.408-0.5)), int(canvas_y*(0.919-0.5))).click().perform()
        await asyncio.sleep(2)
        return 0
    for i in img_group:
        ActionChains(driver).move_to_element_with_offset(canvas, int(i["result"][0]-(canvas_x*0.5)), int(i["result"][1]-(canvas_y*0.5))).click().perform()
        await asyncio.sleep(1)
    await asyncio.sleep(1)
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\quest\weekly_counter.png", driver, 0.492, 0.551)
    await asyncio.sleep(2)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.598-0.5)), int(canvas_y*(0.917-0.5))).click().perform()
    print(f'iris mysteria confirm weekly skip for {len(img_group)} quests')
    await asyncio.sleep(9)
    canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    await asyncio.sleep(1)
    if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                      aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\quest\out_of_stamina.png"))
                      != None):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.825-0.5))).click().perform()
        await asyncio.sleep(2)
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.408-0.5)), int(canvas_y*(0.919-0.5))).click().perform()
        print(f'iris mysteria do not have enough stamina for weekly skip')
        await asyncio.sleep(2)
        return -1
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\general\menu.png", driver, 0.894, 0.942)
    print(f'iris mysteria weekly skip completed')
    await asyncio.sleep(2)
    return 0