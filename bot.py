import discord
from discord.ext import commands 
import random
from discord.ext.commands import Bot
from random import choice
import asyncio
import datetime
from itertools import cycle
import os

prefix = '/'

Bot = commands.Bot(command_prefix= prefix)

Bot.remove_command('help')

        

@Bot.event
async def on_ready():
    await Bot.change_presence(status=discord.Status.idle, activity=discord.Game('Federal Bureau of Investigation (by V.Auditore)'))
    print("Bot is online")


@Bot.command(pass_context= True)
async def hello(ctx):
    await ctx.send("Hello {}".format(ctx.message.author.mention))


@Bot.command(pass_context= True)
async def info(ctx, usr: discord.Member=None):
    if not usr:
            return await ctx.send('**Используй: /info @username**')
    try:
         emb = discord.Embed(title= "Информация о {}".format(usr.name), colour= 0x39d0d6)
         emb.add_field(name= "Ник", value= usr.name)
         emb.add_field(name= "ID юзера", value= usr.id)
         emb.add_field(name= "Создал аккаунт", value= str(usr.created_at)[:16])
         emb.add_field(name= "Вошёл на сервер", value= str(usr.joined_at)[:16])
         emb.set_thumbnail(url= usr.avatar_url)
         emb.set_author(name= "Bot USS", url= usr.avatar_url)
         emb.set_footer(text= f'Вызвано: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
         emb.timestamp = datetime.datetime.utcnow()
         await ctx.send(embed= emb)
         await ctx.message.add_reaction("✅")
    except Exception as e:
         await ctx.message.add_reaction("❌")
         await ctx.author.send(e)

    


@Bot.command(pass_context= True)
async def ukaz1(ctx):
    """Приветствие"""
    emb = discord.Embed(title= "Приказ по личному составу №080 О назначении на должность D.Director, Начальника академии и его заместителя.", description= "`Я, действующий директор Department of Corrections Rafaelo FIlips, издаю приказ, о назначении на должность заместителя директора департамента коррекций Romeo McCartney, на должность начальника академии - Sota Burbon, на должность его заместителя - Tao Sakurai`", colour= 0x39d0d6)
    emb.add_field(name= "*С момента публикации приказа он вступает в силу.*", value= "ДАТА: 05.01.2019", inline=True)
    emb.set_footer(text= "FBI Bot", icon_url= Bot.user.avatar_url)
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)

@Bot.command(pass_context= True)
async def rules(ctx):
    """Правила"""
    emb = discord.Embed(title= "Правила Discord-сервера FBI.", description= "`Запрещено следующее: flood, caps, offtopic, spam, нецензурная лексика, завуалированный мат, розжиг, неадекватное поведение, оскорбление чувств и/или унижение достоинства другого пользователя, оскорбление и/или  упоминание родных. Запрещено распространение личной информации, реклама сторонних ресурсов/Discord серверов. Запрещены массовые упоминания, упоминания без причины. Запрещена порнография в любых её проявлениях. Запрещены любые проявления оскорблений в NickName.`", colour= 0x39d0d6)
    emb.add_field(name= "**Незнание правил не освобождает вас от ответственности, при присоединении к серверу вы даёте согласие с данными правилами.**", value= "Модератор сам определяет меру наказания.", inline=True)
    emb.set_image(url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgoMOREGlV6dZGUUr306Gtw5s6KmOIMiYyO6BX-dMi_Adrwxh4sg&s")
    emb.set_footer(text= "FBI Bot", icon_url= Bot.user.avatar_url)
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)

@Bot.command(pass_context= True)
async def priv(ctx):
    """Правила"""
    emb = discord.Embed(title= "Federal Bureau of Investigation", description= "`Приветствуем Вас, уважаемые агенты ФБР. Добро пожаловать в официальный discord-сервер FBI.`", colour= 0x39d0d6)
    emb.set_image(url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgoMOREGlV6dZGUUr306Gtw5s6KmOIMiYyO6BX-dMi_Adrwxh4sg&s")
    emb.set_footer(text= "FBI Bot", icon_url= Bot.user.avatar_url)
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)

