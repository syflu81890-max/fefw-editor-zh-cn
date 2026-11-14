# 万紫千红 存档编辑器（简体中文）

**汉化版本：1.3.4**  
基于 [Antiadvocate/fefw-editor](https://github.com/Antiadvocate/fefw-editor) 官方 1.3.4，保留原版存档编辑能力，并提供简体中文界面和中文角色、职业、物品及技能名称。

## 1.3.4 更新内容

- 同步官方 1.3.4 的全部编辑器更新。
- 职业页面新增职业经验修改。
- 职业与熟练度列表支持 Ctrl+A 全选、Shift 连选／拖选。
- 难度和模式修改会同步写入当前周目的所有相关存档槽位。
- 保留中文资料库显示名称；存档内部 ID 和数据结构不做翻译或改写。

## 使用方法

1. 关闭游戏和模拟器。
2. 解压本压缩包到一个有写入权限的文件夹。
3. 双击运行 **FEFW Save Editor.exe**。
4. 选择存档文件夹，通常位于：

   `%APPDATA%\\eden\\nand\\user\\save\\<存档用户目录>\\04007EF01F8AE000\\000\\`

5. 修改完成后按 **Ctrl+S** 保存。

## 重要提醒

- 本工具是非官方逆向存档编辑器，使用前务必备份整个存档文件夹。
- 工具会在首次保存前为存档槽位保留 .bak 备份；仍建议额外复制一份完整存档。
- 建议先用少量、可验证的修改测试，不要随意清空未知标记（Flags）。
- 修改存档时请保持游戏关闭，避免游戏自动保存覆盖编辑结果。
- 本工具只修改存档，不会修改游戏本体。

## 项目地址

汉化分支：[syflu81890-max/fefw-editor-zh-cn](https://github.com/syflu81890-max/fefw-editor-zh-cn)  
原版项目：[Antiadvocate/fefw-editor](https://github.com/Antiadvocate/fefw-editor)
