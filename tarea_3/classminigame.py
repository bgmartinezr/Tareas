import random
import math
import time

#Clase Vampiro y todas sus habilidades
class Vampire:

    hp = 100
    mp = 25
    status = 'OK'
    active_turn = True #Determina si te toca o le toca al oponente
#Inicializacion del Vampiro
    def __init__(self,
                 name:str,
                 height:float) -> None:
        self.name = name
        self.height = height
#Funcion de tomar daño
    def take_damage(self, x:float) -> None:
        self.hp -= x

#Habilidades de ataque
    def leech_blood(self, target) -> None:
        dmg = random.randint(1,8)
        target.take_damage(dmg)
        self.hp += math.floor(dmg/2)
        print(f'{self.name} te chupa la sangre por {dmg} y se cura {math.floor(dmg/2)} \n')
        self.set_turn_activity(False)

    def hypnosis(self, target) -> None:
        if self.mp >= 5:
            self.mp -= 5
            target.set_status('confusion')
            print(f'{self.name} te ha causado confusion \n')
        else:
            print('Miss \n')
        self.set_turn_activity(False)

    def attack(self,target) -> None:
        if self.status=='confusion':
            dice = random.randint(1,20)
            if dice >=10:
                dmg = random.randint(5,20)
                target.take_damage(dmg)
                print(f'{self.name} golpea a {target.name} por {dmg} de daño \n')
            else:
                print('Miss \n')
        else:
            dmg = random.randint(5,20)
            target.take_damage(dmg)
            print(f'{self.name} golpea a {target.name} por {dmg} de daño')
        self.set_turn_activity(False)

#Funcion que establece el turno
    def set_turn_activity(self, activity) -> None:
        self.active_turn = activity

#Clase de personaje
class Person:

    possible_weapons = ['espada','hacha']
    status = 'OK'
    potions = 2
    active_turn = True #Determina si te toca o le toca al oponente
    safe = False
#Inicializacion del personaje
    def __init__(self, name:str, weapon:str) -> None:
        self.name = name
        if weapon not in self.possible_weapons:
            raise ValueError('El arma debe ser una espada o un hacha \n')
        self.weapon = weapon
        self.atk = 10 if self.weapon=='hacha' else 8
        self.hp = 80 if  self.weapon=='hacha' else 85
#Funcion de tomar daño
    def take_damage(self, x:float) -> None:
        self.hp -= x

    def set_status(self, status:str):
        self.status = status
#Estatus de turno
    def set_turn_activity(self, activity) -> None:
        self.active_turn = activity

#Ataques y hechizos
    def attack(self,target) -> None:
        if self.status=='confusion':
            dice = random.randint(1,20)
            if dice >=10:
                dmg = random.randint(5,20)
                target.take_damage(dmg)
                print(f'{self.name} golpea a {target.name} por {dmg} de daño \n')
            else:
                print('Miss \n')
        else:
            dmg = random.randint(5,20)
            target.take_damage(dmg)
            print(f'{self.name} golpea a {target.name} por {dmg} de daño \n')
        self.set_turn_activity(False)

    def h_fire(self,target) -> None:
        if self.status=='confusion':
            dice = random.randint(1,20)
            if dice >=10:
                dmg = random.randint(5,20)
                target.take_damage(dmg)
                print(f'{self.name} hizo hechizo de fuego a {target.name} por {dmg} de daño')
            else:
                print('Miss')
        else:
            dmg = random.randint(5,20)
            target.take_damage(dmg)
            print(f'{self.name} hizo hechizo de fuego a {target.name} por {dmg} de daño \n')
        self.set_turn_activity(False)

    def h_ice(self,target) -> None:
        if self.status=='confusion':
            dice = random.randint(1,20)
            if dice >=10:
                dmg = random.randint(5,20)
                target.take_damage(dmg)
                print(f'{self.name} hizo hechizo de hielo a {target.name} por {dmg} de daño')
            else:
                print('Miss')
        else:
            dmg = random.randint(5,20)
            target.take_damage(dmg)
            print(f'{self.name} hizo hechizo de hielo a {target.name} por {dmg} de daño \n')
        self.set_turn_activity(False)

    def h_thunder(self,target) -> None:
        if self.status=='confusion':
            dice = random.randint(1,20)
            if dice >=10:
                dmg = random.randint(5,20)
                target.take_damage(dmg)
                print(f'{self.name} hizo hechizo de trueno a {target.name} por {dmg} de daño')
            else:
                print('Miss')
        else:
            dmg = random.randint(5,20)
            target.take_damage(dmg)
            print(f'{self.name} hizo hechizo de trueno a {target.name} por {dmg} de daño \n')
        self.set_turn_activity(False)
#Curacion y escape
    def drink_potion(self) -> None:
        if self.potions >= 0:
            dice1 = random.randint(1,4)
            dice2 = random.randint(1,4)
            heal = dice1 + dice2 + 2
            self.hp += heal
            print(f'Te curas {heal} ahora tu hp es de {self.hp} \n')
            self.set_turn_activity(False)
        else:
            print('Buscas en tu mochila una pocion \n')
            time.sleep(2)
            print('Pierdes tu turno por no saber manejar tu inventario \n')

    def check_inventory(self):
        print(f'tienes {self.potions} pociones \n')

