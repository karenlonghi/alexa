# Introdução
Assistentes virtuais são comuns nos dias de hoje. Alexa, Google Home, dentre outras tecnologias disponíveis no mercado, utilizam deep learning para reconhecer falas e executar ações. A proposta deste projeto é criar uma "Alexa" mais simples, com o que foi aprendido em aula.

# Desafio
O desafio proposto pelo professor da matéria de Deep Learning foi criar uma assistente virtual que deveria conter, no mínimo, os seguintes comandos por voz:

1. **Reconhecimento facial**: a máquina só deve iniciar os comandos de voz após reconhecer o rosto cadastrado. No terminal deve imprimir o nome da pessoa reconhecida e a IA deve falar "Boas vindas, (seu nome)".
2. **Cadastrar evento na agenda**: quando a máquina receber este comando, deverá responder "Ok, qual evento devo cadastrar?" (ou outra resposta) e, na sequência, ficará aguardando a resposta. Quando você responder, o algoritmo deverá transcrever sua fala em texto e gravar em um arquivo (.txt) no seu computador (HD, SSD etc.).
3. **Ler agenda**: a máquina deverá abrir a agenda (arquivo .txt) e ler todos os eventos cadastrados.
4. **Reconhecimento de objetos**: a IA deve reconhecer pelo menos dois objetos pela webcam e falar o que reconheceu.

# Desenvolvimento

O projeto foi dividido em três etapas principais, cada uma implementada em um script separado:

### 1. Captura de imagens (`capturas.py`)
Utiliza o **OpenCV** com o classificador **Haar Cascade** (`haarcascade_frontalface_default.xml`) para detectar rostos em tempo real pela webcam. A cada captura válida, a imagem do rosto é convertida para escala de cinza, redimensionada para 220x220 pixels e salva em disco, formando o dataset de treinamento (50 fotos por pessoa).

### 2. Treinamento do modelo (`treinamento.py`)
Lê todas as imagens salvas na pasta de fotos, converte cada uma para escala de cinza e associa um rótulo numérico a cada pessoa com base no nome do arquivo (ex: `kaue_1.jpg` → rótulo `1`, `karen_1.jpg` → rótulo `2`). Com esse conjunto de imagens e rótulos, o modelo é treinado usando o algoritmo **Eigenfaces** (`cv2.face.EigenFaceRecognizer_create()`), que aplica **PCA (Análise de Componentes Principais)** para extrair as características mais relevantes dos rostos e reduzir a dimensionalidade das imagens. O modelo treinado é salvo em um arquivo `.yml` (`classificadoreigen.yml`), que é carregado posteriormente pelo script de reconhecimento.

### 3. Reconhecimento e interação (`reconhecimento.py`)
Este é o script principal, que integra todas as funcionalidades da assistente:

- **Reconhecimento facial**: carrega o modelo `.yml` treinado e, a cada frame capturado pela webcam, detecta rostos e usa `reconhecedor_face.predict()` para identificar a pessoa e o nível de confiança da predição. Se o rosto corresponder a um dos rótulos cadastrados, a IA dá as boas-vindas por voz (via **pyttsx3**) e libera os comandos de voz; caso contrário, o rosto é marcado como "Desconhecido" e os comandos ficam bloqueados.
- **Reconhecimento de voz**: usa a biblioteca **SpeechRecognition** com o motor do Google (`recognize_google`) para transcrever a fala do usuário em texto, que é comparado a comandos pré-definidos (strings exatas) para acionar cada funcionalidade.
- **Síntese de voz**: as respostas da assistente são faladas usando **pyttsx3**, configurado com a voz em português (Maria, via SAPI5 do Windows).
- **Agenda**: os comandos de cadastro, leitura e exclusão de eventos manipulam um arquivo de texto local (`agenda.txt`), onde cada evento é gravado como uma nova entrada.
- **Clima**: usa a biblioteca **geocoder** para obter a localização aproximada do usuário via IP, e consulta a **API do OpenWeatherMap** para retornar temperatura e condição climática atual.
- **Calculadora por voz**: interpreta uma frase falada no formato `número operador número` (ex: "10 + 5") e retorna o resultado da operação.
- **Piadas e curiosidades**: seleciona aleatoriamente uma frase de listas pré-definidas no código.
- **Reconhecimento de objetos**: usa a biblioteca **cvlib**, com o modelo **YOLOv3-tiny**, para detectar objetos comuns (pessoa, celular, controle remoto, televisão, livro) em tempo real pela webcam, desenhando as caixas delimitadoras na tela e falando os objetos identificados.

### Bibliotecas principais utilizadas
- `opencv-contrib-python` — captura de vídeo, detecção facial (Haar Cascade) e reconhecimento facial (Eigenfaces)
- `cvlib` — reconhecimento de objetos com YOLOv3-tiny
- `speech_recognition` — transcrição de voz para texto
- `pyttsx3` — síntese de voz (texto para fala)
- `requests` + `geocoder` — consulta de clima via API externa e geolocalização por IP

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
