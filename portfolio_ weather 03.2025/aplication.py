import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from tkinter import *
from tkinter import messagebox

#Criando interface gráfica com tkinter
class aplicacao:
    def __init__(self):    
        self.layout = Tk()
        self.layout.title("Previsão do tempo")
        self.layout.geometry("400x150")
        self.tela = Frame(self.layout)

        self.login = Label(self.tela, text="Clique para realizar a Previsao do tempo:")
        self.login.place(x=10, y=10)
        self.botao = Button(self.tela, text="Buscar previsão", command=self.buscar_previsao)

        self.tela.pack()
        self.login.pack()
        self.botao.pack()

        mainloop()

    def buscar_previsao(self):
        try:
            # Configurando o driver do Selenium
            driver = webdriver.Chrome()

            # URL do site de previsão do tempo
            driver.get("https://www.google.com/search?q=clima&oq=clima&gs_lcrp=EgZjaHJvbWUyBggAEEUYPDIGCAEQRRg7MgYIAhBFGDkyBggDEEUYPdIBCDI3MzRqMGo0qAIAsAIB&sourceid=chrome&ie=UTF-8") 

            # Aguardando o carregamento da temperatura
            try:
                temperatura = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "wob_tm"))
                ).text
                print(f"Temperatura capturada: {temperatura}")
            except Exception as e:
                raise Exception(f"Erro ao capturar a temperatura: {e}")

           # Aguardando o carregamento da umidade
            try:
                umidade = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.ID, "wob_hm"))
                ).text
                print(f"Umidade capturada: {umidade}")
            except Exception as e:
                raise Exception(f"Erro ao capturar a umidade: {e}")
            
            # Aguardando o carregamento da Horário
            try:
                horario = WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.ID, "wob_dts"))
                ).text
                print(f"Umidade capturada: {umidade}")
            except Exception as e:
                raise Exception(f"Erro ao capturar a umidade: {e}")


            # Salvando os dados em um arquivo CSV
            with open("previsao_tempo.csv", mode="w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["Horário","Temperatura", "Umidade"])
                writer.writerow([horario, temperatura, umidade])

            # Exibindo mensagem de sucesso
            messagebox.showinfo("Sucesso", "Previsão do tempo salva com sucesso!")
            driver.quit()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar previsão: {e}") 

            
        finally:
            driver.quit()  

tl = aplicacao()
