import openai

OPENAI_KEY = "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"


class Dilemma:
	def __init__(self, description, question):
		self.description = description
		self.question = question


class Character:
	def __init__(self, character, description=None, opening_nickname=""):
		self.character = character
		self.description = character if description is None else description
		self.opening = "Hi " + opening_nickname + ", " if opening_nickname != "" else "Hi, "


class Conversation:
	def __init__(self, character: Character):
		self.character = character
		self.session_prompt = "The following is a question to " + character.description + ".\n"
		self.key = OPENAI_KEY

	def get_answer(self, question):
		openai.api_key = self.key
		prompt_text = self.session_prompt + self.character.opening + question
		print("******"+prompt_text+"********")
		response = openai.Completion.create(
			engine="text-davinci-002",
			prompt=prompt_text,
			temperature=0.7,
			max_tokens=50,
			top_p=1,
			frequency_penalty=0,
			presence_penalty=0,
		)
		content = response.choices[0].text
		return content.replace(". ", ".\n")


class AdviceGenerator:
	def __init__(self, characters=None, dilemmas=None):
		self.conversations = [] if characters is None else [Conversation(c) for c in characters]
		self.dilemmas = [] if dilemmas is None else dilemmas

	def add_character(self, character: Character):
		self.conversations.append(Conversation(character))

	def add_dilemma(self, dilemma: Dilemma):
		self.dilemmas.append(dilemma)

	def print_advices(self):
		for dilemma in self.dilemmas:
			print(("#" * 7) + "  ", dilemma.description, ":  " + ("#" * 7) + "\n")
			for conv in self.conversations:
				print(conv.character.character, ":")
				print(conv.get_answer(dilemma.question))
				print("-" * 14)
			print("\n\n")


advGen = AdviceGenerator()

# ------------ add Characters: ------------
advGen.add_character(Character(character="Mom", description="my mother", opening_nickname="mom"))
advGen.add_character(Character(character="Dad", description="my father", opening_nickname="dad"))
advGen.add_character(Character(character="Friend", description="a friend"))
advGen.add_character(Character(character="Bestie", description="my bestie", opening_nickname="bestie"))
advGen.add_character(Character(character="Dude", description="a friend", opening_nickname="dude"))

# ------------ add Dilemmas: --------------
# 1
d = Dilemma(description="Move out of my apartment",
			question="I'm debating if I should move out of my apartment or not."
					 " I love the apartment and the location, but my roommates are annoying and we fight a lot."
					 " what do you think I should do?")
advGen.add_dilemma(d)

# 2
d = Dilemma(description="Go to a concert or study",
			question="I'm debating if I should go to a concert or to stay home to study to my exam this week."
					 " what do you think I should do?")
advGen.add_dilemma(d)

# 3
d = Dilemma(description="Walk home late or take the bus",
			question="I wonder if I should walk home or take the bus."
					 " It’s late to walk out, but a short way home.."
					 " what do you think I should do?")
advGen.add_dilemma(d)

# 4
d = Dilemma(description="Should I report car hitting a parking car",
			question="I saw a car hitting a parking car. I don't know any of them."
					 "should I report it?")
advGen.add_dilemma(d)

# 5
d = Dilemma(description="What to wear tonight",
			question="I'm wondering what I should wear tonight.. what do you think?")
advGen.add_dilemma(d)

# 6
d = Dilemma(description="Break up with my girlfriend",
			question="I've been wondering for a while if I should break up with my girlfriend or not."
					 " what do you think?")
advGen.add_dilemma(d)

# 7
d = Dilemma(description="Cheating in the exam",
			question="I studied so hard to the exam but I know everyone will cheat in it, and the grade is relative."
					 " should I also cheat?")
advGen.add_dilemma(d)

# 8
d = Dilemma(description="Save or spend my money?",
			question="I want to save money for next year, but my best friend are all flying to Mexico this summer.."
					 " do you think I should save money or join them?")
advGen.add_dilemma(d)

# 9
d = Dilemma(description="Caught my friend in a lie",
			question="I Caught my friend in a lie yesterday and I know it will be embarrassing for her if"
					 " I'll talk to her about it.. do you think I should tell her?")
advGen.add_dilemma(d)




advGen.print_advices()