# Tweet内容を入力するための画面
import tkinter
import sys

# 終了動作
def EscapeKey(event):
    print('終了コマンドが送られました。')
    sys.exit()

# 実行動作
def ReturnKey(event):
    TweetMsg = EditBox.get()
    print("ツイートします："+TweetMsg)
    sys.exit()

# 取得＆設定
UserID = ""

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

# 動作設定
window.bind('<Escape>', EscapeKey)
window.bind('<Control-Return>', ReturnKey)

window.mainloop()