@Bot.command(pass_context= True)
async def meme(ctx):
    """Правила"""
    emb = discord.Embed(title= "Screenshots and Memes.", description= "`Доброго времени суток, уважаемые участники USS. Если у Вас имееться множество интересных или смешных скриншотов касаемых SAMP'a и прочих игр, Вы можете поделиться этим в этом текстовом канале. `", colour= 0x39d0d6)
    emb.add_field(name= "**Offtop/flood в данном канале карается длительным mute`ом.**", value= "С уважением, USS Team.", inline=True)
    emb.set_image(url= "https://i.imgur.com/wYO2dTc.jpg")
    emb.set_footer(text= "USS Bot", icon_url= Bot.user.avatar_url)
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)

@Bot.command(pass_context= True)
async def forma(ctx):
    emb = discord.Embed(title= "Форма получения роли.", description= "`Уважаемые агенты, для получения роли заполните форму ниже.`", colour= 0x39d0d6)
    emb.add_field(name= f"**Ваш nickname - Ваша должность.**", value= "Например, Александр Романов - Директор ФБР", inline=True)
    emb.set_image(url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgoMOREGlV6dZGUUr306Gtw5s6KmOIMiYyO6BX-dMi_Adrwxh4sg&s")
    emb.set_footer(text= "FBI Bot", icon_url= Bot.user.avatar_url)
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)


@Bot.command(pass_context= True) 
async def help(ctx): 
    emb = discord.Embed(title= "Команды", colour= 0x39d0d6)
    emb.add_field(name= "Информация про команды", value= "`{}help`".format(prefix))
    emb.add_field(name= "Проверить ping", value= "`{}ping`".format(prefix))
    emb.add_field(name= "Игра Coin", value= "`{}coin`".format(prefix))
    emb.add_field(name= "Посмотреть аватарку юзера", value= "`{}avatar @username`".format(prefix))
    emb.add_field(name= "Игра 8-ball", value= "`{}ball`".format(prefix))
    emb.add_field(name= "Правила сервера", value= "`{}rules`".format(prefix))
    emb.add_field(name= "Информация о юзере", value= "`{}info @username`".format(prefix))
    emb.add_field(name= "Команды для модератора:", value= "`/say <channel> <text>`,`/frick`,`/mute`,`/clear`,`/unmute`,`/ban`,`/kick`", inline=True)
    emb.set_image(url= "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgoMOREGlV6dZGUUr306Gtw5s6KmOIMiYyO6BX-dMi_Adrwxh4sg&s")
    emb.set_footer(text= f'Вызвано: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed= emb)

@Bot.command()
@commands.has_permissions(administrator = True) 
async def say(ctx, channel: discord.TextChannel, *, cnt):
   await ctx.message.delete() 
   embed = discord.Embed(description = cnt, colour = 0x00ff80) 
   await channel.send(embed=embed) 

@Bot.command(pass_context=True, name= 'ping', brief= 'Показать текущую задержку')
@commands.cooldown(1, 1, commands.BucketType.user)
async def ping(ctx):
        try:
            await ctx.message.delete()
        except:
            pass
        emb = discord.Embed(title= '**Текущая задержка:**', description= f'``{Bot.ws.latency * 1000:.0f} ms``', colour= 0x00ff80)
        emb.set_author(name= f'Ping', icon_url= Bot.user.avatar_url)
        emb.set_footer(text= f'{ctx.author}', icon_url= ctx.author.avatar_url)
        emb.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=emb)

