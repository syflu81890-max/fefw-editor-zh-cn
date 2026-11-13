"""简体中文界面层：只翻译界面文案，不修改存档字段、ID 或游戏数据。"""
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

_TRANSLATIONS = {
    "Fortune's Weave Save Editor":"万紫千红 存档编辑器",
    "Item catalogue":"物品目录","Search by name, Japanese name or id…":"按名称、日文名或 ID 搜索…",
    "Type":"类型","All types":"所有类型","Internal duplicates":"内部重复项",
    "Double-click or Enter also works":"双击或按 Enter 键也可选择",
    "Item":"物品","Japanese":"日文","Id":"ID","Name":"名称","Slot":"存档槽位",
    "Save":"保存","Reload":"重新读取","⟳ Reload":"⟳ 重新读取","Snapshot":"创建快照",
    "Restore…":"恢复快照…","Open folder…":"打开存档文件夹…","Ready":"就绪",
    "Also edit this route's other saves":"同时修改本路线的其他存档",
    "Units":"角色","Convoy":"输送队","Gold":"金钱","Supports":"支援关系",
    "Player":"玩家","Classes":"职业","Flags":"标记","Mounts":"兵种与坐骑",
    "Stats":"能力值","Inventory":"物品栏","Class":"职业","Arts & skills":"战技与技能",
    "Copy unit in…":"从其他存档复制角色…","Remove unit":"移除角色",
    "No unit selected":"未选择角色","Open a save folder to begin.":"请先打开存档文件夹。",
    "Make copies match":"同步其他副本","Points gained from level-ups":"升级获得的能力点",
    "Hit points":"生命","Strength":"力量","Magic":"魔力","Dexterity":"技巧",
    "Speed":"速度","Luck":"幸运","Defense":"守备","Resistance":"魔防","Charm":"魅力",
    "These are what the unit has gained from levelling, not the totals shown in-game.":"这里显示的是角色升级获得的数值，并非游戏内最终总值。",
    "Changing HP gained moves max HP with it. Edits apply on Enter / Tab; ":"修改获得的 HP 时，最大 HP 也会随之变化。按 Enter / Tab 应用修改；",
    "Carried items":"携带物品","Select a slot, then choose its replacement.":"先选择一个物品栏位，再选择要替换的物品。",
    "Allow any item type (can break the game)":"允许任意物品类型（可能导致游戏异常）",
    "Add item…":"添加物品…","Remove item":"移除物品","Include monster / internal classes":"包含怪物／内部职业",
    "Change class":"更换职业","Current class":"当前职业","Search classes…":"搜索职业…",
    "Internal name":"内部名称","Everything in storage, materials included, by slot.":"按栏位显示所有仓库物品，包括素材。",
    "Repair convoy":"修复输送队","Filter the convoy…":"筛选输送队…",
    "Slot · Item":"栏位 · 物品","Qty":"数量","Quantity":"数量","Set qty":"设置数量",
    "All materials…":"全部素材…","New amount":"新数值","Set gold":"设置金钱",
    "Characters":"角色","Search characters…":"搜索角色…",
    "Only characters in this save":"仅显示此存档中的角色","Character":"角色",
    "Convs":"对话数","Top":"最高","Support partner":"支援对象","Points":"点数",
    "Max":"上限","Conversations seen":"已观看对话","In party":"在队伍中",
    "Record conversation as seen:":"记录已观看的支援对话：","Forget…":"清除记录…",
    "Support points:":"支援点数：","Apply":"应用","No character selected":"未选择角色",
    "Open a save to see what it records.":"打开存档以查看记录内容。",
    "No save folder open":"尚未打开存档文件夹","Name":"名称","Lv":"等级",
    "Use this":"使用此项","Cancel":"取消","OK":"确定",
    "Run settings":"游戏设置","Difficulty":"难度","Mode":"模式",
    "Army-wide values, stored in GameUserData at the start of the save.":"全军通用数值，存储在存档开头的 GameUserData 中。",
    "Renown exp":"声望经验","Karma Shards":"业力碎片",
    "Classes this unit has":"角色拥有的职业","Weapon masteries":"武器熟练度",
    "Value":"数值","Flags":"标记","Weapon":"武器","Rank":"等级","Exp":"经验",
    "Next rank at":"下一级所需经验","Change…":"更改…","Add…":"添加…","Remove":"移除",
    "Swap…":"替换…","Set current":"设为当前职业","Set rank…":"设置等级…",
    "Set exp…":"设置经验…","Saved flags":"已保存标记","Add flag…":"添加标记…",
    "Set value…":"设置数值…","Reads as":"含义","List":"列表",
    "Battalions & mounts":"部队与坐骑","This save's pool":"此存档的可用列表",
    "Unit":"角色","Battalion":"部队","Mount":"坐骑","Entry":"条目","Kind":"类别",
    "Record id":"记录 ID","Assign to unit":"分配给角色","Clear unit's":"清除角色分配",
    "Remove from pool":"从列表中移除",
    "Search units or classes…  (Ctrl+F)":"搜索角色或职业…（Ctrl+F）",
    "Show enemies & NPCs":"显示敌人和 NPC","No character selected":"未选择角色",
    "Pick an item from the catalogue first.":"请先从物品目录中选择物品。",
    "Pick an inventory slot first.":"请先选择一个物品栏位。",
    "Pick a class from the list first.":"请先从列表中选择职业。",
    "Pick a unit first.":"请先选择角色。",
    "Pick a convoy row first.":"请先选择输送队栏位。",
    "Pick a support partner on the Supports page first.":"请先在“支援关系”页面选择支援对象。",
    "Pick a unit on the Mounts page first.":"请先在“兵种与坐骑”页面选择角色。",
    "Pick a battalion in the pool first.":"请先从可用列表中选择部队。",
    "Only battalions can be assigned here.":"这里只能分配部队。",
    "Nothing to undo.":"没有可撤销的操作。","Nothing to redo.":"没有可重做的操作。",
    "Undone — Ctrl+Y puts it back.":"已撤销 — 按 Ctrl+Y 可恢复。",
    "Redone.":"已重做。","No snapshots yet — press Snapshot first.":"尚无快照，请先创建快照。",
    "Snapshot of ":"已创建快照：","Restored ":"已恢复快照：",
    "Open any slot in your save folder":"选择存档文件夹中的任意存档槽位",
    "Pick a snapshot to restore":"选择要恢复的快照",
    "Copy a unit from which save?":"选择要从哪个存档复制角色",
    "Quantity":"数量","How many?":"请输入数量：","Flag value":"标记数值",
    "New value (0 – 2147483647):":"新数值（0 – 2147483647）：",
    "Value to store (0 – 254, or anything wider):":"要写入的数值（0 – 254，或更大的数值）：",
    "Mastery exp":"熟练度经验","Exp for this weapon (0 – 65535):":"此武器的经验值（0 – 65535）：",
    "That is the unit's current class. Change the ":"这已经是角色当前的职业。请改为选择其他职业。",
    "Save editor":"存档编辑器",
    "Pick an item from the catalogue first.":"请先从目录中选择一个物品。",
    "Nothing changed — that unit has no such item slot here.":"没有发生变化 — 该角色没有对应的物品栏位。",
    "Enemy and NPC records are read-only — their layout isn't fully known.":"敌人和 NPC 记录为只读 — 其数据结构尚未完全解析。",
    "This slot's convoy doesn't need repairing.":"此存档槽位的输送队无需修复。",
    "No skill names available (skill_ids.json is missing).":"没有可用的技能名称（缺少 skill_ids.json）。",
    "This file's GameUserData isn't the known layout.":"此文件的 GameUserData 结构与已知格式不符。",
    "No materials found in the item list.":"物品列表中没有找到素材。",
    "No save folder open":"尚未打开存档文件夹",
    "Normal":"普通","Hard":"困难","Maddening":"疯狂","Casual":"休闲","Classic":"经典",
    "today ":"今天 ","match":"项匹配","matches":"项匹配",
    "Gold lives at a fixed place in every slot of this game (GameUserData ":"金钱存储在本作每个存档槽位的固定位置（GameUserData ",
    "Renown exp is the army's total; the level itself follows the game's own ":"声望经验是全军累计值；声望等级由游戏自身的 ",
    "Playthrough ":"周目 ","Level ":"等级 ","Current class":"当前职业",
}
# Longer phrases are translated first; remaining exact/embedded English fragments
# are deliberately limited to presentation text.
def tr(value):
    if not isinstance(value, str) or not value:
        return value
    if value in _TRANSLATIONS:
        return _TRANSLATIONS[value]
    out = value
    for src in sorted(_TRANSLATIONS, key=len, reverse=True):
        if len(src) > 3 and src in out:
            out = out.replace(src, _TRANSLATIONS[src])
    return out

