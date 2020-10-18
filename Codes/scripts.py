from time import sleep
from pyautogui import press, hotkey
import sys
from jsonpickle import decode, encode
from os import chdir, path, getcwd


class Hero:
    Vida = 100
    Mana= 100
    Stamina = 100

    def __init__(self):
        self.Nome = ""
        self.Raça = ""
        self.Classe = ""
        self.magia = 0
        self.força = 0
        self.inteligência = 0
        self.audacia = 0
        self.bravura = 5
        self.Arkron = False
        self.Arma = ""
        self.Dano = 0
        self.Criado = False

        #Armamentos
    def atualizar_armamento(self):
        if self.Classe == "Arqueiro":
            self.Arma = "Arco Leve"
            self.Dano = 10

        elif self.Classe == "Guerreiro":
            self.Arma = "Machado Leve"
            self.Dano = 10

        elif self.Classe == "Mago":
            self.Arma = "Cajado de Chamas"
            self.Dano = 10

        elif self.Classe == "Assassino":
            self.Arma = "Punhal Serrado"
            self.Dano = 10

    def atualizar_atributos(self):
        if self.Classe == "Arqueiro":
            self.inteligência += 20

        elif self.Classe == "Guerreiro":
            self.força += 20

        elif self.Classe == "Mago":
            self.magia += 20

        elif self.Classe == "Assassino":
            self.audacia += 20

        if self.Raça == "Elfo":
            self.inteligência += 20

        elif self.Raça == "Orc":
            self.força += 20

        elif self.Raça == "Humano":
            self.audacia += 20

        elif self.Raça == "Draconiano":
            self.magia += 20

        elif self.Raça == "Espectro":
            self.magia += 10
            self.inteligência += 10





def iniciar():
    press("F11")
    for c in range(4):
        hotkey("ctrl", "+")
    return


def finalizar():
    press("F11")
    for c in range(4):
        hotkey("ctrl", "-")
    hotkey("ctrl", "z")
    return


