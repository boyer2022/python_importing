# import bot, user_input
from bot import program_name, generate_computer_response
from user_input import *

print('Welcome to ' + program_name)

print('Type "STOP" to end.')

ask_question('How was your day?')

while True:
    bot_response = generate_computer_response()
    response = ask_question(bot_response)
    if response.upper() == 'STOP':
        break

print('Thanks for the interesting conversation!')