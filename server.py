<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Nandi Corporate Travel AI (Demo)</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
body{margin:0;font-family:system-ui;background:#0b1020;color:#e5e7eb;display:flex}
.main{flex:1}
header{padding:12px;background:#020617;font-weight:600}
section{padding:10px}
.card{background:#fff;color:#020617;border-radius:12px;padding:12px;margin-top:10px}
.meta{font-size:13px;color:#475569}
.price{font-weight:700;margin-top:6px}
.gst{font-size:12px;color:#475569}
button,select,input{padding:8px;border-radius:8px;border:none}
button{background:#2563eb;color:white;cursor:pointer}
.controls{display:flex;gap:8px;flex-wrap:wrap}
.status{padding:6px 10px;border-radius:8px;font-size:13px}
.pending{background:#fde68a;color:#92400e}
.approved{background:#bbf7d0;color:#065f46}
.support{width:280px;background:#020617;border-left:1px solid #1e293b;display:flex;flex-direction:column}
.support-header{padding:10px;font-weight:600}
.support-body{flex:1;padding:10px;font-size:14px}
.support-msg{background:#111827;padding:8px;border-radius:8px;margin-bottom:6px}
.support-input{display:flex;gap:6px;padding:8px}
@media print{
.support,.controls,.approval-controls{display:none}
body{background:white;color:black}
}
</style>
</head>

<body>

<div class="main">

<header>🏢 Nandi Corporate Travel – Itinerary</header>

<section class="controls">
Fare:
<select id="fareType" onchange="render()">
<option value="public">Public</option>
<option value="corporate">Corporate</option>
</select>

<button onclick="addSegment()">➕ Add City</button>
<button onclick="saveDraft()">💾 Save Draft</button>
<button onclick="emailItinerary()">📧 Email</button>
<button onclick="exportPDF()">📄 Export PDF</button>
</section>

<section>
<h4>Passenger Details</h4>
<input id="pName" placeholder="Passenger Name">
<input id="pEmp" placeholder="Employee ID">
<input id="pEmail" placeholder="Email">
</section>

<section class="approval-controls">
<h4>Approval Status</h4>
<span id="approvalStatus" class="status pending">Pending Approval</span>
<button onclick="approve()">Approve</button>
</section>

<section id="itinerary"></section>

</div>

<!-- SUPPORT CHAT -->
<div class="support">
<div class="support-header">💬 Customer Support</div>
<div class="support-body" id="supportBody">
<div class="support-msg">Hi 👋 How can I help you?</div>
</div>
<div class="support-input">
<input id="supportInput" placeholder="Type message…" onkeydown="if(event.key==='Enter')sendSupport()">
<button onclick="sendSupport()">Send</button>
</div>
</div>

<script>
const GST=0.05;
let approval="Pending";
let segments=[
 {from:"BLR",to:"DEL",public:8000,corp:7600},
 {from:"DEL",to:"LHR",public:24000,corp:22800}
];

function addSegment(){
 segments.push({from:"City",to:"City",public:10000,corp:9500});
 render();
}

function approve(){
 approval="Approved";
 document.getElementById("approvalStatus").innerText="Approved";
 document.getElementById("approvalStatus").className="status approved";
 saveDraft();
}

function render(){
 const box=document.getElementById("itinerary");
 box.innerHTML="";
 const type=fareType.value;
 let total=0;

 segments.forEach((s,i)=>{
 const base=type==="public"?s.public:s.corp;
 const gst=Math.round(base*GST);
 total+=base+gst;

 box.innerHTML+=`
 <div class="card">
 <h4>✈ Segment ${i+1}: ${s.from} → ${s.to}</h4>
 <div class="price">₹${base+gst}</div>
 <div class="gst">Base ₹${base} + GST ₹${gst}</div>
 </div>`;
 });

 box.innerHTML+=`
 <div class="card">
 <h4>💰 Total Trip Cost</h4>
 <div class="price">₹${total}</div>
 </div>`;
}

function saveDraft(){
 const data={
 segments,approval,
 passenger:{
 name:pName.value,
 emp:pEmp.value,
 email:pEmail.value
 }
 };
 localStorage.setItem("corpTrip",JSON.stringify(data));
 alert("Draft saved");
}

const saved=localStorage.getItem("corpTrip");
if(saved){
 const d=JSON.parse(saved);
 segments=d.segments;
 approval=d.approval;
 pName.value=d.passenger.name;
 pEmp.value=d.passenger.emp;
 pEmail.value=d.passenger.email;
 if(approval==="Approved"){
 document.getElementById("approvalStatus").innerText="Approved";
 document.getElementById("approvalStatus").className="status approved";
 }
}
render();

function emailItinerary(){
 const body=document.getElementById("itinerary").innerText;
 window.location.href="mailto:?subject=Corporate Travel Itinerary&body="+encodeURIComponent(body);
}

function exportPDF(){window.print();}

function sendSupport(){
 const t=supportInput.value;
 if(!t)return;
 supportBody.innerHTML+=`<div class="support-msg">${t}</div>`;
 supportBody.innerHTML+=`<div class="support-msg">Thanks 👍 We’ll assist you shortly.</div>`;
 supportInput.value="";
}
</script>

</body>
</html>
