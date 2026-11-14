# FEFW Save Editor 简体中文外置语言包 v1.0（实验版）

本包将现有简体中文界面翻译、角色/道具/职业/技能名称映射从编辑器源码主体中分离，作为独立目录加载。

## 重要限制

- **适用对象：官方 source.zip 源码版**，不是官方 Windows 预编译 EXE。
- 官方 Windows ZIP 是 PyInstaller 打包程序，没有官方语言插件接口；把本语言包直接放在 EXE 旁边不会生效。
- 本安装器只对源码目录的启动入口做一个小型加载补丁，并在旁边保存备份；不修改存档格式、字段、ID 或写入逻辑。
- 需要 Python 3.10+，并按官方 README 安装 requirements.txt。
- 这是首个实验版，尚未完成所有系统/版本的实机 GUI 验证。安装前请保留官方源码 ZIP。

## 安装

1. 从官方 Release 下载 `FEFW-Save-Editor-v1.3.6-source.zip` 并解压。
2. 将本语言包 ZIP 解压到单独文件夹。
3. 在命令提示符中运行：

```bat
python install_zh_cn.py --target "D:\路径\FEFW-Save-Editor"
```

4. 进入官方源码目录，运行 `FEFW Save Editor.bat`。

安装器会创建 `editor.py.zhcn-backup`，并把语言模块复制到源码目录的 `zh_CN` 子目录。

## 卸载

```bat
python install_zh_cn.py --target "D:\路径\FEFW-Save-Editor" --uninstall
```

## 更新官方版本

官方更新后，重新解压新的 source.zip 到一个干净目录，再对新目录运行本安装器即可。翻译资料不需要重新制作；如果上游重构启动代码或数据接口，安装器/兼容层可能需要更新。

## 目前包含

- 界面简体中文
- 角色名称中文映射与自动音译 fallback
- 道具名称中文映射与自动翻译/音译 fallback
- 职业名称中文映射
- 技能名称翻译
- 保留日文原始名称用于识别，不修改存档数据

## 安全提示

本包提供 Python 源码，不包含 EXE，也不要求关闭 Windows Defender 或绕过安全提示。建议只从官方仓库下载原版源码和本语言包。
