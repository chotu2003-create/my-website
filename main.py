import os
from flask import Flask, request, jsonify
import yt_dlp
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>INSTANT PRO HUB</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<style>
body{margin:0;font-family:sans-serif;background:#000;color:white;text-align:center}
.tabs{position:sticky;top:0;background:#111;display:flex;z-index:10}
.tabs button{flex:1;padding:15px;background:#222;border:none;color:white;font-weight:bold}
.tabs button.active{background:#00f2fe;color:#000}
.page{display:none;padding:20px;max-width:500px;margin:auto}
.page.active{display:block}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:20px}
.card{background:#1a1a1a;padding:20px;border-radius:15px;text-decoration:none;color:white;border:1px solid #333}
.card i{font-size:32px;display:block;margin-bottom:8px;color:#00f2fe}
.search-box{background:#1a1a1a;display:flex;align-items:center;padding:5px 10px;border-radius:30px;margin-top:15px}
.search-box input{flex:1;background:transparent;border:none;color:white;padding:12px;outline:none}
.search-box button{background:#00f2fe;border:none;padding:10px 15px;border-radius:50%}
input,select{width:92%;padding:12px;margin:8px 0;border-radius:8px;border:none;background:#1a1a1a;color:white}
.btn{background:linear-gradient(135deg,#00f2fe,#4facfe);border:none;padding:12px 20px;border-radius:8px;color:#000;font-weight:bold;width:94%;margin-top:10px}
</style>
</head>
<body>
<h2 style="margin:15px 0">INSTANT PRO HUB</h2>
<div class="tabs">
<button class="active" onclick="openTab('home',this)">Home</button>
<button onclick="openTab('tools',this)">Tools</button>
</div>

<div id="home" class="page active">
<div class="search-box">
<i class="fab fa-google" style="color:#888"></i>
<input id="gSearch" placeholder="Search ya link daalo...">
<button onclick="doSearch()"><i class="fas fa-search"></i></button>
</div>
<div class="grid">
<a class="card" href="https://www.instagram.com" target="_blank"><i class="fab fa-instagram"></i>Instagram</a>
<a class="card" href="https://www.facebook.com" target="_blank"><i class="fab fa-facebook"></i>Facebook</a>
<a class="card" href="https://web.whatsapp.com" target="_blank"><i class="fab fa-whatsapp"></i>WhatsApp</a>
<a class="card" href="https://www.youtube.com" target="_blank"><i class="fab fa-youtube"></i>YouTube</a>
<a class="card" href="https://x.com" target="_blank"><i class="fab fa-twitter"></i>Twitter</a>
<a class="card" href="https://web.telegram.org" target="_blank"><i class="fab fa-telegram"></i>Telegram</a>
</div>
</div>

<div id="tools" class="page">
<h3>All Video Downloader</h3>
<p style="font-size:12px;color:#aaa">Insta / YT / FB / TikTok</p>
<input id="vlink" placeholder="Koi bhi link paste karo">
<button class="btn" onclick="downloadInsta()">Download Now</button>
<p id="result" style="margin-top:15px;font-size:13px"></p>
</div>

<script>
function openTab(id,el){
document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
document.getElementById(id).classList.add('active');
document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'));
el.classList.add('active');
}
function doSearch(){
let q=document.getElementById('gSearch').value;
if(q) window.open('https://www.google.com/search?q='+encodeURIComponent(q),'_blank');
}
async function downloadInsta(){
let link=document.getElementById('vlink').value;
if(!link) return alert('Link daalo');
document.getElementById('result').innerHTML='Downloading...';
let res=await fetch('/download?url='+encodeURIComponent(link));
let data=await res.json();
if(data.url) window.open(data.url,'_blank');
else document.getElementById('result').innerHTML=data.error || 'Error';
}
</script>
</body>
</html>
    """

@app.route('/download')
def download():
    url = request.args.get('url')
    try:
        ydl_opts = {'format':'best'}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return jsonify({'url': info['url']})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
