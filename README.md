# Like and comment for icourse163

A python script designed for like and comments to MOOC. 

用于[中国大学MOOC](https://www.icourse163.org/)点赞和评论的Python脚本

## 简介

本脚本通过中国大学MOOC的二维码扫描功能登录系统，并可保持登录状态10日左右，如果您的登录状态已经过期，请删除`session.pickle`再次运行脚本。

本脚本依赖的库主要基于`requests`库。如果您未安装此库，请自行使用`pip`安装。

## 运行方法

1. 安装必要的库。

2. 下载本脚本，并使用`python`运行。

1. 如果您第一次使用此脚本，会在脚本同级目录中出现`qr.png`。您需要提前打开`中国大学MOOC`的二维码扫描功能，打开并扫描`qr.png`，并确定登录。

1. 输入`pid`号，该字段来源于您所需要点赞和评论的网址。以此网址为例`https://www.icourse163.org/learn/SDCJDX-1206683820?tid=1467034465#/learn/forumdetail?pid=1328261532`，`pid`为`1328261532`。

1. 如果终端中出现如下，则证明成功。

```
输入pid:1328261532
//#DWR-INSERT
//#DWR-REPLY
dwr.engine._remoteHandleCallback('1648477205532','0',87);

200
输入pid:
```

> 本脚本会在同级目录中存储`session.pickle`文件，本文件可以保持登录状态。但在创建10日内会失效。如果您的登录状态已经过期，请删除`session.pickle`再次运行脚本。

