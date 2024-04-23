import os
import tkinter as tk
from tkinter import ttk
from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
from tkinter import messagebox


class EbookApp:
    def __init__(self, master):
        self.master = master
        self.master.title(
            "E-Book: A Jornada do Corinthians na Libertadores de 2012")
        self.master.geometry("800x600")

        # Carregar e exibir imagem
        self.load_image()

        # Botão para reproduzir vídeo
        self.play_button = Button(
            self.master, text="Assistir Entrevista", command=self.play_video)
        self.play_button.pack()

        # Lista de trechos de gols importantes
        self.gols_importantes = [
            {"titulo": "Gol de Emerson contra o Santos",
                "imagem": "sheikgol.jpg"},
            {"titulo": "Gol de Romarinho contra o Boca Juniors",
                "imagem": "romarinho.jpg"},
            {"titulo": "Gol de Paulinho contra o Vasco",
                "imagem": "paulinho.jpg"},
            {"titulo": "Defesa de Cássio contra o Vasco",
                "imagem": "cassio.jpg"},
            # Adicione mais trechos de gols importantes conforme necessário
        ]

        # Configuração inicial
        self.current_chapter = 0
        self.create_widgets()

    def load_image(self):
        # Carregar imagem
        image_path = "capaliberta.jpg"
        image = Image.open(image_path)
        image = image.resize((400, 300), Image.LANCZOS)
        self.img = ImageTk.PhotoImage(image)

        # Exibir imagem em um widget Label
        self.image_label = Label(self.master, image=self.img)
        self.image_label.pack()

    def create_widgets(self):
        # Título e botões de navegação
        self.chapter_label = tk.Label(
            self.master, text="Capítulo 1: Preparação e Expectativas", font=("Arial", 18))
        self.chapter_label.pack(pady=20)

        self.prev_button = ttk.Button(
            self.master, text="Capítulo Anterior", command=self.prev_chapter)
        self.prev_button.pack(side=tk.LEFT, padx=10)

        self.next_button = ttk.Button(
            self.master, text="Próximo Capítulo", command=self.next_chapter)
        self.next_button.pack(side=tk.RIGHT, padx=10)

        # Área de exibição de texto
        self.text_area = tk.Text(self.master, wrap="word", height=20, width=80)
        self.text_area.pack()

        # Exibição de trechos de gols importantes
        self.gol_frame = tk.Frame(self.master)
        self.gol_frame.pack(pady=20)

        # Carrega trechos de gols importantes e comentários sobre a campanha do Corinthians em cada capítulo
        self.load_content()

    def load_content(self):
        # Carrega trechos de gols importantes
        for widget in self.gol_frame.winfo_children():
            widget.destroy()

        if self.current_chapter == 0:
            # Exibir trechos de gols apenas no primeiro capítulo
            for gol in self.gols_importantes:
                img_path = gol["imagem"]
                img = Image.open(img_path)
                img = img.resize((150, 100), Image.LANCZOS)
                img = ImageTk.PhotoImage(img)

                label = ttk.Label(self.gol_frame, text=gol["titulo"])
                label.pack()

                image_label = ttk.Label(self.gol_frame, image=img)
                image_label.image = img
                image_label.pack()

        # Comentários sobre a campanha do Corinthians em cada capítulo
        campanha = [
            "A campanha do Corinthians na Libertadores de 2012 foi histórica para o clube e para os torcedores. O time entrou na competição determinado a conquistar o título que até então lhe escapava. Sob o comando do técnico Tite, o Corinthians demonstrou um futebol sólido e consistente ao longo de toda a jornada.",
            "No capítulo 2 comentamos sobre a campanha do Corinthians na fase de grupos.",
            "No capítulo 3 discutimos as oitavas de final.",
            "No capítulo 4 falamos sobre as quartas de final.",
            "No capítulo 5 abordamos as semifinal.",
            "No capítulo 6 detalhamos a final.",
            "No capítulo 7 analisamos quem foi o artilheiro da equipe, quem deu mais assistências e quem foi o melhor jogador."
        ]

        if self.current_chapter > 0:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, campanha[self.current_chapter - 1])

    def prev_chapter(self):
        if self.current_chapter > 0:
            self.current_chapter -= 1
            self.update_chapter()

    def next_chapter(self):
        # Simula a existência de mais capítulos
        if self.current_chapter < 5:
            self.current_chapter += 1
            self.update_chapter()
        else:
            messagebox.showinfo(
                "Fim do E-book", "Você alcançou o último capítulo!")

    def update_chapter(self):
        # Atualiza o título do capítulo
        self.chapter_label.config(text=f"Capítulo {self.current_chapter + 1}")

        # Atualiza o texto do capítulo (pode adicionar mais texto conforme necessário)
        if self.current_chapter == 0:
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(
                tk.END, "A campanha do Corinthians na Libertadores de 2012 foi histórica para o clube e para os torcedores. O time entrou na competição determinado a conquistar o título que até então lhe escapava. Sob o comando do técnico Tite, o Corinthians demonstrou um futebol sólido e consistente ao longo de toda a jornada.")

        # Carrega trechos de gols importantes e comentários sobre a campanha do Corinthians em cada capítulo
        self.load_content()


def main():
    root = tk.Tk()
    app = EbookApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
