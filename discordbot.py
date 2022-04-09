# インストールした discord.py を読み込む
# py -3 -m pip install -U discord.py[voice]
# py -3 xxxxxx\discordbot.py
import discord
from discord.ext import commands

# ========================================
# Botのアクセストークン
# ========================================
TOKENS = {}
TOKEN_SELECTOR = ""

# ========================================
# チャットID
# ========================================
GET_CHANNEL_ID = 0  # 送信用チャンネル
POST_CHANNELS = {
    "": 0,
}
CHANNEL_SELECTOR = ""

# 接続に必要なオブジェクトを生成
client = discord.Client()


@client.event
# bot起動時に実行されるイベントハンドラを定義
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


@client.event
# メッセージを受け取った際のイベント
async def on_message(message: discord.Message):

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    channel: discord.channel.TextChannel = message.channel

    # 送信用チャンネルかを確認
    if channel.id != GET_CHANNEL_ID:
        return

    # 送信先チャンネルを設定
    target_channel = client.get_channel(POST_CHANNELS[CHANNEL_SELECTOR])
    target_channel: discord.channel.TextChannel = target_channel

    # 送信用チャンネルから受け取った内容を送信
    await target_channel.send(message.content)

# Botの起動とDiscordサーバーへの接続
client.run(TOKENS[TOKEN_SELECTOR])
