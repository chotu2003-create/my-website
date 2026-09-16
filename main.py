from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Social Hub - All Apps in One</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
body { background: #0f0f0f; color: white; font-family: sans-serif; text-align: center; margin:0; padding:20px; }
h1 { margin-top: 30px; }
p { color: #aaa; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; max-width: 400px; margin: 30px auto; }
.card { background: #1e1e1e; border-radius: 20px; padding: 25px 10px; text-decoration: none; color: white; transition: 0.2s; }
.card:hover { transform: scale(1.05); background: #2a2a2a; }
.card i { font-size: 40px; margin-bottom: 10px; }
.fa-instagram { color: #E1306C; }
.fa-facebook { color: #1877F2; }
.fa-whatsapp { color: #25D366; }
.fa-snapchat { color: #FFFC00; }
.fa-youtube { color: #FF0000; }
.fa-twitter { color: #1DA1F2; }
.fa-telegram { color: #26A5E4; }
.fa-tiktok { color: #fff; }
</style>
</head>
<body>
<h1>🚀 My Social Hub</h1>
<p>Ek jagah se saare Social Apps chalao</p>
<div class="grid">
  <a class="card" href="https://www.instagram.com" target="_blank"><i class="fab fa-instagram"></i><br>Instagram</a>
  <a class="card" href="https://www.facebook.com" target="_blank"><i class="fab fa-facebook"></i><br>Facebook</a>
  <a class="card" href="https://web.whatsapp.com" target="_blank"><i class="fab fa-whatsapp"></i><br>WhatsApp</a>
  <a class="card" href="https://www.snapchat.com" target="_blank"><i class="fab fa-snapchat"></i><br>Snapchat</a>
  <a class="card" href="https://www.youtube.com" target="_blank"><i class="fab fa-youtube"></i><br>YouTube</a>
  <a class="card" href="https://twitter.com" target="_blank"><i class="fab fa-twitter"></i><br>Twitter / X</a>
  <a class="card" href="https://web.telegram.org" target="_blank"><i class="fab fa-telegram"></i><br>Telegram</a>
  <a class="card" href="https://www.tiktok.com" target="_blank"><i class="fab fa-tiktok"></i><br>TikTok</a>
</div>
<p style="margin-top:40px; font-size:12px;">Made by Chotu</p>
</body>
</html>
    """
if __name__ == '__main__':
    app.run()
