from urllib.request import urlopen
shakespeare=urlopen('http://composingprograms.com/shakespeare.txt')
# print(shakespeare)
words=set(shakespeare.read().decode().split())

{w for w in words if len(w)==6 and w[::-1] in words}