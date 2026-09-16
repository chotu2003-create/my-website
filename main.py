from flask import Flask, Response
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>My Social Hub</title>
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#ff0055">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
body{
  margin:0; padding:20px; text-align:center; color:white; font-family:sans-serif;
  background: linear-gradient(-45deg, #0f0f0f, #1a0a1f, #0f1a2e, #1f0a0a);
  background-size:400% 400%;
  animation: gradient 12s ease infinite;
  min-height:100vh;
}
@keyframes gradient{
  0%{background-position:0% 50%} 50%{background-position:100% 50%} 100%{background-position:0% 50%}
}
.search-box{margin:20px auto;max-width:400px;display:flex;background:rgba(255,255,255,0.1);backdrop-filter:blur(10px);border-radius:25px;padding:5px; border:1px solid rgba(255,255,255,0.1);}
.search-box input{flex:1;background:transparent;border:none;color:white;padding:12px 15px;outline:none;font-size:16px;}
.search-box button{background:#ff0055;border:none;color:white;border-radius:20px;padding:10px 20px;cursor:pointer;font-weight:bold;}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:15px;max-width:400px;margin:20px auto;}
.card{background:rgba(30,30,30,0.8);backdrop-filter:blur(10px);border-radius:20px;padding:25px 10px;text-decoration:none;color:white;display:block;border:1px solid rgba(255,255,255,0.05);}
.card:hover{background:rgba(50,50,50,0.9);transform:scale(1.05);transition:0.2s;}
.card i{font-size:45px;margin-bottom:8px;display:block;}
.fa-instagram{color:#E1306C} .fa-facebook{color:#1877F2} .fa-whatsapp{color:#25D366} .fa-snapchat{color:#FFFC00} .fa-youtube{color:#FF0000} .fa-twitter{color:#1DA1F2} .fa-telegram{color:#26A5E4} .fa-tiktok{color:white}
.footer{margin-top:30px;color:#999;font-size:14px;}
.install-btn{display:none; margin:15px auto; background:white; color:black; padding:10px 20px; border-radius:20px; border:none; font-weight:bold; cursor:pointer;}
</style>
</head>
<body>
<h1>🚀 My Social Hub</h1>
<p>Ek jagah se saare Social Apps chalao</p>

<button id="installBtn" class="install-btn">📲 App Install Karo</button>

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

if('serviceWorker' in navigator){navigator.serviceWorker.register('/sw.js');}

let deferredPrompt;
const installBtn = document.getElementById('installBtn');
window.addEventListener('beforeinstallprompt', (e) => {
  e.preventDefault(); deferredPrompt = e; installBtn.style.display = 'block';
});
installBtn.addEventListener('click', () => {
  installBtn.style.display = 'none'; deferredPrompt.prompt();
});
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

@app.route('/manifest.json')
def manifest():
    return Response("""
{
  "name": "My Social Hub",
  "short_name": "SocialHub",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#0f0f0f",
  "theme_color": "#ff0055",
  "icons": [
    {"src": "https://cdn-icons-png.flaticon.com/512/2111/2111463.png","sizes":"512x512","type":"image/png"}
  ]
}
""", mimetype='application/json')

@app.route('/sw.js')
def sw():
    return Response("""
self.addEventListener('install', e => self.skipWaiting());
self.addEventListener('fetch', e => e.respondWith(fetch(e.request)));
""", mimetype='application/javascript')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
