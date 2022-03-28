# http.server学習用　便宜上こちらのフォルダに置く
# 該当フォルダでこのファイルを実行すればlocalhost:8000でHTMLファイルを表示できる
# ただし、セキュリティ的に問題あることと動作が怪しいので検証にしか使わない
import http.server
import socketserver

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()