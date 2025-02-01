import os
import discord
import json
import re
import requests
import matplotlib.pyplot as plt
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

def query_deepseek(messages):
    """Consulta a API do DeepSeek com mensagens estruturadas"""
    headers = {
        'Authorization': f'Bearer {DEEPSEEK_API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": messages,
        "temperature": 0.3
    }
    
    try:
        response = requests.post(
            'https://api.deepseek.com/v1/chat/completions',
            headers=headers,
            json=data
        )
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        return f"Erro na API: {str(e)}"

def generate_chart(data):
    """Gera um gráfico com base nos dados estruturados"""
    plt.figure(figsize=(10, 6))
    
    chart_type = data.get('chart_type', 'line')
    x = data.get('x_data', [])
    y = data.get('y_data', [])
    
    try:
        if chart_type == 'line':
            plt.plot(x, y, marker='o', color='b')
        elif chart_type == 'bar':
            plt.bar(x, y, color='g')
        elif chart_type == 'pie':
            plt.pie(y, labels=x, autopct='%1.1f%%')
        else:
            raise ValueError("Tipo de gráfico não suportado")
            
        plt.title(data.get('title', 'Gráfico Gerado pelo DeepSeek'))
        plt.xlabel(data.get('x_label', 'Eixo X'))
        plt.ylabel(data.get('y_label', 'Eixo Y'))
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('chart.png')
        plt.close()
        return True
    except Exception as e:
        plt.close()
        raise e

@bot.command(name='graph')
async def graph(ctx, *, query: str):
    """Gera um gráfico com base nos dados (Ex: !graph vendas de 2023: Jan 1500, Fev 2000, Mar 1800)"""
    system_msg = (
        "Converta a consulta em JSON com: chart_type (line/bar/pie), "
        "x_data (lista), y_data (lista), title, x_label, y_label. "
        "Exemplo: {\"chart_type\": \"bar\", \"x_data\": [\"Jan\", \"Fev\", \"Mar\"], "
        "\"y_data\": [1500, 2000, 1800], \"title\": \"Vendas 2023\"}"
    )
    
    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": query}
    ]
    
    async with ctx.typing():
        response = query_deepseek(messages)
        
        # Extrai JSON da resposta
        json_match = re.search(r'```json\s*(.*?)\s*```', response, re.DOTALL)
        if json_match:
            chart_data = json_match.group(1)
        else:
            chart_data = response
        
        try:
            data = json.loads(chart_data)
            if generate_chart(data):
                await ctx.send(
                    content=f"**Gráfico gerado para:** {query}",
                    file=discord.File('chart.png')
                )
        except Exception as e:
            await ctx.send(f"Erro ao gerar gráfico: {str(e)}")

@bot.event
async def on_ready():
    print(f'Bot {bot.user.name} pronto!')

if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)