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
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<style>
body{margin:0;font-family:sans-serif;color:white;text-align:center;min-height:100vh;background:#000;overflow-x:hidden}
body:before{content:'';position:fixed;top:0;left:0;width:100%;height:100%;z-index:-2;background:radial-gradient(circle at 20% 20%, #ff0055 0%, transparent 40%), radial-gradient(circle at 80% 80%, #7c00ff 0%, transparent 40%), radial-gradient(circle at 50% 50%, #00d4ff 0%, transparent 50%), #0a0a0a}
.tabs{position:sticky;top:0;background:rgba(17,17,17,0.9);backdrop-filter:blur(15px);display:flex;justify-content:space-around;padding:10px 0;z-index:10;border-bottom:1px solid #222}
.tabs button{background:#222;border:none;color:white;padding:10px 18px;border-radius:20px;cursor:pointer}
.tabs button.active{background:#ff0055}
.page{display:none;padding:20px;max-width:500px;margin:auto}
.page.active{display:block}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:15px}
.card{background:rgba(30,30,30,0.7);border:1px solid rgba(255,255,255,0.1);border-radius:20px;padding:22px 10px;text-decoration:none;color:white;display:block}
.card i{font-size:38px;display:block;margin-bottom:6px}
.search-box{background:rgba(30,30,30,0.8);display:flex;align-items:center;padding:5px 15px;border-radius:30px;margin-bottom:20px;border:1px solid #333}
.search-box input{flex:1;background:transparent;border:none;color:white;outline:none;padding:12px 5px;font-size:16px}
.search-box button{background:#ff0055;border:none;color:white;width:42px;height:42px;border-radius:50%;cursor:pointer}
input, select{width:92%;padding:12px;margin:8px 0;border-radius:12px;border:1px solid #333;background:#222;color:white;outline:none}
.btn{background:linear-gradient(135deg,#ff0055,#7c00ff);border:none;color:white;padding:13px 20px;border-radius:12px;width:92%;cursor:pointer;margin-top:10px;font-weight:bold}
.box{background:#1a1a1a;padding:15px;border-radius:15px;margin-top:15px;text-align:left;border:1px solid #333;word-break:break-all}
.tool-menu{display:flex;gap:8px;overflow-x:auto;padding-bottom:10px;scrollbar-width:none}
.tool-menu button{white-space:nowrap;background:#222;border:1px solid #333;color:white;padding:8px 14px;border-radius:20px}
.tool-menu button.active{background:#ff0055}
#fakeChatPreview{background:#0a3320 url('https://user-images.githubusercontent.com/15075759/28719144-86dc0f70-73b1-11e7-911d-60d70fcded21.png');padding:10px;border-radius:10px;min-height:300px;text-align:left;display:flex;flex-direction:column}
.chat-msg{padding:8px 12px;border-radius:8px;margin:6px 0;max-width:75%;width:fit-content;font-size:14px}
.chat-msg.receive{background:white;color:black;align-self:flex-start;border-top-left-radius:0}
.chat-msg.sent{background:#dcf8c6;color:black;align-self:flex-end;border-top-right-radius:0}
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
<a class="card" href="https://x.com"><i class="fab fa-twitter" style="color:#1DA1F2"></i>X / Twitter</a>
<a class="card" href="https://web.telegram.org"><i class="fab fa-telegram" style="color:#26A5E4"></i>Telegram</a>
<a class="card" href="https://www.snapchat.com"><i class="fab fa-snapchat" style="color:#FFFC00"></i>Snapchat</a>
<a class="card" href="https://www.tiktok.com"><i class="fab fa-tiktok" style="color:white"></i>TikTok</a>
</div>
</div>

<div id="tools" class="page">
<div class="tool-menu">
<button class="active" onclick="openTool('instaTool',this)">Insta DL</button>
<button onclick="openTool('ytTool',this)">YT Search</button>
<button onclick="openTool('fontTool',this)">Font Style</button>
<button onclick="openTool('fakeTool',this)">Fake Chat</button>
</div>

<div id="instaTool" class="tool-page">
<h3>All Video Downloader</h3>
<p style="font-size:12px;color:#aaa">Insta / YT / TikTok / FB sab chalega</p>
<input id="vlink" placeholder="Koi bhi link paste kar">
<button class="btn" onclick="downloadInsta()">Download Karo</button>
<div id="instaResult" class="box" style="display:none"></div>
</div>

<div id="ytTool" class="tool-page" style="display:none">
<h3>YouTube Search - FIXED</h3>
<input id="ytQuery" placeholder="Gaana / video naam likh">
<button class="btn" onclick="searchYT()">Search Karo</button>
<div id="ytResult" class="box" style="display:none"></div>
</div>

<div id="fontTool" class="tool-page" style="display:none">
<h3>Font Style Generator</h3>
<input id="fontInput" placeholder="Apna naam likh" oninput="genFonts()">
<div id="fontResult" class="box">Upar likh bhai</div>
</div>

<div id="fakeTool" class="tool-page" style="display:none">
<h3>Fake WhatsApp Chat - Sent + Receive</h3>
<input id="fakeName" placeholder="Naam likh (Ex: Jaan)">
<select id="msgType">
<option value="receive">Received - White Left</option>
<option value="sent">Sent - Green Right</option>
</select>
<input id="fakeMsg" placeholder="Message likh">
<button class="btn" onclick="addFakeMsg()">Message Add Karo</button>
<button class="btn" style="background:#333" onclick="downloadFake()">Screenshot Download</button>
<button class="btn" style="background:#900" onclick="clearFake()">Clear Chat</button>
<div id="fakeChatPreview" style="margin-top:15px"><div style="color:white;text-align:center;font-size:12px;background:rgba(0,0,0,0.4);padding:5px;border-radius:10px" id="fakeHeader">Jaan</div></div>
</div>

</div>

<script>
function openTab(id,btn){
document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'));
document.getElementById(id).classList.add('active');btn.classList.add('active');
}
function openTool(id,btn){
document.querySelectorAll('.tool-page').forEach(p=>p.style.display='none');
document.querySelectorAll('.tool-menu button').forEach(b=>b.classList.remove('active'));
document.getElementById(id).style.display='block';btn.classList.add('active');
}
function doSearch(){
let q=document.getElementById('gSearch').value.trim();
if(!q)return;
if(q.includes('.')&&!q.includes(' ')){if(!q.startsWith('http'))q='https://'+q;window.location.href=q;}
else{window.location.href='https://www.google.com/search?q='+encodeURIComponent(q);}
}
async function downloadInsta(){
 let link=document.getElementById('vlink').value.trim();
 let resDiv=document.getElementById('instaResult');
 if(!link){alert('Link daal');return;}
 resDiv.style.display='block';resDiv.innerHTML='⏳ Nikaal raha hu...';
 try{
  let r=await fetch('/api/dl?url='+encodeURIComponent(link));
  let data=await r.json();
  if(data.error){resDiv.innerHTML='❌ '+data.error;return;}
  resDiv.innerHTML='<a href="'+data.video_url+'" target="_blank" style="color:#25D366;font-weight:bold;font-size:18px">👉 DOWNLOAD KARO</a><br><br><video src="'+data.video_url+'" controls style="width:100%;border-radius:12px"></video>';
 }catch(e){resDiv.innerHTML='❌ Error - Link sahi daal';}
}
async function searchYT(){
 let q=document.getElementById('ytQuery').value.trim();
 let res=document.getElementById('ytResult');
 if(!q){alert('Kuch likh');return;}
 res.style.display='block';res.innerHTML='⏳ Search kar raha hu...';
 try{
  let r=await fetch('/api/ytsearch?q='+encodeURIComponent(q));
  let data=await r.json();
  if(data.error){res.innerHTML='❌ '+data.error;return;}
  let html='';
  data.videos.forEach(v=>{
   html+=`<div style="margin-bottom:14px;border-bottom:1px solid #333;padding-bottom:10px"><img src="${v.thumb}" style="width:100%;border-radius:10px"><br><b>${v.title}</b><br><a href="${v.url}" target="_blank" style="color:#ff0055">▶️ Watch</a> <a href="#" style="color:#25D366;margin-left:10px" onclick="document.getElementById('vlink').value='${v.url}';openTab('tools',document.querySelectorAll('.tabs button')[1]);openTool('instaTool',document.querySelector('.tool-menu button'));downloadInsta();return false;">⬇️ Download</a></div>`;
  });
  res.innerHTML=html || 'Kuch nahi mila';
 }catch(e){res.innerHTML='❌ Error';}
}
const fonts={
 bold: t=>t.split('').map(c=>{let m={"a":"𝐚","b":"𝐛","c":"𝐜","d":"𝐝","e":"𝐞","f":"𝐟","g":"𝐠","h":"𝐡","i":"𝐢","j":"𝐣","k":"𝐤","l":"𝐥","m":"𝐦","n":"𝐧","o":"𝐨","p":"𝐩","q":"𝐪","r":"𝐫","s":"𝐬","t":"𝐭","u":"𝐮","v":"𝐯","w":"𝐰","x":"𝐱","y":"𝐲","z":"𝐳"};return m[c.toLowerCase()]||c}).join(''),
 fancy: t=>t.split('').map(c=>{let m={"a":"𝓪","b":"𝓫","c":"𝓬","d":"𝓭","e":"𝓮","f":"𝓯","g":"𝓰","h":"𝓱","i":"𝓲","j":"𝓳","k":"𝓴","l":"𝓵","m":"𝓶","n":"𝓷","o":"𝓸","p":"𝓹","q":"𝓺","r":"𝓻","s":"𝓼","t":"𝓽","u":"𝓾","v":"𝓿","w":"𝔀","x":"𝔁","y":"𝔂","z":"𝔃"};return m[c.toLowerCase()]||c}).join(''),
};
function genFonts(){
 let t=document.getElementById('fontInput').value;
 let r=document.getElementById('fontResult');
 if(!t){r.innerHTML='Upar likh bhai';return;}
 r.innerHTML=`<div style="padding:8px">𝐁𝐨𝐥𝐝: ${fonts.bold(t)}</div><div style="padding:8px">𝓕𝓪𝓷𝓬𝔂: ${fonts.fancy(t)}</div><div style="padding:8px">✨ ${t} ✨</div><div style="padding:8px">🔥 ${t.toUpperCase()} 🔥</div>`;
}
function addFakeMsg(){
 let name=document.getElementById('fakeName').value||'Jaan';
 let msg=document.getElementById('fakeMsg').value;
 let type=document.getElementById('msgType').value;
 if(!msg)return;
 document.getElementById('fakeHeader').innerText=name;
 let div=document.createElement('div');
 div.className='chat-msg '+type;
 div.innerText=msg + ' ' + new Date().toLocaleTimeString([], {hour:'2-digit',minute:'2-digit'});
 document.getElementById('fakeChatPreview').appendChild(div);
 document.getElementById('fakeMsg').value='';
}
function clearFake(){
 document.getElementById('fakeChatPreview').innerHTML='<div style="color:white;text-align:center;font-size:12px;background:rgba(0,0,0,0.4);padding:5px;border-radius:10px" id="fakeHeader">Jaan</div>';
}
function downloadFake(){
 html2canvas(document.getElementById('fakeChatPreview')).then(c=>{
  let a=document.createElement('a');a.download='fake-chat.png';a.href=c.toDataURL();a.click();
 });
}
</script>
</body></html>
"""

@app.route('/api/dl')
@app.route('/api/insta')
def dl_api():
    url=request.args.get('url')
    if not url: return jsonify({"error":"Link de"}),400
    try:
        ydl_opts={'quiet':True,'skip_download':True,'noplaylist':True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info=ydl.extract_info(url,download=False)
            if 'entries' in info: info=info['entries'][0]
            vurl=info.get('url')
            if not vurl:
                vurl=info['formats'][-1]['url']
            return jsonify({"video_url":vurl})
    except Exception as e:
        return jsonify({"error":str(e)}),500

@app.route('/api/ytsearch')
def ytsearch():
    q=request.args.get('q')
    if not q: return jsonify({"error":"Query de"}),400
    try:
        # FIXED SEARCH - ytsearch ke liye alag options
        ydl_opts={'quiet':True,'skip_download':True,'extract_flat':True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info=ydl.extract_info(f"ytsearch8:{q}",download=False)
            vids=[]
            for e in info.get('entries',[]):
                if e:
                    vids.append({"title":e.get('title'),"url":e.get('url') or f"https://www.youtube.com/watch?v={e.get('id')}", "thumb":e.get('thumbnails',[{}])[0].get('url') if e.get('thumbnails') else f"https://i.ytimg.com/vi/{e.get('id')}/hqdefault.jpg"})
            return jsonify({"videos":vids})
    except Exception as e:
        return jsonify({"error":"YT Search Error: "+str(e)}),500

if __name__=="__main__":
    app.run(host="0.0.0.0",port=int(os.environ.get("PORT",10000)))
