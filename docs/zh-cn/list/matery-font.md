---
title: Matery 主题自定义字体
date: 2020-08-22 16:21:00
author: William
img: /images/1.jpg #文章特征图，推荐使用图床（腾讯云、七牛云、又拍云等）来作为图片路径
top: false #文章是置顶
cover: false #是否加入到首页轮播图中
coverImg: /images/1.jpg #轮播的图片路径，若无，则使用文章的特殊图片
toc: true #是否启用目录
summary: 修改matery主题默认字体，使用自定义字体
categories: Hexo #文章分类，只建议一篇文章一个分类
tags: #标签，可以多个
  - Diyfont
---

### 准备工作

**1. 前提**

- Matery 主题

### 全局字体自定义

**1、在站点根目录下的 source 文件夹内创建一个名为 font 的文件夹（路径为 /source/font/），用来统一存放你要用到的字体。**

```bash
hexo new page font  #创建font文件夹
```

**2、将字体文件放入到 font 文件夹内，字体名称最好为英文(如 /source/font/citydlig1.ttf)**

**3、找到主题文件夹下的 my.css 文件，路径为 /themes/matery/source/css/my.css ，填入下面的代码：**

```css
/*添加自定义字体样式*/
@font-face {
	font-family: 'Gayatri';
	/*字体名*/
	src: url('../font/Gayatri.ttf');
	/*字体路径*/
}

body {
	font-family: 'Gayatri';
	/*字体名*/
}
```

### 局部字体自定义(推荐)

**1、创建字体文件加，添加字体文件通上面的 1、2 步骤**

**2、找到主题文件夹下的 my.css 文件，路径为 /themes/matery/source/css/my.css ，填入下面的代码：**

```css
/*添加自定义字体样式*/
@font-face {
	font-family: 'Gayatri';
	/*字体名*/
	src: url('../font/Gayatri.ttf');
	/*字体路径*/
}

/* 可以局部使用，建议添加 */
.diyFont {
	font-family: 'Gayatri';
}
```

**3、使用，找到对应的模板（header.ejs）中的代码片段使用即可**

```html
<span class="logo-span diyFont"><%= config.title %></span>
```

- 修改方法也就是在 <div class=""> 中增加自己定义的 CSS 类名
