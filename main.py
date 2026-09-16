import os
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    html = '''
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kunal Pro Hub</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
body{margin:0;font-family:sans-serif;color:white;text-align:center;min-height:100vh;background:#000;position:relative;overflow-x:hidden}
body:before{content:"";position:fixed;top:0;left:0;width:100%;height:100%;z-index:-2;background: radial-gradient(circle at 20% 20%, #ff0055 0%, transparent 40%), radial-gradient(circle at 80% 80%, #7c00ff 0%, transparent 40%), radial-gradient(circle at 50% 50%, #00d4ff 0%, transparent 50%), #0a0a0a;animation:bgMove 10s infinite alternate}
@keyframes bgMove{0%{filter:hue-rotate(0deg)}100%{filter:hue-rotate(30deg)}}
.tabs{position:sticky;top:0;background:rgba(17,17,17,0.9);backdrop-filter:blur(15px);display:flex;justify-content:space-around;padding:10px 0;z-index:10;border-bottom:1px solid #222}
.tabs button{background:#222;border:none;color:white;padding:10px 18px;border-radius:20px;cursor:pointer}
.tabs button.active{background:#ff0055;box-shadow:0 0 15px #ff0055}
.page{display:none;padding:20px;max-width:450px;margin:auto}
.page.active{display:block}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:15px}
.card{background:rgba(30,30,30,0.7);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.1);border-radius:20px;padding:22px 10px;text-decoration:none;color:white;display:block}
.card i{font-size:38px;display:block;margin-bottom:6px}
.search-box{background:rgba(30,30,30,0.8);backdrop-filter:blur(10px);display:flex;align-items:center;padding:5px 15px;border-radius:30px;margin-bottom:20px;border:1px solid #333}
.search-box input{flex:1;background:transparent;border:none;color:white;outline:none;padding:12px 5px;font-size:16px}
.search-box button{background:linear-gradient(135deg,#ff0055,#ff7a00);border:none;color:white;width:42px;height:42px;border-radius:50%;cursor:pointer}
input,select{width:90%;padding:12px;margin:8px 0;border-radius:12px;border:1px solid #333;background:#222;color:white;outline:none}
.btn{background:linear-gradient(135deg,#ff0055,#7c00ff);border:none;color:white;padding:13px 20px;border-radius:12px;width:92%;cursor:pointer;margin-top:10px;font-weight:bold}
.box{background:#1a1a1a;padding:15px;border-radius:15px;margin-top:15px;text-align:left;border:1px solid #333}
.fake-chat{background:white;color:black;border-radius:15px;padding:10px;max-width:300px;margin:10px auto;text-align:left}
</style>
</head>
<body>
<h2 style="margin:15px 0;text-shadow:0 0 20px #ff0055">KUNAL PRO HUB 🔥</h2>
<div class="tabs">
<button class="active" onclick="openTab('home',this)">Home</button>
<button onclick="openTab('tools',this)">Tools</button>
<button onclick="openTab('fake',this)">Fake Chat</button>
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
<h3>Video Downloader</h3>
<input id="vlink" placeholder="YouTube / Insta link">
<button class="btn" onclick="downloadVideo()">Download Karo</button>
<h3 style="margin-top:25px">Insta DP Viewer</h3>
<input id="instaUser" placeholder="Username">
<button class="btn" onclick="viewDP()">HD DP Dekho</button>
<div id="dpResult" class="box" style="display:none"></div>
<h3 style="margin-top:25px">Stylish Name Maker</h3>
<input id="sname" placeholder="Naam likho" oninput="makeStylish()">
<div id="styleResult" class="box"></div>
</div>

<div id="fake" class="page">
<h3>Fake Chat Maker</h3>
<input id="fmsg" placeholder="Message">
<select id="ftype"><option>Sent</option><option>Received</option></select>
<button class="btn" onclick="addFakeMsg()">Add Karo</button>
<button class="btn" style="background:#333" onclick="document.getElementById('chatArea').innerHTML=''">Clear</button>
<div id="chatArea" class="fake-chat"></div>
</div>

<script>
function openTab(id,btn){
document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'));
document.getElementById(id).classList.add('active');
btn.classList.add('active');
}
function doSearch(){
let q=document.getElementById('gSearch').value.trim();
if(!q)return;
if(q.includes('.')&&!q.includes(' ')){if(!q.startsWith('http'))q='https://'+q;window.location.href=q;}
else{window.location.href='https://www.google.com/search?q='+encodeURIComponent(q);}
}
function downloadVideo(){
let link=document.getElementById('vlink').value;
if(!link){alert('Link daal');return;}
if(link.includes('youtu')){window.open('https://10downloader.com/download?v='+encodeURIComponent(link));}
else{window.open('https://snapinsta.app/download?url='+encodeURIComponent(link));}
}
function viewDP(){
let u=document.getElementById('instaUser').value.replace('@','').trim();
if(!u){alert('Username daal');return;}
let r=document.getElementById('dpResult');
r.style.display='block';
r.innerHTML='<img src="https://unavatar.io/instagram/'+u+'" style="width:200px;height:200px;border-radius:50%;display:block;margin:10px auto;border:3px solid #ff0055"><p style="text-align:center">@'+u+'</p>';
}
function makeStylish(){
let t=document.getElementById('sname').value;
if(!t){document.getElementById('styleResult').innerHTML='';return;}
let map={'a':'𝖆','b':'𝖇','c':'𝖈','d':'𝖉','e':'𝖊','f':'𝖋','g':'𝖌','h':'𝖍','i':'𝖎','j':'𝖏','k':'𝖐','l':'𝖑','m':'𝖒','n':'𝖓','o':'𝖔','p':'𝖕','q':'𝖖','r':'𝖗','s':'𝖘','t':'𝖙','u':'𝖚','v':'𝖛','w':'𝖜','x':'𝖝','y':'𝖞','z':'𝖟'};
let fancy=t.toLowerCase().split('').map(c=>map[c]||c).join('');
let fonts=[fancy,'『'+t+'』','★ '+t+' ★','꧁'+t+'꧂'];
let html=fonts.map(f=>'<div style="padding:8px;border-bottom:1px solid #222;display:flex;justify-content:space-between"><span>'+f+'</span><button onclick="navigator.clipboard.writeText(\\''+f+'\\')" style="background:#333;border:none;color:white;padding:5px 10px;border-radius:5px">Copy</button></div>').join('');
document.getElementById('styleResult').innerHTML=html;
}
function addFakeMsg(){
let msg=document.getElementById('fmsg').value;
if(!msg)return;
let isSent=document.getElementById('ftype').value.includes('Sent');
let div=document.createElement('div');
div.style.textAlign=isSent?'right':'left';
div.innerHTML='<div style="background:'+(isSent?'#dcf8c6':'#fff')+';padding:8px 12px;border-radius:10px;margin:5px 0;display:inline-block;color:#000">'+msg+'</div>';
document.getElementById('chatArea').appendChild(div);
document.getElementById('fmsg').value='';
}
</script>
</body>
</html>
'''
    return html
if __name__ == "__main__":
    port=int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port)