def batalha(hero, Poções, inimigo, ataque, vida_inimigo, arma):
    """Batalha(Nome do inimigo, HP por ataque, HP do inimigo, arma do inimigo)"""
    print(f'\n~ {hero.Nome} empunha {hero.Arma} ')
    cont = 1
    sair = False
    while True:
        sleep(3)
        if hero.Vida <= 0:
            print(f"Você foi derrotado pelo {inimigo}...")
            finalizar()
            return
            break
        print("\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
        print(f'\n\n      \033[31m{inimigo}: HP - {vida_inimigo}%\033[33m \n\n\n                              \033[34m{hero.Nome.upper()}: HP- {hero.Vida}%   Stamina- {hero.Stamina}%  Mana - {hero.Mana}%\033[33m\n')
        print("\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰▱")
        while True:
            print("\n1)Atacar\n2)Tomar poção\n3)Fugir")
            ask1 = int(input("\nO que você vai fazer? "))
            if ask1 == 1:
                print("\n▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰ Ataques ▰▱▰▱▰▱▰▱▰▱▰▱▰▱▰")
                print("1)Ataque leve - custa 15 de Stamina e tira 10 de HP")
                print("2)Ataque médio - custa 25 de Stamina e tira 20 de HP")
                print("3)Ataque pesado - custa 35 de Stamina e tira 30 de HP")
                print("4)Ataque mágico - custa 45 de Mana e tira 30 de HP")
                if hero.Arkron == True:
                    print(f"5)Ataque de Arkron - custa 100 de Mana e tira {hero.Dano}")
                ask2 = int(input("\nO que você vai fazer? "))
                if ask2 == 1:
                    if hero.Stamina >= 15:
                        if hero.força >= 30: 
                            vida_inimigo -= 15
                            if hero.audacia >= 30:
                                hero.Stamina -= 10
                            else:
                                hero.Stamina -= 15
                            print(f"\nO {inimigo} perdeu 15 de vida \n")
                            break
                        else:
                            vida_inimigo -= 10
                            if hero.audacia >= 30:
                                hero.Stamina -= 10
                            else:   
                                hero.Stamina -= 15
                            print(f"\nO {inimigo} perdeu 10 de vida \n")
                            break
                    else:
                        print("\nVocê não tem Stamina Suficiente")
                        sleep(2)
                if ask2 == 2:
                    if hero.Stamina >= 25:
                        if hero.força >= 30:
                            vida_inimigo -= 25
                            if hero.audacia >= 30:
                                hero.Stamina -= 20
                            else:
                                hero.Stamina -= 25
                            print(f"\nO {inimigo} perdeu 25 de vida \n")
                            break
                        else:
                            vida_inimigo -= 20
                            if hero.audacia >= 30:
                                hero.Stamina -= 20
                            else:
                                hero.Stamina -= 25
                            print(f"\nO {inimigo} perdeu 20 de vida \n")
                            break
                    else:
                        print("\nVocê não tem Stamina Suficiente")
                        sleep(2)
                if ask2 == 3:
                    if hero.Stamina >= 35:
                        if hero.força >= 30:
                            vida_inimigo -= 35
                            if hero.audacia >= 30:
                                hero.Stamina -= 30
                            else:
                                hero.Stamina -= 35
                            print(f"\nO {inimigo} perdeu 30 de vida \n")
                            break
                        else:
                            vida_inimigo -= 30
                            if hero.audacia >= 30:
                                hero.Stamina -= 30
                            else:
                                hero.Stamina -= 35
                            print(f"\nO {inimigo} perdeu 30 de vida \n")
                            break
                    else:
                        print("\nVocê não tem Stamina Suficiente")
                        sleep(2)
                if ask2 == 4:
                    if hero.Mana >= 40:
                        if hero.magia >= 30:
                            vida_inimigo -= 35
                            print(f"\nO {inimigo} perdeu 35 de vida \n")
                            hero.Mana -= 40
                            break
                        else:
                            vida_inimigo -= 30
                            print(f"\nO {inimigo} perdeu 30 de vida \n")
                            hero.Mana -= 45
                            break
                    else:
                        print("\nVocê não tem Mana Suficiente")
                        sleep(2)

                if ask2 == 5:
                    if hero.Arkron == True:
                        if hero.Mana >= 100:
                            if hero.magia >= 30:
                                vida_inimigo -= hero.Dano + 5
                                print(f"\nO {inimigo} perdeu {hero.Dano + 5} de vida \n")
                                hero.Mana -= 95
                                break
                            else:
                                vida_inimigo -= hero.Dano
                                print(f"\nO {inimigo} perdeu {hero.Dano} de vida \n")
                                hero.Mana -= 100
                                break
                        else:
                            print("\nVocê não tem Mana Suficiente")
                            sleep(2)
                    else:
                        print("Você não tem nenhum armamento de Arkron!")
                else: 
                    print("Opção inválida!")
            if ask1 == 2:
                cont = 1
                print("\n▰▱▰▱▰▱▰▱▰▱▰▱ Poções ▰▱▰▱▰▱▰▱▰▱▰▱")
                for k, i in Poções.items():
                    print(f"{cont})Poção de {k}    Qtd - {i}")
                    cont += 1
                ask2 = int(input("\nQual poção você deseja? "))
                if ask2 == 1:
                    if Poções["Vida"] >= 1:
                        if hero.magia >= 30:
                            hero.Vida += 65
                            print("\nVocê Recuperou 65 de HP")
                            Poções["Vida"] -= 1
                            break
                        else:
                            hero.Vida += 60
                            Poções["Vida"] -= 1
                            print("\nVocê Recuperou 60 de HP")
                            break
                    else:
                        print("\nVocê não tem mais Poções de Vida")
                        break
                if ask2 == 3:
                    if Poções["Stamina"] >= 1:
                        if hero.magia >= 30:
                            hero.Stamina += 65
                            print("\nVocê Recuperou 65 de Stamina")
                            Poções["Stamina"] -= 1
                            break
                        else:
                            hero.Stamina += 60
                            Poções["Stamina"] -= 1
                            print("\nVocê Recuperou 60 de Stamina")
                            break
                    else:
                        print("\nVocê não tem mais Poções de Stamina")
                        break
                if ask2 == 2:
                    if Poções["Magia"] >= 1:
                        if hero.magia >= 30:
                            hero.Mana += 65
                            print("\nVocê Recuperou 65 de Magia")
                            Poções["Magia"] -= 1
                            break
                        else:
                            hero.Mana += 60
                            Poções["Magia"] -= 1
                            print("\nVocê Recuperou 60 de Magia")
                            break
                    else:
                        print("\nVocê não tem mais Poções de Magia")
                        break
                else: 
                    print("Opção inválida!")
            if ask1 == 3:
                print("Você fugiu da batalha...")
                hero.audacia -= 5
                sair = True
                break
            else: 
                print("Opção inválida!")
        if sair == True:
            break
        if hero.Vida == 0:
            print(f"Você foi derrotado pelo {inimigo}...")
            break
            sys.exit()
            return
            
        if vida_inimigo <= 0:
            print(f"\nVocê derrotou o {inimigo}!")
            hero.bravura +=5
            hero.Vida = 100
            hero.Stamina = 100
            hero.Mana = 100
            break
            return
        if vida_inimigo <= 30 and cont == 1:
            cont -= 1
            sleep(2)
            print(f"\no {inimigo} tomou uma poção de vida, e recuperou 40 de HP\n")
            vida_inimigo += 40
        if hero.Vida != 0 and vida_inimigo != 0:
            if hero.inteligência >= 30:
                print(f"\033[31m\nO {inimigo} te atacou com uma {arma}, e tirou {ataque - 5} de HP de você\n\033[33m\n")
                hero.Vida -= ataque - 5
            else:        
                print(f"\033[31m\nO {inimigo} te atacou com uma {arma}, e tirou {ataque} de HP de você\033[33m\n\n")
                hero.Vida -= ataque


def logo():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    logo= "\033[31m      ██████\n     ██       █    █  █████   █████  ██████       █████   ██     ██  ██  █████\n     ██       ██  ██  █    █  ██     ██   █       █    █  ██     ██  ██  ██\n     ██         ██    █████   █████  █████   ███  █████   ██     ██  ██  █████\n\033[34m     ██         ██    █    █  ██     ██  ██       █    █  ██     ██  ██  ██\n      ██████    ██    █████   █████  ██   ██      █████   █████  ██████  █████\n\033[m"
    
    list(logo)

    for c in logo:
        print(f'{c}', end="", flush=True)
        sleep(0.01)
    
    for c in range(13): 
        sleep(0.5)
        print("\n")
    return


def abertura():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    logo = "\033[32m              ██\n            ██  ███    ██████     █     ██   ██████      █████     █       █\n          ██      ██   ██    ██   ██   ██    ██    ██   ██    ██   ██     ██\n         ██    █████   ██   ██    ██  ██     ██   ██    ██   ███   ████   ██\n         ██  ██   ██   █████      ████       █████      ██  █ ██   ██ ██  ██\n         ████     ██   ██  ██     ██  ██     ██  ██     ██ █  ██   ██  ██ ██\n         ██       ██   ██   ██    ██   ██    ██   ██    ███   ██   ██    ██\n         ██       ██   █     ██   █     ██   █     ██    █████     █\n                   █  \n\033[m"
    list(logo)
    for c in logo:
        print(f'{c}', end="", flush=True)
        sleep(0.01)
    
    for c in range(13): 
        sleep(0.5)
        print("\n")
    return


def delay(texto):
    list(texto)
    for c in texto:
        if c == "." or c == "?" or c == "!":
            sleep(0.5) 
        print(f'{c}', end="", flush=True)
        sleep(0.03)


def fim_parte1():
    texto = """\033[32m           

             
                          ██████     █    ██       █     
                         ██               ███     ██     
                         ██         ██    ████   ███     
                         ██████     ██    ██ ██ ██ █     
                         ██         ██    ██  ███  █     
                         ██         ██    ██       █     
                         ██         ██    ██       █     
                         █          █     █        █     


                            █████          ██
                           ██    ██      ██  ███
                           ██     ██    ██     ██
                           ██      ██   ██    ███
                           ██      ██   ██  ██ ██
                           ██     ██    ████   ██
                           ██    ██     ██      █
                           ██████       █       █



              ██████        ██        ██████        ██       ███████      
             ██     ██    ██  ███    ██     ██   ████████  ███     █       
             ██     ██   ██     ██   ██    ██       ██     ██          
             ██   ██     ██    ███   ██   ██        ██     ██     █  
             ██████      ██  ██ ██   ██████         ██     ███████        
             ██          ████   ██   ██   ██        ██     ██           
             ██          ██     ██   ██    ██       ██     ███     █ 
             ██          ██      █   ██     ██      ██      ████████
             █           █           █               █            



                         █         █   █           █
                         ██       ██   ███       ███
                         ██       ██   ████     ████
                         ██       ██   ██ ██   ██ ██
                         ██       ██   ██  ██ ██  ██
                         ██       ██   ██   ███   ██
                          ██     ██    ██         ██
                           ███████     █           █






                           """
    list(texto)
    for c in texto:
        print(f'{c}', end="", flush=True)
        sleep(0.005)

    sleep(7)
    return
    

def iniciar_personagem():
    chdir("..")
    chdir("Saves")
    if path.exists(path.join(getcwd(), "hero.json")):
        ask = input("\033[33mExiste uma Save do personagem, deseja continuar ou recomeçar? ").upper()
        if ask == "CONTINUAR":
            with open("hero.json", "r") as arquivo:
                cont = arquivo.read()
                objeto = decode(cont)
                chdir("..")
                chdir("Codes")
                return objeto
        else: 
            objeto = Hero()
            chdir("..")
            chdir("Codes")
            return objeto
    else:
        objeto = Hero()
        chdir("..")
        chdir("Codes")
        return objeto



def salvar_hero(objeto):
    chdir("..")
    chdir("Saves")
    with open("hero.json", "w") as arquivo:
        cont = encode(objeto)
        arquivo.write(cont)
    chdir("..")
    chdir("Codes")


def iniciar_historia():
    chdir("..")
    chdir("Saves")
    if path.exists(path.join(getcwd(), "save_historia.json")):
        ask = input("\033[33mDeseja continuar a história de onde parou ou recomeçar? ").capitalize()
        if ask == "Continuar":
            with open("save_historia.json", "r") as arquivo:
                cont = arquivo.read()
                lista = decode(cont)
                chdir("..")
                chdir("Codes")
                return lista
        else:
            chdir("..")
            chdir("Codes")
            lista = []
            return lista
    else:
        lista = []
        chdir("..")
        chdir("Codes")
        return lista


def salvar_historia(objeto):
    chdir("..")
    chdir("Saves")
    with open("save_historia.json", "w") as arquivo:
        cont = encode(objeto)
        arquivo.write(cont)
    chdir("..")
    chdir("Codes")