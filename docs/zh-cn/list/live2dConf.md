---
title: live2d看板娘配置
date: 2020-08-22 11:21:00
author: William
img: /images/1.jpg #文章特征图，推荐使用图床（腾讯云、七牛云、又拍云等）来作为图片路径
top: false #文章是置顶
cover: false #是否加入到首页轮播图中
coverImg: /images/1.jpg #轮播的图片路径，若无，则使用文章的特殊图片
toc: true #是否启用目录
summary: 看板娘的配置相关记录
categories: Plug-ins #文章分类，只建议一篇文章一个分类
tags: #标签，可以多个
  - Live2d
---

### 准备工作

**1. 前提**

- Node.js version 10.0+
- git

**2. 链接**

- [live2d 源码下载](https://github.com/fghrsh/live2d_demo)

### 安装 Hexo

**1、下载 live2d 源码并解压，并将 assets 目录拷贝到/source/js/live2d_assets/**

```bash
git clone https://github.com/fghrsh/live2d_demo.git
```

**2、在主题下的 layout/\_partial 目录下打开 head.ejs,并将 waifu.css 文件引入，代码如下：**

```html
<% if (theme.live2d && theme.live2d.enable) { %>
<link
	rel="stylesheet"
	type="text/css"
	href="<%- theme.jsDelivr.url %><%- url_for('/js/live2d_assets/waifu.css') %>"
/>
<% } %>
```

**3、在主题下的 layout/\_partial 目录下新建 live2d.ejs 文件，内容如下：**

```html
<!-- waifu-tips.js 依赖 JQuery 库  头部已经引用了JQuery，此处不引入-->
<!-- 实现拖动效果，需引入 JQuery UI -->

<script src="<%- theme.jsDelivr.url %><%- url_for('/js/jquery-ui.min.js') %>"></script>

<div class="waifu">
	<div class="waifu-tips"></div>
	<canvas id="live2d" class="live2d"></canvas>
	<div class="waifu-tool">
		<span class="fui-home"></span>
		<span class="fui-chat"></span>
		<span class="fui-eye"></span>
		<span class="fui-user"></span>
		<span class="fui-photo"></span>
		<span class="fui-info-circle"></span>
		<span class="fui-cross"></span>
	</div>
</div>

<script src="<%- theme.jsDelivr.url %><%- url_for('/js/live2d_assets/waifu-tips.js') %>"></script>
<script src="<%- theme.jsDelivr.url %><%- url_for('/js/live2d_assets/live2d.js') %>"></script>

<script type="text/javascript">
	live2d_settings['modelId'] = 1
	live2d_settings['modelTexturesId'] = 87

	var waifuTips =
		"<%- theme.jsDelivr.url %><%- url_for('/js/live2d_assets/waifu-tips.json') %>"
	initModel(waifuTips)
</script>
```

**4、在主题目录下的 layout/index.ejs 文件末尾，加入如下代码：**

```ejs
<% if (theme.live2d.enable) { %> <%- partial('_partial/live2d') %> <% } %>
```

**5、live2d 加载调整**

- 修改主题下的 source/js/live2d_assets/assets/waifu-tips.js 文件内的参数即可
- 修改 waifu-tips.json，定制live2d的提示语，可以自己修改成个性化提示语。

**6、重新编译启动项目**

```bash
hexo clean & hexo g & hexo s
```
