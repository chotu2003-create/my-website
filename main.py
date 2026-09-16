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
body{background:#0f0f0f;color:white;font-family:sans-serif;text-align:center;margin:0;padding:20px;}
.search-box{margin:20px auto;max-width:400px;display:flex;background:#222;border-radius:25px;padding:5px;}
.search-box input{flex:1;background:transparent;border:none;color:white;padding:12px 15px;outline:none;font-size:16px;}
.search-box button{background:#ff0055;border:none;color:white;border-radius:20px;padding:10px 20px;cursor:pointer;}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:15px;max-width:400px;margin:20px auto;}
.card{background:#1e1e1e;border-radius:20px;padding:25px 10px;text-decoration:none;color:white;display:block;}
.card:hover{background:#2a2a2a;transform:scale(1.05);transition:0.2s;}
.card i{font-size:45px;margin-bottom:8px;display:block;}
.fa-instagram{color:#E1306C} .fa-facebook{color:#1877F2} .fa-whatsapp{color:#25D366} .fa-snapchat{color:#FFFC00} .fa-youtube{color:#FF0000} .fa-twitter{color:#1DA1F2} .fa-telegram{color:#26A5E4} .fa-tiktok{color:white}
.footer{margin-top:30px;color:#666;font-size:14px;}
</style>
</head>
<body>
<h1>🚀 My Social Hub</h1>
<p>Ek jagah se saare Social Apps chalao</p>
<div class="search-box">
<input type="text" id="searchInput" placeholder="Google me search karo...">
<button onclick="doSearch()">Search</button>
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
<div class="footer">Made by Kunal ❤️</div>
<script>
function doSearch(){let q=document.getElementById('searchInput').value;if(q)window.location.href='https://www.google.com/search?q='+q;}
document.getElementById('searchInput').addEventListener('keypress',function(e){if(e.key==='Enter')doSearch();});
</script>
</body>
</html>
"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
