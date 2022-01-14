[原文](https://www.jianshu.com/p/1bfa7ec83bb6)

此问题并不仅仅针对中文乱码,还解决因为头文件乱码:

```
# !/usr/bin/env python
# coding=utf-8
```
如在终端正常输出为:

```
suggestion: block  Rate: 83.47  label: liveness
```

乱码为:
```
ϵͳ�Ҳ���ָ����·����
```
解决办法:

设置-扩展-Run Code configuration-Executor Map - settings.json

添加/修改内容
```
"code-runner.executorMap": {
    ...
    "python": "set PYTHONIOENCODING=utf8 & $pythonPath -u $fullFileName",
    ...
    }
"code-runner.respectShebang": false,
```
"code-runner.respectShebang": false是因为python文件配置有头文件会产生错误.