# paiza_python
競技用Pythonのチートコード

## 標準入力
### 複数行
```python
n = [input() for _ in range()]
```

### 一行に複数入力
```python
n = input().split()
print(n[0])
print(n[1])
```

### map()
```python
a, b = map(int, input().split())
```

### map()じゃあかんのか？
```python
a, b = [int(x) for x in input().split()]
```

## 標準出力
### 文字列に変換
str() 

### 絶対値
abs()

### 小文字を大文字
```python
print(input_line.upper())
```

### 改行文字をなくして連結する
```python
print("令和" + str(reiwa) + "年", end="")
print(str(month) + "月")
令和4年3月
```

### len関数
```python
tea = ["緑茶", "紅茶", "烏龍茶"]
print(len(tea))
3
```

### del list内要素を削除
```python
del o[0]
```

### join() list内容を横に並べて出力
出力する数字の間にブランクを挿入している
```python
o=' '.join(o)
```

### 引数なしのprint()
改行として扱われる

### sep 配列を1要素ずつカンマ区切りで出力
```python
print(*n, sep=",")
```

#### 別解答 .join() メソッドを使う
```python
print(",".join(S))
```

### .format() を使用して1000の位にカンマ区切り
```python
n = '{:,}'.format(1000)
```

### 3文字スライス
```python
print(n[:3])
```

### 桁数の表示
```python
print(len(str(n)))
```
### .format()メソッドを使用して小数点3桁固定
```Python
print('{:.3f}'.format(N))
```

### .format()は複数の引数が使える。また左から引数が対になるため下記のように省略が可能
```python
print("{:.{}f}".format(N, M))
```
### .format()3桁で空きは空白で埋めるの書き方は以下
```python
print("{: >3}".format(n))
# 右揃えでx桁に足りない部分をiで埋める書式
"{:i>x}"
```

### , 区切り
```python
print(X, Y)
```
### 論理積
```python
print(a and b)
```

### notを数値で表示（逆の数字を表示）
```python
print(int(not n))
```
### xor
```python
print(a^b)
```

### nand
```python
print(int(not (a and b)))
```

### nor
```python
print(int(not (a or b)))
```

### xnor(not xor)
```python
print(int(not (a ^ b)))
```

## Technique
### 
```python
```

### ord() Unicodeのコードポイントを調べる
下記のord("A")とord("A")は大文字を表します。
```python
if ord(c) >= ord("A") and ord(c) <= ord("Z"):
```

別解答として`isupper()`を用いることもできる。

### 偶数のみ抽出
```python
X = [i for i in range(N) if i % 2 == 0]
```

### foreachに相当するイテラブルオブジェクト
```python
for i in K:
```
配列を順に読み込む

### list
map(#, #)第一引数にINTなど変更したい関数
```python
# mapによる
a, b = map(int, input().split())
# 別の方法
n, k, t = [int(x) for x in input().split()]
```

### ドモルガンの法則による解法
```python
print(int(not((not (a) and not (b)) or not (c)) ^ d))
# 以下のように変換できる
print(((a or b) and c) ^ d)
```

## CamelCase or snake_case
Class名はUpperCamelCase

それ以外はsnake_case

## 画像繰り返し
# 画像用辞書
items_imges = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

# ここから下を記述しよう
# 出力するアイテム数を変数に代入
item_cnt = int(input())

# 標準入力にあるアイテムを出力する
```python
while item_cnt > 0:
  item = input()
  print("<img src = '" + items_imges[item] + "'>")
  item_cnt = item_cnt - 1
```

### enumarate()
列挙する