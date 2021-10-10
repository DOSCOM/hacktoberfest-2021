from Global import data
from App import Bots
from Config import *

class run(Bots.bot):
	def __init__(self, data):
		super().__init__(data, token = os.environ['TOKEN'])

if __name__ == '__main__':
	bot = run(data)
	bot.start()