  from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>My Social Hub</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
body{margin:0;padding:20px;text-align:center;color:white;font-family:sans-serif;background:#0f0f0f;min-height:100vh;position:relative;overflow-x:hidden}
.bg{position:fixed;top:0;left:0;width:100%;height:100%;z-index:-1}
.b{position:absolute;border-radius:50%;filter:blur(70px);opacity:0.35}
.b1{width:250px;height:250px;background:#ff0055;top:-40px;left:-60px}
.b2{width:350px;height:350px;background:#6a11cb;top:40%;right:-80px}
.b3{width:300px;height:300px;background:#00c6ff;bottom:-50px;left:20%}
.search{margin:20px auto;max-width:400px;display:flex;background:#222;border-radius:25px;padding:5px}
.search input{flex:1;background:transparent;border:none;color:white;padding:12px 15px;outline:none;font-size:16px}
.search button{background:#ff0055;border:none;color:white;border-radius:20px;padding:10px 20px;cursor:pointer}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:15px;max-width:400px;margin:20px auto}
.card{background:#1e1e1e;border-radius:20px;padding:25px 10px;text-decoration:none;color:white;display:block}
.card i{font-size:42px;margin-bottom:8px;display:block}
.fa-instagram{color:#E1306C} .fa-facebook{color:#1877F2} .fa-whatsapp{color:#25D366} .fa-snapchat{color:#FFFC00} .fa-youtube{color:#FF0000} .fa-twitter{color:#1DA1F2} .fa-telegram{color:#26A5E4} .fa-tiktok{color:white}
</style>
</head>
<body>
<div class="bg"><div class="b b1"></div><div class="b b2"></div><div class="b b3"></div></div>
<h1>My Social Hub</h1>
<p style="color:#aaa">Ek jagah se saare Social Apps chalao</p>
<div class="search">
<input type="text" id="s" placeholder="Google me search karo...">
<button onclick="if(document.getElementById('s').value)location.href='https://www.google.com/search?q='+document.getElementById('s').value">Search</button>
</div>
<div class="grid">
<a class="card" href="https://instagram.com"><i class="fab fa-instagram"></i>Instagram</a>
<a class="card" href="https://facebook.com"><i class="fab fa-facebook"></i>Facebook</a>
<a class="card" href="https://web.whatsapp.com"><i class="fab fa-whatsapp"></i>WhatsApp</a>
<a class="card" href="https://snapchat.com"><i class="fab fa-snapchat"></i>Snapchat</a>
<a class="card" href="https://youtube.com"><i class="fab fa-youtube"></i>YouTube</a>
<a class="card" href="https://twitter.com"><i class="fab fa-twitter"></i>Twitter / X</a>
<a class="card" href="https://telegram.org"><i class="fab fa-telegram"></i>Telegram</a>
<a class="card" href="https://tiktok.com"><i class="fab fa-tiktok"></i>TikTok</a>
</div>
<p style="color:#555;margin-top:30px">Made by Kunal</p>
</body>
</html>
"""
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
