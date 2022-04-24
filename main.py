import json
import random
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(request):
    request.lower()
    if request in data:
        return random.choice(data[request])
    elif len(get_close_matches(request, data.keys())) > 0:
        yn = input(
            f'Did you mean "{get_close_matches(request, data.keys())[0]}" instead?\n'
            f'Enter Y if yes and N no: ').lower()
        if yn == 'y':
            return random.choice(data[get_close_matches(request, data.keys())[0]])
        elif yn == 'n':
            new_query = input(
                'The word does not exist.\n'
                'You can leave us(Just enter "Q")\n'
                'either You can try to enter your word again: '
            ).lower()
            if new_query == "q":
                return "Goodbye"
            else:
                return translate(new_query)
        else:
            return "We didn't understand your entry"
    else:
        return 'You probably have the incorrect word. Please double check it'


query = input('Enter your word: ')
app = translate(query)
print(app)
