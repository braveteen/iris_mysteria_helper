## [中文](./README.md)

# Iris Mysteria Helper

Based on [Selenium WebDriver](https://github.com/SeleniumHQ/) for browser automation and [OpenCV](https://github.com/opencv) for image recognition.

## Purpose

Free your hands by automatically logging in to Iris Mysteria and performing actions.

#### Features include but not limited to:
   - Academy Training
   - Daily Ancient Particle Quest
   - Weekly Material
   - Current Event
   - Receive Gifts And Mission Rewards



## Before Using

#### Due to various reasons....... It is only suitable for veterans and not recommended for newbies
   - click features will not pop-up the tutorial banner which block clicks and image recognition
   - Ancient particle and all weekly material stages have been cleared
   - Event stages should not result in defeat
   - Sufficient skip tickets stocked
   
   
### Essential Configuration
  #### In Iris Mysteria
   1. In the "game(ゲーム)" menu of settings(設定), disable the opening animation(オープニング) when events(イベント) start(開催). Select "Never Play"(常に再生しない)
   2. Rename the team used for event stages from the default name "パーティーxx" to "event_clear", or disable event-related functions in the helper config
  #### In config.json of Helper
   1. Fill in the "account" and "password" with your DMM account and password
   2. Set "enable" to false in "event" to disable the event feature, or configure the event team name in Iris Mysteria
## WARN
  ### Avoid improper operations
   - Scroll operations use absolute coordinates. If you want to change the browser window size or zoom level, please disable the weekly feature first
   - In non-headless mode, make sure the browser window is not minimized or switched to another tab. The mouse cursor should not be positioned on the browser interface, and avoid clicking on the command prompt
   - (It is recommended to switch to headless mode after the initial use. Set "headless" to true in the configuration file)
  ### Potential issues
   - You can manually open the same Chrome browser that the program uses for operation. If you have chosen to save usernames and passwords during manual DMM login, the program may not clear the previously filled values and continue to add usernames and passwords at the end, causing login failures
   - If the Chrome browser used by the program is not up to date, the automatically updated driver version may not work
  ## License
  ### MIT
  
Feel free to edit and modify.