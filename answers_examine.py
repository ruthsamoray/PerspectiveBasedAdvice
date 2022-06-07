import numpy as np
import matplotlib.pyplot as plt

answers = {}

topics = ["Move out from my apartment",
		  "Walk home late or take the bus",
		  "What to wear tonight",
		  "Break up with my girlfriend",
		  "Save or spend my money?"]

answers["Move out from my apartment"] = {
	"Mom": "Hi honey, I think that you should do what makes you happy."
		   "If you are unhappy with your roommates and you are constantly fighting,"
		   " then maybe moving out is the best option. But, if you love your apartment and the location,"
		   " then maybe you can try to work things out with your roommates."
		   "Ultimately, the decision is up to you and what will make you the happiest.",

	"Dad": "I think you should move out."
		   " It's not worth staying in a place where you're constantly fighting with your roommates."
		   " You should find a place that you can enjoy and that won't add stress to your life.",

	"Friend": "You should move out of your apartment."
			  " You don't want to be in a situation where you're constantly fighting with your roommates."
			  " It's not worth it to stay in an apartment that you're not happy with."
}

answers["Walk home late or take the bus"] = {
	"Mom": "If it's late at night and you're alone, I think you should take the bus."
		   "It's always better to err on the side of caution when you're by yourself.",

	"Dad": "If it's late and you're not comfortable walking home alone, then you should take the bus.",

	"Friend": "If you feel comfortable walking home, then I think that would be the best option."
			  "It would be a good way to get some exercise in and you wouldn't have to worry about taking the bus."
}

answers["What to wear tonight"] = {
	"Mom": "Your best bet would be to go with something simple, like a pair of jeans and a nice blouse.",

	"Dad": "I think you should wear the blue shirt and black pants.",

	"Friend": "For a night out, I would recommend a cute dress or a nice blouse with jeans."
			  "If you want to go more casual, a cute top with shorts would be great."
			  "Whatever you choose, make sure you feel confident and comfortable in it!"
}

answers["Break up with my girlfriend"] = {
	"Mom": "There is no easy answer to this question, and it ultimately depends on what is going on in your"
		   " relationship and how you feel about your girlfriend. If you are happy with her and the relationship,"
		   " then there is no need to break up. However, if you are unhappy and feel like the relationship is not"
		   " going anywhere, then breaking up may be the best option. Ultimately, the decision is up to you and"
		   " you need to do what is best for you.",

	"Dad": "Well, it depends."
		   "If you're unhappy with her, then it might be time to move on."
		   "However, if you're still in love with her and you think the relationship has potential,"
		   " then you might want to try to work things out. "
		   "Ultimately, it's up to you to decide what's best for you.",

	"Friend": "If you have been wondering about it for a while, then it sounds like you already have your answer."
}

answers["Save or spend my money?"] = {
	"Mom": "I think you should save money for next year.",

	"Dad": "Hi! I think it depends on what your priorities are."
		   " If saving money is more important to you than going to Mexico,"
		   " then you should save your money. However, if you feel like going to Mexico would be a more"
		   " valuable experience for you, then you should go and enjoy yourself!",

	"Friend": "I think you should fly to Mexico with your friends!"
}

form_responses = []
form_responses.append({"Dad": {"Mom":2, "Dad":5, "Friend":10},
						  "Mom":{"Mom":14, "Dad":2, "Friend":2},
						  "Friend":{"Mom":1, "Dad":10, "Friend":6}})

form_responses.append({"Dad": {"Mom":5, "Dad":5, "Friend":6},
						  "Friend":{"Mom":4, "Dad":4, "Friend":8},
						  "Mom":{"Mom":7, "Dad":7, "Friend":3}})

form_responses.append({"Mom": {"Mom":10, "Dad":6, "Friend":1},
						  "Dad":{"Mom":4, "Dad":11, "Friend":2},
						  "Friend":{"Mom":3, "Dad":0, "Friend":14}})

form_responses.append({"Dad": {"Mom":8, "Dad":3, "Friend":6},
						  "Mom":{"Mom":7, "Dad":2, "Friend":8},
						  "Friend":{"Mom":2, "Dad":12, "Friend":3}})

form_responses.append({"Friend": {"Mom":5, "Dad":2, "Friend":10},
						  "Dad":{"Mom":7, "Dad":4, "Friend":6},
						  "Mom":{"Mom":5, "Dad":11, "Friend":1}})

results = {"Dad": 0, "Mom": 0, "Friend": 0}

results_compared = {"Dad": {"Mom": 0, "Friend": 0}, "Mom": {"Dad": 0, "Friend": 0}, "Friend": {"Dad": 0, "Mom": 0}}
results_by_topic = {}

for i in range(len(topics)):
	topic_res = 0
	for char in form_responses[i]:
		results[char] += form_responses[i][char][char] / 17
		topic_res += form_responses[i][char][char] / 17
		for other in results_compared[char]:
			results_compared[char][other] += form_responses[i][char][other] / 17
	results_by_topic[topics[i]] = topic_res / 3

# ########### print the results ############
print("-"*5, "results", "-"*5)
for char in results:
	results[char] = results[char]/5
	print(char, ":  ", results[char])
print("\n")
print("-"*5, "results with others", "-"*5)
for char in results_compared:
	for other in results_compared[char]:
		results_compared[char][other] = results_compared[char][other] / 5
		print(char, "with", other, ":  ", results_compared[char][other])

print(results_by_topic)

# ########### plot the results ############
for char in results_compared:
	results_compared[char][char] = results[char]

labels = ["Mom", "Dad", "Friend"]
plot_data = {}
for l in labels:
	plot_data[l] = [results_compared["Mom"][l], results_compared["Dad"][l], results_compared["Friend"][l]]

width = 0.25
r1 = np.arange(3)
r2 = [x + width for x in r1]
r3 = [x + width for x in r2]

plt.bar(r1, plot_data["Mom"], color="blue", width=width, edgecolor='white', label='Mom')
plt.bar(r2, plot_data["Dad"], color="red", width=width, edgecolor='white', label='Dad')
plt.bar(r3, plot_data["Friend"], color="orange", width=width, edgecolor='white', label='Friend')

plt.ylabel("people's guesses")
plt.xlabel("true answer")
plt.xticks([r + width for r in range(3)], labels)
plt.legend()
plt.title("results by character")
plt.tight_layout()
plt.show()



for char in results_compared:
	results_compared[char][char] = results[char]

width = 0.4

plt.bar(results_by_topic.keys(), results_by_topic.values(), width=width)

plt.ylabel("average success for all characters")
plt.xticks(range(5), ["Move out \nfrom my \napartment",
							   "Walk home \nlate or \ntake the bus",
							   "What to \nwear tonight",
							   "Break up \nwith my \ngirlfriend",
							   "Save or \nspend my \nmoney?"])
plt.title("results by topic")
plt.tight_layout()
plt.show()

