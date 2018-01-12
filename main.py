import os
import sys
import json
import tkinter
from twitter import *

# 終了動作
def EscapeKey(event):
    print('終了コマンドが送られました。')
    sys.exit()

# 実行動作
def ReturnKey(event):
    TweetMessage = EditBox.get()
    print("ツイートします："+TweetMessage)
    t = Twitter(auth=OAuth(AccessToken, AccessTokenSecret, ConsumerKey, ConsumerSecret))
    t.statuses.update(status=TweetMessage)
    sys.exit()

if __name__ == '__main__':
    # 取得＆設定
    UserIDPath = os.getenv('HOMEDRIVE') + os.getenv('HOMEPATH') + '\\OneDrive\\ドキュメント\\TwitterKey_0x0553.json'
    temp = open(UserIDPath, 'r')
    UserIDData = json.load(temp)
    UserID = UserIDData['UserID']
    ConsumerKey = UserIDData['ConsumerKey']
    ConsumerSecret = UserIDData['ConsumerSecret']
    AccessToken = UserIDData['AccessToken']
    AccessTokenSecret = UserIDData['AccessTokenSecret']

    # windowの設定
    window = tkinter.Tk()
    window.title('Simple Tweet（UserID：'+UserID+'）')
    window.geometry('640x48+0+0')
    window.maxsize(640, 48)
    window.minsize(640, 48)

    # オブジェクト
    label = tkinter.Label(window, text="★ ツイート内容の入力 ★ ")
    label.place(x=2, y=4)
    label2 = tkinter.Label(window, text="Created by TomSuzuki \nat 2018")
    label2.place(x=490, y=10)
    EditBox = tkinter.Entry(window, width='52', font=('游ゴシック', 12))
    EditBox.place(x=0, y=24)
    EditBox.focus_set()

    # 動作設定
    window.bind('<Escape>', EscapeKey)
    window.bind('<Control-Return>', ReturnKey)

    window.mainloop()


