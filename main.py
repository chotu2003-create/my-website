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
<style>
body { background:#0f0f0f; color:white; font-family:sans-serif; text-align:center; margin:0; padding:20px; }
.search-box { margin:20px auto; max-width:400px; display:flex; background:#222; border-radius:25px; padding:5px; }
.search-box input { flex:1; background:transparent; border:none; color:white; padding:12px 15px; outline:none; font-size:16px; }
.search-box button { background:#ff0055; border:none; color:white; border-radius:20px; padding:10px 20px; cursor:pointer; }
h1 { margin-top:10px; }
p { color:#aaa; }
.grid { display:grid; grid-template-columns:1fr 1fr; gap:15px; max-width:400px; margin:20px auto; }
.card { background:#1e1e1e; border-radius:20px; padding:25px 10px; text-decoration:none; color:white; display:block; }
.card:hover { background:#2a2a2a; transform:scale(1.05); transition:0.2s; }
.icon { font-size:45px; }
.footer { margin-top:30px; color:#666; font-size:14px; }
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
<a class="card" href="https://instagram.com"><div class="icon">📸</div>Instagram</a>
<a class="card" href="https://facebook.com"><div class="icon">📘</div>Facebook</a>
<a class="card" href="https://web.whatsapp.com"><div class="icon">💬</div>WhatsApp</a>
<a class="card" href="https://snapchat.com"><div class="icon">👻</div>Snapchat</a>
<a class="card" href="https://youtube.com"><div class="icon">▶️</div>YouTube</a>
<a class="card" href="https://twitter.com"><div class="icon">🐦</div>Twitter / X</a>
<a class="card" href="https://telegram.org"><div class="icon">✈️</div>Telegram</a>
<a class="card" href="https://tiktok.com"><div class="icon">🎵</div>TikTok</a>
</div>

<div class="footer">Made by Kunal ❤️</div>

<script>
function doSearch(){
  let q = document.getElementById('searchInput').value;
  if(q) window.location.href = 'https://www.google.com/search?q=' + q;
}
document.getElementById('searchInput').addEventListener('keypress', function(e){
  if(e.key === 'Enter') doSearch();
});
</script>
</body>
</html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
