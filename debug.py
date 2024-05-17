import text_to_speech as tts
import gui_contr as gc
import time

#tts.synthesize_speech("取得可能なドメイン名は、検索からそのまま申し込むことができます。")

#gc.write_comment("取得可能なドメイン名は、検索からそのまま申し込むことができます。")

#gc.expr_emote("qestion")
speaker = 0
text = "私は金沢大学のマスコットキャラクター候補として設定された金髪のアンドロイドです。まだ名前はありませんが、元気な女子大学生をイメージしたフレンドリーなキャラクターです。金沢大学のお知らせやキャンパスの情報など、お役に立てることがあれば何でもお聞きください！"
while True:
    print(speaker)
    tts.tester(text, speaker)
    speaker += 1
    time.sleep(3)
