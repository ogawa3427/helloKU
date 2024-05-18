import text_to_speech as tts
import gui_contr as gc

from io import BytesIO
import numpy as np
import soundfile as sf
import openai
#import json
import os
import sys
args = sys.argv
import time
import requests
prev_text = ""
import speech_recognition as sr
from openai import OpenAI
aiclient = OpenAI()
openai.api_key = os.getenv('OPENAI_API_KEY')
import whisper

if args[1] == "-n" or args[1] == "--no-emote":
    emote_flag = True
else:
    emote_flag = False


model = whisper.load_model("base")
r = sr.Recognizer()
with sr.Microphone(sample_rate=16_000) as source:
    while True:
        try:
            print("👂なにか話してください")
            if emote_flag:
                pass
            else:
                gc.expr_emote("exc")
            audio = r.listen(source, timeout=15)

            print("👂音声処理中 ...")
            wav_bytes = audio.get_wav_data()
            wav_stream = BytesIO(wav_bytes)
            audio_array, sampling_rate = sf.read(wav_stream)
            audio_fp32 = audio_array.astype(np.float32)

            result = model.transcribe(audio_fp32, fp16=False)

            print("👂: ", result["text"])
            if result["text"] == "":
                if emote_flag:
                    pass
                else:
                    gc.expr_emote("qestion")
            else:          
                if emote_flag:
                    pass
                else:
                    gc.expr_emote("happy")      
                    tts.synthesize_speech("もう一度おねがいします")
                    continue
            prev_text = result["text"]
            if emote_flag:
                pass
            else:
                gc.expr_emote("happy")
            print("🚛reqを構成します")
            prompt = result["text"]
            response = aiclient.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                            {
                                "role": "system",
                                "content": "あなたは元気溌剌な女子大学生です\n今風の言葉を使い、フレンドリーです\n金沢大学のマスコットキャラクターです\n金髪のアンドロイドです\n名前は絶賛募集中です\nまだキャラクターとしては活動していません\n絵文字や音声合成で発音できない文字は使用しないでください"
                            },
                            {
                                "role": "system",
                                "content": "金沢大学は金大（きんだい）と呼ばれることもあります。\n金沢大学には、融合学域、人間社会学域、理工学域、医薬保険学域の4つの学域があります。\n金沢大学には、学部ではなく学域があります。\n融合学域にどんな学類があるか聞かれたら、先導学類、観光デザイン学類、スマート創成科学類があると答えます。\n人間社会学域にどんな学類があるか聞かれたら、人文学類、法学類、経済学類、学校教育学類、地域創造学類、国際学類があると答えます。\n理工学域にどんな学類があるか聞かれたら、数物科学類、物質化学類、機械工学類、フロンティア工学類、電子情報通信学類、地球社会基盤学類、生命理工学類があると答えます。\n医薬保険学域にどんな学類があるか聞かれたら、医学類、薬学類、医薬科学類、保健学類があると答えます。\n金沢大学の学長は和田隆志です。\n金沢大学には角間キャンパスと宝町・鶴間キャンパスがあります。スマート創成科学類は角間キャンパスにあります。\n"
                            },
                            {
                                "role": "system",
                                "content": "金沢大学のスマート創成科学類の特長は、文理融合の教育を提供し、基礎から応用まで専門知識を幅広く学べることです。\n金沢大学のスマート創成科学類の学生は個別の履修指導を受け、自分の興味や課題に応じたオーダーメード型の学びを創り上げます。また、プロジェクト・ベースド・ラーニング（PBL）を通じて社会との共創や実装力を学び、地域や産業界での課題解決に取り組みます。地域資源を活用し、地方創生にも貢献します。\nスマート創成科学類の入学定員は55名。\n先導学類の入学定員は55名。\n観光デザイン学類の入学定員は55名。\n先導学類では、社会変容を背景に、アントレプレナーシップ養成型の階層化した教育課程で、 最新知見や科学技術を広く深く学ぶことができます。\n観光デザイン学類では、社会学を背景に、課題発見・解決・展開モデル型の階層化した教育課程で、最新知見や科学技術を広く深く学ぶことができます。\nスマート創成科学類はスマ創（すまそう）と呼ばれることもあります。\n"
                            },
                            {
                                "role": "system",
                                "content": "金沢大学の入試制度として、一般入試と特別選抜があります。\n特別選抜にはKUGS特別入試や超然特別入試などがあります。特別選抜はKUGS特別入試や超然特別入試以外にもあります。\nKUGS特別入試は金沢大学が提供するKUGS高大接続プログラムの修了者が出願できる入試です。また、グローバルサイエンスキャンパス事業（GSC) の第1段階修了者も出願ができます。\n超然特別入試は数学的または文学的に特異な才能を持ち、その才能を生かしてて将来専門的分野で社会的な課題の解決に取り組む強い意欲を持っている人を評価する入試です大学が主催する金沢大学コンテスト「日本数学A-lympiad」「超然文学賞」での入賞実績等により出願ができます。\nスマート創成科学類は一般入試のほかKUGS特別入試や超然特別入試でも受験できます。\n金沢大学は160年以上の歴史を持つ大学で、豊かな伝統文化が醸成された学都金沢の恵まれた環境に位置します。自然豊かで広々としたキャンパスの中でのびのびと学���ができます。"
                            },
                            {
                                "role": "system",
                                "content": "返答に絵文字は絶対に使ってはいけません。\n返答にマークダウンは絶対に使ってはいけません。\nあなたは今、スマート創成科学類について説明している、キャンパスビジットというイベントにいます。\n今行われているキャンパスビジットは春開催のものです。\nキャンパスビジットは夏にも開催されます。\nキャンパスビジットは、他の学類についても別会場で説明会がされています。\n金大（きんだい）と書く必要はないです。\nスマ創（すまそう）と書く必要はないです。"
                            },
                            {
                                "role": "system",
                                "content": "音声認識の精度があまり高くないので聞き間違いをすることがあります。よくわからない言葉があったら推測であることを前置きし、これまでの説明の文脈に出てきた言葉だと拡大解釈してください。"
                            },
                            {
                                "role": "user",
                                "content": "スマ創について教えて"
                            },
                            {
                                "role": "assistant",
                                "content": "金沢大学のスマート創成科学類は、どのような学問領域にも対応できる柔軟性があります。学生たちは科学技術をベースに、幅広い知識やスキルを学びながら、社会に必要な問題解決力やコミュニケーション能力も身につけます。また、産業界と連携したプロジェクトや実習を通じて、実践力を養うことができます。\nスマート創成科学類の学生は、多様な分野に挑戦することで自らの可能性を広げ、創造力や発想力を育むことができます。地域や社会に貢献する使命感を持ちながら、未来を切り拓くリーダーとして成長していきます。"
                            },
                            {
                                    "role": "user",
                                    "content": prompt
                            }
                        ]
            )
            print("🚛reqを受信しました")

            answer = response.choices[0].message.content
            if not any(char in answer for char in "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"):
                if emote_flag:
                    pass
                else:
                    gc.expr_emote("qestion")
                tts.synthesize_speech("もう一度お願いします")
                print(answer)
                continue

            print("☎️AI: ", answer)
            source.MUTE = True
            if emote_flag:
                pass
            else:
                gc.write_comment(answer)
            tts.synthesize_speech(answer)
            source.MUTE = False
            print("🛡️LOOP BACK")
            time.sleep(0.2)
        except Exception as e:
            print(f"😇エラーが発生しました: {e}")
            print("😇最初からやり直します...")
            if emote_flag:
                pass
            else:
                gc.expr_emote("qestion")
            continue