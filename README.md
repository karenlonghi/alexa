# Introdução
Assistentes virtuais são comuns nos dias de hoje. Alexa, Google Home dentre outras tecnologias disponíveis no mercado utilizam deep learning para reconhecer falas e executar ações. A proposta do projeto é criar uma "alexa" mais simples, com o que foi aprendido em aula.

# Desafio
O desafio proposto pelo professor da matéria de Deep Learning, foi de criar uma assistente virtual, que deveria conter no mínimo os seguintes comandos por voz:

1) “Reconhecimento facial”: a máquina só deve iniciar os comendos de voz após reconhecer o rosto cadastrado. No terminal deve imprimir o nome da pessoa reconhecida e a IA deve falar “Boas vindas, (seu nome)".

2) “Cadastrar evento na agenda”: quando a máquina receber este comando, deverá responder: “Ok, qual evento devo cadastrar?” (ou outra resposta) e na sequência ficará aguardando a resposta. Quando você responder, o algoritmo deverá transcrever sua fala em texto e gravar em um arquivo (.txt) no seu computador (HD, SSD etc.).

3) “Ler agenda”: a máquina deverá abrir a agenda (arquivo .txt) e ler todos os eventos cadastrados.
   
4) “Reconhecimento de objetos”: A IA deve reconhecer pelo menos dois objetos pela WEBCAM e falar o que ela reconheceu.

# Desenvolvimento
Nesse projeto, foram utilizadas as bibliotecaa opencv, tensorflow
Esse arquivo fará a captura das fotos do seu rosto para poder iniciar a Alexa.
