import random
from django.shortcuts import render


def index(request):

    previsoes = {

        "amor": [

            "Uma conexão sincera pode surgir quando você menos esperar.",

            "Seu coração encontrará paz e reciprocidade.",

            "O amor florescerá em momentos simples.",

            "Uma nova fase amorosa está se aproximando.",

            "Alguém especial poderá cruzar seu caminho em breve.",

            "Uma conversa inesperada despertará sentimentos profundos.",

            "O universo prepara encontros cheios de significado.",

            "Seu brilho emocional atrairá pessoas verdadeiras.",

            "Pequenos gestos revelarão grandes sentimentos.",

            "Uma relação antiga poderá ganhar novos rumos.",

            "A energia do amor estará mais forte nos próximos dias.",

            "Seu coração encontrará respostas que procura há tempos."

        ],

        "profissional": [

            "Seu esforço será reconhecido em breve.",

            "Uma nova oportunidade aparecerá.",

            "Grandes aprendizados estão chegando.",

            "Seu futuro profissional reserva crescimento.",

            "Novos desafios trarão evolução para sua carreira.",

            "Uma ideia simples poderá gerar grandes resultados.",

            "Seu talento chamará atenção das pessoas certas.",

            "Mudanças positivas surgirão no ambiente profissional.",

            "Você está mais próximo do sucesso do que imagina.",

            "A persistência abrirá portas importantes.",

            "Uma nova fase financeira começará a se fortalecer.",

            "Seu conhecimento será valorizado em breve."

        ],

        "pessoal": [

            "Você está evoluindo mais do que imagina.",

            "Boas energias cercam seus próximos dias.",

            "Seu futuro reserva tranquilidade e crescimento.",

            "A paz que você procura está mais próxima.",

            "Momentos de clareza ajudarão em decisões importantes.",

            "Você descobrirá forças que ainda não conhecia.",

            "Seu caminho será iluminado por boas escolhas.",

            "Uma fase de renovação emocional está começando.",

            "Confie mais na sua intuição.",

            "A felicidade estará presente nas pequenas conquistas.",

            "Seu equilíbrio interior ficará mais forte.",

            "O universo está alinhando novas oportunidades para você."

        ]
    }

    mensagem = ""

    if request.method == "POST":

        categoria = request.POST.get("categoria")

        if categoria in previsoes:
            mensagem = random.choice(previsoes[categoria])

    return render(request, "index.html", {
        "mensagem": mensagem
    })