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

# なんか納得行かないｗ
N = int(input())
for i in range(1, N+1):
    for j in range(1, i+1):
        if j == i:
            print(j)
        else:
            print(j, end=" ")
            
# 微妙に納得行かないｗ
N = int(input())

M = [0] * N
values = input().split()
# listにintでvaluesを代入していく（listをint化するため？）
for i in range(N):
    M[i] = int(values[i])
# 二重ループ処理、以降は前の問題と同じ
for i in range(N):
    for j in range(1, M[i] + 1):
        # 最大値を比較する対象がM[i]の値となる
        if j == M[i]:
            print(j)
        else:
            print(j, end=" ")

# B相当の問題らしい↑の問題の応用で解ける※変数名がクソなのはいつものこと
N = input().split() #標準入力1行目（N[1]のみ使った）
M = input().split() #標準入力2行目
K = [0] * int(N[1]) # [0, 0, 0, 0]
# 標準入力3行目をlistにする（split()を使用するためにこの時点ではstr）
values = input().split()
# int型listに変換してる感じ
for i in range(int(N[1])):
    K[i] = int(values[i])
# 出力用カウント変数
L = 0

# 今回のハマリポイントややこしいことせずにこれだけで解ける
# 他の言語で言うところのforeachでイテラブルオブジェクトK[2, 6, 1, 1]が順に代入される
for i in K:
    for j in range(i):
        if j == i - 1:
            print(M[L])
        else:
            print(M[L], end=" ")
        L += 1

# 辞書を使った文字変換
m = {'A':'4',  'E':'3', 'G':'6'}
t = ''.join(m.get(c, c) for c in s)

# 罫線あり九九
i = 1
for i in range(1,10):
	for j in range(1,10):
	    if j == 9:
	        k = i * j
	        print("{: >2}".format(k))
	    else:
	        k = i * j
	        print("{: >2} | ".format(k), end="")
# こういう手もある
        # print("{: >2}".format(i * j), end="")
        # if j == 9:
        #     print()
        # else:
        #     print(end=" | ")
	if i < 9:
	    print("=" * (9 * 2 + 3 * (9-1)))

### in演算子
if 0 in a:
    print("NO")
else:
    print("YES")

### ソートする問題
n = int(input())
num = [int(x) for x in input().split()]
num.sort()
print(*num, sep=', ')


### 内包表記でかいけつ

text= input()
def n_gram(text, n):
    return [ text[idx:idx + n] for idx in range(len(text) -n + 1)]

print(n_gram(text, 1))

print(n_gram(text, 2))

print(n_gram(text, 3))


## 力技

text = input()

ret = []
ret2 = []
ret3 = []
for i in range(len(text)):
    ret.append(text[i])
print(ret)
    
for i in range(len(text) -1):
    ret2.append(text[i:i+2])
print(ret2)

for i in range(len(text) -2):
    ret3.append(text[i:i+3])
print(ret3)

## while 2で何回割り切れるか

n = int(input())
even = 0
while n % 2 == 0:
        even += 1
        n /= 2
print(even)


## n進数に変換

N,M=map(int,input().split())

array=[]
while N>=1:
    array.append(N%M)
    N/=M
    N=int(N)

array=list(reversed(array))

answer=0

for num in array:
    answer*=10
    answer+=num
    
print(answer)

## n!の末尾に０がいくつ付くか？
###実は因数分解の問題のためn/5がいくつあるかをカウントする

n = int(input())
count_zero = 0
while n > 0:
    count_zero += int(n / 5)
    n /= 5
print(count_zero)

### enumarate
enemies = ["スライム", "モンスター", "ゾンビ", "ドラゴン", "魔王"]
# ここに、要素をループで表示するコードを記述する
for (i, number) in enumerate(enemies):
    print(str(i+1) + "番目の"+ number +"が現れた")

### append
# 各要素を3倍にして新しいリストを作成する
numbers = [12, 34, 56, 78, 90]

