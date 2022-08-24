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


with open("configuracion.json") as f:
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Comando
bot.remove_command("help") # Borra el comando por defecto !help

@bot.command()
async def sillabanana(ctx,  keko1):
    await ctx.message.delete()
    await ctx.send("Generando Silla Banana 🍌", delete_after=0)
    time.sleep(3)
    
    response = requests.get(f"https://www.habbo.es/api/public/users?name={keko1}")
   
    
    habbo = response.json()['figureString']
    

   
    

    
    
   
    
    url = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo +"&action=sit&direction=4&head_direction=4&gesture=std&size=m"
    img1 = Image.open(io.BytesIO(requests.get(url).content))
    img1 = img1.resize((64,110), Image.Resampling.LANCZOS)#tamaño del keko 1
    
    
   
    
    
    img2 = img1.copy()
    
    BrazoSofa = Image.open(r"imagenes/BrazoSofa.png").convert("RGBA")
    img1 = BrazoSofa.resize((131,157), Image.Resampling.LANCZOS)#tamaño Brazo Sofa
    
    img1 = Image.open(r"imagenes/sofa.png").convert("RGBA") #Imagen del sofa habbo club
    img1 = img1.resize((131,157), Image.Resampling.LANCZOS)


    

    
    

    img1.paste(img2,(29,5), mask = img2) #Posicion del keko 1
    
    ###
    

   

    img1.paste(BrazoSofa,(0,0), mask = BrazoSofa) #Posicion del trozo de sofa
    
  
   
    
    
   


    
    
    
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)

        await ctx.send(file=discord.File(fp=image_binary, filename='keko.png'))

      




      
    
    
         

         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])    


