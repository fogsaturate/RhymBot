import discord
from discord import app_commands
import math
from enum import Enum
from dotenv import load_dotenv
import os

load_dotenv(".env")
DISCORD_TOKEN: str = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')




class Speed(Enum):
    SpeedMinusMinusMinus = 1 / 1.35
    SpeedMinusMinus = 1 / 1.25
    SpeedMinus = 1 / 1.15
    Normal = 1
    SpeedPlus = 1.15
    SpeedPlusPlus = 1.25
    SpeedPlusPlusPlus = 1.35
    SpeedPlusPlusPlusPlus = 1.45

def ease_in_expo_deq_hard(acc: float, star: float):
    exponent = 100 - 12 * star
    if exponent < 5:
        exponent = 5
    return 0 if acc == 0 else math.pow(2, exponent * acc - exponent)

def calculate_rp(acc: float, star: float):
    return round(
        math.pow(
            (star * ease_in_expo_deq_hard(acc, star) * 100) / 2, 2
            ) / 1000, 2
        )



@client.tree.command()
@app_commands.describe(
    accuracy='The accuracy you got on the play. (Example: 99.50)',
    star_rating='The star rating the map. (Example: 7.3)',
    speed='The speed you played the map at.'
)
async def rp_calculator(interaction: discord.Interaction, accuracy: float, star_rating: float, speed: Speed):
    """Calculates RP you achieved from a score."""
    try:
        await interaction.response.send_message(str(calculate_rp(accuracy / 100, (star_rating * speed.value))) + "RP")
    except OverflowError:
        await interaction.response.send_message("Overflow Error. Please do not put in ridiculously high numbers.")
    except Exception as e:
        await interaction.response.send_message(f"An unexpected error occured: {e}")

client.run(DISCORD_TOKEN)
