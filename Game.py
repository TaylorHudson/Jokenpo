from random import randint
from sys import exit
import os
from time import sleep

class Game:
    def __init__(self,jogador:str):
        self.opçoes_jogador = ["pedra","Pedra","Papel","papel","Tesoura","tesoura"]
        self.opcoes_pc = ["Pedra","Papel", "Tesoura"]
        self.opçoes_continuar = [1,0]
        self.jogador = jogador

    def run(self):
        print("-"*18 , "Jokenpô","-"*18)
        self.jogada_jogador1()

    def jogada_jogador1(self):
        self.escolha = input(f"\n{self.jogador} escolha Pedra, Papel ou Tesoura: ").capitalize().strip()

        if self.escolha in self.opçoes_jogador: 
            if self.escolha == "Pedra":
                escolha_jogador = self.escolha
            elif self.escolha == "Papel":
                escolha_jogador = self.escolha
            elif self.escolha == "Tesoura":
                escolha_jogador = self.escolha

            escolha_pc = self.jogada_pc()
            if escolha_pc == escolha_jogador:
                print("Empate")
                self.jogarNovamente()

            elif escolha_pc == "Tesoura" and escolha_jogador == "Papel"\
            or escolha_pc == "Papel" and escolha_jogador == "Pedra"\
            or escolha_pc == "Pedra" and escolha_jogador == "Tesoura":
                print("Derrota")
                print(f"Você escolheu {escolha_jogador} e seu adversário {escolha_pc}")
                self.jogarNovamente()

            elif escolha_jogador == "Tesoura" and escolha_pc == "Papel"\
            or escolha_jogador == "Papel" and escolha_pc == "Pedra"\
            or escolha_jogador == "Pedra" and escolha_pc == "Tesoura":
                print("Vitoria")
                print(f"Você escolheu {escolha_jogador} e o seu adversário {escolha_pc}")
                self.jogarNovamente()
        else:
            os.system('cls')
            print("Erro, opção inválida")
            self.jogada_jogador1()

    def jogada_pc(self):
        chance = randint(0,2)
        if chance == 0:
            escolha_comp = self.opcoes_pc[0]
        if chance == 1:
            escolha_comp = self.opcoes_pc[1]
        if chance == 2:
            escolha_comp = self.opcoes_pc[2]

        return escolha_comp

    def jogarNovamente(self):
        try:
            jogar_de_novo = int(input("\n1 - Jogar Novamente | 0 - Sair : "))
            while jogar_de_novo not in self.opçoes_continuar:
                self.jogarNovamente()
        except ValueError:
            print("Você digitou algo incorreto.\nEspere alguns segundos e tente novamente. ")
            sleep(2)
            os.system('cls')
            self.jogarNovamente()
        
        if jogar_de_novo == 1:
            os.system('cls')
            self.run()
        else:
            exit()