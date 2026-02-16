import discord
from discord.ext import commands
import aiohttp
import asyncio
import time
import json

# --- CONFIGURAÇÕES ---
TOKEN = '' # TOKEN SELF DISCORD
GEMINI_KEY = '' # TOKEN GEMINI API
CANAL_ID = 00000000000 # ID DO CANAL ONDE É ENVIADO A QUIZ 
ID_LORDBOT = 00000000000 # ID DO USER/BOT QUE ENVIA A QUIZ

GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?key={GEMINI_KEY}"

class QuizBot(commands.Bot):
    async def on_ready(self):
        print(f"\n{'='*40}")
        print(f"✅ BOT OPERACIONAL: {self.user}")
        print(f"📡 DEV BY: AlissonRyanZ")
        print(f"{'='*40}\n")

    async def on_message(self, message):
        if message.channel.id != CANAL_ID or message.author.id == self.user.id:
            return

        if message.author.id == ID_LORDBOT:
            texto_pergunta = ""
            
            if message.embeds:
                for embed in message.embeds:
                    partes = [str(embed.title or ""), str(embed.description or "")]
                    for field in embed.fields:
                        partes.append(str(field.value or ""))
                    texto_pergunta = " ".join(partes).strip()
            else:
                texto_pergunta = message.content.strip()

            if "Rodada #" not in texto_pergunta and "📢" not in texto_pergunta:
                return

            if any(p in texto_pergunta.lower() for p in ["acertou!", "tempo restante", "placar"]):
                return

            print(f"🎯 [QUESTÃO]: {texto_pergunta[:70]}...")
            
            inicio = time.time()
            try:
                payload = {
                    "contents": [{
                        "parts": [{"text": f"Responda ao quiz com APENAS a palavra ou número correto. Pergunta: {texto_pergunta}"}]
                    }],
                    "generationConfig": {
                        "temperature": 0.1,
                        "maxOutputTokens": 10
                    }
                }
                
                async with aiohttp.ClientSession() as session:
                    async with session.post(GEMINI_URL, json=payload) as resp:
                        data = await resp.json()
                        
                        if resp.status == 200:
                            res = data['candidates'][0]['content']['parts'][0]['text'].strip().lower()
                            res = res.split('\n')[0].replace(".", "").replace("*", "").strip()
                            
                            tempo_ia = time.time() - inicio
                            print(f"⏱️ IA Respondeu em {tempo_ia:.2f}s: {res}")
                            
                            if res:
                                await message.channel.send(res)
                                print(f"🚀 [ENVIADO]: {res}")
                        else:
                            print(f"❌ Erro na API (Status {resp.status}): {data}")

            except Exception as e:
                print(f"❌ [ERRO SISTEMA]: {e}")

bot = QuizBot(command_prefix="!", self_bot=True)
bot.run(TOKEN)
