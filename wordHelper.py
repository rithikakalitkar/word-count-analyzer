import os
import socket


def count_words(file_name):
    with open(file_name, 'r') as f1:
        lines = f1.readlines()
        word_count = sum([len(l.split()) for l in lines])
    return word_count


def list_top3_words(file_name):
    word_rep = {}
    with open(file_name, 'r') as f1:
        lines = f1.readlines()
        for line in lines:
            words = line.split()
            for word in words:
                if word.lower() in word_rep.keys():
                    word_rep[word.lower()] += 1
                else:
                    word_rep[word.lower()] = 1

    sorted_word_rep = sorted(word_rep.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_rep[:3]
    return [sorted_word_rep[0][0], str(sorted_word_rep[0][1]), sorted_word_rep[1][0], str(sorted_word_rep[1][1]), sorted_word_rep[2][0], str(sorted_word_rep[2][1])]


def get_ip_address():
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    return ip_addr

os.mkdir('output')
outFile = open("output/result.txt", 'w')
allFiles = os.listdir("/home/data")
txtFiles = []
for file in allFiles:
    if ".txt" in file:
        txtFiles.append("/home/data/" + file)
outFile.write("Txt files at the locations /home/data: " + ", ".join(txtFiles) + "\n")
total_word_count = 0
for fileName in txtFiles:
    word_count = count_words(fileName)
    outFile.write("Word Count in " + fileName + " is " + str(word_count) + "\n")
    top_3_words = list_top3_words(fileName)
    outFile.write("Top 3 words with their wordCount :" + "\n")
    for i in top_3_words:
        outFile.write(i[0] +" : " +str(i[1]) +"\n")


    total_word_count += word_count
outFile.write("Total number of words in both the files: " + str(total_word_count)+"\n")
outFile.write("IpAddress: " + str(get_ip_address()))
outFile.close()

with open("output/result.txt", 'r') as file:
    for line in file.readlines():
        print(line)