import aircv
import os
import asyncio
import time
from selenium.webdriver.common.action_chains import ActionChains

def img_compare(img_rsc, img_dfn):
    result = aircv.find_template(img_rsc, img_dfn, threshold=0.99)
    return result

def img_group_compare(img_rsc, img_dfn, threshold = 0.93):
    result = aircv.find_all_template(img_rsc, img_dfn, threshold)
    return result

async def img_appear(canvas, img_path, driver = None, x = 0, y = 0):
    canvas_x = canvas.rect['width']
    canvas_y = canvas.rect['height']
    while(1):
        await asyncio.sleep(7)
        canvas.screenshot(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
        img_rsc = aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png")
        img_dfn = aircv.imread(img_path)
        result = img_compare(img_rsc, img_dfn)
        if(result != None):
            await asyncio.sleep(2)
            print("find image", img_path, result['confidence'], time.strftime('%y-%m-%d %H:%M:%S'))
            return result
        if((driver!=None) and (x != 0 or y != 0)):
            await asyncio.sleep(0.5)
            ActionChains(driver).move_to_element_with_offset(canvas, int(canvas_x*(x-0.5)), int(canvas_y*(y-0.5))).click().perform()
            print(f"click {int(canvas_x*x)},{int(canvas_y*y)} {img_path} untill image appear")


if(__name__ == "__main__"):
    img_compare(aircv.imread(f"{os.path.abspath(os.path.dirname(__file__))}"+r"\imageresource\canvas.png"),aircv.imread('./imageresource/login/login_config.png'))