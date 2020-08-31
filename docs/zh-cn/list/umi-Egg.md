---
title: Umi+TypeScript+Egg.js案例
date: 2020-08-23 20:26:00
author: William
img: /images/1.jpg #文章特征图，推荐使用图床（腾讯云、七牛云、又拍云等）来作为图片路径
top: false #文章是置顶
cover: false #是否加入到首页轮播图中
coverImg: /images/1.jpg #轮播的图片路径，若无，则使用文章的特殊图片
toc: true #是否启用目录
summary: 一个简单的商品管理App
categories: Store #文章分类，只建议一篇文章一个分类,此为多级分类写法
tags: [Umi, TypeScript, Egg.js] #标签，可以多个
---

### 准备工作

- Node.js
- yarn

### 服务端实现

**1、全局安装 yarn 和 tyarn（淘宝源）,执行如下命令**

```bash
cnpm i -g yarn tyarn   #全局安装yarn和tyarn
yarn --version  #插件版本号
tyarn --version  #插件版本号
```

**2、创建一个工程目录，并在其内新建一个 server 文件夹，并用 vscode 打开**

**3、生成 egg.js 工程骨架,执行如下代码**

```bash
cd server
cnpm init egg --type=simple
```

- 初始化项目过程如下：

```
npx: 396 瀹夎鎴愬姛锛岀敤鏃?44.12 绉?[egg-init] use registry: https://r.npm.taobao.org
[egg-init] target dir is E:\work\Store\server\init
[egg-init] fetching npm info of egg-init-config
[egg-init] use boilerplate: simple(egg-boilerplate-simple)
[egg-init] fetching npm info of egg-boilerplate-simple
[egg-init] downloading https://registry.npm.taobao.org/egg-boilerplate-simple/download/egg-boilerplate-simple-3.3.1.tgz
[egg-init] extract to C:\Users\William\AppData\Local\Temp\egg-init-boilerplate
[egg-init] collecting boilerplate config...
? project name (init) sky
? project name sky
? project description
? project description
? project author william
? project author william
? cookie security keys (1598198778935_8356)
? cookie security keys 1598198778935_8356
[egg-init] write to E:\work\Store\server\init\.autod.conf.js
[egg-init] write to E:\work\Store\server\init\.eslintignore
[egg-init] write to E:\work\Store\server\init\.eslintrc
[egg-init] write to E:\work\Store\server\init\README.md
[egg-init] write to E:\work\Store\server\init\.gitignore
[egg-init] write to E:\work\Store\server\init\package.json
[egg-init] write to E:\work\Store\server\init\app\router.js
[egg-init] write to E:\work\Store\server\init\config\config.default.js
[egg-init] write to E:\work\Store\server\init\config\plugin.js
[egg-init] write to E:\work\Store\server\init\app\controller\home.js
[egg-init] write to E:\work\Store\server\init\test\app\controller\home.test.js
[egg-init] usage:
      - cd E:\work\Store\server\init
      - npm install
      - npm start / npm run dev / npm test
```

**4、添加 mysql 数据库驱动依赖,执行如下代码**

```bash
tyarn add egg-mysql
```

- 配置 config/plugin.js 文件

```js
mysql: {
    enable: true,
    package: 'egg-mysql',
  },
```

**5、配置数据库信息,执行如下代码**

- 配置 config/config.default.js 文件

```js
// add mysql config
config.mysql = {
	client: {
		host: 'localhost',
		port: 3306,
		user: 'root',
		password: 'root',
		database: 'demo',
	},
}
```

**6、编写 Controller,并配置 API 路由**

- 在 app/controller 目录下新建 product.js 文件，内容如下：

```js
/* eslint-disable eol-last */
const { Controller } = require('egg');

class ProductController extends Controller {
  async listProduct() {
    const { ctx, service } = this;
    const keyword = ctx.query.keyword;
    const products = await service.product.findProducts(keyword);  //调用查询服务
    ctx.body = products;
  }
}

module.exports = ProductController;
```

- 在 app 下新建 service 文件夹和其内部新建 product.js 文件，内容如下：

```js
const { Service } = require('egg')

class ProductService extends Service {
  async findProducts(keyword) {
    const client = this.app.mysql;
    const sql = 'select id, name, price, imgurl from product'  //sql查询语句

    if (!keyword) {
      return await client.query(sql);
    } else {
      return await client.query(`${sql} where name like ?`, [`%${keyword}%`]);
    }
  }
}

module.exports = ProductService;
```

- 打开app下的router.js文件，对路由进行配置如下：

```js
'use strict';

/**
 * @param {Egg.Application} app - egg application
 */
module.exports = app => {
  const { router, controller } = app;
  router.get('/', controller.home.index);
  router.get('/api/products', controller.product.listProducts);  
};
```

- 测试API是否生效

```bash
tyarn dev
```

**7、编写 Service,实现数据库查询**

