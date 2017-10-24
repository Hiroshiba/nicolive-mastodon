## nicolive-mastodon
マストドンのトゥートを[HTML5コメントジェネレーター](http://www.kilinbox.net/2016/01/HCG.html)に流し込むツール。

```markdown
マストドン
　　↓
**nicolive-mastodon**  # これ！
　　↓
HTML5コメントジェネレーター
　　↓
（OBS Studioなどの外部配信ツール）
　　↓
ニコニコ生放送
```

### 実行方法

#### windows
最新版の.exeをダウンロード＆実行します。[exeファイル配布場所](https://github.com/Hiroshiba/nicolive-mastodon/releases)

マストドンのアカウントとパスワードを入力すると使用可能になります。

#### その他のOS
pythonコードをダウンロード＆実行します。

```bash
# download
git clone git@github.com:Hiroshiba/nicolive-mastodon.git

# run
python run.py
```

### 設定方法
設定ファイル（config.json）を編集することで設定できます。

```json
{
  "api_base_url": "ここにマストドンのURLを入力します。例：https://mstdn.jp",
  "path_html5_comment_generator": "ここにHTML5コメントジェネレーターのディレクトリパスを指定します。",
  "execute_command": [
    "実行したいコマンドを書いておくと、トゥートが読み込まれるたびに実行します。",
    "例： ./softalk/SofTalk.exe /W:{user}）{text}",
    "↑の例だと、ユーザー名とテキスト内容をSofTalk.exeで読み上げます。"
  ],
  "highlight":  [
    "トゥートを絞り込む単語を指定できます",
    "無指定だとすべてのトゥートを取り込みます。"
  ]
}
```

### ライセンス
[MITライセンス](./LICENSE)です。