# ここに、各要素を3倍にして新しいリストを作成するコードを記述する
numbers2 = []
for i in numbers:
    numbers2.append(i * 3)

print(numbers2)

# ドットで文字を出力しよう

letter_A = [[0,0,1,1,0,0],
            [0,1,0,0,1,0],
            [1,0,0,0,0,1],
            [1,1,1,1,1,1],
            [1,0,0,0,0,1],
            [1,0,0,0,0,1]]

# ここに、ドットを表示するコードを記述する
for list in letter_A:
    for dot in list:
        if dot == 1:
            print("@", end="")
        elif dot == 0:
            print(" ", end="")
    print("")
print()

# 2次元リストで画像を配置
# 標準入力内容

1,1,1,1
0,0,0,0
2,3,4,2
_

# 画像用リスト
players_img = [
    "Empty.png",
    "Dragon.png",
    "Crystal.png",
    "Hero.png",
    "Heroine.png"]
    
team = []
while True:
    line = input()
    if line == "_":
        break
    team.append(line.split(","))

print("<table>")
for line in team:
    print("<tr>")
    for person in line:
        print("<td><img src='" + players_img[int(person)] + "'></td>")
    print("</tr>")
print("</table>")

# list初期化して値を入れてく方法

N = int(input())

A = [0] * N
values = input().split()
for i in range(N):
    A[i] = int(values[i])

for a in A:
    print(a)

# flagで判定

n = [10, 13, 21, 1, 6, 51, 10, 8, 15, 6]
flag = False
for i in n:
    if i == 6:
        print("Yes")
        flag = True
        break
if not flag:
    print("No")

# 二次元配列を二重ループで出力
li = [[6, 5, 4, 3, 2, 1], [3, 1, 8, 8, 1, 3]]

for i in range(len(li)):
    for j in range(len(li[i])):
        print(li[i][j], end="")

        if j < len(li[i]) - 1:
            print(end=" ")
        else:
            print()

# 二次元配列の入力など
n, m, k, l = map(int, input().split())
# 二次元配列のから配列を作成
list = [[0] * m for i in range(n)]
# 空の二次配列に標準入力から値を入れていく
for i in range(n):
    value = input().split()
    for j in range(m):
        list[i][j] = int(value[j])
# 完成した二次元配列から指定された部分を表示
print(list[k-1][l-1])

# tmpを使って入れ替え
a, b = map(int, input().split())

tmp = a
a = b
b = tmp

print(a, b)

# 配列内で入れ替え
A, B, N = map(int, input().split())
a = [int(x) for x in input().split()]

a[A-1], a[B-1] = a[B-1], a[A-1]
for ele in a:
    print(ele)

# スライスを用いる
A, B, N = map(int, input().split())
a = [int(x) for x in input().split()]
# A-1からBの範囲をスライスして出力
for ele in a[A-1:B]:
    print(ele)

# 配列を逆に
n = int(input())
list = [int(x) for x in input().split()]
lists = reversed(list)
for i in lists:
    print(i)

# count関数使えってことだったらしい
N, M = map(int, input().split())
A = [int(x) for x in input().split()]

print(A.count(M))

# 要素の削除
n, m = map(int, input().split())
list = [int(x) for x in input().split()]
del list[m-1]
for i in list:
    print(i)

# 要素の挿入
N, M, K = map(int, input().split())
list = [int(x) for x in input().split()]
list.insert(M-1, K)
for i in list:
    print(i)

# 並び替えて重複を除くsortしてset
list = [1, 3, 5, 1, 2, 3, 6, 6, 5, 1, 4]
sort = sorted(set(list))
for i in sort:
    print(i)

# マンハッタン距離とか言うのを使用し点2.3からの各点の距離を求める
N = int(input())
x = [0] * N
y = [0] * N
for i in range(N):
    value = input().split()
    x[i] = int(value[0])
    y[i] = int(value[1])

for i in range(N):
    print(abs(x[i]-2) + abs(y[i]-3))

