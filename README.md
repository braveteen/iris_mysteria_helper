## [English](./README_EN.md)

# 爱丽丝秘跡助手

基于 [Selenium WebDriver](https://github.com/SeleniumHQ/) 用于浏览器操控 和 [OpenCV](https://github.com/opencv) 用于图像识别.

## 用途

解放双手 自动登录爱丽丝秘跡并自动执行操作

#### 功能包括但不限于
   - 学园训练
   - 每日苍粒子关卡
   - 每周素材关卡
   - 当期活动关卡
   - 每月试炼的困难地区
   - 领取礼物和任务奖励
   - 每天到指定时间能够自动执行等等



## 使用之前

#### 因为种种原因......只能养老而不适用于新号
   - 有充足的skip券
   - 活动关卡的战斗不能出现战败的情况
   - 苍粒子和所有的每周素材关卡已经通关过
   - 点击功能时不会弹出教程挡住点击和图形识别
   
   
### 必要的配置
  #### 在爱丽丝秘跡
   1. 在设置(設定)的game(ゲーム)里面 关闭event(イベント)开始时的(開催時の)opening(オープニング)播放 选择从不播放(常に再生しない)
   2. 用来执行活动关卡的队伍 从默认名"パーティーxx"改名为"event_clear" 或者在config关闭event
   3. 试炼的1王队伍改名为"palvin" 2王队伍"amniacorum" 3王队伍"bilvgarden" 或者在config关闭ordeal
  #### 在助手和config.json
   1. 解压路径必须是纯英文的
   2. 在"account"和"password"填入DMM账号和密码
   3. 设置"event"的"enable"为false关闭活动功能 或者在在爱丽丝秘跡里配置活动队伍名称
   4. 设置"ordeal"的"enable"为false关闭试炼功能 或者在在爱丽丝秘跡里配置试炼队伍名称

## 注意事项
  ### 更加方便的使用
   - 建议首次使用后切换成无头模式 在配置文件里设置"headless"为true
   - config里设置"loop"的"enable"为true并在"trigger_hour"填入每天触发自动执行的时机(本机时间的小时) 将会每天到时间自动执行
   - 可以为助手使用单独的代理 config设置"proxy"的"abide_system"为false 并在下方填入代理地址
  ### 避免不当操作
   - scroll操作使用绝对坐标执行 若要改变浏览器大小或缩放比例 请先关闭weekly功能
   - 非无头模式下 注意浏览器窗口不能被最小化或者切换浏览器的tab 鼠标不能位于浏览器界面上 也不要点击命令提示符的界面
  ### 可能问题
   - 可以手动打开程式使用的同一chrome进行操作 如果手动操作DMM登陆选择了保存用户名和密码 登陆时可能不会清理原来填入的值而是在后面继续添加用户名和密码 导致无法登录
   - 如果程式使用的chrome没有维持在最新版本的话 程式自动更新的driver版本可能会无法使用
  ## License
  ### MIT
欢迎自由编辑和修改

#### 队伍名称配置如图
![tutorial](https://github.com/munezawa/iris_mysteria_helper/assets/34181587/36ea56c0-68f9-471b-9026-4760f6d9e9b5)
#### 部分flow chart
![flow_chart](https://github.com/munezawa/iris_mysteria_helper/assets/34181587/bb25e048-0a76-48cb-81b3-64213274270b)
