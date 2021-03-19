import discord # Main Module for discord API wrapper
import json    # Module required to read to bot_config.json file

prefix = '<3'  # Prefix of the bot '<3'

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} is cloud')
    async def on_message(self, message):
        if message.author is self.user:
            return
        if message.content == f'{prefix} test':
            await message.channel.send('test works!, YESWON GAY')

def get_token():
    """grepping token from config file
    args:
        client_token : token of the cleint
    """
    with open ('bot_config.json', 'r') as json_file:
        json_object = json.load(json_file)
        json_pair   = json_object.items()
        client_token = json_pair['token']
    return client_token

client = MyClient()     # declaring bot variable
client.run(get_token()) # running the bot
