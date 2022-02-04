import requests

class Electric:
    def electric(self):
        ## Pickchu
        ### Type
        response = requests.get('https://pokeapi.co/api/v2/type/13/')
        type = response.json()
        print('\nType: ' + type['name'])
        ### Name
        response = requests.get('https://pokeapi.co/api/v2/pokemon-species/25/')
        species = response.json()
        print('Species: ' + species['name'])
        ### Hp
        response = requests.get('https://pokeapi.co/api/v2/stat/1/')
        stat = response.json()
        print(stat['name'] + ': 35')
        ### Attack
        response = requests.get('https://pokeapi.co/api/v2/stat/2/')
        stat = response.json()
        print(stat['name'] + ': 55')
        ### Defense
        response = requests.get('https://pokeapi.co/api/v2/stat/3/')
        stat = response.json()
        print(stat['name'] + ': 40')
        ### Special Attack
        response = requests.get('https://pokeapi.co/api/v2/stat/4/')
        stat = response.json()
        print(stat['name'] + ': 50')
        ### Special Defense
        response = requests.get('https://pokeapi.co/api/v2/stat/5/')
        stat = response.json()
        print(stat['name'] + ': 50')
        ### Speed
        response = requests.get('https://pokeapi.co/api/v2/stat/6/')
        stat = response.json()
        print(stat['name'] + ': 90' + '\n')


class Rock:
    def rock(self):
        ## Onix
        ### Type
        response = requests.get('https://pokeapi.co/api/v2/type/6/')
        type = response.json()
        print('\nType: ' + type['name'])
        ### Name
        response = requests.get('https://pokeapi.co/api/v2/pokemon-species/95/')
        species = response.json()
        print('Species: ' + species['name'])
        ### Hp
        response = requests.get('https://pokeapi.co/api/v2/stat/1/')
        stat = response.json()
        print(stat['name'] + ': 35')
        ### Attack
        response = requests.get('https://pokeapi.co/api/v2/stat/2/')
        stat = response.json()
        print(stat['name'] + ': 45')
        ### Defense
        response = requests.get('https://pokeapi.co/api/v2/stat/3/')
        stat = response.json()
        print(stat['name'] + ': 160')
        ### Special Attack
        response = requests.get('https://pokeapi.co/api/v2/stat/4/')
        stat = response.json()
        print(stat['name'] + ': 30')
        ### Special Defense
        response = requests.get('https://pokeapi.co/api/v2/stat/5/')
        stat = response.json()
        print(stat['name'] + ': 45')
        ### Speed
        response = requests.get('https://pokeapi.co/api/v2/stat/6/')
        stat = response.json()
        print(stat['name'] + ': 70' + '\n')


class Fire:
    def fire(self):
        ## Charmander
        ### Type
        response = requests.get('https://pokeapi.co/api/v2/type/10/')
        type = response.json()
        print('\nType: ' + type['name'])
        ### Name
        response = requests.get('https://pokeapi.co/api/v2/pokemon-species/4/')
        species = response.json()
        print('Species: ' + species['name'])
        ### Hp
        response = requests.get('https://pokeapi.co/api/v2/stat/1/')
        stat = response.json()
        print(stat['name'] + ': 39')
        ### Attack
        response = requests.get('https://pokeapi.co/api/v2/stat/2/')
        stat = response.json()
        print(stat['name'] + ': 52')
        ### Defense
        response = requests.get('https://pokeapi.co/api/v2/stat/3/')
        stat = response.json()
        print(stat['name'] + ': 43')
        ### Special Attack
        response = requests.get('https://pokeapi.co/api/v2/stat/4/')
        stat = response.json()
        print(stat['name'] + ': 60')
        ### Special Defense
        response = requests.get('https://pokeapi.co/api/v2/stat/5/')
        stat = response.json()
        print(stat['name'] + ': 50')
        ### Speed
        response = requests.get('https://pokeapi.co/api/v2/stat/6/')
        stat = response.json()
        print(stat['name'] + ': 65' + '\n')


class Water:
    def water(self):
        ## Squirtle
        ### Type
        response = requests.get('https://pokeapi.co/api/v2/type/11/')
        type = response.json()
        print('\nType: ' + type['name'])
        ### Name
        response = requests.get('https://pokeapi.co/api/v2/pokemon-species/7/')
        species = response.json()
        print('Species: ' + species['name'])
        ### Hp
        response = requests.get('https://pokeapi.co/api/v2/stat/1/')
        stat = response.json()
        print(stat['name'] + ': 44')
        ### Attack
        response = requests.get('https://pokeapi.co/api/v2/stat/2/')
        stat = response.json()
        print(stat['name'] + ': 48')
        ### Defense
        response = requests.get('https://pokeapi.co/api/v2/stat/3/')
        stat = response.json()
        print(stat['name'] + ': 65')
        ### Special Attack
        response = requests.get('https://pokeapi.co/api/v2/stat/4/')
        stat = response.json()
        print(stat['name'] + ': 50')
        ### Special Defense
        response = requests.get('https://pokeapi.co/api/v2/stat/5/')
        stat = response.json()
        print(stat['name'] + ': 64')
        ### Speed
        response = requests.get('https://pokeapi.co/api/v2/stat/6/')
        stat = response.json()
        print(stat['name'] + ': 43' + '\n')


class Grass:
    def grass(self):
        ## bulbasaur
        ### Type
        response = requests.get('https://pokeapi.co/api/v2/type/12/')
        type = response.json()
        print('\nType: ' + type['name'])
        ### Name
        response = requests.get('https://pokeapi.co/api/v2/pokemon-species/1/')
        species = response.json()
        print('Species: ' + species['name'])
        ### Hp
        response = requests.get('https://pokeapi.co/api/v2/stat/1/')
        stat = response.json()
        print(stat['name'] + ': 45')
        ### Attack
        response = requests.get('https://pokeapi.co/api/v2/stat/2/')
        stat = response.json()
        print(stat['name'] + ': 49')
        ### Defense
        response = requests.get('https://pokeapi.co/api/v2/stat/3/')
        stat = response.json()
        print(stat['name'] + ': 49')
        ### Special Attack
        response = requests.get('https://pokeapi.co/api/v2/stat/4/')
        stat = response.json()
        print(stat['name'] + ': 65')
        ### Special Defense
        response = requests.get('https://pokeapi.co/api/v2/stat/5/')
        stat = response.json()
        print(stat['name'] + ': 65')
        ### Speed
        response = requests.get('https://pokeapi.co/api/v2/stat/6/')
        stat = response.json()
        print(stat['name'] + ': 45' + '\n')

class PokemonAPI(Electric, Rock, Fire, Water, Grass):
    def start(self):
        looping = 0
        while looping != 1:
            user_input = input('\n[electric/rock/fire/water/grass] > ')
            if user_input == 'electric':
                looping += 1
                x.electric()
            elif user_input == 'rock':
                looping += 1
                x.rock()
            elif user_input == 'fire':
                looping += 1
                x.fire()
            elif user_input == 'water':
                looping += 1
                x.water()
            elif user_input == 'grass':
                looping += 1
                x.grass()
            else:
                print('undefined')

x = PokemonAPI()
x.start()
