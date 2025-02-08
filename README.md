# Music Player 🎵

Este é um simples reprodutor de música desenvolvido em Python utilizando a biblioteca Tkinter e o tema `ttkthemes`. Ele cria uma interface gráfica minimalista para reprodução de áudio.

## 📌 Tecnologias Utilizadas
- Python
- Tkinter (Interface Gráfica)
- ttk e ttkthemes (Estilização de botões e janelas)

## 📥 Instalação

Certifique-se de ter o Python instalado em seu sistema. Em seguida, instale as dependências necessárias:
```bash
pip install ttkthemes
```

## 🚀 Como Executar

1. Baixe ou clone este repositório.
2. Execute o script Python:
```bash
python music_player.py
```

## 📜 Código Principal

```python
from tkinter import *   # Import tkinter library
from tkinter import ttk
from ttkthemes import ThemedTk

class Player:
    def __init__(self):
        self.window = ThemedTk(theme="black")  # Cria uma janela com tema
        self.window.title("Music Player")
        self.window.resizable(0,0)
        self.window.geometry("300x400+800+300")
        self.window.config(bg="#333333")

        self.btn = ttk.Button(self.window, text="Play")
        self.btn.pack()

        self.window.mainloop()

Player()  # Cria um objeto da classe Player
```

## 📌 Melhorias Futuras
- Adicionar suporte a arquivos de áudio (MP3, WAV, etc.)
- Implementar botões de controle (Play, Pause, Stop)
- Exibir informações sobre a faixa em reprodução
- Melhorar a interface com novos temas e ícones

## 📄 Licença
Este projeto é de código aberto e pode ser modificado livremente.

---
Desenvolvido com ❤️ usando Python e Tkinter.

