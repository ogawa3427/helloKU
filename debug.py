import text_to_speech as tts
import gui_contr as gc
import time

#tts.synthesize_speech("取得可能なドメイン名は、検索からそのまま申し込むことができます。")

#gc.write_comment("取得可能なドメイン名は、検索からそのまま申し込むことができます。")

#gc.expr_emote("qestion")
speakers = [
    {
        "name": "めたん",
        "type": "ノーマル",
        "id": 2
    },
    {
        "name": "ずんだ",
        "type": "ノーマル",
        "id": 3
    },
    {
        "name": "つむぎ",
        "type": "ノーマル",
        "id": 8
    },
    {
        "name": "はう",
        "type": "ノーマル",
        "id": 10
    },
    {
        "name": "りつ",
        "type": "ノーマル",
        "id": 9
    },
    {
        "name": "ひまり",
        "type": "ノーマル",
        "id": 14  
    },
    {
        "name": "そら",
        "type": "ノーマル",
        "id": 16   
    },
    {
        "name": "もちこ",
        "type": "ノーマル",
        "id": 20 
    },
    {
        "name": "WhileCUL",
        "type": "ノーマル",
        "id": 23
    },
    {
        "name": "鬼",
        "type": "人間",
        "id": 27
    },
    {
        "name": "7",
        "type": "ノーマル",
        "id": 29
    },
    {
        "name": "7",
        "type": "アナウンス",
        "id": 30
    },
    {
        "name": "みこ",
        "type": "ノーマル",
        "id": 43   
    
    },
    {
       "name": "さよ",
        "type": "ノーマル",
        "id": 46
    },
    {
        "name": "なな",
        "type": "ノーマル",
        "id": 54
    },
    {
        "name": "ねこつかいある",
        "type": "ノーマル",
        "id": 55
    },
    {
        "name": "ねこつかいぴい",
        "type": "ノーマル",
        "id": 58
    },
    {
        "name": "うさぎ",
        "type": "ノーマル",
        "id": 61
    },
    {
        "name": "まろん",
        "type": "ノーマル",
        "id": 67
    },
    {
        "name": "あいえるたん",
        "type": "ノーマル",
        "id": 68
    },
    {
        "name": "にあ",
        "type": "ノーマル",
        "id": 74
    }
]

text = "私は金沢大学のマスコットキャラクター候補として設定された金髪のアンドロイドです。まだ名前はありませんが、元気な女子大学生をイメージしたフレンドリーなキャラクターです。金沢大学のお知らせやキャンパスの情報など、お役に立てることがあれば何でもお聞きください！"

while True:
    input_text = input("type here:")
    tts.tester(text, input_text)

for speaker in speakers:
    print(speaker["name"])
    print(speaker["type"])
    print(speaker["id"])
    tts.tester(text, speaker["id"])
    time.sleep(3)
