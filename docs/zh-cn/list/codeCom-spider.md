---
title: gulp压缩静态资源和字体压缩
date: 2020-08-22 11:01:00
author: William
img: /images/1.jpg #文章特征图，推荐使用图床（腾讯云、七牛云、又拍云等）来作为图片路径
top: false #文章是置顶
cover: false #是否加入到首页轮播图中
coverImg: /images/1.jpg #轮播的图片路径，若无，则使用文章的特殊图片
#password: 8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92
toc: true #是否启用目录
mathjax: false #是否激活mathjax数学公式
summary: 使用gulp压缩静态资源和字体压缩插件实现网站自动化部署
categories: Plug-ins #文章分类，只建议一篇文章一个分类
tags: #标签，可以多个
  - Gulp
  - Spider
---

### 准备工作

**1. 前提**

- HEXO-THEME-MATERY
- Node.js

**2. 相关链接**

- [Gulp 官网](https://www.gulpjs.com.cn/)
- [spider github 仓库](https://github.com/aui/font-spider)
- [font-spider 官网](https://www.font-spider.org/)

### 代码压缩(推荐)

**1、全局安装 gulp,在项目根目录下执行如下命令:**

```cmd
# 全局安装gulp模块
cnpm install gulp -g
# 安装各种小功能模块  执行这步的时候，可能会提示权限的问题，最好以管理员模式执行
cnpm install gulp gulp-htmlclean gulp-htmlmin gulp-minify-css gulp-uglify gulp-imagemin --save
# 额外的功能模块
cnpm install gulp-debug gulp-clean-css gulp-changed gulp-if gulp-plumber gulp-babel babel-preset-es2015 del @babel/core --save
```

**2、在 hexo 根目录中创建一个新文件 gulpfile.js 并将以下内容复制到文件中，内附有中文注释，可根据您的需要进行修改**

```js
var gulp = require('gulp')
var debug = require('gulp-debug')
var cleancss = require('gulp-clean-css') //css压缩组件
var uglify = require('gulp-uglify') //js压缩组件
var htmlmin = require('gulp-htmlmin') //html压缩组件
var htmlclean = require('gulp-htmlclean') //html清理组件
var imagemin = require('gulp-imagemin') //图片压缩组件
var changed = require('gulp-changed') //文件更改校验组件
var gulpif = require('gulp-if') //任务 帮助调用组件
var plumber = require('gulp-plumber') //容错组件（发生错误不跳出任务，并报出错误内容）
var isScriptAll = true //是否处理所有文件，(true|处理所有文件)(false|只处理有更改的文件)
var isDebug = true //是否调试显示 编译通过的文件
var gulpBabel = require('gulp-babel')
var es2015Preset = require('babel-preset-es2015')
var del = require('del')
var Hexo = require('hexo')
var hexo = new Hexo(process.cwd(), {}) // 初始化一个hexo对象

// 清除public文件夹
gulp.task('clean', function () {
	return del(['public/**/*'])
})

// 下面几个跟hexo有关的操作，主要通过hexo.call()去执行，注意return
// 创建静态页面 （等同 hexo generate）
gulp.task('generate', function () {
	return hexo.init().then(function () {
		return hexo
			.call('generate', {
				watch: false,
			})
			.then(function () {
				return hexo.exit()
			})
			.catch(function (err) {
				return hexo.exit(err)
			})
	})
})

// 启动Hexo服务器
gulp.task('server', function () {
	return hexo
		.init()
		.then(function () {
			return hexo.call('server', {})
		})
		.catch(function (err) {
			console.log(err)
		})
})

// 部署到服务器
gulp.task('deploy', function () {
	return hexo.init().then(function () {
		return hexo
			.call('deploy', {
				watch: false,
			})
			.then(function () {
				return hexo.exit()
			})
			.catch(function (err) {
				return hexo.exit(err)
			})
	})
})

// 压缩public目录下的js文件
gulp.task('compressJs', function () {
	return gulp
		.src(['./public/**/*.js', '!./public/libs/**']) //排除的js
		.pipe(gulpif(!isScriptAll, changed('./public')))
		.pipe(gulpif(isDebug, debug({ title: 'Compress JS:' })))
		.pipe(plumber())
		.pipe(
			gulpBabel({
				presets: [es2015Preset], // es5检查机制
			})
		)
		.pipe(uglify()) //调用压缩组件方法uglify(),对合并的文件进行压缩
		.pipe(gulp.dest('./public')) //输出到目标目录
})

// 压缩public目录下的css文件
gulp.task('compressCss', function () {
	var option = {
		rebase: false,
		//advanced: true, //类型：Boolean 默认：true [是否开启高级优化（合并选择器等）]
		compatibility: 'ie7', //保留ie7及以下兼容写法 类型：String 默认：''or'*' [启用兼容模式； 'ie7'：IE7兼容模式，'ie8'：IE8兼容模式，'*'：IE9+兼容模式]
		//keepBreaks: true, //类型：Boolean 默认：false [是否保留换行]
		//keepSpecialComments: '*' //保留所有特殊前缀 当你用autoprefixer生成的浏览器前缀，如果不加这个参数，有可能将会删除你的部分前缀
	}
	return gulp
		.src(['./public/**/*.css', '!./public/**/*.min.css']) //排除的css
		.pipe(gulpif(!isScriptAll, changed('./public')))
		.pipe(gulpif(isDebug, debug({ title: 'Compress CSS:' })))
		.pipe(plumber())
		.pipe(cleancss(option))
		.pipe(gulp.dest('./public'))
})

// 压缩public目录下的html文件
gulp.task('compressHtml', function () {
	var cleanOptions = {
		protect: /<\!--%fooTemplate\b.*?%-->/g, //忽略处理
		unprotect: /<script [^>]*\btype="text\/x-handlebars-template"[\s\S]+?<\/script>/gi, //特殊处理
	}
	var minOption = {
		collapseWhitespace: true, //压缩HTML
		collapseBooleanAttributes: true, //省略布尔属性的值 <input checked="true"/> ==> <input />
		removeEmptyAttributes: true, //删除所有空格作属性值 <input id="" /> ==> <input />
		removeScriptTypeAttributes: true, //删除<script>的type="text/javascript"
		removeStyleLinkTypeAttributes: true, //删除<style>和<link>的type="text/css"
		removeComments: true, //清除HTML注释
		minifyJS: true, //压缩页面JS
		minifyCSS: true, //压缩页面CSS
		minifyURLs: true, //替换页面URL
	}
	return gulp
		.src('./public/**/*.html')
		.pipe(gulpif(isDebug, debug({ title: 'Compress HTML:' })))
		.pipe(plumber())
		.pipe(htmlclean(cleanOptions))
		.pipe(htmlmin(minOption))
		.pipe(gulp.dest('./public'))
})

// 压缩 public/medias 目录内图片
gulp.task('compressImage', function () {
	var option = {
		optimizationLevel: 5, //类型：Number 默认：3 取值范围：0-7（优化等级）
		progressive: true, //类型：Boolean 默认：false 无损压缩jpg图片
		interlaced: false, //类型：Boolean 默认：false 隔行扫描gif进行渲染
		multipass: false, //类型：Boolean 默认：false 多次优化svg直到完全优化
	}
	return gulp
		.src('./public/medias/**/*.*')
		.pipe(gulpif(!isScriptAll, changed('./public/medias')))
		.pipe(gulpif(isDebug, debug({ title: 'Compress Images:' })))
		.pipe(plumber())
		.pipe(imagemin(option))
		.pipe(gulp.dest('./public'))
})
// 执行顺序： 清除public目录 -> 产生原始博客内容 -> 执行压缩混淆 -> 部署到服务器
gulp.task(
	'build',
	gulp.series(
		'clean',
		'generate',
		'compressHtml',
		'compressCss',
		'compressJs',
		'compressImage',
		gulp.parallel('deploy')
	)
)

// 默认任务
gulp.task(
	'default',
	gulp.series(
		'clean',
		'generate',
		gulp.parallel('compressHtml', 'compressCss', 'compressJs', 'compressImage')
	)
)
//Gulp4最大的一个改变就是gulp.task函数现在只支持两个参数，分别是任务名和运行任务的函数
```

- 注意：这个加入了图片压缩，如果不想用图片压缩可以把第 154 行的 "compressImage", 和第 165 行的 ,"compressImage" 去掉即可

**3、执行压缩方式（二选一即可）**

- 3.1 直接在 Hexo 根目录执行 gulp 或者 gulp default ，这个命令相当于 hexo cl&&hexo g 并且再把代码和图片压缩。

```bash
gulp
#OR
gulp default #相当于 hexo cl&&hexo g
```

- 3.2 在 Hexo 根目录执行 gulp build

```bash
gulp build  #生成、压缩文件后并自动部署
```

### 字体压缩（Spider）

**1、全局安装 spider,在项目根目录下执行如下命令:**

```cmd
cnpm install font-spider -g
```

**2、在 CSS 中使用 webfont**

```css
/*声明 WebFont*/
@font-face {
	font-family: 'pinghei';
	src: url('../font/pinghei.eot');
	src: url('../font/pinghei.eot?#font-spider') format('embedded-opentype'), url('../font/pinghei.woff')
			format('woff'), url('../font/pinghei.ttf') format('truetype'), url('../font/pinghei.svg')
			format('svg');
	font-weight: normal;
	font-style: normal;
}

/*使用选择器指定字体*/
.home h1,
.demo > .test {
	font-family: 'pinghei';
}
```

- 特别说明： @font-face 中的 src 定义的 .ttf 文件必须存在，其余的格式将由工具自动生成

**3、运行 font-spider**

```bash
font-spider ./demo/*.html  #页面依赖的字体将会自动压缩好，原 .ttf 字体会备份
```
