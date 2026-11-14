@echo off
chcp 65001 >nul
title FEFW 简体中文语言包安装器
echo ==========================================
echo   FEFW Save Editor 简体中文外置语言包
echo ==========================================
echo.
echo 请先从官方 v1.3.6 Release 下载并解压 source.zip。
echo 下面输入包含 editor.py 的源码文件夹完整路径。
echo.
set /p TARGET=源码目录：
if "%TARGET%"=="" (
  echo 未输入目录，已取消。
  pause
  exit /b 1
)
py -3 "%~dp0install_zh_cn.py" --target "%TARGET%"
if errorlevel 1 (
  echo.
  echo 安装未完成。请确认已安装 Python 3.10 或更高版本。
  pause
  exit /b 1
)
echo.
echo 安装完成。以后双击源码目录中的“启动简体中文.bat”即可运行。
pause
