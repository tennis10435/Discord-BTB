import discord
import asyncio
import requests

client = discord.Client()

@client.event
async def on_ready():
    print("[+] {0}(으)로 접속됨".format(client.user.name))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='태랑이엄마생각중..'))

@client.event
async def on_message(message):
    if message.content.startswith('!뮤트'):
        if not message.author.guild_permissions.administrator:
            await message.channel.send("`권한이 없습니다.`")
            return
        if message.author.guild_permissions.manage_messages:
            await message.delete()
            await message.channel.set_permissions(message.mentions[0],read_messages=True,send_messages=False)

            embed1 = discord.Embed(title= '', description=(''))
            embed1.set_author(name=f'{message.mentions[0].name} 님을 뮤트 하였습니다.', icon_url=message.mentions[0].avatar_url)
            await message.channel.send(embed=embed1)
            
    if message.content.startswith('!차단'):
        if message.author.guild_permissions.manage_messages:
            await message.delete()
            reason = message.content[30:]

            if reason == '':
                reason = 'None'
            else:
                pass

            try:
                await message.mentions[0].ban(delete_message_days=2, reason=reason)
            except discord.Forbidden as e:
                embed1 = discord.Embed(title= '', description=(f'{e}'))
                embed1.set_author(name=f'{message.mentions[0].name} 님을 차단 하는데 에러가 발생 하였습니다.')
                await message.channel.send(embed=embed1)
                return
            except discord.HTTPException as e:
                embed1 = discord.Embed(title= '', description=(f'{e}'))
                embed1.set_author(name=f'{message.mentions[0].name} 님을 차단 하는데 에러가 발생 하였습니다.')
                await message.channel.send(embed=embed1)
                return

            embed1 = discord.Embed(title= '', description=(f'**사유 : ** ``{reason}``'))
            embed1.set_author(name=f'{message.mentions[0].name} 님의 차단 로그 입니다.')
            await message.channel.send(embed=embed1)

client.run('ODM5NzM1NDEwMTkyNDE2Nzc5.YJN-iw.49JotaJoIV0oiQMRRnV3IuhfPX0')
