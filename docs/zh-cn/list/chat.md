---
title: 配置客服功能
date: 2020-08-21 17:26:00
author: William
img: /images/1.jpg #文章特征图，推荐使用图床（腾讯云、七牛云、又拍云等）来作为图片路径
top: false #文章是置顶
cover: false #是否加入到首页轮播图中
coverImg: /images/1.jpg #轮播的图片路径，若无，则使用文章的特殊图片
toc: true #是否启用目录
summary: 搭建客服在线聊天功能
categories: Plug-ins #文章分类，只建议一篇文章一个分类,此为多级分类写法
tags: #标签，可以多个
  - Chat
---

### 准备工作

- [crisp 官网](https://app.crisp.chat/initiate/signup/)

### 客服聊天窗口配置

**1、在官网注册账号**

**2、注册完成后设置**

- 登录刚才注册的账户——设置——网站设置——添加网站——Integrations。

![配置](/images/arc_img/1.png)

- 比如：html 方式
  - 就是复制 JS 代码片段到你的到 head 标签里。

```javascript
<script type="text/javascript">window.$crisp=[];window.CRISP_WEBSITE_ID="c0e401ec-3f83-44f6-8acb-32637905848a";(function(){d=document;s=d.createElement("script");s.src="https://client.crisp.chat/l.js";s.async=1;d.getElementsByTagName("head")[0].appendChild(s);})();</script>
```

**3、其他的设置**

- 点击设置——网站设置，自己根据需要设置即可，比如显示位置，颜色，自己的头像等。
