# PaperHandle

用于将多行文本快速合并为一行。

## 1 Instruction

### 1.1 UI

左上方为输入区域，可输入文本；

左下方为文本转换区域，同步转换左上方输入区域的文本。不可编辑；

右侧为输出区域，保存输出文本，且可编辑；

点击左下方按钮`Append and Clear`，将文本转换区域的内容添加到右侧输出区域保存，同时清空左侧所有内容。

### 1.2 Text Processing

当前文本处理操作包括：

- 将一个或多个连续空白符[*]统一替换为一个空格；
- 去除句首与句尾的空白符[*]。

[*] 空白符包括：空格、换行、换页、制表符等。

### 1.3 Shortcut

重新定义了`复制`:`Ctrl+C`与`粘贴`:`Ctrl+V`的行为：

1. 复制：`Ctrl+C`将右侧输出区域的内容复制到剪贴板，无论此时光标位置或选中区域。
2. 粘贴：`Ctrl+V`将剪贴板内容粘贴添加到左上输入区域，区域内原有内容保留，无论此时光标位置或选中区域。

## 2 Environmental Configuration

运行代码需要`Python3`，与Python包：`PyQt5`。

### 2.1 Python3

Python3的安装可参考[菜鸟教程](https://www.runoob.com/python3/python3-install.html "菜鸟教程/Python3")。

### 2.2 PyQt5

安装Python后可使用pip等工具安装PyQt。以pip举例：

1. 打开`命令提示符`/`Terminal`/`Powershell`等命令行工具中的任意一个；
2. 运行`pip install pyqt5`，等待。

若因网络原因下载速度慢，可尝试使用国内源：使用命令`pip install pyqt5 -i https://pypi.tuna.tsinghua.edu.cn/simple`安装。

## 3. TODO

- 添加操作提示：当执行`复制`、`粘贴`操作成功时进行提示；
- 添加中英文检测，将英文换行替换为空格，而中文换行直接剔除，不需要空格；
- 添加快捷键，代替按钮`Append and Clear`，以获得更快的操作速度；
- 添加搜索、撤销操作等功能；
- 添加显示行号功能；
- 更美观、人性化的界面。
