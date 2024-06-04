import requests
import json
with open("qa_sprosivracha.jsonl", "a") as f:
    i = 1
    cnt = 0
    while(i < 1000):
        res = requests.get(f"https://sprosivracha.com/questions/{i}")
        if res.ok:
            text = res.content.decode("utf-8")
            if "https://www.google.com/recaptcha" in text:
                print("Captcha!")
                _ = input()
                continue
            questions = text.split("question_text")[1:]
            answers = text.split("answer_text")[1:]
            for question, answer in zip(questions, answers):
                question = question.split("<p>")[1].split("</p>")[0]
                answer = answer.split("<p>")[1].split("</p>")[0]
                f.write(json.dumps({"q": question, "a": answer}) + '\n')
                cnt+=1
                print(cnt)
            i+=1
            print(f"Page {i}")
        else:
            print("No data")
