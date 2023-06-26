import asyncio
import os
import aircv
import sys
import json
from iris_mysteria_img_compare import img_appear
from iris_mysteria_img_compare import img_compare
from iris_mysteria_img_compare import img_group_compare
from iris_mysteria_skip import weekly_skip
from selenium.webdriver.common.action_chains import ActionChains

async def ordeal(driver):
    with open(os.path.abspath(os.path.dirname(__file__))+'\config.json','r', encoding='UTF-8') as f:
        ordeal_info=json.loads(f.read())["ordeal"]
    area = None
    for i in ordeal_info:
        if(ordeal_info[i]==0):
            area = i
            break
    if(area == None):
        print(f'iris mysteria monthly all ordeal area is already cleared')
        await asyncio.sleep(2)
        return 0




    await asyncio.sleep(2)
    print(f'iris mysteria monthly ordeal {area} area is selected')
    await asyncio.sleep(3)
    canvas = driver.find_element("xpath", '//*[@id="unity-canvas"]')
    canvas_x = canvas.rect['width']
    canvas_y = canvas.rect['height']
    await asyncio.sleep(1)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.953-0.5)), int(canvas_y*(0.917-0.5))).click().perform()
    print('''iris mysteria click menu for monthly ordeal''')
    await asyncio.sleep(2)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.554-0.5)), int(canvas_y*(0.305-0.5))).click().perform()
    print('''iris mysteria click ordeal in menu''')
    await asyncio.sleep(7)
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\ordeal\ordeal_title.png")
    await asyncio.sleep(7)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.898-0.5)), int(canvas_y*(0.084-0.5))).click().perform()
    print('''iris mysteria entry ordeal hard mode''')
    await asyncio.sleep(5)
    if(area == "palvin"):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.125-0.5)), int(canvas_y*(0.500-0.5))).click().perform()
    elif(area == "amniacorum"):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.316-0.5)), int(canvas_y*(0.167-0.5))).click().perform()
    elif(area == "bilvgarden"):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.507-0.5)), int(canvas_y*(0.167-0.5))).click().perform()
    print(f'iris mysteria entry {area} of monthly ordeal')
    await asyncio.sleep(5)
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\ordeal\ordeal_indicator.png")
    await asyncio.sleep(2)
    canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    await asyncio.sleep(1)
    if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                      aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\ordeal\depart_unavailable.png"))
                      != None):
        print(f'iris mysteria area {area} is unavailable now')
        await asyncio.sleep(1)
        if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\ordeal\already_cleared.png"))
                        != None):
            with open(os.path.abspath(os.path.dirname(__file__))+'\config.json','r+', encoding='UTF-8') as f:
                data=json.loads(f.read())
                data["ordeal"][area] = 1
                f.seek(0)
                json.dump(data, f, indent=4)
                f.truncate()
        return 0

    await asyncio.sleep(2)
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+f"\imageresource\ordeal\{area}.png",driver,0.112,0.921)
    await asyncio.sleep(2)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.179-0.5)), int(canvas_y*(0.787-0.5))).click().perform()
    print(f'iris mysteria click depart button in ordeal menu')
    await asyncio.sleep(4)
    canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    await asyncio.sleep(1)
    if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                      aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\ordeal\ordeal_skip.png"))
                      != None):
        print(f'iris mysteria area {area} is going to skip')
        await asyncio.sleep(2)
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.614-0.5)), int(canvas_y*(0.694-0.5))).click().perform()
        print(f'iris mysteria area {area} confirm skip')
        await asyncio.sleep(10)
        canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
        await asyncio.sleep(1)
        while(1):
            if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                            aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\general\menu.png"))
                            != None):
                await asyncio.sleep(2)
                break
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.894-0.5)), int(canvas_y*(0.942-0.5))).click().perform()
            await asyncio.sleep(7)
            canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.179-0.5)), int(canvas_y*(0.787-0.5))).click().perform()
        print(f'iris mysteria skip {area} complete')
        await asyncio.sleep(4)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.714-0.5)), int(canvas_y*(0.770-0.5))).click().perform()
    print(f'iris mysteria area {area} confirm depart')
    await asyncio.sleep(300)
    while(1):
        await asyncio.sleep(2)
        if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                    aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\extreme_hard_mode.png"))
                    != None):
            pass
        elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                    aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\general\command.png"))
                    != None):
            for i in range(0,4):
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.054-0.5)), int(canvas_y*(0.051-0.5))).click().perform()
                await asyncio.sleep(1)
            for i in range(0,5):
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.236+(i*0.170)-0.5)), int(canvas_y*(0.105-0.5))).click().perform()
                await asyncio.sleep(1)
            print("iris mysteria event switch battle mode from command to custom")
        elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                    aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\general\manual.png"))
                    != None):
            for i in range(0,3):
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.054-0.5)), int(canvas_y*(0.051-0.5))).click().perform()
                await asyncio.sleep(1)
            print("iris mysteria event switch battle mode from manual to custom")
        elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                    aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\general\semi-auto.png"))
                    != None):
            for i in range(0,2):
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.054-0.5)), int(canvas_y*(0.051-0.5))).click().perform()
                await asyncio.sleep(1)
            print("iris mysteria ordeal switch battle mode from semi-auto to custom")
        elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                    aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\general\auto.png"))
                    != None):
            for i in range(0,1):
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.054-0.5)), int(canvas_y*(0.051-0.5))).click().perform()
                await asyncio.sleep(1)
            print("iris mysteria ordeal switch battle mode from auto to custom")
        elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                    aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\ordeal\ordeal_next.png"))
                    != None):
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.894-0.5)), int(canvas_y*(0.942-0.5))).click().perform()
            print("iris mysteria ordeal stage cleared click next")
        elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                    aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\ordeal\ordeal_result.png"))
                    != None):
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.916-0.5))).click().perform()
            print("iris mysteria ordeal close result info menu")
        elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                    aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\first_clear_reward.png"))
                    != None):
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.872-0.5))).click().perform()
            print("iris mysteria ordeal stage confirm first clear reward")
        elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                    aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\bonus_quest.png"))
                    != None):
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.406-0.5)), int(canvas_y*(0.680-0.5))).click().perform()
            print("iris mysteria ordeal stage close bonus quest")
        elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                    aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\relationship_increase.png"))
                    != None):
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.840-0.5))).click().perform()
            print("iris mysteria ordeal stage close relationship increase menu")
        elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                    aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\general\level_up.png"))
                    != None):
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.711-0.5))).click().perform()
            print("iris mysteria ordeal stage close player level increase menu")
        elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                    aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\ordeal\ordeal_indicator.png"))
                    != None):
            print("iris mysteria ordeal compelete")
            await asyncio.sleep(4)
            break
        await asyncio.sleep(10)
        canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    