@commands.has_permissions(administrator=True)
@Bot.command()
async def frick(ctx):

    role = ctx.guild.get_role(669956301052444692) 

    balbes = "Фрик"
    bot = "бота"
    bots = "бота"
    member = "участников"
    members = "участников"

    members_counter = len(ctx.guild.members)
    role_counter = len([m for m in ctx.guild.members if role in m.roles])
    bots_counter = len([m for m in ctx.guild.members if m.bot])
    valid_members = [m for m in ctx.guild.members if not m.bot and role not in m.roles]

    if members_counter - bots_counter < 2:
        return await ctx.send(f'{ctx.author.mention} Ты один на сервере, {"не считая меня!" if bots_counter == 1 else f"не считая {bots_counter} {bot}!"}')

    elif not valid_members:
        return await ctx.send('**ой, все пользователи уже Фрики!** :smirk:')

    elif len(valid_members) is 1:
        await ctx.send(f'{ctx.author.mention} Ну тут выбор очевиден! На сервере остался только один человек без роли :smirk:')
        random_member = valid_members[0]
    else:
        await ctx.send(f'{ctx.author.mention} Немного подожди, я выбераю рандомного Фрика среди **{members_counter}** {member}! :smirk:'
                       f'\nА если быть точнее то из **{members_counter - bots_counter - role_counter}**, т.к на сервере ' + \
                       (f'**{bots_counter}** {bots}' if bots_counter > 1 else 'есть я, а я не считаюсь') + \
                       f' и у **{role_counter}** {members} уже есть роль!')

        try:
            await asyncio.sleep(5)
            random_member = choice(valid_members)
            await random_member.add_roles(role)
        except Exception as error:
            return await ctx.send(f'**Произошло GG **{type(error).__name__}**:\n{error}')
            
        try:
            emb = discord.Embed(
                color=0x99ff99,
                description=f'Роль {role.mention} присуждается {random_member.mention}\nТеперь на сервере **{role_counter + 1}** {balbes}')
            emb.set_footer(text= f"Вызвал(а): {ctx.author.nick if ctx.author.nick else ctx.author.name}", icon_url=str(ctx.message.author.avatar_url))
            await ctx.send(embed=emb)
            await ctx.message.add_reaction("✅")
        except Exception as e:
            await ctx.message.add_reaction("❌")
            await ctx.author.send(e)
        
        
    
@Bot.command()
async def avatar(ctx, member: discord.Member=None):
    if not member:
            return await ctx.send('**Используй: /avatar @username**')
    try:
         user = ctx.message.author if (member == None) else member
         embed = discord.Embed(title=f'Аватар пользователя {user}', description= f'[Ссылка на изображение]({user.avatar_url})', color=user.color)
         embed.set_footer(text= f'Вызвано: {ctx.message.author}', icon_url= str(ctx.message.author.avatar_url))
         embed.set_image(url=user.avatar_url)
         embed.timestamp = datetime.datetime.utcnow()
         await ctx.send(embed=embed)
         await ctx.message.add_reaction("✅")
    except Exception as e:
         await ctx.message.add_reaction("❌")
         await ctx.author.send(e)
    

    

@Bot.command()
async def coin(ctx):
    num=random.randint(1,2)
    if (num == 1):
           await ctx.send("Вым выпал - Орёл")
           print("[?coin] - done")
    if(num == 2):    
           await ctx.send("Вам выпала - Решка")
           print("[?coin] - done")
        
@Bot.command()
async def ball(ctx, text: str=None):
     if not text:
             return await ctx.send('**Используй: /ball "Вопрос"**')
     try:
             num=random.randint(1,4)
             if (num == 1):
                await ctx.send("Однозначно - да :ok_hand_tone5: ")
                print("[?coin] - done")
             if(num == 2):    
                 await ctx.send("Мой ответ - нет :thumbsdown_tone5: ")
                 print("[?coin] - done")
             if (num == 3):
                 await ctx.send("Скорее всего :smiling_imp: ")
                 print("[?coin] - done")
             if (num == 4):
                 await ctx.send("Даже не думай :skull_crossbones: ")
                 print("[?coin] - done")
                 await ctx.message.add_reaction("✅")
     except Exception as e:
         await ctx.message.add_reaction("❌")
         await ctx.author.send(e)