#Tira un dado para ver si puedes escapar
    def escape(self) -> None:
        dice = random.randint(1,20)
        if dice == 20:
            self.safe = True
        else:
            print('No puedes escapar, pelea \n')

#Cambio de turno
def change_turns(player,vampire):
    player.active_turn = not player.active_turn
    vampire.active_turn = not vampire.active_turn

####################MAIN DEL JUEGO###############################3
if __name__ == '__main__':
#Seleccion de nombre y arma
    print('Bienvenido a la aventura \n\n')
    player_name = input('Dime tu nombre: ')
    weapon = None

    while weapon not in ['espada','hacha']:
        print('Puedes usar una espada o un hacha')
        print('Ingresa la opcion que prefieras \n')
        print('1. Espada')
        print('2. Hacha \n')
        weapon_choice = input('ingresa el numero: \n')
        if str(weapon_choice) == '1':
            weapon = 'espada'
        elif str(weapon_choice) == '2':
            weapon = 'hacha'
        else:
            weapon= 'Selecciona un arma valida \n'
#Inicio narrativa
    player = Person(player_name, weapon)
    time.sleep(1)
    print(f'Eres {player.name} y cargas una {player.weapon} \n')
    print('Caminas por la ciudad y ves una figura misteriosa \n')

#Instancia y presentacion random de Vampiro
    vampire_names = ['Dio','Dracula','Alucard','Salinas']
    vampire_heights = [120, 170, 180, 190, 200, 210]
    vampire_name = random.choice(vampire_names)
    vampire_height = random.choice(vampire_heights)

    vampire = Vampire(vampire_name, vampire_height)
    time.sleep(1)
    print(f'Ves una figura a la distancia, parece medir {vampire.height} cm \n')
    time.sleep(3)
    print('Humano, me has despertado de mi largo sueño \n')
    print(f' SOY {vampire.name.upper()} EL VAMPIRO PREPARATE PARA MORIR \n\n\n\n')

#############################################################################

    print(r'''                 /##########\
                              /   \###/    \
                             /     \#/      \
                          /\|               |/\
                          | | \ ==\    /== / | |
                           \|  \<|>\  /<|>/  |/     /|
                    \__     |    -   \  -    |     /#|
                     \#\     |        |      |   /###|
                      \##\   |       \|     |  /#####|
                       \###\  |   _______  | /######|
                        \####\ | / \/ \/ \|/#######|
                        |######\|        |#########|
                        |########\______/##########|
                        |#########\    /##########/
                        |##########\  |#########/\
                        /###########\/########/###\
                    /################\######/########\
                   /##################\###/###########\
                  /###################\#/##############\
                 /####################/#################\
                /###################/####################\ \n\n\n\n''')

#############################################################################



# Inicio de combate
    time.sleep(2)
    print('\n\n')
    print(f'Comienza la batalla {player.name} \n')

    time.sleep(1)
#Define quien inicia
    coin = random.randint(1,2)
    if coin == 1:
        player.set_turn_activity(True)
        vampire.set_turn_activity(False)
    else:
        player.set_turn_activity(False)
        vampire.set_turn_activity(True)

# Checa que ambos sigan con vida o el jugador no haya escapado
    while player.hp > 0 and vampire.hp > 0 and not player.safe:
        while player.active_turn:
            print('/'*80)
            print(f'Tu HP: {player.hp}')
            print(f'HP de tu rival: {vampire.hp}')
            print('/'*80)

#Menu del jugador
            actions = [1,2,3,4,5]
            action = 0
            while action not in actions:
                print('\n')

                print('Elige tu accion')
                print('1. Atacar')
                print('2. Tomar pocion ')
                print('3. Escapar')
                print('4. Checar inventario')
                print('5. Hechizos')

                action = int(input('Que quieres hacer? \n\n\n'))

            if action == 1:
                player.attack(vampire)
            elif action == 2:
                player.drink_potion()
            elif action == 3:
                player.escape()
            elif action == 4:
                player.check_inventory()
            else:
                hechizos = [1,2,3]
                hechizo = 0
                while hechizo not in hechizos:
                    print('\n')

                    print('Elige tu hechizo')
                    print('1. Fuego')
                    print('2. Hielo ')
                    print('3. Trueno')

                    action = int(input('Escoge un hechizo \n\n\n'))

                    if action == 1:
                        player.h_fire(vampire)
                        break
                    elif action == 2:
                        player.h_ice(vampire)
                        break
                    else:
                        player.h_thunder(vampire)
                        break

        while vampire.active_turn:
            print('/'*80)
            print(f'Tu HP: {player.hp}')
            print(f'HP de tu rival: {vampire.hp}')
            print('/'*80)
            print('\n')
            dice = random.randint(1,20)
            if dice <= 12:
                vampire.attack(player)
            elif dice <=17:
                vampire.leech_blood(player)
            else:
                vampire.hypnosis(player)

        vampire.set_turn_activity(not vampire.active_turn)
        player.set_turn_activity(not player.active_turn)

    if vampire.hp <= 0:
        print('Felicidades, has vencido al vampiro \n')
        print('Fanfarrias ♫ \n')
    elif player.safe:
        print('Escapaste del vampiro \n')
    else:
        print('Game Over \n')
