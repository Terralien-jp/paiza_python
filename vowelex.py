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
