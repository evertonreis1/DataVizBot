

---

# 📊 DataVizBot - Gerador de Gráficos com DeepSeek

## 🚀 Sobre o projeto
Este é um bot para **Discord** que utiliza a API do **DeepSeek** para interpretar comandos do usuário, extrair dados estruturados e gerar **gráficos dinâmicos** com `matplotlib`.

O bot permite que usuários enviem comandos com dados de vendas, estatísticas ou outras informações e recebam um gráfico gerado automaticamente.

**Atenção:** O projeto ainda está em fase de desenvolvimento e pode apresentar alguns erros ou falhas.

---

## 🔧 Tecnologias utilizadas
- **[Discord.py](https://discordpy.readthedocs.io/en/stable/)** - API do Discord para bots
- **[DeepSeek API](https://deepseek.com/)** - IA para conversão de consultas em JSON
- **[Matplotlib](https://matplotlib.org/)** - Geração de gráficos

---

## 📌 Funcionalidades
✅ Responde ao comando `!graph` e gera gráficos automaticamente  
✅ Suporta gráficos de **linha, barras e pizza**  
✅ Analisa consultas textuais e converte para JSON  
✅ Gera gráficos a partir de dados fornecidos pelos usuários  
✅ Envia o gráfico diretamente no chat do Discord  

---

## 📥 Instalação e Configuração
### 1️⃣ Clone o repositório:
```bash
git clone https://github.com/evertonreis1/DataVizBot.git
cd DataVizBot
```

### 2️⃣ Crie e ative um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv  # Criar ambiente virtual
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 3️⃣ Instale as dependências:
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure suas credenciais:
Crie um arquivo **.env** e adicione suas chaves:
```env
DEEPSEEK_API_KEY=sua_api_key
DISCORD_TOKEN=seu_token_do_discord
```

### 5️⃣ Execute o bot:
```bash
python bot.py
```

---

## 🎯 Como Usar
Basta enviar um comando no chat do Discord com o formato:
```bash
!graph vendas de 2023: Jan 1500, Fev 2000, Mar 1800
```
O bot responderá com um gráfico baseado nos dados fornecidos! 🎉


---

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para contribuir! 😃

Se precisar de ajuda, me chame! 🚀

---
