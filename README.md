# infomation_monitor_platform
这是一个通用的脚本请求的平台代码，可以在这个平台上面写各种网络请求的脚本，例如刷课、抢票、刷信息等
## 一、项目说明
本项目的出发点是减少重复制造轮子，在日常生活中，很多时候我们需要写个脚本去帮我们刷课，抢票等等，因为我多次写这种脚本，我就想着为啥不去写个通用的平台代码，这样以后每次写脚本都直接配置，不需要写代码。
因为一般的需求主要就是两种：
1. 登陆某个网站，按时刷新某个网页，看我们希望出现的内容有没有出现，例如在豆瓣上面看房子，我们刷新特定页面，看有没有特定的房源出现，如果出现了就通知我们或者直接发送模拟请求锁定房源（课程等）。
2. 登陆某个网站，定时做某种请求，比如典型的就是高校抢课，在某天中午12点把我们的选课请求发送出去

分析以上两种行为，我们能够抽取大量的同逻辑代码，各种需求唯一的不同就是发送的数据和页面不一样，然后各自的请求链接不一样，所以本项目就是致力于把逻辑相同的代码都统一维护，方便后面快速产生对应业务的请求代码。
## 二、项目终极目标
最后只需要配置文件，不需要写代码，配置好跳转数据发送抽取等。

**一口吃不成一个胖子，第一步先完成基本的框架设计，核心代码的完成，这样在写具体请求的时候能够更快完成。**
## 三、模块介绍
目前主要有四个模块：
1. 异常模块，主要定义项目的各种异常
2. 通知模块，主要用于各类通知的代码，比如邮件，包括以后的短信、电话、微信等等
3. 核心平台模块，目前主要用于维护核心session和做session持久化等操作
4. 工具模块，现在主要有四大工具：
    1. 配置处理工具，主要有ini文件和json文件的配置处理
    2. 时间处理，包含定时器等，时间字符串处理
    3. 文件处理工具
    4. 数据预处理
## 四、demo介绍
目前这个demo比较简单，主要是请求豆瓣的group界面，刷我们需要的房源的demo

## 五、设计说明
整个项目以 request queue 为核心，每个request对应一个operation，每个operation可以往request queue里面增加一个request，也可以同时做其他的事情，比如：email通知。当整个的request queue为空的时候平台退出。