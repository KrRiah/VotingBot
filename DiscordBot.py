import discord
import asyncio
import datetime
import random
from urllib.request import urlopen

client=discord.Client()
token='Njk1NTI3OTE0NTYwNTUzMDUw.Xobe2Q.VjfYCBWA8qBJ6svbHLEZajg8sDY'

@client.event
async def on_ready():
    print('----------------------------------------------------------------------------')
    print(f'| Client ID: {client.user.id}                                             |')
    print(f'| Client Name: {client.user.name}                                                     |')
    print(f'| Client Token: {str(token)} |')
    print('----------------------------------------------------------------------------\n\n=========================================\n\n') 
    messages = [f'{len(client.guilds)}개의 서버 | {len(client.users)}명의 유저', "개발 = Iven#9998.", "「:명령어」로 시작"]
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
        messages.append(messages.pop(0))
        await asyncio.sleep(6)

@client.event
async def on_message(message):
    if message.content.startswith(":명령어"):
        if message.content == ":명령어" or message.content.replace(" ","") == ":명령어":
            embed = discord.Embed(title="명령어 목록입니다!",description=":투표 [주제]",color=0x00aab)
            embed.add_field(name="봇을 만든 제작자입니다.", value=":제작", inline=False)
            embed.add_field(name="투표를 어떻게 하는지 알려드립니다.", value=":투표도움말", inline=False)
            embed.add_field(name="봇을 만들때 사용한 프로그램을 올립니다.", value=":사용프로그램", inline=False)
            embed.add_field(name="투표봇을 사용할수 있는 시간", value=":투표봇시간", inline=False)
            embed.add_field(name="투표봇 제작자들에게 문의를 보낼수 있습니다.", value=":문의", inline=False)
            embed.add_field(name="상대방의 프로필을 확인할수 있습니다..", value=":프사 (맨션)", inline=False)
            embed.add_field(name="내 정보를 확인할수 있습니다.", value=":내정보", inline=False)
            await message.channel.send(embed=embed)
            print('<@' + str(message.author.id) + '> 님이 서버에서 [:명령어]이라고 했습니다.')
            return
    if message.content.startswith(':제작'):
        if message.content == ":제작" or message.content.replace(" ","") == ":제작":
            embed = discord.Embed(title="이 봇을 만든 사람들입니다!",description="--------------------------------",color=0x00aaaa)
            embed.add_field(name="봇을 만든 제작자입니다.", value="Iven#9998", inline=False)
            embed.add_field(name="투표를 만들어주신분", value="아두이노를 하는 사람", inline=False)
            embed.add_field(name="도움을 주신분", value="C̸͒h̸oõ̷͝s̸e̵ ̷m̷e̸͌̕[$KU££ 천마]", inline=False)
            await message.channel.send(embed=embed)
        print('<@' + str(message.author.id) + '> 님이 서버에서 [:제작]이라고 했습니다.')
        return
    if message.content.startswith(':투표도움말'):
        if message.content == ":투표도움말" or message.content.replace(" ","") == ":투표도움말":
            embed = discord.Embed(title="투표명령어 사용 방법!",description="--------------------------------",color=0x00aaaa)
            embed.add_field(name="기본 명령어", value=":투표 「투표주제」", inline=False)
            embed.add_field(name="꿀 팁", value="투표주제 설정시 앞뒤에 ` 를 붙여주세요" , inline=False)
            await message.channel.send(embed=embed)
        print('<@' + str(message.author.id) + '> 님이 서버에서 [:투표도움말]이라고 했습니다.')
        return
    if message.content.startswith(':투표봇시간'):
        if message.content == ":투표봇시간" or message.content.replace(" ","") == ":투표봇시간":
            embed = discord.Embed(title="『투표봇의 온라인시간』",description="--------------------------------",color=0x00aaaa)
            embed.add_field(name="요일", value="매일 (가끔을 제외)", inline=False)
            embed.add_field(name="호스팅비용 부담 불가", value="투표봇은 호스팅을 사용하지 않기 때문에 24시간이 불가능합니다." , inline=False)
            embed.add_field(name="확실한시간", value="Iven#9998이 온라인일떄!", inline=False)
            embed.add_field(name="하지만 그것도...", value="봇 점검 중일때는 오프라인일수도 있습니다", inline=False)
            embed.add_field(name="그럴땐", value="디코봇의 발전을 위해 너그롭게 봐주신다면 감사하겠습니다.", inline=False)
            await message.channel.send(embed=embed)
            print('<@') + str(message.author.id) + '> 님이 서버에서 [:투표봇시간]이라고 했습니다.'
        return
    if message.content.startswith(':사용프로그램'):
        if message.content == ":사용프로그램" or message.content.replace(" ","") == ":사용프로그램":
            embed = discord.Embed(title="봇을 제작할때 사용한 프로그램",description="--------------------------------",color=0x00aaaa)
            embed.add_field(name="기본 프로그램", value="Visual Studio Code(비쥬얼 스튜디오 코드)", inline=False)
            embed.add_field(name="언어", value="Python(파이썬)", inline=False)
            await message.channel.send(embed=embed)
        print('<@') + str(message.author.id) + '> 님이 서버에서 [:사용프로그램]이라고 했습니다.'
        return
    if message.content.startswith(':문의'):
        if message.content == ":문의" or message.content.replace(" ","") == ":문의":
            embed = discord.Embed(title="투표봇 문의안내",description="--------------------------------",color=0x00aaaa)
            embed.add_field(name="여기로 연락주세요", value="Iven#9998", inline=False)
            embed.add_field(name="카카오톡", value="추후 공지", inline=False)
            await message.channel.send(embed=embed)
        print('<@') + str(message.author.id) + '> 님이 서버에서 [:문의]이라고 했습니다.'
        return
    if message.content.startswith(":발로"):
        if message.content == ":발로" or message.content.replace(" ","") == ":발로":
            embed = discord.Embed(title="발로란트를 즐겨보세요!",description="[발로란트](https://beta.playvalorant.com/ko-kr/)",color=0x00aab)
            await message.channel.send(embed=embed)
        print('<@') + str(message.author.id) + '> 님이 서버에서 [:발로]이라고 했습니다.'
        return
    if message.content.startswith(":발전"):
        if message.content == ":발전" or message.content.replace(" ","") == ":발전":
            embed = discord.Embed(title="발로란트유저의 슈듄을 확인해 보세요!",description="[발로란트 전적보러가기](https://valorant.dak.gg/)",color=0x00aab)
            await message.channel.send(embed=embed)
        print('<@') + str(message.author.id) + '> 님이 서버에서 [:발전]이라고 했습니다.'
        return
    if message.content.startswith(":잠수"):
        user = client.get_user(int(message.mentions[0].id))
        embed = discord.Embed(title=f"{user.display_name}님이 잠수입니다." ,description=f"{user.avatar_url}",color=0xcccccc)
        embed.set_thumbnail(url=user.avatar_url)
        await message.channel.send(embed=embed)
        print('<@') + str(message.author.id) + '> 님이 서버에서 [:잠수]이라고 했습니다.'
        return
    if message.content.startswith(f":프사"):
        user = client.get_user(int(message.mentions[0].id))
        embed = discord.Embed(title=f"{user.display_name}님의 프로필 사진 입니다" ,description=f"{user.avatar_url}",color=0xcccccc)
        embed.set_thumbnail(url=user.avatar_url)
        await message.channel.send(embed=embed)
        print('<@') + str(message.author.id) + '> 님이 서버에서 [:프사]이라고 했습니다.'
        return
    if message.content.startswith(':내정보'):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) +1420070400000) /1000)
        embed = discord.Embed(color=0x00aab)
        embed.add_field(name="이름" , value=message.author.name, inline=True)
        embed.add_field(name="서버닉" , value=message.author.display_name, inline=True)
        embed.add_field(name="가입일" , value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="ID" , value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        print('<@') + str(message.author.id) + '> 님이 서버에서 [:내정보]이라고 했습니다.'
        return
    if message.content.startswith(':시간'):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        await message.channel.send(message.channel, str(a) + '년' + str(b) + '월' + str(c) + '일' + str(d) + '시' + str(e) + '분 입니다.')
        print('<@') + str(message.author.id) + '> 님이 서버에서 [:시간]이라고 했습니다.'
        return
    if message.content.startswith(":투표"):
        if message.content == ":투표" or message.content.replace(" ","") == ":투표":
            embed = discord.Embed(title="Vote Helper!",description=":투표 [주제]와 같이 주제를 입력해 주세요.", color=0x00aaaa)
            await message.channel.send(embed=embed)
            return
        topic = message.content.replace(":투표 ","")
        embed = discord.Embed(title="찬/반 투표",description=topic, color=0x00aaaa)
        msg1 = await message.channel.send(embed=embed)
        await msg1.add_reaction("\U00002705")
        await msg1.add_reaction("\U0000274C")
        await msg1.add_reaction("\U0001F3F3")
        await asyncio.sleep(5)
        msg2 = await message.channel.send("찬/반 투표를 시작합니다. 아래의 \U00002705,\U0000274C 반응을 눌러주세요. 진행자는 투표를 종료하시고 싶으면, \U0001F3F3 눌러서 투표를 종료해주세요.")
        author = message.author
        def check(reaction, user):
            return user == author and str(reaction.emoji) == "\U0001F3F3"
        reaction,user = await client.wait_for('reaction_add', check=check)
        await msg2.delete()
        if reaction.message.reactions[0].count > reaction.message.reactions[1].count:
            total = "찬성으"
        elif reaction.message.reactions[0].count == reaction.message.reactions[1].count:
            total = "중립으"
        elif reaction.message.reactions[0].count < reaction.message.reactions[1].count:
            total = "반대"
        answer = "```\n찬성: " + str(reaction.message.reactions[0].count) + "명\n반대: " + str(reaction.message.reactions[1].count) + "명\n```\n따라서, " + topic + "은 " + total + "로 되었습니다."
        embed = discord.Embed(title="투표 결과!",description=answer, color=0x00aaaa)
        await msg1.edit(embed=embed)
        print('<@' + str(message.author.id) + '> 님이 서버에서 투표명령어를 사용했습니다.')
        return
    if message.content.startswith(":Dm"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)
        print('<@' + str(message.author.id) + '> 님이 서버에서 개인메세지명령어를 사용했습니다.')
    

client.run('Njk1NTI3OTE0NTYwNTUzMDUw.Xobe2Q.VjfYCBWA8qBJ6svbHLEZajg8sDY')




