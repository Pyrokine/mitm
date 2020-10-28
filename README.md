# 快速获取微信文章的标题、作者、链接和时间并导出到json

## 项目地址

原项目地址  
https://github.com/iicey/mitm  
本项目地址  
https://github.com/Pyrokine/mitm  

## 使用说明

### 安装第三方库(Python3)

```
pip install openpyxl
pip install mitmproxy
```

### 设置代理(127.0.0.1:8080)

![1564572090441](https://github.com/Pyrokine/mitm/blob/master/img/1564572090441.png)

![1564572149417](https://github.com/Pyrokine/mitm/blob/master/img/1564572149417.png)

### 安装证书

访问 http://mitm.it/	安装Windows证书，如果提示流量未经过 mitm ，可以尝试更换浏览器，比如 Chrome 浏览器  

### 启动脚本

开启 cmd 或 git bash 切换到当前目录下，执行下面这段代码（使用 mitmweb 替换 mitmdump 开启带界面的模式）

```
mitmdump -s script.py
```

### 最后一步

点开PC微信里微信公众号的列表页，向下滑动即可（必须从这个位置打开单独的公众号窗口，否则是抓取不到的）

![1564572879319](https://github.com/Pyrokine/mitm/blob/master/img/1564572879319.png)
