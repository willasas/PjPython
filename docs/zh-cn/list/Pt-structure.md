---
title: hexo项目结构
date: 2020-07-30 17:35:00
author: William
img: /images/1.jpg #文章特征图，推荐使用图床（腾讯云、七牛云、又拍云等）来作为图片路径
top: false #文章是置顶
cover: false #是否加入到首页轮播图中
coverImg: /images/1.jpg #轮播的图片路径，若无，则使用文章的特殊图片
#password: 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
toc: true #是否启用目录
summary: 基于hexo-theme-matery主题搭建的博客项目目录结构
categories: Project #文章分类，只建议一篇文章一个分类
tags: #标签，可以多个
  - Project structure
---

### 项目目录结构如下

{% pullquote mindmap mindmap-md %}

- .deploy_git #一键将博客同时部署到多个 git 仓库中
- .github #github 自动化部署脚本
- node_modules #插件依赖包管理文件
- public #hexo 生成的静态页面（重点）
- scaffolds #md 模板
- source #网站内容资源文件（重点）
  - \_data #数据文件
    - friend.json #友情链接文件
  - \_ports #文章源文件
  - about #关于菜单内容文件
  - categories #分类菜单内容文件
  - contact #留言板菜单内容文件
  - friends #友情链接菜单内容文件
  - images #文章内图片文件
  - movies #视频菜单内容文件
  - musics #音乐菜单内容文件
  - tags #标签菜单内容文件
  - 404.md #页面报错文件
- theme #主题文件
  - hexo-theme-matery #matery 主题文件夹
    - languages #语言文件
      - default.yml #默认语言
      - zh-CN.yml #简体中文
    - layout #布局（所有的博客页面 HTML 和 JS 及 ejs 模板）
      - \_partial #公共页面（可以引入到 HTML 的任意位置）
      - \_widget #公共页面（可以引入到 HTML 的任意位置）
      - 其他 ejs 文件 #主菜单相关的 ejs 文件
    - source #主题相关的文件
      - css #主题样式文件
      - js #js 文件
        - live2d_assets #live2d 源文件
          - assets
        - matery.js #主题 js 文件
        - sakura.js #樱花特效 js 文件
        - search.js #搜索 js 文件
      - libs
      - medias #媒体资源文件
        - banner #
        - featureimages #
        - reward #打赏二维码图片
        - logo.png #网站 logo
      - favicon.png #网站 favicon（导航前的小图标）
    - \_config.yml #主题配置文件
    - .gitignore #git 版本控制文件
    - LICENSE #
    - README.md #主题使用说明
- .git #项目 git 管理（提交内容等）
- \_config.yml #项目配置文件
- .gitignore #项目 git 管理文件
- db.json
- gulpfile.js #静态资源压缩依赖文件
- package.json #依赖包管理
- package-lock.json #加锁的依赖包管理
- README.md #网站说明

{% endpullquote %}
