# -*- coding: utf-8 -*-
"""Install/uninstall the external zh-CN pack into an official source distribution."""
from __future__ import annotations
import argparse
import shutil
from pathlib import Path

MARKER = "# FEFW_ZH_CN_EXTERNAL_PACK_BOOTSTRAP"

def install(target: Path, pack_dir: Path):
    editor = target / "editor.py"
    if not editor.is_file():
        raise SystemExit("找不到 editor.py。请先解压官方 source.zip，并将目录作为 --target。")
    if not (target / "fefw_layer.py").is_file() or not (target / "fefw_save.py").is_file():
        raise SystemExit("目标目录不像完整的 FEFW Save Editor 源码目录。")
    source = editor.read_text(encoding="utf-8")
    if MARKER in source:
        print("检测到已安装外置汉化包，无需重复安装。")
        return
    anchor = "sys.path.insert(0, HERE)"
    if anchor not in source:
        raise SystemExit("当前官方源码的启动结构与安装器不兼容；未修改任何文件。")
    pack_target = target / "zh_CN"
    if pack_target.exists():
        raise SystemExit("目标目录已存在 zh_CN 文件夹。请先备份或卸载旧汉化包。")
    shutil.copytree(pack_dir, pack_target)
    patch = (
        anchor + "\n"
        + "sys.path.insert(0, os.path.join(HERE, 'zh_CN'))\n"
        + MARKER + "\n"
        + "from bootstrap import install as _install_external_zh_cn\n"
        + "_install_external_zh_cn()"
    )
    backup = editor.with_suffix(".py.zhcn-backup")
    shutil.copy2(editor, backup)
    editor.write_text(source.replace(anchor, patch, 1), encoding="utf-8")
    print("安装完成。备份文件：", backup.name)
    launcher = target / "启动简体中文.bat"
    launcher.write_text(
        '@echo off\r\n'
        'cd /d "%~dp0"\r\n'
        'py -3 -c "import zstandard" >nul 2>&1\r\n'
        'if errorlevel 1 (\r\n'
        '  echo 正在安装编辑器所需依赖 zstandard...\r\n'
        '  py -3 -m pip install --only-binary=:all: -r requirements.txt\r\n'
        '  if errorlevel 1 (echo 依赖安装失败，请检查 Python 和网络。 & pause & exit /b 1)\r\n'
        ')\r\n'
        'py -3 editor.py\r\n'
        'if errorlevel 1 pause\r\n',
        encoding="utf-8"
    )
    print("已创建启动简体中文.bat；双击即可启动。")

def uninstall(target: Path):
    editor = target / "editor.py"
    backup = editor.with_suffix(".py.zhcn-backup")
    if not editor.is_file() or not backup.is_file():
        raise SystemExit("未找到安装备份，无法自动卸载。")
    shutil.copy2(backup, editor)
    backup.unlink()
    shutil.rmtree(target / "zh_CN", ignore_errors=True)
    (target / "启动简体中文.bat").unlink(missing_ok=True)
    print("外置汉化包已卸载，官方源码已恢复。")

def main():
    parser = argparse.ArgumentParser(description="FEFW Save Editor 简体中文外置语言包安装器")
    parser.add_argument("--target", required=True, help="官方 source.zip 解压后的源码目录")
    parser.add_argument("--pack", default=None, help="语言包目录；默认使用安装器旁边的 zh_CN")
    parser.add_argument("--uninstall", action="store_true", help="卸载并恢复备份")
    args = parser.parse_args()
    target = Path(args.target).expanduser().resolve()
    pack = Path(args.pack).expanduser().resolve() if args.pack else Path(__file__).resolve().parent / "zh_CN"
    if args.uninstall:
        uninstall(target)
    else:
        if not pack.is_dir():
            raise SystemExit("找不到 zh_CN 语言数据目录。")
        install(target, pack)

if __name__ == "__main__":
    main()
