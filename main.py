import os, random
import discord
import requests
from discord.ext import commands
from options import TOKEN


intents = discord.Intents.default()
intents.message_content = True
    
bot = commands.Bot(command_prefix='!', intents=intents)

global_warming_questions = {
    'Какой газ является основной причиной парникового эффекта?': ['Углекислый газ (CO2)', 'Метан (CH4)', 'Азот оксид (NOx)'],
    'Какие действия могут помочь сократить выбросы парниковых газов?': ['Использование возобновляемых источников энергии', 'Энергоэффективные технологии', 'Оба варианта'],
    'Что представляют собой антропогенные выбросы?': ['Выбросы, вызванные человеческой деятельностью', 'Выбросы природного происхождения', 'Выбросы из океана'],
    'Какой процесс приводит к увеличению уровня морей?': ['Таяние льдяных шапок на полярных каплях', 'Увеличение солености океанской воды', 'Снижение температуры воды в океане'],
    'Какие регионы мира подвержены особенно высокому риску в связи с глобальным потеплением?': ['Различные регионы, включая Арктику, Африку и Азию', 'Только Африка', 'Только Арктика'],
    'Какое воздействие глобального потепления на экосистемы?': ['Комплексное воздействие, включая как положительные, так и отрицательные аспекты', 'Только отрицательное воздействие', 'Только положительное воздействие']
}



async def ask_question(ctx, question, options):
    question_text = f'{question}\n\n' + '\n'.join([f'{index + 1}. {option}' for index, option in enumerate(options)])
    await ctx.send(question_text)


@bot.event
async def on_ready():
    print(f'Наш бот {bot.user} запущен!')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def ask(ctx):
    await ctx.send(f'Поставьте цифру от 1 до 3!')
    question, options = random.choice(list(global_warming_questions.items()))
    await ask_question(ctx, question, options)

@bot.event
async def on_message(message):
    if message.author.bot:  
        return


    if message.content.isdigit():
        answer_index = int(message.content) - 1
        question, options = random.choice(list(global_warming_questions.items()))
        correct_answer = options.index(global_warming_questions[question][0])
        if answer_index == correct_answer:
            response = f'Верно!'
        else:
            response = f'Неправильно.Попробуйте еще раз.'
        await message.channel.send(response)
    
    
    await bot.process_commands(message)
    
  
     

bot.run(TOKEN)  
