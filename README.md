# Assistente Virtual de Valorant

Um chatbot especializado em Valorant que ajuda jogadores a melhorar suas habilidades no jogo, oferecendo análises de composições, estratégias e dicas personalizadas.

## 📋 Sobre o Projeto

Este projeto é um assistente virtual desenvolvido com Flask e a API da OpenAI, especializado em Valorant. O assistente é capaz de fornecer análises detalhadas sobre composições de agentes, estratégias de ataque e defesa, dicas de economia e comunicação em equipe.

## ✨ Funcionalidades

- Análise detalhada de composições de agentes
- Estratégias específicas para ataque e defesa
- Dicas de controle de economia
- Recomendações de comunicação e trabalho em equipe
- Interface web intuitiva e responsiva

## 🛠️ Tecnologias Utilizadas

- **Python** com Flask para o backend
- **HTML/CSS** para a interface do usuário
- **JavaScript** para interatividade
- **API da OpenAI** para processamento de linguagem natural

## 📦 Pré-requisitos

- Python 3.6 ou superior
- pip (gerenciador de pacotes Python)
- Chave de API da OpenAI

## 🚀 Como Instalar

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_DIRETÓRIO]
```

2. Instale as dependências:
```bash
pip install flask openai
```

3. Configure sua chave de API:
Abra o arquivo `app.py` e substitua "SUA API KEY" pela sua chave de API da OpenAI:
```python
client = OpenAI(
    api_key="sua_chave_api_aqui"
)
```

## 💻 Como Usar

1. Inicie o servidor Flask:
```bash
python app.py
```

2. Abra seu navegador e acesse:
```
http://localhost:5000
```

3. Digite suas perguntas sobre Valorant no chat e receba respostas detalhadas do assistente.

## 📁 Estrutura do Projeto

```
├── app.py              # Arquivo principal do servidor Flask
├── templates/
│   └── index.html      # Template da interface do usuário
└── projeto/            # Arquivos de recursos (imagens)
```

## 🔒 Segurança

- Nunca compartilhe sua chave de API da OpenAI
- Mantenha seu código atualizado
- Utilize variáveis de ambiente para armazenar chaves sensíveis
