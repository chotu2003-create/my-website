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
*{box-sizing:border-box}
body{margin:0;font-family:sans-serif;color:white;text-align:center;min-height:100vh;background:#000;overflow-x:hidden;position:relative}
body::before{content:'';position:fixed;top:0;left:0;width:100%;height:100%;z-index:-2;background: radial-gradient(circle at 20% 20%, #ff0055 0%, transparent 40%), radial-gradient(circle at 80% 80%, #7c00ff 0%, transparent 40%), radial-gradient(circle at 50% 50%, #00d4ff 0%, transparent 50%), #0a0a0a;animation:bgMove 10s infinite alternate}
@keyframes bgMove{0%{filter:hue-rotate(0deg) brightness(1)}100%{filter:hue-rotate(30deg) brightness(1.2)}}
.tabs{position:sticky;top:0;background:rgba(17,17,17,0.8);backdrop-filter:blur(15px);display:flex;justify-content:space-around;padding:10px 0;z-index:10;border-bottom:1px solid #222}
.tabs button{background:#222;border:none;color:white;padding:10px 18px;border-radius:20px;cursor:pointer;transition:0.3s}
.tabs button.active{background:#ff0055;box-shadow:0 0 15px #ff0055}
.page{display:none;padding:20px;max-width:450px;margin:auto}
.page.active{display:block;animation:fade 0.4s}
@keyframes fade{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:translateY(0)}}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:15px}
.card{background:rgba(30,30,30,0.7);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.1);border-radius:20px;padding:22px 10px;text-decoration:none;color:white;display:block;transition:0.3s}
.card:hover{transform:translateY(-5px) scale(1.02);box-shadow:0 10px 30px rgba(255,0,85,0.3);border-color:#ff0055}
.card i{font-size:38px;display:block;margin-bottom:6px;filter:drop-shadow(0 0 10px currentColor)}
.search-box{background:rgba(30,30,30,0.8);backdrop-filter:blur(10px);display:flex;align-items:center;padding:5px 15px;border-radius:30px;margin-bottom:20px;border:1px solid rgba(255,255,255,0.15);box-shadow:0 5px 20px rgba(0,0,0,0.5)}
.search-box input{flex:1;background:transparent;border:none;color:white;outline:none;padding:12px 5px;font-size:16px}
.search-box button{background:linear-gradient(135deg,#ff0055,#ff7a00);border:none;color:white;width:42px;height:42px;border-radius:50%;cursor:pointer;box-shadow:0 0 15px rgba(255,0,85,0.6)}
input,select{width:90%;padding:12px;margin:8px 0;border-radius:12px;border:1px solid #333;background:rgba(34,34,34,0.8);color:white;outline:none}
.btn{background:linear-gradient(135deg,#ff0055,#7c00ff);border:none;color:white;padding:13px 20px;border-radius:12px;width:92%;cursor:pointer;margin-top:10px;font-weight:bold;box-shadow:0 5px 20px rgba(255,0,85,0.4)}
.box{background:rgba(26,26,26,0.8);backdrop-filter:blur(10px);padding:15px;border-radius:15px;margin-top:15px;text-align:left;border:1px solid #333}
.fake-chat{background:white;color:black;border-radius:15px;padding:10px;max-width:300px;margin:10px auto;text-align:left}
.fake-msg{padding:8px 12px;border-radius:10px;margin:5px 0;display:inline-block}
</style>
</head>
<body>
<h2 style="margin:15px 0;text-shadow:0 0 20px #ff0055">KUNAL'S PRO HUB 🔥</h2>
<div class="tabs">
<button class="active" onclick="openTab('home')">Home</button>
<button onclick="openTab('tools')">Tools</button>
<button onclick="openTab('fake')">Fake Chat</button>
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
<h3>📥 Video Downloader</h3>
<input id="vlink" placeholder="YouTube / Insta link paste karo">
<button class="btn" onclick="downloadVideo()">Download Karo</button>
<h3 style="margin-top:25px">👁️ Insta DP Viewer</h3>
<input id="instaUser" placeholder="Username - ex: virat.kohli">
<button class="btn" onclick="viewDP()">HD DP Dekho</button>
<div id="dpResult" class="box" style="display:none"></div>
<h3 style="margin-top:25px">✨ Stylish Name Maker</h3>
<input id="sname" placeholder="Apna naam likho" oninput="makeStylish()">
<div id="styleResult" class="box"></div>
</div>

<div id="fake" class="page">
<h3>😂 Fake WhatsApp Chat Maker</h3>
<input id="fname" placeholder="Naam">
<input id="fmsg" placeholder="Message">
<select id="ftype"><option>Sent (You)</option><option>Received</option></select>
<button class="btn" onclick="addFakeMsg()">Add Karo</button>
<button class="btn" style="background:#333;box-shadow:none" onclick="document.getElementById('chatArea').innerHTML=''">Clear</button>
<div id="chatArea" class="fake-chat"></div>
</div>

<script>
function openTab(id){
document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'));
document.getElementById(id).classList.add('active');
event.target.classList.add('active');
}
function doSearch(){
let q=document.getElementById('gSearch').value.trim();
if(!q)return;
if(q.includes('.')&&!q.includes(' ')){if(!q.startsWith('http'))q='https://'+q;window.location.href=q;}
else{window.location.href='https://www.google.com/search?q='+encodeURIComponent(q);}
}
function downloadVideo(){
let link=document.getElementById('vlink').value;
if(!link){alert('Link daal!');return;}
if(link.includes('youtu')){window.open('https://10downloader.com/download?v='+encodeURIComponent(link));}
else{window.open('https://snapinsta.app/download?url='+encodeURIComponent(link));}
}
function viewDP(){
let u=document.getElementById('instaUser').value.replace('@','').trim();
if(!u){alert('Username daal');return;}
let r=document.getElementById('dpResult');
r.style.display='block';
r.innerHTML='<img src="https://unavatar.io/instagram/'+u+'" style="width:200px;height:200px;border-radius:50%;display:block;margin:10px auto;border:3px solid #ff0055"><p style="text-align:center">@'+u+'</p><a href="https://unavatar.io/instagram/'+u+'" target="_blank" style="color:#ff0055;text-align:center;display:block">HD Download</a>';
}
function makeStylish(){
let t=document.getElementById('sname').value;
if(!t){document.getElementById('styleResult').innerHTML='';return;}
let map={'a':'𝖆','b':'𝖇','c':'𝖈','d':'𝖉','e':'𝖊','f':'𝖋','g':'𝖌','h':'𝖍','i':'𝖎','j':'𝖏','k':'𝖐','l':'𝖑','m':'𝖒','n':'𝖓','o':'𝖔','p':'𝖕','q':'𝖖','r':'𝖗','s':'𝖘
