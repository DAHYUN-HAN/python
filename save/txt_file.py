from os import write


info = [["이름", "한다현"], ["생년월일", "19970718"]]

#utf-8 : 한글깨짐 방지
with open('output.txt', 'w', encoding = 'utf-8') as file:
    for line in info :
        write_line = line[0] + '\t' + line[1] + '\n'
        file.write(write_line)