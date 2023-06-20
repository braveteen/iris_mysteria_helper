import asyncio
import os
import aircv
import sys
from iris_mysteria_img_compare import img_appear
from iris_mysteria_img_compare import img_compare
from iris_mysteria_img_compare import img_group_compare
from iris_mysteria_skip import normal_skip
from selenium.webdriver.common.action_chains import ActionChains



async def event(driver):
    # return 1 when no event
    # return 0 when execute completed
    await asyncio.sleep(5)
    canvas = driver.find_element("xpath", '//*[@id="unity-canvas"]')
    canvas_x = canvas.rect['width']
    canvas_y = canvas.rect['height']
    await asyncio.sleep(1)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.953-0.5)), int(canvas_y*(0.917-0.5))).click().perform()
    print('''iris mysteria click menu for event battle''')
    await asyncio.sleep(2)
    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.449-0.5)), int(canvas_y*(0.305-0.5))).click().perform()
    print('''iris mysteria click quest in menu''')
    await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\quest\quest_home_title.png")
    await asyncio.sleep(7)



    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.500-0.5))).click().perform()
    print('''iris mysteria entry event quest''')
    await asyncio.sleep(3)
    canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
    await asyncio.sleep(2)
    img_group = img_group_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                    aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\event_indicator.png"))
    if(len(img_group)==0):
        print(f'iris mysteria no event current')
        await asyncio.sleep(3)
        return 0
    mark = img_group[0]
    for i in img_group:
        if(i["result"][0]<mark["result"][0]):
            mark = i
    ActionChains(driver).move_to_element_with_offset(canvas, int(mark["result"][0]-(canvas_x*0.5)), int(mark["result"][1]-(canvas_y*0.5))).click().perform()
    
    
    
    
    # ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.320-0.5)), int(canvas_y*(0.500-0.5))).click().perform()
    # await asyncio.sleep(5)
    # ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.599-0.5)), int(canvas_y*(0.779-0.5))).click().perform()
    # await asyncio.sleep(5)
    # ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.291-0.5)), int(canvas_y*(0.380-0.5))).click().perform()
    


    await asyncio.sleep(10)
    event_type = "default"
    while(1):
        canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
        await asyncio.sleep(1)
        if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\party_appear.png"))
                        != None):
            event_type = "default"
            break
        elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\conversation_indicator.png"))
                        != None):
            await asyncio.sleep(1)
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.672-0.5)), int(canvas_y*(0.819-0.5))).click().perform()
            await asyncio.sleep(10)
        elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\raid_event_indicator.png"))
                        != None):
            await asyncio.sleep(1)
            event_type = "raid"
            break
        await asyncio.sleep(10)

    if(event_type == "raid"):
        print("iris mysteria raid event function is still incompleted")
    else:
        print("iris mysteria event type is regular")
        await img_appear(canvas, f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\event_clear_party.png",driver,0.112,0.921)
        canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
        await asyncio.sleep(1)
        while(1):
            await asyncio.sleep(2)
            if(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\extreme_hard_mode.png"))
                        != None):
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.296-0.5)), int(canvas_y*(0.166-0.5))).click().perform()
                print("iris mysteria event switch to extreme hard quest")
            elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\hard_mode.png"))
                        != None and
                img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\extrem_hard_already.png"))
                        == None):
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.187-0.5)), int(canvas_y*(0.166-0.5))).click().perform()
                print("iris mysteria event switch to hard quest")
            elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\new_quest_indicator.png"))
                        != None):
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.789-0.5)), int(canvas_y*(0.921-0.5))).click().perform()
                print("iris mysteria event click quest start")
            elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\conversation_indicator.png"))
                        != None):
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.672-0.5)), int(canvas_y*(0.819-0.5))).click().perform()
                print("iris mysteria event click conversation fast forward")
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
                print("iris mysteria event switch battle mode from semi-auto to custom")
            elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\general\auto.png"))
                        != None):
                for i in range(0,1):
                    ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.054-0.5)), int(canvas_y*(0.051-0.5))).click().perform()
                    await asyncio.sleep(1)
                print("iris mysteria event switch battle mode from auto to custom")
            elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\next_indicator.png"))
                        != None):
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.894-0.5)), int(canvas_y*(0.942-0.5))).click().perform()
                print("iris mysteria event stage cleared click next")
            elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\first_clear_reward.png"))
                        != None):
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.872-0.5))).click().perform()
                print("iris mysteria event stage confirm first clear reward")
            elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\bonus_quest.png"))
                        != None):
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.406-0.5)), int(canvas_y*(0.680-0.5))).click().perform()
                print("iris mysteria event stage close bonus quest")
            elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\relationship_increase.png"))
                        != None):
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.840-0.5))).click().perform()
                print("iris mysteria event stage close relationship increase menu")
            elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\general\level_up.png"))
                        != None):
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.711-0.5))).click().perform()
                print("iris mysteria event stage close player level increase menu")
            elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\event\skip_button.png"))
                        != None):
                print("iris mysteria event new stages are all completed")
                await asyncio.sleep(2)
                break
            elif(img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),
                        aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\quest\out_of_stamina.png"))
                        != None):
                print("iris mysteria event out of stamina in new stage")
                await asyncio.sleep(2)
                ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(0.500-0.5)), int(canvas_y*(0.825-0.5))).click().perform()
                await asyncio.sleep(2)
                return 0
            await asyncio.sleep(10)
            canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
        count = 0
        while(1):
            if(await normal_skip(driver,canvas)== -1):
                print(f"iris mysteria skip event {count} times completed")
                await asyncio.sleep(1)
                break
            count = count + 1
        print(f"iris mysteria event completed")
    await asyncio.sleep(2)
    return 0
