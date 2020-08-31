---
title: hexo思维导图使用
date: 2020-08-22 11:21:00
author: William
img: /images/1.jpg #文章特征图，推荐使用图床（腾讯云、七牛云、又拍云等）来作为图片路径
top: false #文章是置顶
cover: false #是否加入到首页轮播图中
coverImg: /images/1.jpg #轮播的图片路径，若无，则使用文章的特殊图片
toc: true #是否启用目录
summary: 思维导图配置
categories: Plug-ins #文章分类，只建议一篇文章一个分类
tags: #标签，可以多个
  - mindmap
---

### 准备工作

- [mindmap github 仓库](https://github.com/HunterXuan/hexo-simple-mindmap)

### 操作指南

**1、安装插件，在 hexo 根目录下执行如下代码：**

```bash
npm install hexo-simple-mindmap
```

**2、在.md 文件中使用**
{% pullquote mindmap mindmap-md %}

- [hexo 思维导图使用](https://github.com/HunterXuan/hexo-simple-mindmap)
  - 前言
  - 操作指南
    - 准备需要的文件
    - 为主题添加 CSS/JS 文件
  - 使用方法

{% endpullquote %}

### 注意事项

- 该功能在 hexo 5.1.0 版本似乎存在 bug，导致 mindmap 无法渲染成功

![页面渲染结果](/images/arc_img/2.png)
