# 実行は Ctrl+F5（デスクトップ-1363）
import os
import json
from twitter import *

# パスや設定、初期化など
UserIDPath = os.getenv('HOMEDRIVE') + os.getenv('HOMEPATH') + '\\OneDrive\\ドキュメント\\TwitterKey_b1017055.json'
TweetMessage = ''

# ユーザー情報を読み込み
temp = open(UserIDPath, 'r')
UserIDData = json.load(temp)
ConsumerKey = UserIDData['ConsumerKey']
ConsumerSecret = UserIDData['ConsumerSecret']
AccessToken = UserIDData['AccessToken']
AccessTokenSecret = UserIDData['AccessTokenSecret']

# Twitter関連
t = Twitter(auth=OAuth(AccessToken, AccessTokenSecret, ConsumerKey, ConsumerSecret))
t.statuses.update(status=TweetMessage)

# デバッグ出力空間
print(UserIDPath)
