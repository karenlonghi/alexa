# Introdução
Assistentes virtuais são comuns nos dias de hoje. Alexa, Google Home, dentre outras tecnologias disponíveis no mercado, utilizam deep learning para reconhecer falas e executar ações. A proposta deste projeto é criar uma "Alexa" mais simples, com o que foi aprendido em aula.

# Desafio
O desafio proposto pelo professor da matéria de Deep Learning foi criar uma assistente virtual que deveria conter, no mínimo, os seguintes comandos por voz:

1. **Reconhecimento facial**: a máquina só deve iniciar os comandos de voz após reconhecer o rosto cadastrado. No terminal deve imprimir o nome da pessoa reconhecida e a IA deve falar "Boas vindas, (seu nome)".
2. **Cadastrar evento na agenda**: quando a máquina receber este comando, deverá responder "Ok, qual evento devo cadastrar?" (ou outra resposta) e, na sequência, ficará aguardando a resposta. Quando você responder, o algoritmo deverá transcrever sua fala em texto e gravar em um arquivo (.txt) no seu computador (HD, SSD etc.).
3. **Ler agenda**: a máquina deverá abrir a agenda (arquivo .txt) e ler todos os eventos cadastrados.
4. **Reconhecimento de objetos**: a IA deve reconhecer pelo menos dois objetos pela webcam e falar o que reconheceu.

# Desenvolvimento
Neste projeto, foram utilizadas as bibliotecas OpenCV, TensorFlow, cvlib (YOLOv3), SpeechRecognition, pyttsx3, entre outras. O reconhecimento facial foi implementado com o algoritmo **Eigenfaces**, e o reconhecimento de objetos com o modelo **YOLOv3-tiny**.

# Como usar

### 1. Pré-requisitos
- Baixe e instale o **Python 3.11**.
- Instale as dependências do projeto:
```bash
  pip install -r requirements.txt
```
- Instale a versão correta do OpenCV:
```bash
  pip install opencv-contrib-python==4.10.0.84
```

### 2. Captura das fotos (`capturas.py`)
1. Troque o caminho da pasta `fotos` na **linha 14** para o caminho da sua máquina.
2. Execute o arquivo `capturas.py`.
3. Pressione **`Q`** para tirar cada foto. É necessário capturar **50 fotos** ao todo.

### 3. Treinamento do modelo (`treinamento.py`)
1. Troque o nome na **linha 17 ou 19** para o seu nome.
2. Troque o caminho da pasta `fotos` na **linha 7** para o caminho da sua máquina.
3. Execute o arquivo `treinamento.py`.

### 4. Reconhecimento (`reconhecimento.py`)
1. Troque o nome na **linha 273** para o seu nome.
2. Execute o arquivo `reconhecimento.py`.

### 5. Comandos de voz disponíveis
Após o reconhecimento facial, você pode fazer as seguintes perguntas:
- "Cadastrar evento na agenda"
- "Ler agenda"
- "Ver clima"
- "Apagar agenda"
- "Me conte uma piada"
- "Calculadora"
- "Me conte uma curiosidade"
- "Reconhecer objeto" *(utiliza o YOLOv3, reconhece: pessoa, celular, controle remoto, televisão, livro)*
