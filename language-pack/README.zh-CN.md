# FEFW Save Editor 简体中文外置语言包 v1.0（实验版）

本包把简体中文界面翻译及角色/道具/职业/技能名称翻译独立保存，尽量避免每次官方更新都重做整套汉化。

## 重要限制（请先看）

**本包目前适用于官方 source.zip 源码版，不支持直接汉化官方 Windows EXE。**

官方 Windows 版使用 PyInstaller `--onefile` 打包，程序模块封装在单文件内部，没有外部语言插件接口。单独把语言包放在 EXE 旁边不会生效。直接拆包/重打包官方 EXE 也有兼容性和安全风险，因此本包不做这种操作。

## 准备

1. 下载官方 [v1.3.6 Release](https://github.com/Antiadvocate/fefw-editor/releases/tag/v1.3.6) 中的 `FEFW-Save-Editor-v1.3.6-source.zip` 并解压。
2. Windows 安装 Python 3.10 或更高版本，并确保安装时启用了 Python Launcher（`py` 命令）。
3. 解压本语言包 ZIP。

## 安装（尽量一键）

双击本包中的 `安装汉化.bat`，输入包含 `editor.py` 的官方源码目录完整路径。安装器会：

- 先备份原始 `editor.py` 为 `editor.py.zhcn-backup`
- 复制独立的 `zh_CN` 语言模块
- 在官方源码启动入口加入很小的加载补丁
- 生成 `启动简体中文.bat`

以后双击源码目录里的 `启动简体中文.bat` 启动。首次启动若缺少 `zstandard`，启动器会尝试通过 pip 安装官方 requirements 中的依赖。

## 卸载

在命令提示符中运行：

```bat
py -3 install_zh_cn.py --target "D:\路径\FEFW-Save-Editor" --uninstall
```

注意：卸载命令中的 `install_zh_cn.py` 是本语言包目录里的安装器路径。卸载会恢复备份的 `editor.py` 并删除 `zh_CN` 目录及启动器。

## 官方版本更新

不要把新版本源码覆盖在旧目录上。每次官方更新时：

1. 下载新的官方 source.zip，解压到一个全新文件夹。
2. 对新文件夹再次运行本语言包的 `安装汉化.bat`。
3. 翻译数据仍然沿用原来的语言包；如果上游改了程序入口或内部数据接口，可能需要更新加载兼容层。

这比每次重新合并所有汉化代码轻得多，但**不是对所有未来版本都保证零修改**。

## 安全与存档

- 本包只有可读 Python 源码和 JSON 翻译数据，不含 EXE。
- 不要求关闭 Defender 或绕过 SmartScreen。
- 翻译只影响界面显示，不应改写存档 ID 或数据；实际使用仍请先备份存档。
- 首版属于实验版，尚未在你的 Windows 环境完成完整 GUI 实机验证。
