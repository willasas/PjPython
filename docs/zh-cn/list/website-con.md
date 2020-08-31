---
title: hexo网站搭建及优化
date: 2020-08-21 14:21:00
author: William
img: /images/1.jpg #文章特征图，推荐使用图床（腾讯云、七牛云、又拍云等）来作为图片路径
top: false #文章是置顶
cover: false #是否加入到首页轮播图中
coverImg: /images/1.jpg #轮播的图片路径，若无，则使用文章的特殊图片
#password: 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
toc: true #是否启用目录
mathjax: false #是否激活mathjax数学公式
summary: 使用hexo搭建博客网站和使用matery主题美化网站
categories: 
	- Website 
	- Hexo #文章分类，只建议一篇文章一个分类
tags: #标签，可以多个
  - Plug-ins
  - Website SEO
  - Matery
---

### 准备工作

**1. 前提**

- Node.js version 10.0+
- git

**2. 链接**

- [Hexo 使用说明](https://hexo.io/docs/)
- [Hexo-theme-matery](https://github.com/blinkfox/hexo-theme-matery/blob/develop/README_CN.md)
- [hexo-generator-search](https://github.com/wzpan/hexo-generator-search)
- [hexo-permalink-pinyin](https://github.com/viko16/hexo-permalink-pinyin)
- [wordcount](https://github.com/willin/hexo-wordcount)
- [hexo-deployer-git](https://github.com/hexojs/hexo-deployer-git)
- [lazyload](https://github.com/Troy-Yang/hexo-lazyload-image)
- [jsDelivr](https://www.jsdelivr.com/)

### 安装 Hexo

**1、修改 NPM 镜像源,并安装 Hexo-cli，执行如下命令：**

```cmd
npm config set registry https://registry.npm.taobao.org #修改淘宝镜像源
d:
cd dev/workspace/hexo       #Enter the workspace
cnpm install -g hexo-cli    #Install hexo
hexo init                   #Initialize project
code .                      #Open project with VS Code
```

**2、创建一个例子，并启动服务**

```bash
hexo new "hello"  #创建名为hello的例子
hexo server   #启动服务
```

- 更多命令请参考[Writing](https://hexo.io/docs/writing.html)

**3、项目结构**

{% pullquote mindmap mindmap-md %}

- scaffolds #md mould
- source/\_ports #Articles and pages md
- themes.hexo-theme-matery #themes
  - source
    - medias
      - banner #banner img
      - featureimages #24 featured pictures
  - layout
    - \_partial
      - footer.ejs #footer info
      - socila-link.ejs #Modify social links info
      - bg-cover-content.ejs #banner img change js
  - \_config.yml #Topic related configuration
- \_config.yml #hexo configuration

{% endpullquote %}

### 安装主题

**1、下载 matery 主题并解压，将解压后的文件复制到 hexo 的 themes 文件夹内**

```bash
git clone https://github.com/blinkfox/hexo-theme-matery.git
```

**2、修改 Hexo 根目录的 \_config.yml 文件的 theme 值**

```yml
# Extensions
## Plugins: https://hexo.io/plugins/
## Themes: https://hexo.io/themes/
theme: hexo-theme-matery
```

- 其他设置：

```yml
# 修改分页
## Set per_page to 0 to disable pagination
per_page: 12
pagination_dir: page
# 修改语言
language: zh-CN
# 修改URL
## If your site is put in a subdirectory, set url as 'http://yoursite.com/child' and root as '/child/'
url: https://github.com/willasas/willasas.github.io
```

**3、新建页面**

- 执行如下命令，创建页面：

```bash
hexo new page "categories"  #新建分类页
hexo new page "tags"  #新建标签页
hexo new page "about"  #新建关于我页
hexo new page "friends"  #新建友情链接页（可选）
```

- 编辑分类页（/source/categories/index.md），添加如下内容：

```md
---
title: categories
date: 2020-07-30 15:37:34
type: 'categories'
layout: 'categories'
---
```

- 其他页面的 index.md 文件内容同上，只需要将 title、type、layout 的值改成对应的页面名即可（例如 title: tags）

- 若新建了友情链接页面，则在 source 目录下新建 \_data 目录，在 \_data 目录中新建 friends.json 文件，文件内容如下所示：

```json
[
	{
		"avatar": "https://avatars1.githubusercontent.com/u/33866172?s=60&v=4", //图标
		"name": "willasas", //名称
		"introduction": "文章管理系统",
		"url": "https://willasas.github.io/ArticleManagementSystem/#/", //url
		"title": "着陆" //标题
	},
	{
		"avatar": "https://portrait.gitee.com/uploads/avatars/user/1619/4857389_aclor_1596096000.png!avatar30",
		"name": "亚黎",
		"introduction": "国内请访问",
		"url": "https://gitee.com/aclor",
		"title": "着陆"
	}
]
```

### 安装搜索功能(hexo-generator-search)

**1、安装搜索插件，命令如下：**

```bash
cnpm install hexo-generator-search --save
```

**2、在 Hexo 根目录下的 \_config.yml 文件中，新增以下的配置项：**

```
search:
  path: search.xml
  field: post
```

### 安装中文链接转拼音插件(推荐)

**1、安装命令如下：**

```terminal
cnpm i hexo-permalink-pinyin --save
```

**2、在 hexo 根目录下的\_config.yml 文件中，配置如下：**

```_config.yml
permalink_pinyin:
  enable: true
  separator: '-' # default: '-'
```

### 安装文章字数统计插件(可选)

**1、安装命令如下：**

```terminal
cnpm i --save hexo-wordcount
```

**2、修改主题下的\_config.yml 文件件内容如下：**

```yml
postInfo:
  date: true
  update: false
  wordCount: false # 设置文章字数统计为 true.
  totalCount: false # 设置站点文章总字数统计为 true.
  min2read: false # 阅读时长.
  readCount: false # 阅读次数.
```

### 安装懒加载(建议)

**1、全局安装懒加载插件，命令如下：**

```cmd
cnpm install hexo-lazyload-image --save
```

**2、修改根目录下的\_config.yml 文件件内容如下：**

```yml
# hexo-lazyload-image
## Docs: https://github.com/Troy-Yang/hexo-lazyload-image
lazyload:
  enable: true
  onlypost: false # 是否只对文章的图片做懒加载
  loadingImg: ./source/images/loading.gif # eg ./images/loading.gif 自定义loading图片
```

### 其他配置

**1、修改网站页脚信息**

- 编辑 themes/hexo-theme-matery/layout/\_partial/footer.ejs 文件，包括站点、使用的主题、访问量等。

**2、修改社交链接**

- 在主题的 \_config.yml 文件中, 默认支持 QQ、GitHub 和邮箱的配置，可以在主题文件的 /layout/\_partial/social-link.ejs 文件中，新增、修改需要的社交链接地址，增加链接可参考如下代码：

```ejs
<a href="https://github.com/" class="tooltipped" target="_blank" data-tooltip="访问我的GitHub" data-position="top" data-delay="50">
    <i class="fa fa-github"></i>
</a>
```

**3、CND 加速（建议）**

- 放在 Github 的资源在国内加载速度比较慢，因此需要使用 CDN 加速来优化网站打开速度，jsDelivr + Github 便是免费且好用的 CDN，非常适合博客网站使用。也可以选择主流云服务商提供的对象存储+CDN 来获得更快速及稳定的访问效果，费用低到几乎可忽略。

### 一键部署

**1、修改根目录下的\_config.yml 文件件内容如下：**

```yml
# Deployment
## Docs: https://hexo.io/docs/deployment.html
deploy:
  - type: git
    repo: https://github.com/willasas/willasas.github.io
		branch: master
		ignore_hidden: false
	- type: git
    repo: https://gitee.com/aclor/myblog
		branch: master
		ignore_hidden: false
```

**2、先使用 git 初始化项目，然后安装自动化部署插件**

```bash
git init   #git初始化
git remote add origin https://github.com/willasas/willasas.github.io.git  #建立连接
npm install hexo-deployer-git --save  #安装插件
npm run deploy   #运行插件
```

**3、运行自动化部署**

```bash
hexo clean && hexo g && hexo s  #生成并启动服务，在本地的4000端口查看预览效果
# OR
gulp build  #自动化部署
```

### 部署到 Github

**1、提交代码到 dev 分支**

```bash
git checkout -q -b dev  #创建并切换到dev分支
git add .
git commit -m "dev demo"
git push --set-upstream origin dev  #设置本地分支追踪远程分支
```

**2、提交代码到 master 分支**

```bash
hexo clean && hexo g  #重新生成代码
```

```bash
git checkout master  #切换到master分支
git add .
git commit -m "master demo"
git push --set-upstream origin master  #设置本地分支追踪远程分支
```

**3、GitHub Page 部署**

- 选择 your repository-》settings-》GitHub pages then copy your website address