def _patch_widget(cls):
    old_init = cls.__init__
    def init(self, *args, **kwargs):
        if "text" in kwargs: kwargs["text"] = tr(kwargs["text"])
        old_init(self, *args, **kwargs)
    cls.__init__ = init
    old_configure = cls.configure
    def configure(self, cnf=None, **kwargs):
        if "text" in kwargs: kwargs["text"] = tr(kwargs["text"])
        return old_configure(self, cnf, **kwargs)
    cls.configure = configure

def install():
    for cls in (ttk.Label, ttk.Button, ttk.Checkbutton, ttk.Radiobutton):
        _patch_widget(cls)
    # Keep Combobox values unchanged: some are internal enum values used by logic.
    old_heading = ttk.Treeview.heading
    def heading(self, column, option=None, **kwargs):
        if "text" in kwargs: kwargs["text"] = tr(kwargs["text"])
        return old_heading(self, column, option, **kwargs)
    ttk.Treeview.heading = heading
    old_add = ttk.Notebook.add
    def add(self, child, **kwargs):
        if "text" in kwargs: kwargs["text"] = tr(kwargs["text"])
        return old_add(self, child, **kwargs)
    ttk.Notebook.add = add
    old_title = tk.Wm.title
    def title(self, string=None):
        return old_title(self, tr(string)) if string is not None else old_title(self)
    tk.Wm.title = title
    for name in ("showerror", "showwarning", "showinfo", "askyesno", "askyesnocancel"):
        old = getattr(messagebox, name)
        def wrap(*args, _old=old, **kwargs):
            args = tuple(tr(a) if isinstance(a, str) else a for a in args)
            if "title" in kwargs: kwargs["title"] = tr(kwargs["title"])
            if "message" in kwargs: kwargs["message"] = tr(kwargs["message"])
            return _old(*args, **kwargs)
        setattr(messagebox, name, wrap)
    for name in ("askopenfilename", "askdirectory"):
        old = getattr(filedialog, name)
        def wrap_dialog(*args, _old=old, **kwargs):
            if "title" in kwargs: kwargs["title"] = tr(kwargs["title"])
            return _old(*args, **kwargs)
        setattr(filedialog, name, wrap_dialog)
