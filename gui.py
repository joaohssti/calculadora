import customtkinter as ctk


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora")
        self.geometry("600x400")
        self.resizable(False, False)

        # frame display e clear
        self.display_frame = ctk.CTkFrame(self)
        self.display_frame.pack(pady=10)
        self.display = ctk.CTkLabel(self.display_frame, text="")
        self.clear_button = ctk.CTkButton(self.display_frame, text="C", command=self.limpar_display)
        self.display.grid(row=0, column=0)
        self.clear_button.grid(row=0, column=1)

        # frame números
        self.botoes = "7894561230"  # ordenados no padrão de calculadora
        self.frame = ctk.CTkFrame(self)
        
        self.frame.pack(pady=20)
        self.criar_botoes_numericos()


    def criar_botoes_numericos(self):
        for i in range(10):
            botao = ctk.CTkButton(self.frame, text=self.botoes[i],
                                  command=lambda num=self.botoes[i]: self.botao_numerico(num))
            botao.grid(row=i // 3, column=i % 3, padx=5, pady=5)

    def limpar_display(self):
        self.display.configure(text="")

    def botao_numerico(self, numero) -> None:
        self.display.configure(text = self.display.cget("text") + numero)
    
if __name__ == "__main__":
    app = App()
    app.mainloop()
