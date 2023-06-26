s = open('24_1.txt').readline()
s = s.replace('A', ' ').replace('C', ' ') # заменяем ненужные символы на пробелы 

print(max(len(l) for l in s.split())) # генератор из кусков