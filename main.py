import os
from flask import Flask, request, jsonify
import yt_dlp
app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>KUNAL PRO HUB</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
body{margin:0;font-family:sans-serif;color:white;text-align:center;min-height:100vh;background:#000;overflow-x:hidden}
body:before{content:'';position:fixed;top:0;left:0;width:100%;height:100%;z-index:-2;background:radial-gradient(circle at 20% 20%, #ff0055 0%, transparent 40%), radial-gradient(circle at 80% 80%, #7c00ff 0%, transparent 40%), radial-gradient(circle at 50% 50%, #00d4ff 0%, transparent 50%), #0a0a0a}
.tabs{position:sticky;top:0;background:rgba(17,17,17,0.9);backdrop-filter:blur(15px);display:flex;justify-content:space-around;padding:10px 0;z-index:10;border-bottom:1px solid #222}
.tabs button{background:#222;border:none;color:white;padding:10px 18px;border-radius:20px;cursor:pointer}
.tabs button.active{background:#ff0055}
.page{display:none;padding:20px;max-width:450px;margin:auto}
.page.active{display:block}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:15px}
.card{background:rgba(30,30,30,0.7);border:1px solid rgba(255,255,255,0.1);border-radius:20px;padding:22px 10px;text-decoration:none;color:white;display:block}
.card i{font-size:38px;display:block;margin-bottom:6px}
.search-box{background:rgba(30,30,30,0.8);display:flex;align-items:center;padding:5px 15px;border-radius:30px;margin-bottom:20px;border:1px solid #333}
.search-box input{flex:1;background:transparent;border:none;color:white;outline:none;padding:12px 5px;font-size:16px}
.search-box button{background:#ff0055;border:none;color:white;width:42px;height:42px;border-radius:50%;cursor:pointer}
input{width:90%;padding:12px;margin:8px 0;border-radius:12px;border:1px solid #333;background:#222;color:white;outline:none}
.btn{background:linear-gradient(135deg,#ff0055,#7c00ff);border:none;color:white;padding:13px 20px;border-radius:12px;width:92%;cursor:pointer;margin-top:10px;font-weight:bold}
.box{background:#1a1a1a;padding:15px;border-radius:15px;margin-top:15px;text-align:left;border:1px solid #333}
</style></head>
<body>
<h2 style="margin:15px 0">KUNAL PRO HUB</h2>
<div class="tabs">
<button class="active" onclick="openTab('home',this)">Home</button>
<button onclick="openTab('tools',this)">Tools</button>
</div>

<div id="home" class="page active">
<div class="search-box">
<i class="fab fa-google" style="color:#888"></i>
<input id="gSearch" placeholder="Search ya link daalo..." onkeydown="if(event.key==='Enter')doSearch()">
<button onclick="doSearch()"><i class="fas fa-search"></i></button>
</div>
<div class="grid">
<a class="card" href="https://www.instagram.com"><i class="fab fa-instagram" style="color:#E1306C"></i>Instagram</a>
<a class="card" href="https://www.facebook.com"><i class="fab fa-facebook" style="color:#1877F2"></i>Facebook</a>
<a class="card" href="https://web.whatsapp.com"><i class="fab fa-whatsapp" style="color:#25D366"></i>WhatsApp</a>
<a class="card" href="https://www.youtube.com"><i class="fab fa-youtube" style="color:red"></i>YouTube</a>
<a class="card" href="https://x.com"><i class="fab fa-twitter" style="color:#1DA1F2"></i>X</a>
<a class="card" href="https://web.telegram.org"><i class="fab fa-telegram" style="color:#26A5E4"></i>Telegram</a>
</div>
</div>

<div id="tools" class="page">
<h3>Insta Video Downloader - WORKING</h3>
<input id="vlink" placeholder="Instagram Reels link yaha paste kar">
<button class="btn" onclick="downloadVideo()">Download Karo</button>
<div id="result" class="box" style="display:none"></div>
</div>

<script>
function openTab(id,btn){
document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'));
document.getElementById(id).classList.add('active');btn.classList.add('active');
}
function doSearch(){
let q=document.getElementById('gSearch').value.trim();
if(!q)return;
if(q.includes('.')&&!q.includes(' ')){if(!q.startsWith('http'))q='https://'+q;window.location.href=q;}
else{window.location.href='https://www.google.com/search?q='+encodeURIComponent(q);}
}
async function downloadVideo(){
 let link=document.getElementById('vlink').value.trim();
 let resDiv=document.getElementById('result');
 if(!link){alert('Link daal bhai');return;}
 resDiv.style.display='block';
 resDiv.innerHTML='⏳ Video nikal raha hu...';
 try{
   let r = await fetch('/api/insta?url='+encodeURIComponent(link));
   let data = await r.json();
   if(data.error){resDiv.innerHTML='❌ Error: '+data.error;return;}
   resDiv.innerHTML='<p>✅ Mil gaya!</p><a href="'+data.video_url+'" target="_blank" style="color:#25D366;font-weight:bold;font-size:18px">👉 DOWNLOAD KARO</a><br><br><video src="'+data.video_url+'" controls style="width:100%;border-radius:12px;margin-top:10px"></video>';
 }catch(e){resDiv.innerHTML='❌ Server error, dobara try kar';}
}
</script>
</body></html>
"""

@app.route('/api/insta')
def insta_api():
    url = request.args.get('url')
    if not url: return jsonify({"error":"Link de"}),400
    try:
        ydl_opts={'quiet':True,'skip_download':True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info=ydl.extract_info(url,download=False)
            if 'entries' in info: info=info['entries'][0]
            vurl=info.get('url') or info['formats'][-1]['url']
            return jsonify({"video_url":vurl})
    except Exception as e:
        return jsonify({"error":str(e)}),500

if __name__=="__main__":
    port=int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port)
