# AutoHS
欢迎任何批评建议~

在 `constants/constants` 里有一些参数可以设置...

可以先跑一跑 `demo/` 下的一些文件

### 我目前用的挂机卡组 (标准模式-解解拖拖牧)
目前手牌识别只能识别这幅套牌里的牌(需要自行测试哈希然后记下来)

目前幸运币不支持带皮肤……
- 2x (1) 倦怠光波
- 2x (1) 护甲商贩
- 2x (1) 神圣惩击
- 2x (2) 噬骨殴斗者
- 1x (2) 暗言术：灭
- 2x (3) 亡首教徒
- 2x (3) 噬灵疫病
- 2x (3) 狂傲的兽人
- 2x (3) 神圣化身
- 1x (4) 暗言术：毁
- 2x (4) 狂乱
- 2x (4) 神圣新星
- 1x (5) 泰兰·弗丁
- 2x (5) 锈骑劫匪
- 1x (5) 除奇致胜
- 1x (6) 凯恩·血蹄
- 1x (7) 吞噬者穆坦努斯
- 1x (7) 灵魂之镜
- 1x (9) 戈霍恩之血

神秘代码:
```
AAECAa0GCMi+A/rfA/PuA6bvA6iKBMGfBPCfBKOgBAuvugPXvgPcvgPmvgPLzQP44wOS5AOY6gOb6wOEnwSFnwQA
```

### 如果想要用自己的卡组
我觉得需要经过一下几步:

- 你需要能认出每一张手牌, AutoHS使用图片哈希来识别图片, 
   你需要录入新卡的哈希, 可以通过 `demo/identify_cards.py` 
   去读取手牌卡画哈希
- 把哈希和对应名称录入到 `constants/hash_vals.py` 中
- 写出卡牌逻辑, 可以参照 `card.py`
- 把卡牌和中文名对应, 需要更新 `name2card.py`

好像有点麻烦...


### 如何运行
运行 `main.py` 即可，注意本脚本需要屏幕分辨率为 1920 * 1080、炉石全屏，在运行时按下 Ctrl+Q 可以退出脚本。
需要把炉石放在最前台。

你可以把战网客户端最小化到任务栏，或是放在炉石应用下面，丹青不要关闭战网客户端。有时炉石会意外关闭，这时程序会试图重新打开炉石。

### 文件说明
- `demo/catch_screen_demo.py` : 运行此文件会获取炉石传说进程的整个截屏
(无论是在前台还是后台),并画上一些坐标基准线,方便判断想实现的操作的坐标值
- `demo/count_cards_demo.py`: 数出有几张手牌,需要在对战界面调用
- `demo/count_minion_demo.py`: 数出有几个随从,需要在对战界面调用
- `demo/find_avaiable_demo.py`: 测试一下场上的我的怪都能不能动,需要在对战界面调用
- `demo/get_minion_attack_and_health.demo.py`: 测出场上的怪的攻击和血量,需要在对战界面调用
- `demo/get_taunt_and_divin_shield_demo.py`: 测出场上的怪是否是嘲讽或者圣盾,需要在对战界面调用
- `demo/get_window_name.py` : 显示当前所有窗口的名称和编号,可以用来看炉石传说叫什么名字……
- `demo/identify_cards_demo.py`: 测出手里的手牌都是什么,需要在对战界面调用
- `demo/mouse_control_demo.py` : 一个样例程序展现了如何控制鼠标


### 待办列表
- [ ] 补全注释
- [ ] 补全Readme
- [X] 识别手牌
- [X] 识别场面
- [ ] 更有脑子的瞎打
- [X] 随机化点击
- [ ] 智能表情
- [ ] 英雄打脸 
- [X] 卡组研发 (牧师) 
- [ ] 换起始手牌
- [X] 一键退出
- [X] 重写FSM(为什么会用递归实现...)
- [ ] 什么时候试一试 Replay-Attack

### 关于截取屏幕,以及opnecv2
使用的是win的接口。在矩阵里第一维是行号，而在opencv里，windows接口里和mouse接口里第一维是列号。

矩阵里的色彩排序为(B,G,R)

### 关于控制鼠标
原本想通过发送信号的方式在让炉石在后台也能接收到鼠标点击

但是发现炉石应该是所谓的接受直接输入的进程，信号模拟它不会接收……

所以只能使用很low的鼠标点击了

也许能直接模拟网络发包？


### 关于网络连接的观察
一打开炉石就会建立两个TCP连接，这两个所有的数据都是加密的。像分解卡牌， 只有退出了某个卡牌的分解界面（就是可以撤销的界面）才会发包确认分解结果。

实验下来感觉只有其中一条连接在真的交换数据。

点击匹配会新建一个连接,这个连接是加密的。在匹配完成后连接就销毁。

进入对战会又新建一个连接,这个是纯TCP没有加密，不过我仍然无法解析数据交换的格式……（总之不是json..……）。

任何一个操作都会触发数据传输（比如空中乱晃鼠标……），而如果什么都不做炉石也会每个5秒跟服务器互相ping一下,应该是在确认是否掉线


