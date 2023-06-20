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

async def scroll_down(driver, canvas):
    await asyncio.sleep(2)
    # switch focus to canvas internal
    ActionChains(driver).move_to_element_with_offset(canvas, -300, 0).click().perform()
    await asyncio.sleep(1)
    ActionChains(driver).move_to_element_with_offset(canvas, -300, 0).click().perform()
    await asyncio.sleep(2)
    for i in range(0,37):
        ActionChains(driver).scroll(320,360,0,100).perform()
        await asyncio.sleep(0.1)
    print("perform scroll action completed")
    await asyncio.sleep(2)


async def weekly_clear(driver, quest_type):
    # return 0 when all clear success or already cleared
    # return -1 when out of stamina
    with open(os.path.abspath(os.path.dirname(__file__))+'\config.json','r', encoding='UTF-8') as f:
        quest_info=json.loads(f.read())['weekly'][quest_type]
    diffculty = None
    for i in quest_info:
        if(quest_info[i]==0):
            diffculty = i
            break
    if(diffculty == None):
        print(f'iris mysteria weekly {quest_type} quest is already cleared')
        await asyncio.sleep(2)
        return 0




    await asyncio.sleep(2)
    print(f'iris mysteria weekly {quest_type} quest {diffculty} diffculty is selected')
    await asyncio.sleep(3)
    canvas = driver.find_element("xpath", '//*[@id="unity-canvas"]')
    canvas_x = canvas.rect['width']
    canvas_y = canvas.rect['height']
    await asyncio.sleep(1)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.953-0.5)), int(canvas_y*(0.917-0.5))).click().perform()
    print('''iris mysteria click menu for weekly battle''')
    await asyncio.sleep(2)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.449-0.5)), int(canvas_y*(0.305-0.5))).click().perform()
    print('''iris mysteria click quest in menu''')
    await asyncio.sleep(7)
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\quest\quest_home_title.png")
    await asyncio.sleep(7)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.695-0.5)), int(canvas_y*(0.472-0.5))).click().perform()
    print('''iris mysteria entry gather quest''')
    await asyncio.sleep(2)
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\quest\gather_quest_title.png")
    await asyncio.sleep(3)
    if(quest_type == "material"):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.084-0.5)), int(canvas_y*(0.167-0.5))).click().perform()
    elif(quest_type == "gem"):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.191-0.5)), int(canvas_y*(0.167-0.5))).click().perform()
    elif(quest_type == "present"):
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.294-0.5)), int(canvas_y*(0.167-0.5))).click().perform()
    print(f'iris mysteria entry {quest_type} of gather quest')


    result = 0
    while(result != -1):
    
        await asyncio.sleep(3)
        ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.851-0.5)), int(canvas_y*(0.921-0.5))).click().perform()
        print('''iris mysteria click skip button''')
        await asyncio.sleep(3)



        
        if(diffculty == "easy"):
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.148-0.5)), int(canvas_y*(0.174-0.5))).click().perform()
        elif(diffculty == "moderate"):
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.227-0.5)), int(canvas_y*(0.174-0.5))).click().perform()
        elif(diffculty == "hard"):
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.305-0.5)), int(canvas_y*(0.174-0.5))).click().perform()
        elif(diffculty == "hell"):
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.383-0.5)), int(canvas_y*(0.174-0.5))).click().perform()
        await asyncio.sleep(3)



        canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
        await asyncio.sleep(1)
        if(len(img_group_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\quest\weekly_indicator.png")))
                        != 0):
            print(f"iris mysteria find quest uncleared of {diffculty} diffculty in {quest_type} gather")
            result = await weekly_skip(driver, canvas)
            await asyncio.sleep(2)
        else:
            if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                            aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+f"\imageresource\quest\{quest_type}_bottom.png"))
                            != None):
                print(f"iris mysteria all quest is cleared in {diffculty} diffculty of {quest_type} this week")
                with open(os.path.abspath(os.path.dirname(__file__))+'\config.json','r+', encoding='UTF-8') as f:
                    data=json.loads(f.read())
                    data["weekly"][quest_type][diffculty] = 1
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
                if(diffculty == "easy"):
                    diffculty = "moderate"
                elif(diffculty == "moderate"):
                    diffculty = "hard"
                elif(diffculty == "hard"):
                    diffculty = "hell"
                elif(diffculty == "hell"):
                    print("exceed highest diffculty")
                    await asyncio.sleep(2)
                    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.408-0.5)), int(canvas_y*(0.919-0.5))).click().perform()
                    await asyncio.sleep(2)
                    break
                await asyncio.sleep(3)
            else:
                await scroll_down(driver, canvas)
                await asyncio.sleep(2)
                print("iris mysteria scrolling down to find quest")

                






    if(result == -1):
        print(f'iris mysteria out of stamina in {quest_type} {diffculty} of weekly gather quest')
    elif(result == 0):
        print(f'iris mysteria {quest_type} {diffculty} of weekly gather quest is cleared')
    await asyncio.sleep(2)
    return result

async def weekly_material(driver):
    return await weekly_clear(driver, "material")

async def weekly_gem(driver):
    return await weekly_clear(driver, "gem")

async def weekly_present(driver):
    return await weekly_clear(driver, "present")

