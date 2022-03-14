#母音を変数に 
vowel = 'aeiouAEIOU'
#標準入力
name = input()
#cname変数に母音じゃないものをjoinしていって出力
#'間に挿入する文字列'.join([連結したい文字列のリスト])
cname = ''.join(s for s in name if s not in vowel)
print(cname)

#複数行の入出力
input_line = int(input())
for i in range(input_line):
    n = input()
    print(n)

# 繰り返し出力
input_line = 'one two three four five'
n = input_line.split()
for i in n:
    print(i)

# tomato_counter
lerning = 25
rest = 5
tomato = lerning + rest
print("トータル勉強トマト")
tomats = int(input())

total_tomato = tomato * tomats
print(str(tomato / 60) + "時間勉強した")

# 配列内配列動くけど力技過ぎて納得行かない
n = int(input())
m = [input().split() for _ in range(n)]
for i in range(n):
    # m[i]のままだと上手くdelできないので別の変数に
    o = m[i]
    # listの先頭を除去（求められた仕様）
    del o[0]
    # listを並列して出力するおまじない
    o=' '.join(o)
    print(o)

# 1 - 100 までの数値を間に空白をあけつつ出力する。ただし最後の数値には空白をつけない。
for i in range(100):
    if i != 99:
        print(i + 1, end=" ")
    else:
        print(i + 1)

# 標準入力からの100の文字列を空listに追加する。
str = []
for i in range(100):
    str.append(input())

# 3行3列を出力するコード。自分で書いてクソみたいだなと思ってたらほぼ正解で困惑。
n = input().split()
for i in range(len(n)):
    if (i+1) % 3 == 0:
        print(n[i])
    else:
        print(str(n[i])+' ', end='')

# ２重ループで9*9出力するコード
i = 1
while i <= 9:
	j = 1
	while j <= 9:
		print(i * j, end=" ")
		j = j + 1
    #空printは改行
	print()
	i = i + 1

# 同じく
for i in range(1,10):
	for j in range(1,10):
	    if j == 9:
	        print(i*j)
	    else:
	        print(i*j, end=" ")

# 自分ではクソコードだと思ってるのにほぼあってたときの悲しみ
n = input().split()
for i in range(1,int(n[0])+1):
    if i % int(n[0]) == 0:
        print(n[0])
    else:
        print(i, end=" ")
for j in range(1,int(n[1])+1):
    if j % int(n[1]) == 0:
        print(n[1])
    else:
        print(j, end=" ")