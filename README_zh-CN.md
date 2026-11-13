# 万紫千红存档编辑器（简体中文界面）

这是基于原作者 **Antiadvocate/FEFW Save Editor v1.3.2** 的个人汉化分支。

- 原项目： https://github.com/Antiadvocate/fefw-editor
- 本汉化分支： https://github.com/syflu81890-max/fefw-editor-zh-cn
- 基础版本： v1.3.2
- 汉化范围：主窗口、页面标签、常用按钮、表格标题、搜索提示、部分状态和对话框文案。
- 游戏内角色、物品、职业、技能名称及其 ID 沿用原项目数据，不擅自更改存档标识。

## 构建 Windows 版本

1. 打开本仓库的 **Actions**。
2. 选择 **Build Chinese Windows**。
3. 点击 **Run workflow**，选择 `zh-cn-v1.3.2` 分支运行。
4. 构建成功后，在本次运行页面底部的 **Artifacts** 下载 `FEFW-Save-Editor-zh-CN-windows`。

也可以在该分支有新提交时自动触发构建。

## 使用提醒

- 使用前先关闭游戏。
- 首次编辑前请备份整个存档目录。
- 编辑器只有在按下“保存”后才会写入存档；原始文件会按原程序逻辑备份为 `.bak`。
- 本项目为非官方逆向工具，汉化分支不保证适用于其他游戏或编辑器版本。

## 汉化实现说明

界面翻译集中在 `i18n_zh_cn.py`。它只处理 UI 展示文案，不翻译游戏数据 ID、存档键、枚举值或 JSON 数据表。遇到仍显示英文的界面文字，可以在该文件补充映射。
