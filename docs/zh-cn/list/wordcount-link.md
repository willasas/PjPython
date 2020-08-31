---
title: 中文链接转拼音和字数统计
date: 2020-07-30 17:35:00
author: William
img: /images/1.jpg #文章特征图，推荐使用图床（腾讯云、七牛云、又拍云等）来作为图片路径
top: false #文章是置顶
cover: false #是否加入到首页轮播图中
coverImg: /images/1.jpg #轮播的图片路径，若无，则使用文章的特殊图片
toc: true #是否启用目录
summary: 优化中文链接和文章字数统计
categories: Plug-ins #文章分类，只建议一篇文章一个分类
tags: #标签，可以多个
  - Chinese link to Pinyin
  - Word count
---

### 准备工作

- [hexo-permalink-pinyin 插件官网](https://github.com/viko16/hexo-permalink-pinyin)
- [wordcount 插件官网](https://github.com/willin/hexo-wordcount)

### 中文链接转拼音

**1、安装插件**

```bash
cnpm i hexo-permalink-pinyin --save
```

**2、在 Hexo 根目录下的 \_config.yml 文件中，新增以下的配置项**

```yml
# hexo-permalink-pinyin
## Docs: https://github.com/viko16/hexo-permalink-pinyin
permalink_pinyin:
  enable: true
  separator: '-' # default: '-'
```

### 文章字数统计

**1、安装插件**

```bash
cnpm i --save hexo-wordcount
```

**2、在 matery 主题目录下的 \_config.yml 文件中，新增以下的配置项**

```yml
# 文章字数统计、阅读时长、总字数统计等
# 文章信息--若要开启文章字数统计，需要安装 hexo-wordcount 插件，安装命令: `npm i --save hexo-wordcount`
postInfo:
  date: true # 发布日期
  update: true # 更新日期
  wordCount: true # 文章字数统计
  totalCount: true # 站点总文章字数
  min2read: true # 文章阅读时长
  readCount: true # 文章阅读次数
```
