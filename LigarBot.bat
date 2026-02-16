@echo off
title ARQuizMaster - Operacional
cls
echo ==========================================
echo    INICIANDO AMBIENTE VIRTUAL (VENV)
echo ==========================================
:: Garante que as dependencias estao instaladas
call .\venv\Scripts\activate
echo Instalando/Atualizando dependencias...
pip install -q discord.py-self aiohttp

echo ==========================================
echo          LIGANDO O BOT DE QUIZ
echo ==========================================
:: Executa o bot usando o python do venv
.\venv\Scripts\python.exe bot.py
pause
