import telebot,threading

class bot:
	def __init__(self, data, token):
		self.bot = telebot.TeleBot(token=token,threaded=False)

		@self.bot.message_handler(content_types=["new_chat_members"])
		def new_member(message):
			if message.json["new_chat_member"]["username"].lower() == "doscom_hacktoberfest_bot":
				bot.send_message(message.chat.id, "Hai Semuanya...")
			else:
				bot.send_message(message.chat.id, f"Halo Selamat Bergabung {message.json['new_chat_member']['first_name']}")

		@self.bot.message_handler(commands="start")
		def welcome(message):
			teks = "Selamat datang di Hacktoberfest 2021"
			self.bot.send_message(message.chat.id,teks)

		@self.bot.message_handler(commands="help")
		def help(message):
			teks = "List kontribusi teman-teman :\n"
			for x in data:
				teks+=f"\n/{x}"
			teks += "\n\nContoh : /commands -course -api"
			self.bot.send_message(message.chat.id,teks)

		@self.bot.message_handler(commands=data.keys())
		def list_data(message):
			command = message.text.replace("/","")
			json = data[command.split(" ")[0]].data
			json_sorted = dict(sorted(json.items(), key=lambda item: item[0], reverse=True))
			for x in json_sorted:
				if ("-course" in command.lower()) and ("course" in x.lower()):
					self.bot.send_message(message.chat.id,json[x],parse_mode="HTML",disable_web_page_preview=True)
				if ("-api" in command.lower()) and ("api" in x.lower()):
					self.bot.send_message(message.chat.id,json[x],parse_mode="HTML",disable_web_page_preview=True)
				if ("-course" not in command.lower()) and ("-api" not in command.lower()) and ("course" not in x.lower()) and ("api" not in x.lower()):
					if "photo" in x.lower():
						try:
							self.bot.send_photo(message.chat.id, json[x])
						except Exception as e:
							self.bot.send_message(message.chat.id, "Ada kesalahan pada foto, periksa kembali.")
					else:
						self.bot.send_message(message.chat.id,json[x],parse_mode="HTML",disable_web_page_preview=True)
		
	def base_run(self):
		while True:
			try:
				self.bot.polling()
			except Exception as e:
				file1 = open("App/Bots/logs.txt","a")
				file1.write(str(e)+"\n\n")
				file1.close()
				self.bot.stop_polling()

	def start(self):
	    bot = threading.Thread(target=self.base_run)
	    bot.start()

if __name__ == '__main__':
	print("is not the main program")