@Bot.command()
@commands.has_permissions(administrator = True) 
async def cmd(ctx):
    await ctx.message.delete() 
    role = ctx.guild.get_role(656579155479232513) 
    emb = discord.Embed(title= "GIVEAWAY начат", description=f" {role.mention} **Для участия нажмите на реакцию ниже. Приз: 50.000$. Результат через 12 часов.**", color=0x99ff99)
    emb.set_footer(text= f"Cпонсор: {ctx.author.nick if ctx.author.nick else ctx.author.name}", icon_url=str(ctx.message.author.avatar_url))
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=emb) 

@Bot.command()
@commands.has_permissions(administrator = True) 
async def giveaway1(ctx, channel: discord.TextChannel, msgid: int):
    await ctx.message.delete() 
    message = await channel.fetch_message(msgid)
    users = set([user for reaction in message.reactions for user in await reaction.users().flatten()])
    random_member = random.sample(users, 1)[0] 
    emb = discord.Embed(title= "GIVEAWAY закончен", description=f"**Участник {random_member.mention} выиграл приз! Поздравляем!**", color=0x99ff99)
    emb.set_footer(text= f"Cпонсором был: {ctx.author.nick if ctx.author.nick else ctx.author.name}", icon_url=str(ctx.message.author.avatar_url))
    emb.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=emb)

@Bot.command()
@commands.has_permissions(administrator= True)
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)

@Bot.command()
async def unmute(ctx, member : discord.Member = None):
    if member == None:
        await ctx.send("**Используй: /unmute '@username'**")
    else:
        membern = member.nick
        if member.nick == None:
            membern = member.name
        unmute_cnt = f"Пользователь {membern} быз раззамучен модератором {ctx.author}!"
        emb = discord.Embed(title= "UnMute", description= unmute_cnt, colour= 0x000000)
        role = ctx.guild.get_role(676100496779509767)
        await member.remove_roles(role)
        await ctx.send(embed= emb)
        await ctx.message.add_reaction("✅")


    
@Bot.command(pass_context= True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.User = None, reason = None):
    if member == None:
        await ctx.send("**Используй: /ban '@username' 'причина'**")
    elif reason == None:
        await ctx.send("**Используй: /ban '@username' 'причина'**")
    else:
        await ctx.guild.ban(member)
        emb = discord.Embed(title= "**Участник {}, был забанен.**".format(member), description= "**По причине: {}**".format(reason), color= 0x000000)
        await ctx.send(embed= emb)
        await member.send(f'Вас забанили на сервере {ctx.guild.name} по причине {reason}.')
        await ctx.message.add_reaction("✅")
    
    
@Bot.command()
@commands.has_permissions(administrator = True)
async def mute(ctx, member: discord.Member = None, seconds = None, reason = None):
    if member == None:
        await ctx.send("**Используй: /mute '@username' 'время' (секунды) 'причина'**")
    elif seconds == None:
        await ctx.send("**Используй: /mute '@username' 'время' (секунды) 'причина'**")
    elif reason == None:
        await ctx.send("**Используй: /mute '@username' 'время' (секунды) 'причина'**")
    else:
        role = ctx.guild.get_role(676100496779509767) 
        sec = float(seconds)
        emb = discord.Embed()
        await member.add_roles(role)
        emb.set_author(name = "{} замучен на {} секунд по причине: {}".format(member, seconds, reason))
        await ctx.send(embed = emb)
        await asyncio.sleep(sec)
        await member.remove_roles(role)
        embed = discord.Embed()
        embed.set_author(name = "{} размучен по истечении времени.".format(member))
        await ctx.send(embed = embed)
        await ctx.message.add_reaction("✅")

@Bot.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.User = None, reason= None):
    if member == None:
        await ctx.send("Используй: /kick '@username' 'причина'")
    elif reason == None:
        await ctx.send("Используй: /kick '@username' 'причина'")
    else:
        await ctx.guild.kick(member)
        emb = discord.Embed(title= "Участник {}, был кикнут.".format(user), description= "По причине: {}".format(reason), color= 0x000000)
        await ctx.send(embed= emb)
        await member.send(f'Вас кикнули с сервера {ctx.guild.name} по причине {reason}.')
        await ctx.message.add_reaction("✅")



token = os.environ.get('BOT_TOKEN')

Bot.run(str(token))