- demo.sql为项目数据库文件
```demo.sql
/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MariaDB
 Source Server Version : 100504
 Source Host           : localhost:3307
 Source Schema         : demo

 Target Server Type    : MariaDB
 Target Server Version : 100504
 File Encoding         : 65001

 Date: 24/08/2020 22:16:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product`  (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `price` decimal(10, 2) NOT NULL,
  `imgurl` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8 COLLATE = utf8_bin ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES (1, '联想拯救者电竞手机Pro', 4199.00, 'https://imgchr.com/i/dyKvEF');
INSERT INTO `product` VALUES (2, '华为 HUAWEI P30 Pro', 3688.00, 'https://imgchr.com/i/dyKbj0');
INSERT INTO `product` VALUES (3, '华为 HUAWEI P40', 4188.00, 'https://imgchr.com/i/dyKxN4');
INSERT INTO `product` VALUES (4, '三星 Galaxy A51', 2599.00, 'https://imgchr.com/i/dyKOBT');
INSERT INTO `product` VALUES (5, '一加 OnePlus 8', 4199.00, 'https://imgchr.com/i/dyKLuV');
INSERT INTO `product` VALUES (6, '魅族17 Pro', 4699.00, 'https://imgchr.com/i/dyKXHU');

SET FOREIGN_KEY_CHECKS = 1;
```

**8、测试 API**

### 客户端实现

**1、新建一个client文件夹，并执行如下代码：**

```bash
cd client
npm install umi -gnpm install umi -g  #全局安装umi
tyarn create @umijs/umi-app #创建脚手架 或npx @umijs/create-umi-app
yarn install  #安装依赖 或tyarn
yarn start 或 npm run start #启动项目,在浏览器打开http://localhost:8000
```

**2、打开src/pages/index.tsx文件，编辑前端页面，代码如下：**

```tsx
import React, { useState, useEffect, ChangeEvent } from 'react';
import styles from './index.less';
import { request } from 'umi';

interface Product {
  id: number;
  name: string;
  price: number;
  imgurl: string;
}

//假数据
export default () => {
  const [product, setProducts] = useState<Product[]>([
    {
      id: 1,
      name: '苹果',
      price: 5.64,
      imgurl: 'https://ftp.bmp.ovh/imgs/2020/08/947e18ef3b6f10f1.png',
    },
    {
      id: 2,
      name: '香蕉',
      price: 6.24,
      imgurl: 'https://ftp.bmp.ovh/imgs/2020/08/947e18ef3b6f10f1.png',
    },
    {
      id: 3,
      name: '菠萝',
      price: 2.88,
      imgurl: 'https://ftp.bmp.ovh/imgs/2020/08/947e18ef3b6f10f1.png',
    },
    {
      id: 4,
      name: '梨',
      price: 11.9,
      imgurl: 'https://ftp.bmp.ovh/imgs/2020/08/947e18ef3b6f10f1.png',
    },
  ]);

  // 函数申明
  const fetchProductList = async (keyword: string = '') => {
    const result = await request('/api/products', {
      params: { keyword },
    });
    setProducts(result);
  };
  // 函数调用
  useEffect(() => {
    fetchProductList();
  }, []);

  // 搜索功能实现
  const [keyword, setKeyword] = useState<string>('');
  const searchInputChangeHandler = (e: ChangeEvent<HTMLInputElement>) => {
    const txt = e.target.value;
    setKeyword(txt);
  };

  // 监听搜索按钮事件
  const searchButtonClickHandler = () => {
    fetchProductList(keyword);
  };

  return (
    <div className={styles.searchPage}>
      <div className={styles.searchBar}>
        <input
          className={styles.searchInput}
          onChange={searchInputChangeHandler}
        />
        <button
          className={styles.searchButton}
          onClick={searchButtonClickHandler}
        >
          搜索
        </button>
      </div>

      <div className={styles.productList}>
        {product.map(product => {
          return (
            <div className={styles.productItem} key={product.id}>
              <img
                className={styles.productImage}
                src={product.imgurl}
                alt=""
                width="50"
              />
              <div className={styles.productInfo}>
                <div className={styles.productTitle}>{product.name}</div>
                <div className={styles.productPrice}>{product.price}</div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};
```

- 编辑index.less文件，此文件为样式文件

```less
.searchPage {
  padding: 5px;
}

.searchBar {
  display: flex;
  margin-bottom: 10px;
}

.searchInput {
  width: 100%;
  margin-right: 5px;
}

.searchButton {
  width: 60px;
}

.productList {
  background-color: aqua;
}

.productItem {
  display: flex;
  border-bottom: 1px solid #cccccc;
  padding: 10px;
}

.productImage {
  margin-right: 10px;
}

.productInfo {}

.productTitle {
  font-size: 16px;
}

.productPrice {
  font-size: 18px;
  color: #b30a0a;
  font-style: italic;
}
```

**3、配置根目录下的.umirc.ts文件，解决前后端跨域问题**

```ts
import { defineConfig } from 'umi';

export default defineConfig({
  nodeModulesTransform: {
    type: 'none',
  },
  routes: [{ path: '/', component: '@/pages/index' }],
  proxy: {
    '/api': {
      target: 'http://127.0.0.1:7001/',
      changeOrigin: true,
    },
  },
});
```

