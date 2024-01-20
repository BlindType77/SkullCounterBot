import discord
from discord.ext import commands
from discord_webhook import DiscordWebhook
intents = discord.Intents.default()
intents.emojis = True
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

message_counts = {}
emoji_counts = {}  # Dictionary to store emoji counts for users
SkullHook = DiscordWebhook(url="WEBHOOK")
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    await bot.process_commands(message)  # Process commands first
    skull_emoji = '💀'
    if message.author.id == 'USERID':  # specifc user id
        emojis = ['1070071178980491415']  # Emojis for reacting
     
        
        # Update message count for the user
        user_id = message.author.id
        if user_id not in message_counts:
            message_counts[user_id] = 0
        message_counts[user_id] += 1
        
        if message_counts[user_id] >= 10:
            for emoji_id in emojis:
                emoji = bot.get_emoji(int(emoji_id))
                if emoji:
                    message_counts[user_id] = 0
                    await message.add_reaction(emoji)
                    
    
    elif skull_emoji in message.content:
        skull_emoji = '💀'
        skull_emoji1 = '☠'
        skull_emoji2 = 1097985765784428584
        # Count skull emoji occurrences in the message content
        skull_count = message.content.count(skull_emoji)
        
        # Update emoji count for the user
        user_id = message.author.id
        if user_id not in emoji_counts:
            emoji_counts[user_id] = 0
        emoji_counts[user_id] += skull_count
        if emoji_counts[user_id] >= 50:
            SkullHook.content("I can take this shit anynore...")
            SkullHook.execute()
            await message.delete()
        elif skull_emoji in message.content:
            SkullHook.content = f"{message.author}, you've used the skull emoji {emoji_counts[user_id]} time(s) in total."
            SkullHook.execute()
          
    # Process custom commands
    print("The message's content was", message.content)
    await bot.process_commands(message)

# Command definitions
@bot.command()
async def userid(ctx, member: discord.Member):
    await ctx.send(member.mention)

@bot.command()
async def emoji(ctx):
    await ctx.message.add_reaction('📑')
@bot.command()
async def kill(ctx):
    '''
    Kill FrogBot you Bastard!!
    '''
    if ctx.message.author.id in [468899271031128074]:

        await ctx.message.delete()
        await ctx.send("Counter Bot Shutting down!!")
        exit()
    
bot.run('TOKEN')  # Where 'TOKEN' is your bot token


