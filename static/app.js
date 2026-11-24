const $=s=>document.querySelector(s);
const state={areas:[],area:localStorage.getItem("area-news-area")||"mohakhali",items:[],filter:"all"};
const icons=["🎓","🏥","🚌","🏙️"];
function esc(v){return String(v??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));}
function safeUrl(v){try{const u=new URL(v);return ["https:","http:"].includes(u.protocol)?esc(u.href):"#"}catch{return "#"}}
async function api(url){const r=await fetch(url);if(!r.ok)throw Error((await r.json().catch(()=>({}))).detail||"Could not load data");return r.json();}
function toast(t){const el=$("#toast");el.textContent=t;el.classList.add("show");setTimeout(()=>el.classList.remove("show"),2500);}
function current(){return state.areas.find(a=>a.id===state.area)||state.areas[0];}
function renderArea(a){
 $("#areaTitle").textContent=a.name+" / "+a.region;$("#feedScope").textContent=a.name;$("#areaOverview").textContent=a.overview;
 $("#scopeLabel").textContent=a.id==="mohakhali"?"LOCAL":a.id==="dhaka"?"CITY":"NATIONAL";
 const entries=Object.entries(a.key_spots||{}),places=entries.flatMap(x=>x[1]);$("#placeCount").textContent=places.length||"—";
 $("#directoryGrid").innerHTML=entries.length?entries.map(([k,v],i)=>'<article class="directory-card"><div>'+icons[i%4]+'</div><h3>'+esc(k)+'</h3><p>'+v.map(esc).join(" · ")+'</p></article>').join(""):'<div class="empty">Directory expansion is planned for this coverage area. Mohakhali’s original guide remains available.</div>';
}
function renderNews(items){
 state.items=items;const shown=state.filter==="local"&&state.area!=="mohakhali"?[]:items;
 $("#newsStatus").textContent=shown.length?shown.length+" stories · Open a headline to visit its source":"No headlines found. Try another search or refresh.";
 $("#newsGrid").innerHTML=shown.length?shown.map(x=>'<article class="news-card"><small>'+esc(x.source||"News source")+'</small><h3><a href="'+safeUrl(x.url)+'" target="_blank" rel="noopener noreferrer">'+esc(x.title)+'</a></h3><p>'+esc(x.published||"Latest update")+'</p></article>').join(""):'<div class="empty">No stories to show right now.</div>';
}
async function loadArea(){
 const a=current();if(!a)return;localStorage.setItem("area-news-area",a.id);renderArea(a);
 $("#weatherContent").textContent="Loading…";$("#newsGrid").innerHTML='<div class="empty">Loading headlines…</div>';
 const results=await Promise.allSettled([api("/api/news?area="+encodeURIComponent(a.id)),api("/api/weather?area="+encodeURIComponent(a.id))]);
 if(results[0].status==="fulfilled")renderNews(results[0].value.items);else $("#newsStatus").textContent=results[0].reason.message;
 if(results[1].status==="fulfilled"){const w=results[1].value;$("#weatherContent").textContent=w.available?Math.round(w.temperature)+"° · "+w.description+" · Humidity "+w.humidity+"%":"—° · Add OPENWEATHER_API_KEY for live weather";}else $("#weatherContent").textContent=results[1].reason.message;
 $("#updatedAt").textContent="UPDATED "+new Date().toLocaleTimeString([],{hour:"2-digit",minute:"2-digit"});
}
async function search(){
 const q=$("#searchInput").value.trim();if(q.length<2){toast("Enter at least 2 characters.");return;}
 $("#newsStatus").textContent="Searching…";
 try{const r=await api("/api/search?q="+encodeURIComponent(q)+"&area="+encodeURIComponent(state.area));renderNews(r.items);$("#newsStatus").textContent=r.items.length+" results for "+q;}
 catch(e){$("#newsStatus").textContent=e.message;}
}
async function init(){
 try{const r=await api("/api/areas");state.areas=r.areas;if(!state.areas.some(a=>a.id===state.area))state.area="mohakhali";
 $("#areaSelect").innerHTML=state.areas.map(a=>'<option value="'+esc(a.id)+'">'+esc(a.name+" — "+a.subtitle)+'</option>').join("");
 $("#areaSelect").value=state.area;await loadArea();
 }catch(e){$("#newsStatus").textContent=e.message;toast("Area News could not connect to its API.");}
}
$("#areaSelect").addEventListener("change",e=>{state.area=e.target.value;state.filter="all";document.querySelectorAll(".tabs button").forEach(b=>b.classList.toggle("active",b.dataset.filter==="all"));loadArea();});
$("#refreshBtn").addEventListener("click",loadArea);$("#searchBtn").addEventListener("click",search);
$("#searchInput").addEventListener("keydown",e=>{if(e.key==="Enter")search();});
document.querySelectorAll(".tabs button").forEach(b=>b.addEventListener("click",()=>{state.filter=b.dataset.filter;document.querySelectorAll(".tabs button").forEach(x=>x.classList.toggle("active",x===b));renderNews(state.items);}));
if("serviceWorker" in navigator)addEventListener("load",()=>navigator.serviceWorker.register("/static/sw.js").catch(()=>{}));
init();
