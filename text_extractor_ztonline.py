import requests
import json
with open("qa_03online.jsonl", "a") as f:
    i = 187
    cnt = 0
    while(i < 50000):
        res = requests.get(f"https://03online.com/news/{i}")
        if res.ok:
            text = res.content.decode("utf-8")
            if "https://www.google.com/recaptcha" in text:
                print("Captcha!")
                _ = input()
                continue
            question_urls = text.split("question-short-block")[1:]
            for question_url in question_urls:
                question_url = "https://03online.com{}".format(question_url.split('a href="')[1].split('"')[0])
                res2 = requests.get(question_url)
                if not res.ok:
                    continue
                text2 = res2.content.decode("utf-8")
                try:
                    question = text2.split("content question")[1].split("<!-- google_ad_section_start -->")[1].split('<div>')[1].split('</div>')[0].replace('<br>', '\n')
                    answer = text2.split("answer-block doctor-block")[1].split('content">')[1].split("</div>")[0].replace('<br>', '')
                    f.write(json.dumps({"q": question, "a": answer}) + '\n')
                    cnt+=1
                    print(cnt)
                except:
                    print("El problemo")
                    continue
            i+=1
            print(f"Page {i}")
        else:
            print("No data")
