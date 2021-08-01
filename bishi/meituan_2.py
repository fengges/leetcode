import sys
line= sys.stdin.readline().strip()

low=[l for l in line if l.islower()]
print(abs(len(line)-2*len(low))//2)