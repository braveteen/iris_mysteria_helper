
Chinese
Alice Mysteria Assistant
Based on Selenium WebDriver for browser automation and OpenCV for image recognition.

Purpose
Free your hands by automatically logging in to Alice Mysteria and performing actions.

Features include but not limited to:
Academy Training
Daily Canglizi Levels
Weekly Material Levels
Current Event Levels
Collecting gifts and task rewards, and more
Before Using
Due to various reasons... It is only suitable for old accounts and not recommended for new accounts
The tutorial pop-ups will not block clicks and image recognition
Canglizi and all weekly material levels have been cleared
Event levels should not result in defeat
Sufficient skip tickets are available
Required Configuration
In Alice Mysteria
In the game settings, disable the opening animation when events start. Select "Never Play" (常に再生しない).
Rename the team used for event levels from the default name "パーティーxx" to "event_clear", or disable event-related functions in the assistant.
In assistant's config.json
Fill in the "account" and "password" with your DMM account credentials.
Set "enable" to false in "event" to disable the event functionality, or configure the event team name in Alice Mysteria.
Important Notes
Avoid improper operations
Scroll operations use absolute coordinates. If you want to change the browser size or zoom level, please disable the weekly feature first.
In non-headless mode, make sure the browser window is not minimized or switched to another tab. The mouse cursor should not be positioned on the browser interface, and avoid clicking on the command prompt.
(It is recommended to switch to headless mode after the initial use. Set "headless" to true in the configuration file.)
Potential issues
You can manually open the same Chrome browser that the program uses for operation. If you have chosen to save usernames and passwords during manual DMM login, the program may not clear the previously filled values and continue to add usernames and passwords at the end, causing login failures.
If the Chrome browser used by the program is not up to date, the automatically updated driver version may not work.
License
MIT
Feel free to edit and modify.

Here is the revised English version of your markdown.
