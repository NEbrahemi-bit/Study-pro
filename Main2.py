import discord 
from discord.ext import commands 
import os 
from openai import OpenAI

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

intenta = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!",intents=intents)

@bot.even
async def ON_ready():
  print(f"Logged in as {bot.user}")
  
def ask_ai(prompt):
try:
  # Fixed: Change method, model name, and parameters
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{role": "user", "content":prompt}]
  response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role":"user","content": prompt}]
  )
 
  # fixed: Correct way to access the text response 
  return response.choices[0].message.content
  except Exception as e:
  return f"Error:{e}"
return response.choices[0].message.content
except Exception as e:

  @bot.command()
  async def explain(ctx,*,topic):
    prompt = f"Explain this topic in simple terms for studying:{topic}"
    await ctx.send(ask_ai(prompt))


@bot.commands()
async def question(ctx,*, topic):
  prompt = f"create 5 study questions about:{topic}"
  await ctx.send(ask_ai(prompt))


@bot.command()
async def answers(ctx,*,topic):
  prompt = f"provide answers to common questions about:{topic}"
  await ctx.send(ask_ai(prompt)) 


@bot.command()
async def studymode(ctx. *, topic):
  await ctx.send(f"study mode started for: **{topic}**")

  questions = ask_ai(f"Create 3 quiz questions about {topic}")
  await ctx.send("Questions:\n" + questions)

  answers = ask_ai(f"provide answers for these questions :\n{questions}")
  await ctx.send("Answers:\n" + answers)


@bot.run(DISCORD_TOKEN)
