from random import randint
import requests
from datetime import datetime
from datetime import datetime, timedelta


class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer,hp,power):
        self.hp = randint(50, 70)
        self.power = randint(5,10)

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.last_feed_time = self
        
        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    
    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}"

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    def attack(self,enemy):
        if isinstance(enemy,Wizard):
            chance = randint(1,5)
            if chance ==1:
                return "Покемон-волшебник применил щит в сражении"
            if enemy.hp > self.power:
                enemy.hp -= self.power
                return f"""Сражение @{self.pokemon_trainer} над @{enemy.pokemon_trainer}
                Здоровье @{enemy.pokemon_trainer} теперь {enemy.hp}"""
            else:
                enemy.hp = 0
                return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}!"
            
    def feed(self,feed_interval=20,hp_inserease=20):
        return super().feed(feed_interval,hp_inserease)
    
    
    

class Wizard(Pokemon):
    def feed(self,feed_interval=20,hp_increase=20):
        return super().feed(feed_interval,hp_increase)
    
class Fighter(Pokemon):
    def attack(self,enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().atatck(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-аттаку силой: {super_power}"
    
    def info(self):
        return "У тебя покемон-боец \n\n"+ super().info()
    

def feed(self, feed_interval = 20, hp_increase = 20 ):
    current_time = datetime.current()  
    delta_time = timedelta(hours=feed_interval)  
    if (current_time - self.last_feed_time) > delta_time:
        self.hp += hp_increase
        self.last_feed_time = current_time
        return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
    else:
        return f"Следующее время кормления покемона: {current_time+delta_time}"
    
    
    
    
    
    
    
    
    