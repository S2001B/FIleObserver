import random

class Speaker:
    def speak(self, speach: str) -> str:
        return speach
    
class Mover:
    def move(self, x: float=1, y: float=2) -> str:
        return f"Moving X coordinates:{x} | Y coordinates: {y}"
    
class Robot:
    def __init__(self, speak: Speaker, move: Mover):
        self.speaker = speak
        self.mover = move 
    
    def operate(self):
        return "\n".join([self.speaker.speak("Hola Como estas, mi Robota"), 
                       self.mover.move(random.uniform(0, 100), random.uniform(0, 100))])

speaker = Speaker()
mover = Mover()
bot = Robot(speaker, mover)
print(bot.operate())