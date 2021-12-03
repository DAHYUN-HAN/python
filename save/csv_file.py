import csv

#newline='' : 자동 줄바꿈을 없애줌
#utf-8-sig : 한글 깨짐 방지
f = open('output1.csv', 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(f)
writer.writerow(["이름", "한다현"])
writer.writerow(["생년월일", "19970718"])
f.close()

info = [["이름", "한다현"], ["생년월일", "19970718"]]
with open('output2.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(info)