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

## CamelCase or snake_case
Class名はUpperCamelCase

それ以外はsnake_case