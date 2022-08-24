import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashCommand, SlashContext


with open("configuracion.json") as f:
    config = json.load(f)

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

slash = SlashCommand(bot, sync_commands=True)
@slash.slash(
    name="sillabanana", description="Keko habbo Hotel",
    options=[
                create_option(
                  name="keko1",
                  description="Escribe el keko 1",
                  option_type=3,
                  required=True
                ),
                 create_option(
                  name="hotel",
                  description="Elige él hotel",
                  option_type=3,
                  required=True,
                  choices=[
                      create_choice(
                          name="ES",
                          value="es"
                      ),
                      create_choice(
                          name="BR",
                          value="com.br"
                      ),
                      create_choice(
                          name="COM",
                          value="com"
                      ),
                      create_choice(
                          name="DE",
                          value="de"
                      ),
                      create_choice(
                          name="FR",
                          value="fr"
                      ),
                      create_choice(
                          name="FI",
                          value="fi"
                      ),
                      create_choice(
                          name="IT",
                          value="it"
                      ),
                      create_choice(
                          name="TR",
                          value="com.tr"
                      ),
                      create_choice(
                          name="NL",
                          value="nl"
                       )
                  ]
                
               
                  
                )
             ])


async def _sillabanana(ctx:SlashContext, keko1:str,hotel:str):
   
    
   
    await ctx.defer()
    
    
    response = requests.get(f"https://www.habbo.{hotel}/api/public/users?name={keko1}")
   
    
    habbo = response.json()['figureString']
    

   
    

    
    
   
    
    url = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo +"&action=sit&direction=4&head_direction=4&gesture=std&size=m"
    img1 = Image.open(io.BytesIO(requests.get(url).content))
    img1 = img1.resize((64,110), Image.Resampling.LANCZOS)#tamaño del keko 1
    
    
   
    
    
    img2 = img1.copy()
    
    BrazoSofa = Image.open(r"imagenes/BrazoSofa.png").convert("RGBA")
    img1 = BrazoSofa.resize((131,157), Image.Resampling.LANCZOS)#tamaño Brazo Sofa
    
    img1 = Image.open(r"imagenes/sofa.png").convert("RGBA") #Imagen del sofa
    img1 = img1.resize((131,157), Image.Resampling.LANCZOS)


    

    
    

    img1.paste(img2,(29,5), mask = img2) #Posicion del keko 1
    
    ###
    

   

    img1.paste(BrazoSofa,(0,0), mask = BrazoSofa) #Posicion BrazoSofa
    
  
   
    
    
   


    
    
    
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(file=discord.File(fp=image_binary, filename='keko.png'))

      




      
    
    
         

         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])    


