import os
from flask import Flask, request, jsonify, redirect
import yt_dlp

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kunal Pro Hub</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<style>
body{margin:0;font-family:sans-serif;color:white;text-align:center;min-height:100vh;background:#000}
body:before{content:'';position:fixed;top:0;left:0;width:100%;height:100%;z-index:-2;background:radial-gradient(circle at 20% 20%, #ff0055 0%, transparent 40%), radial-gradient(circle at 80% 80%, #7c00ff 0%, transparent 40%), #0a0a0a}
.tabs{position:sticky;top:0;background:rgba(17,17,17,0.9);backdrop-filter:blur(15px);display:flex;justify-content:space-around;padding:10px 0;z-index:10}
.tabs button{background:#222;border:none;color:white;padding:10px 18px;border-radius:20px}
.tabs button.active{background:#ff0055}
.page{display:none;padding:20px;max-width:450px;margin:auto}
.page.active{display:block}
input{width:90%;padding:12px;margin:8px 0;border-radius:12px;border:1px solid #333;background:#222;color:white}
.btn{background:linear-gradient(135deg,#ff0055,#7c00ff);border:none;color:white;padding:13px;border-radius:12px;width:92%;font-weight:bold;cursor:pointer}
.box{background:#1a1a1a;padding:15px;border-radius:15px;margin-top:15px;word-break:break-all}
</style></head>
<body>
<h2>KUNAL PRO HUB</h2>
<div class="tabs">
<button class="active" onclick="openTab('tools',this)">Tools</button>
<button onclick="openTab('home',this)">Home</button>
</div>

<div id="home" class="page">
<h3>Welcome</h3>
<p>Tools me jaake Insta download kar</p>
</div>

<div id="tools" class="page active">
<h3>Insta Video Downloader - NEW FIX</h3>
<input id="vlink" placeholder="Instagram Reels link paste kar">
<button class="btn" onclick="downloadVideo()">Download Karo</button>
<div id="result" class="box" style="display:none"></div>
</div>

<script>
function openTab(id,btn){
document.querySelectorAll('.page').forEach(p=>p.classList.remove('active'));
document.querySelectorAll('.tabs button').forEach(b=>b.classList.remove('active'));
document.getElementById(id).classList.add('active');btn.classList.add('active');
}
async function downloadVideo(){
 let link=document.getElementById('vlink').value.trim();
 let resDiv=document.getElementById('result');
 if(!link){alert('Link daal bhai');return;}
 resDiv.style.display='block';
 resDiv.innerHTML='⏳ Video nikal raha hu, ruk ja...';
 try{
   let r = await fetch('/api/insta?url='+encodeURIComponent(link));
   let data = await r.json();
   if(data.error){resDiv.innerHTML='❌ Error: '+data.error;return;}
   resDiv.innerHTML='<p>✅ Video mil gaya!</p><a href="'+data.video_url+'" target="_blank" style="color:#25D366;font-weight:bold;font-size:18px">👉 Yaha Click Karke Download Kar</a><br><br><video src="'+data.video_url+'" controls style="width:100%;border-radius:12px;margin-top:10px"></video>';
 }catch(e){resDiv.innerHTML='❌ Server error, dobara try kar';}
}
</script>
</body></html>
"""

@app.route('/api/insta')
def insta_api():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "Link nahi diya"}), 400
    try:
        ydl_opts = {'quiet': True, 'skip_download': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            # insta pe kabhi kabhi list aati hai
            if 'entries' in info:
                info = info['entries'][0]
            video_url = info.get('url')
            # agar direct url nahi to best format nikalo
            if not video_url and 'formats' in info:
                video_url = info['formats'][-1]['url']
            return jsonify({"video_url": video_url, "title": info.get('title','')})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port=int(os.environ.get("PORT",10000))
    app.run(host="0.0.0.0",port=port)
