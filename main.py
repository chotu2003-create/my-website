import os
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kunal's Pro Hub</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
body{margin:0;font-family:sans-serif;background:#0a0a0a;color:white;text-align:center}
.tabs{position:sticky;top:0;background:#111;display:flex;justify-content:space-around;padding:10px 0;z-index:10;border-bottom:1px solid #222}
.tabs button{background:#222;border:none;color:white;padding:10px 15px;border-radius:20px;cursor:pointer}
.tabs button.active{background:#ff0055}
.page{display:none;padding:20px;max-width:450px;margin:auto}
.page.active{display:block}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:15px}
.card{background:#1e1e1e;border-radius:18px;padding:18px 10px;text-decoration:none;color:white;display:block}
.card i{font-size:36px;display:block;margin-bottom:5px}
input,select{width:90%;padding:12px;margin:8px 0;border-radius:10px;border:none;background:#222;color:white;outline:none}
.btn{background:#ff0055;border:none;color:white;padding:12px 20px;border-radius:10px;width:92%;cursor:pointer;margin-top:10px;font-weight:bold}
.box{background:#1a1a1a;padding:15px;border-radius:15px;margin-top:15px;text-align:left}
.fake-chat{background:white;color:black;border-radius:15px;padding:10px;max-width:300px;margin:10px auto;text-align:left}
.fake-msg{background:#dcf8c6;padding:8px 12px;border-radius:10px;margin:5px 0;display:inline-block}
</style>
</head>
<body>
<h2 style="margin:15px 0">KUNAL'S PRO HUB 🔥</h2>
<div class="tabs">
<button class="active" onclick="openTab('home')">Home</button>
<button onclick="openTab('tools')">Tools</button>
<button onclick="openTab('fake')">Fake Chat</button>
</div>

<div id="home" class="page active">
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
<h3>📥 Insta / YT Video Downloader</h3>
<input id="vlink" placeholder="YouTube / Insta link yaha paste karo">
<button class="btn" onclick="downloadVideo()">Download Karo</button>

<h3 style="margin-top:25px">👁️ Insta DP Viewer (HD)</h3>
<input id="instaUser" placeholder="Insta username likho - ex: virat.kohli">
<button class="btn" onclick="viewDP()">HD DP Dekho</button>
<div id="dpResult" class="box" style="display:none"></div>

<h3 style="margin-top:25px">✨ Stylish Name Maker</h3>
<input id="sname" placeholder="Apna naam likho" oninput="makeStylish()">
<div id="styleResult" class="box"></div>
</div>

<div id="fake" class="page">
<h3>😂 Fake WhatsApp Chat Maker</h3>
<input id="fname" placeholder="Naam - ex: Girlfriend">
<input id="fmsg" placeholder="Message - ex: I love you">
<select id="ftype"><option>Sent (You)</option><option>Received</option></select>
<button class="btn" onclick="addFakeMsg()">Chat me Add Karo</button>
<button class="btn" style="background:#333" onclick="document.getElementById('chatArea').innerHTML=''">Clear Chat</button>
<div id="chatArea" class="fake-chat"></div>
<p style="color:#777;font-size:12px;margin-top:10px">Screenshot leke dost ko bhej de, prank ho jayega!</p>
</div>

<script>
function openTab(id){
document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'));
document.getElementById(id).classList.add('active');
event.target.classList.add('active');
}
function downloadVideo(){
let link=document.getElementById('vlink').value;
if(!link){alert('Link daal pehle!');return;}
if(link.includes('youtu')){window.open('https://10downloader.com/download?v='+encodeURIComponent(link));}
else {window.open('https://snapinsta.app/download?url='+encodeURIComponent(link));}
}
function viewDP(){
let u=document.getElementById('instaUser').value.replace('@','').trim();
if(!u){alert('Username daal');return;}
let r=document.getElementById('dpResult');
r.style.display='block';
r.innerHTML='<img src="https://unavatar.io/instagram/'+u+'" style="width:200px;height:200px;border-radius:50%;display:block;margin:10px auto" onerror="this.src=`https://instagram.com/'+u+'/favicon.ico`"><p style="text-align:center">@'+u+'</p><a href="https://unavatar.io/instagram/'+u+'" download target="_blank" style="color:#ff0055;text-align:center;display:block">HD Download Karo</a>';
}
function makeStylish(){
let t=document.getElementById('sname').value;
if(!t){document.getElementById('styleResult').innerHTML='';return;}
let fonts=[
t.split('').map(c=>String.fromCharCode(c.charCodeAt(0)+0x1D400-97)).join(''),
'𝕮'+t.slice(1),
'『'+t+'』',
'★ '+t+' ★',
'꧁༒☬'+t+'☬༒꧂'
];
let map={'a':'𝖆','b':'𝖇','c':'𝖈','d':'𝖉','e':'𝖊','f':'𝖋','g':'𝖌','h':'𝖍','i':'𝖎','j':'𝖏','k':'𝖐','l':'𝖑','m':'𝖒','n':'𝖓','o':'𝖔','p':'𝖕','q':'𝖖','r':'𝖗','s':'𝖘','t':'𝖙','u':'𝖚','v':'𝖛','w':'𝖜','x':'𝖝','y':'𝖞','z':'𝖟'};
let fancy=t.toLowerCase().split('').map(c=>map[c]||c).join('');
fonts.unshift(fancy);
let html=fonts.map(f=>'<div style="padding:8px;border-bottom:1px solid #222;display:flex;justify-content:space-between"><span>'+f+'</span><button onclick="navigator.clipboard.writeText(\\''+f+'\\')" style="background:#333;border:none;color:white;padding:5px 10px;border-radius:5px">Copy</button></div>').join('');
document.getElementById('styleResult').innerHTML=html;
}
function addFakeMsg(){
let name=document.getElementById('fname').value||'Person';
let msg=document.getElementById('fmsg').value;
if(!msg){alert('Message likh');return;}
let isSent=document.getElementById('ftype').value.includes('Sent');
let div=document.createElement('div');
div.style.textAlign=isSent?'right':'left';
div.innerHTML='<div class="fake-msg" style="background:'+(isSent?'#dcf8c6':'#fff')+'">'+msg+'</div>';
document.getElementById('chatArea').appendChild(div);
document.getElementById('fmsg').value='';
}
</script>
</body>
</html>"""
if __name__ == "__main__":
    port=int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port)
