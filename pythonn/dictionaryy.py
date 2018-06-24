phone_book = {
	'qazi': ['123-456-7890', 'qazi@qazi.com'], 
	'bob': ['222-222-2222', 'bob@bob.com'],
	'cat': ['333-333-3333', 'cat@cat.com']
	}
	
# DICT[qazi] --> list of things containing ph# and email.
print(phone_book['cat'][0])
print(phone_book['bob'][0])
print(phone_book['qazi'][1])

# let's store another person
phone_book['billy'] = ['111-111-1111', 'billy@billy.com']

# notice billy is now in the dictionary
print(phone_book)

# get billy's e-mail address
print(phone_book['billy'][1])
