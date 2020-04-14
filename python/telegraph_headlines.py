import numpy as np

authors = ['Melanie Phillips', 'Janet Daley','Robbie Gibb', 'Ann Widdecombe', 'Dominic Raab', 'Allison Pearson', 'Norman Tebbit', 'Daniel Hannan', 'John Redwood', 'Nick Timothy', 'Boris Johnson', 'Fraser Nelson', 'Katie Hopkins', 'Rod Liddle', 'Toby Young', 'Max Hastings', 'Charles Moore', 'Laurence Fox', 'Ricky Gervais', 'Piers Morgan', 'Peter Hitchens']

bad_things = ['cancer', 'coronavirus', 'teenage pregnancy', 'youth illiteracy', 'youth unemployment', 'dementia', 'child poverty', 'depression', 'climate change', 'North Korea']
bugbears = ['the European Union', 'the licence fee', 'the creeping rise of youth culture', 'Michel Barnier', 'Jean-Claude Juncker', 'the BBC', 'generation snowflake', "'woke' culture", "'generation me'", 'the collapse of the traditional family', 'Meghan Markle', 'Price Harry', 'Ed Miliband', 'Sir Keir Starmer', 'the Labour Party', 'Islam', 'the metropolitan elite', "left wing 'academia'", 'uncontrolled immigration', 'the trans rights industry', "'feminism'", 'the weather forecasting elite', 'Olivia Coleman', "Guardian-reading liberalism"]
good_things = ['traditional marriage', 'Christian Values', 'British Values', 'military discipline', 'the Blitz Spirit', 'curtsying', 'deference', 'good old fashioned manners' ]
good_people = ['Nigel Farage', 'Winston Churchill', 'Margaret Thatcher', 'Boris Johnson', 'the Queen', 'Prince Philip', 'Prince William', 'the police', 'the army', 'Tim Martin', 'David Davis', 'Mark Francois' ]

templates = ["It's true: $BB really is to blame for $BT",
             "We are seeing a return to $GT, and let me tell you, it's no bad thing",
             "How $BB could learn a thing or two from $GP",
             "God save the Queen: she is the perfect example of $GT for the modern age",
             "In this time of crisis, why on Earth is $GP still being silenced by $BB?",
             "A hero for our times: why Coronavirus has been the making of $GP",
             "Only one question matters now: what would $GP do?",
             "At a time of crisis, there is nothing wrong with invoking $GT",
             "To the despair of his opponents, $GP is more popular than ever",
             "$BT: why ministers need to be honest about $BB",
             "I was 'cancelled' for criticising $BB, but now more than ever we must hold the government to account over $BT",
             "The self-pitying $BB needed a war: and in $BT they have one",
             "Has $BT finally taught $BB to respect the older generation?",
             "$BT has blown away the dishonest ideas of $BB",
             "$BB must start thinking about others if we're to stop $BT",
             "What did the Romans and the Greeks teach $GP about $BT?",
             "No $BT please, we're British",
             "Worried about $BT? Here's the prescription from $GP",
             "We need you, $GP. Your health is the health of the nation.",
             "Let's believe in Britain and lead the world in the battle against $BT.",
             "Disdainful $BB is doing a disservice to British democracy" ]


class Article:
	def __init__(self):
		self.author = np.random.choice(authors)

	def construct(self):
		bad_thing = np.random.choice(bad_things)
		bugbear = np.random.choice(bugbears)
		good_thing = np.random.choice(good_things)
		good_person = np.random.choice(good_people)

		syntax = np.random.choice(templates)

		for x, thing in zip(['$BT','$GT','$BB', '$GP'],[bad_thing,good_thing,bugbear,good_person]):
			syntax = syntax.replace(x,thing)

		self.headline = syntax

		return None

	def show(self):
		print('--'*12)
		print('%s:'%self.author)
		print(self.headline)
		print('--'*12)
		return None


article = Article()
article.construct()
article.show()