from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

class Bot:
	def __init__(self):
		pass


# Screens for menu. Choices list.
screenMenu = {
				'mainMenu': """
							\n
							MENU (Opções)
							\n
							1. /funcionamento -> Horarios de funcionamento. 
							2. /retirada -> Hoŕarios de retirada de produtos. 
							3. /pesquisar -> Procurar por item/produto. 
							4. /listar -> Lista de produtos. 
							5. /atendent -> Falar com atendente. 
							6. /ajuda -> Ajuda 
				"""
				}

# List types products.
listaItens = None

# Commands

# Info of Bot. state_bot -> state of bot with normal, asking questions.
Bot, updater, state_bot = None, None, None

# Register bot and commands to bot
def registerBot(bot, update, state):
	global Bot, updater,  state_bot
	Bot, updater, state_bot = bot, update, state


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Olá! Como vai?\n Em que posso ajudar?\n Digite "/menu" para acessar menu principal. \n Digite "/help" para ajuda.\n Digite "/listar" para ver produtos alimenticios disponiveis e preços.\n\n\n :)\n')
    #update.message.reply_text(screenMenu['mainMenu'])
	
def mainMenu(update: Update, context: CallbackContext) -> None:
	update.message.reply_text(screenMenu['mainMenu'])

# Consulta
def consult(item: str) -> str:
	"""Consultar produto."""
	d = []
	text = '\nNome - Valor\n'
	import csv
	
	with open('data/alimentos.csv', 'r') as csvFile:
		data = csv.DictReader(csvFile, delimiter=';')
		for i in data:
			if str.lower(item) == 'arroz':
				d.append((i['Nome'], i['Valor']))
				text += i['Nome'] + ' - ' + i['Valor'] + '\n'
			else:
				text = "Desculpe não encontramos seu produtos em nosso acervo.\nConsidere falar com um de nossos atendentes."
			
	return text
	
def search(update: Update, context: CallbackContext) -> None:
	global state_bot
	update.message.reply_text("Qual item deseja procurar? \nDigite nome do produto.")
	state_bot = 1
	
def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
	"""Echo the user message."""
	global state_bot
	if state_bot == 1:
		user_question = consult(update.message.text)
		update.message.reply_text(user_question)
		state_bot = 0
		return 0
		
	update.message.reply_text("Olá. Em que posso ajudar? :) ")
	update.message.reply_text(screenMenu['mainMenu'])
	print('testes')
	

def getName(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(Bot['name'])

# Method "retirada". 
def retirada(update: Update, context: CallbackContext) -> None:
	update.message.reply_text("Por favor qual dia e horario seriam mais convenientes para retirada de suas compras? \nIremos marcar essa data para retirda de suas compras.")
	state_bot = 0
	
# Return informations
def getInfo():
    pass

# Close conversation.
def quitTalk():
    pass

# Get data file for infos
def getData():
    pass

# Natural Language input/output
def nlOut(msg: str) -> str:
    return 'x'

# List data
def listar(update: Update, context: CallbackContext) -> None:
	d = []
	text = '\nNome - Valor\n'
	import csv
	# Load data csv
	with open('data/data.csv', 'r') as csvFile:
		data = csv.DictReader(csvFile, delimiter=';')
		for i in data:
			d.append((i['Nome'], i['Valor']))
			text += i['Nome'] + ' - ' + i['Valor'] + '\n'
			
	update.message.reply_text(text)
	return 1