# フィボナッチ数
# リスト数入力と初期化
N = int(input())
list = [0] * N
# 1以下はこういう決まり
list[0] = 0
list[1] = 1

for i in range(2, N):
    # 2以降はこういう決まり
        list[i] = list[i-2] + list[i-1]

for i in list:
    print(i)

# ブランク明けて横並び出力
n = int(input())
for i in range(1, n + 1):
    if i != n:
        print(i, end=" ")
    else:
        print(i)

# N行K列出力する二重ループ
N, K = map(int, input().split())
for i in range(1, K+1):
    for i in range(1, N+1):
        if i == N:
            print(i)
        else:
            print(i, end=" ")
print()

# 二次元配列、なんか2行目のKは_でもいけるっぽい習った気がするけど忘れた…
# この場合戻り地を保存しないとのこと

N, K = map(int, input().split())
list = [input().split() for K in range(N)]
# list = [input().split() for _ in range(N)]

for i in range(N):
    for j in range(K):
        if j == K-1:
            print(list[i][j])
        else:
            print(list[i][j], end=" ")
print()

# なんかしらんけどnとk逆にしててはまってた
n, k = map(int, input().split())
a = [input().split() for _ in range(n)]

for i in range(n):
    for j in range(k):
        if a[i][j] == "1":
            print(i + 1, j + 1)
            break

# 正解したもののもうちょいスマートにやれる模様
N, K = map(int, input().split())
# ここを工夫するとint化するためにvalue変数作らずにすむ
list = [input().split() for _ in range(N)]
maxvalue = 0
for i in range(N):
    for j in range(K):
        value = int(list[i][j])
        if value >= maxvalue:
            maxvalue = value
print(maxvalue)

# sum使わない模様
N, K = map(int, input().split())
list = [[int(i) for i in input().split()] for _ in range(N)]
for i in range(N):
    print(sum(list[i]))

# 1列目を除外するのにifを使った
N = int(input())
list = [[int(i) for i in input().split()] for _ in range(N)]
for i in list:
    value = 0
    for j in range(len(i)):
        if j != 0:
            value += i[j]
    print(value)

#スライスを使う方法もある模様
n = int(input())

for _ in range(n):
    k_a = [int(i) for i in input().split()]
    # nで良かろうものをkとして定義
    k = k_a[0]
    # 配列の１～をaに代入
    a = k_a[1:]
    # （列の）合計値初期化
    s = 0
    for i in range(k):
        s += a[i]
    print(s)

# Nの階段作るやつ
N = int(input())
for i in range(1, N+1):
    # 列をiまで繰り返す（範囲を１～i（i+1)とする）
    for j in range(1, i+1):
        # 最大範囲が列の末となる
        if j == i:
            print(j)
        else:
            print(j, end=" ")

# 掛けた数字が0以下のこともあるんやでｗとかいうクソトラップにハマったが取りうる最大値（最小値）を初期化するすべを学んだ
N, K = map(int, input().split())
listN = [int(i) for i in input().split()]
listK = [int(i) for i in input().split()]

maxvalue = -10000

for i in range(N):
    for j in range(K):
        value = listN[i] * listK[j]
        if value > maxvalue:
            maxvalue = value
print(maxvalue)

# てっきり配列の行列を入れ替える問題かと思ったら出力を入れ替えるだけの問題だった
N, K = map(int, input().split())
list = [input().split() for _ in range(N)]
for i in range(K):
    for j in range(N):
        if j == N -1:
            print(list[j][i])
        else:
            print(list[j][i], end=" ")

# かけ算表を作る問題　listの宣言方法をミスっていた。知識として0ではなくnoneを指定する方法があることを学んだ。
n = int(input())
a = [int(i) for i in input().split()]
# 0ではなくnoneでも可
list = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        list[i][j] = a[i] * a[j]

for i in range(n):
    for j in range(n):
        if j == n-1:
            print(list[i][j])
        else:
            print(list[i][j], end=" ")

