#母音を変数に 
vowel = 'aeiouAEIOU'
#標準入力
name = input()
#cname変数に母音じゃないものをjoinしていって出力
cname = ''.join(s for s in name if s not in vowel)
print(cname)
