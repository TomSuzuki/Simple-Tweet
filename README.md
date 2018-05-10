# Simple Tweet
Tweetするだけのプログラムです。  
Ctrl+Enter：ツイート  
Esc：取り消し  

改行はできません。
文字列だけ送ることができます。  

使用する場合はmain.pyのスクリプトにあるUserIDPathの場所に以下の形式でTwitterの情報を書いてください。  
  
  
temp.json  
~~~~
{
"UserID": "@*****",  
"ConsumerKey": "**************",  
"ConsumerSecret": "***********",  
"AccessToken": "********-*********************",  
"AccessTokenSecret": "***********************"  
}  
~~~~
  
windowsなら
start.exeから start.vbs を開き、start.batを開いてmain.pyを実行できます。
