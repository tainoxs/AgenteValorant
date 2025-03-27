from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key="SUA API KEY"
)

lista_mensagens = [
    {
        "role": "system",
        "content": "Você é um especialista em Valorant, focado em ajudar jogadores a melhorar suas habilidades. "
                   "Ao analisar composições, sempre estruture sua resposta no seguinte formato:\n\n"
                   "## Análise da Composição\n"
                   "[Lista dos agentes com suas características principais em tópicos com **negrito**]\n\n"
                   "## Estratégias no Mapa\n"
                   "### Ataque\n"
                   "[Estratégias ofensivas em tópicos numerados]\n\n"
                   "### Defesa\n"
                   "[Estratégias defensivas em tópicos numerados]\n\n"
                   "## Controle de Economia\n"
                   "[Dicas sobre gerenciamento de créditos e compras]\n\n"
                   "## Comunicação e Trabalho em Equipe\n"
                   "[Dicas sobre callouts e coordenação]\n\n"
                   "Use **negrito** para destacar nomes de agentes e conceitos importantes. "
                   "Mantenha uma linguagem técnica mas acessível, e sempre incentive o trabalho em equipe."
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json['message']
    
    lista_mensagens.append({"role": "user", "content": user_message})
    
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=lista_mensagens
    )
    
    response_content = resposta.choices[0].message.content
    lista_mensagens.append({"role": "assistant", "content": response_content})
    
    return jsonify({"response": response_content})

if __name__ == '__main__':
    app.run(debug=True)