# 素数カウント
n = int(input())
# カウント変数の初期化
ans = 0
# 1は素数の条件に含まれるので２からSTART
for i in range(2, n + 1):
    # ループ完了管理フラグ
    is_prime = True
    # i ** (1/2) で割り切れなければ素数
    for j in range(2, int(i ** (1 / 2)) + 1):
        # Nの値まで２重ループを回したのでループ終了
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        ans += 1

print(ans)

# log2　２が素数であることを利用した解き方
n = int(input())

ans = 0
for i in range(1, n + 1):
    now = i
    # ２で割り切れる時にカウントする
    while now % 2 == 0:
        now //= 2
        ans += 1

print(ans)

# ただのFIZZBUZZ
hour = 24
minit = 60
for i in range(hour):
    for j in range(minit):
        if (i + j) % 3 == 0 and (i + j) % 5 == 0:
            print('FIZZBUZZ')
        elif (i + j) % 3 == 0:
            print('FIZZ')
        elif (i + j) % 5 == 0:
            print('BUZZ')
        else:
            print()
# 突然の格子点
max = 0
for x in range(1, 99):
    for y in range(1, 99 - x):
        if max < x * y and x ** 3 + y ** 3 < 100000:
           max = x * y
print(max)

# 通貨の最小支払い枚数を求める
X, Y, Z = map(int, input().split())
# 1白石で支払う場合（最大枚数だがXとYが0の場合最小枚数になり得る）
minmai = Z
# 2重ループで通過XとYの枚数をカウント
for i in range(Z // X + 1):
    # 0ということもあり得る
    for j in range(Z // Y + 1):
        # X、Y通貨で支払った残りをvalueとして求める
        if i * X + j * Y <= Z:
            value = Z - i * X - j * Y
            # 最小枚数の更新ループ
            if i + j + value < minmai:
                minmai = i + j + value
print(minmai)

# フラグ使って直角三角形あるかどうか探すやつ
N = int(input())
flag = False

for b in range(1, N):
    for c in range(1, N - b):
        a = N - b - c
        # ここで颯爽と三平方の定理さんが登場！
        if a ** 2 == b ** 2 + c **2:
            flag = True
            
# フラグ管理について新たな知見を得た          
if flag:
    print("YES")
else:
    print("NO")

# ただカウントしただけ
n = int(input())
list = [int(i) for i in input().split()]
k = int(input())
count = 0
for i in range(n):
    if list[i] == k:
        count += 1
print(count)

# flagもvalueも不要な冗長版クソコード
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())
flag = False
for i in range(n):
    if a[i] == k:
        flag = True
        value = i + 1
        break
if flag:
    print(value)
else:
    print(0)

# list.index()を使うと楽かもしれん
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

if k in a:
    print(a.index(k) + 1)
else:
    print(0)

# index_kは最終的に条件にあったものに上書きされるからこれでええやろとおもったら正解するも微妙に違うぽい
n = int(input())
list = [int(i) for i in input().split()]
k = int(input())

index_k = 0
for i in range(n):
    if list[i] == k:
        index_k = i+1

print(index_k)

# rangeで逆向きに指定？
n = int(input())
a = [int(x) for x in input().split()]
k = int(input())

index_of_k = 0
# range(start, stop[, step])
for i in range(n - 1, -1, -1):
    if a[i] == k:
        index_of_k = i + 1
        break

print(index_of_k)

# 簡単
n = int(input())
list = [int(i) for i in input().split()]
k = int(input())
for i in range(n):
    if list[i] == k:
        print(i+1)

# max, min
list = [int(i) for i in input().split()]
print(max(list), min(list))

# list.sort()を使うと最小値が左先頭に来る[0]、最大値は最後になる[-1]
n = int(input())
a = [int(x) for x in input().split()]

a.sort()

print(a[-1], a[0])

# iではなく変数噛ませたほうが無難
n = int(input())
list = [int(x) for x in input().split()]
for i in range(n):
    if list[i] % 2 == 0:
        break
print(i+1)