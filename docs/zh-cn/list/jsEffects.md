---
title: Hexo 博客添加动态科技背景
date: 2020-08-22 11:21:00
author: William
img: /images/1.jpg #文章特征图，推荐使用图床（腾讯云、七牛云、又拍云等）来作为图片路径
top: false #文章是置顶
cover: false #是否加入到首页轮播图中
coverImg: /images/1.jpg #轮播的图片路径，若无，则使用文章的特殊图片
toc: true #是否启用目录
summary: 添加动态科技背景和樱花特效
categories: Plug-ins #文章分类，只建议一篇文章一个分类
tags: #标签，可以多个
  - JS
  - Effects
---

### 准备工作

**1. 前提**

**2. 链接**

- [sakura.js](https://cdn.jsdelivr.net/gh/Yafine/cdn@3.2.7/source/js/sakura.js)

### 添加动态科技线条背景

**1、在 themes/matery/layout/layout.ejs 文件中添加如下代码：**

```javascript
<!--动态线条背景-->
<script type="text/javascript"
color="0 185 241" opacity='0.7' zIndex="-2" count="200" src="//cdn.bootcss.com/canvas-nest.js/1.0.0/canvas-nest.min.js">
</script>
```

- 参数说明：
  - color：表示线条颜色，三个数字分别为 (R,G,B)，默认：（0,0,0）
  - opacity：表示线条透明度（0~1），默认：0.5
  - count：表示线条的总数量，默认：150
  - zIndex：表示背景的 z-index 属性，css 属性用于控制所在层的位置，默认：-1

### 添加樱花飘落效果

**1、下载 sakura.js 文件后，将其放在 themes/matery/source/js 目录下**

**2、在 themes/matery/layout/layout.ejs 文件内添加下面的内容：**

```JavaScript
<script type="text/javascript">
//只在桌面版网页启用特效
var windowWidth = $(window).width();
if (windowWidth > 768) {
    document.write('<script type="text/javascript" src="/js/sakura.js"><\/script>');
}
</script>
```

**3. 也可以直接在 themes/matery/layout/layout.ejs 文件内添加下面的内容：**

```JavaScript
<!-- 樱花特效cdn引用 -->
<script src="https://cdn.jsdelivr.net/gh/wallleap/cdn/js/sakura.js"></script>
```
