<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>AgriCold Connect</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --forest:#1a5c2a;--moss:#2e8b57;--mint:#a8d5b5;--sage:#d6efd8;
  --ice:#1b4f72;--glacier:#2e86c1;--frost:#d4e6f1;
  --amber:#f0a500;--amber-lt:#fef3d0;
  --red:#c0392b;--red-lt:#fdecea;
  --ink:#1a1f2e;--ink-60:#5a6070;--ink-30:#c2c7d0;
  --paper:#f4f6f2;--white:#ffffff;
  --card-bg:#ffffff;--border:rgba(0,0,0,.07);
  --cr:12px;--sh:0 2px 14px rgba(26,92,42,.10);
}
body.dark{
  --ink:#e8eaf0;--ink-60:#9aa0b0;--ink-30:#3a4050;
  --paper:#0f1117;--white:#1a1d27;--card-bg:#1e2130;
  --border:rgba(255,255,255,.07);--sage:#1a3020;--frost:#0d2035;
  --amber-lt:#2a1f00;--red-lt:#2a0a08;--sh:0 2px 14px rgba(0,0,0,.4);
}
html{font-size:15px}
body{font-family:'DM Sans',sans-serif;background:var(--paper);color:var(--ink);min-height:100vh;display:flex;flex-direction:column;transition:background .3s,color .3s}

/* ══ LOGIN PAGE ══ */
#loginPage{display:flex;min-height:100vh;background:var(--paper)}
#loginPage.hidden{display:none}
.login-left{flex:1;background:linear-gradient(145deg,var(--forest),#0d3318);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:48px;position:relative;overflow:hidden}
.login-left::before{content:'';position:absolute;inset:0;background:url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffffff' fill-opacity='0.03'%3E%3Ccircle cx='30' cy='30' r='20'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E")}
.login-brand{display:flex;flex-direction:column;align-items:center;gap:16px;margin-bottom:48px;z-index:1}
.login-logo{width:80px;height:80px;border-radius:20px;overflow:hidden;box-shadow:0 8px 32px rgba(0,0,0,.3)}
.login-brand-name{font-family:Arial,sans-serif;font-weight:700;font-size:2rem;color:#fff;text-transform:uppercase;letter-spacing:.05em}
.login-brand-sub{font-size:.85rem;color:var(--mint);text-align:center;max-width:260px;line-height:1.6}
.login-features{z-index:1;display:flex;flex-direction:column;gap:16px;width:100%;max-width:300px}
.login-feature{display:flex;align-items:center;gap:14px;background:rgba(255,255,255,.07);border-radius:12px;padding:14px 18px;border:1px solid rgba(255,255,255,.10)}
.login-feature-icon{font-size:1.4rem}
.login-feature-text{font-size:.83rem;color:rgba(255,255,255,.85);line-height:1.45}
.login-feature-text strong{color:#fff;display:block;margin-bottom:2px}

.login-right{width:480px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:48px 52px;background:var(--white)}
.login-form-title{font-family:'Syne',sans-serif;font-weight:800;font-size:1.6rem;color:var(--ink);margin-bottom:6px}
.login-form-sub{font-size:.83rem;color:var(--ink-60);margin-bottom:32px}
.login-form{width:100%}
.login-field{margin-bottom:16px}
.login-label{display:block;font-size:.72rem;font-weight:600;color:var(--ink-60);margin-bottom:6px;text-transform:uppercase;letter-spacing:.04em}
.login-input{width:100%;padding:12px 14px;border:1.5px solid var(--ink-30);border-radius:10px;font-size:.88rem;font-family:'DM Sans',sans-serif;color:var(--ink);background:var(--paper);outline:none;transition:border-color .18s,box-shadow .18s}
.login-input:focus{border-color:var(--moss);box-shadow:0 0 0 3px rgba(46,139,87,.12)}
.login-options{display:flex;align-items:center;justify-content:space-between;margin-bottom:22px}
.login-remember{display:flex;align-items:center;gap:7px;font-size:.8rem;color:var(--ink-60);cursor:pointer}
.login-remember input{accent-color:var(--moss)}
.login-forgot{font-size:.8rem;color:var(--moss);font-weight:600;cursor:pointer;text-decoration:none}
.login-forgot:hover{text-decoration:underline}
.login-btn{width:100%;padding:13px;background:linear-gradient(135deg,var(--forest),var(--moss));color:#fff;font-weight:700;font-size:.95rem;border:none;border-radius:10px;cursor:pointer;font-family:'Syne',sans-serif;box-shadow:0 4px 18px rgba(26,92,42,.3);transition:all .2s;margin-bottom:18px}
.login-btn:hover{transform:translateY(-1px);box-shadow:0 6px 24px rgba(26,92,42,.4)}
.login-btn:active{transform:translateY(0)}
.login-divider{display:flex;align-items:center;gap:12px;margin-bottom:18px}
.login-divider::before,.login-divider::after{content:'';flex:1;height:1px;background:var(--ink-30)}
.login-divider span{font-size:.75rem;color:var(--ink-60)}
.login-demo-btn{width:100%;padding:11px;background:var(--paper);border:1.5px solid var(--ink-30);border-radius:10px;font-size:.85rem;font-weight:600;color:var(--ink-60);cursor:pointer;font-family:'DM Sans',sans-serif;transition:all .18s}
.login-demo-btn:hover{border-color:var(--moss);color:var(--moss);background:var(--sage)}
.login-error{background:var(--red-lt);color:var(--red);border:1px solid rgba(192,57,43,.2);border-radius:8px;padding:10px 14px;font-size:.8rem;margin-bottom:14px;display:none}
.login-error.show{display:block}

/* ══ APP ══ */
#appPage{display:none;flex-direction:column;min-height:100vh}
#appPage.visible{display:flex}

/* ── TOPNAV ── */
.topnav{background:var(--forest);position:sticky;top:0;z-index:100;box-shadow:0 2px 12px rgba(0,0,0,.2);transition:background .3s}
.topnav-bar1{display:flex;align-items:center;justify-content:space-between;padding:0 28px;height:58px;border-bottom:1px solid rgba(255,255,255,.10)}
.logo-mark{display:flex;align-items:center;gap:10px}
.logo-icon{width:36px;height:36px;border-radius:9px;display:flex;align-items:center;justify-content:center;overflow:hidden;background:none;flex-shrink:0}
.logo-name{font-family:Arial,sans-serif;font-weight:700;font-size:1rem;color:#fff;text-transform:uppercase}
.logo-sub{font-size:.65rem;color:var(--mint);margin-top:1px}
.topnav-right{display:flex;align-items:center;gap:9px}
.search-bar{display:flex;align-items:center;gap:7px;background:rgba(255,255,255,.10);border:1px solid rgba(255,255,255,.20);border-radius:9px;padding:6px 13px;width:200px;cursor:pointer}
.search-bar input{border:none;background:transparent;outline:none;font-size:.82rem;color:#fff;font-family:'DM Sans',sans-serif;width:100%;cursor:pointer}
.search-bar input::placeholder{color:rgba(255,255,255,.5)}
.topnav-btn{width:34px;height:34px;border-radius:8px;border:1px solid rgba(255,255,255,.20);background:rgba(255,255,255,.08);display:flex;align-items:center;justify-content:center;font-size:.95rem;cursor:pointer;position:relative;transition:background .18s}
.topnav-btn:hover{background:rgba(255,255,255,.18)}
.notif-dot{position:absolute;top:5px;right:5px;width:7px;height:7px;background:var(--red);border-radius:50%;border:2px solid var(--forest)}
.user-card{display:flex;align-items:center;gap:8px;padding:5px 11px;border-radius:9px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.15);cursor:pointer}
.user-avatar{width:28px;height:28px;border-radius:50%;background:linear-gradient(135deg,var(--glacier),var(--ice));display:flex;align-items:center;justify-content:center;color:#fff;font-family:'Syne',sans-serif;font-weight:700;font-size:.7rem;flex-shrink:0}
.user-name{font-size:.76rem;font-weight:600;color:#fff}
.user-role{font-size:.62rem;color:var(--mint)}
.topnav-bar2{display:flex;align-items:center;padding:0 28px;gap:2px;height:42px}
.nav-item{display:flex;align-items:center;gap:6px;padding:7px 13px;border-radius:7px;color:rgba(255,255,255,.72);font-size:.81rem;font-weight:400;cursor:pointer;transition:background .18s,color .18s;white-space:nowrap;text-decoration:none;border:none;background:transparent}
.nav-item:hover{background:rgba(255,255,255,.10);color:#fff}
.nav-item.active{background:rgba(255,255,255,.16);color:#fff;font-weight:600}
.nav-icon{font-size:.88rem}
.nav-badge{background:var(--amber);color:var(--ink);font-size:.58rem;font-weight:700;padding:1px 6px;border-radius:20px}
.nav-divider{width:1px;height:18px;background:rgba(255,255,255,.15);margin:0 5px}

/* PAGE HEADER */
.page-header{background:var(--white);border-bottom:1px solid var(--border);padding:0 28px;height:54px;display:flex;align-items:center;justify-content:space-between;transition:background .3s}
.page-header-title{font-family:'Syne',sans-serif;font-size:1rem;font-weight:700;color:var(--ink)}
.page-header-sub{font-size:.72rem;color:var(--ink-60)}

/* SECTIONS */
.section{display:none;padding:24px 28px;flex:1;animation:fadeUp .35s ease}
.section.active{display:block}
@keyframes fadeUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}

/* CARDS */
.card{background:var(--card-bg);border-radius:var(--cr);box-shadow:var(--sh);overflow:hidden;margin-bottom:18px;transition:background .3s,box-shadow .3s}
.card-header{padding:15px 20px 11px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--border)}
.card-title{font-family:'Syne',sans-serif;font-size:.92rem;font-weight:700;color:var(--ink)}
.card-body{padding:16px 20px}
.card-action{font-size:.72rem;color:var(--moss);font-weight:600;cursor:pointer;padding:4px 10px;border-radius:7px;border:1px solid var(--moss);background:none;transition:background .18s}
.card-action:hover{background:var(--sage)}

/* STAT CARDS */
.stats-row{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px}
.stat-card{background:var(--card-bg);border-radius:var(--cr);padding:18px 20px;box-shadow:var(--sh);display:flex;flex-direction:column;gap:10px;position:relative;overflow:hidden;transition:background .3s}
.stat-card::before{content:'';position:absolute;top:0;left:0;right:0;height:3px}
.stat-card.green::before{background:linear-gradient(90deg,var(--forest),var(--moss))}
.stat-card.blue::before{background:linear-gradient(90deg,var(--ice),var(--glacier))}
.stat-card.amber::before{background:linear-gradient(90deg,#c87900,var(--amber))}
.stat-card.red::before{background:linear-gradient(90deg,#8e1c13,var(--red))}
.stat-top{display:flex;align-items:center;justify-content:space-between}
.stat-label{font-size:.7rem;font-weight:500;color:var(--ink-60);text-transform:uppercase;letter-spacing:.04em}
.stat-icon{width:32px;height:32px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:.9rem}
.stat-icon.green{background:var(--sage)}.stat-icon.blue{background:var(--frost)}.stat-icon.amber{background:var(--amber-lt)}.stat-icon.red{background:var(--red-lt)}
.stat-value{font-family:'Syne',sans-serif;font-size:1.8rem;font-weight:800;color:var(--ink);line-height:1}
.stat-delta{font-size:.68rem;font-weight:500}
.delta-up{color:var(--moss)}.delta-down{color:var(--red)}

/* GRID */
.grid-2{display:grid;grid-template-columns:1fr 320px;gap:18px}
.grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}

/* TABLE */
.tbl{width:100%;border-collapse:collapse}
.tbl th{font-size:.67rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;color:var(--ink-60);padding:8px 12px;text-align:left;border-bottom:1px solid var(--border);background:var(--paper)}
.tbl td{padding:11px 12px;font-size:.81rem;border-bottom:1px solid var(--border);vertical-align:middle;color:var(--ink)}
.tbl tr:last-child td{border-bottom:none}
.tbl tr:hover td{background:var(--sage)}

/* BADGES */
.badge{display:inline-flex;align-items:center;gap:4px;padding:3px 9px;border-radius:20px;font-size:.68rem;font-weight:600}
.badge-dot{width:5px;height:5px;border-radius:50%}
.badge.active{background:var(--sage);color:var(--forest)}.badge.active .badge-dot{background:var(--moss)}
.badge.pending{background:var(--amber-lt);color:#7a5000}.badge.pending .badge-dot{background:var(--amber)}
.badge.done{background:var(--ink-30);color:var(--ink-60)}.badge.done .badge-dot{background:var(--ink-60)}
.badge.transit{background:var(--frost);color:var(--ice)}.badge.transit .badge-dot{background:var(--glacier)}

/* TEMP */
.temp-unit{display:flex;align-items:center;gap:12px;padding:11px 13px;border-radius:10px;background:var(--paper);border:1px solid var(--border);margin-bottom:10px;transition:background .3s}
.temp-unit:last-child{margin-bottom:0}
.temp-icon{width:36px;height:36px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:1.05rem;flex-shrink:0}
.temp-icon.ok{background:var(--frost)}.temp-icon.crit{background:var(--red-lt)}
.temp-details{flex:1}
.temp-name{font-size:.81rem;font-weight:600;color:var(--ink)}
.temp-sub{font-size:.68rem;color:var(--ink-60);margin-top:1px}
.temp-gauge{display:flex;flex-direction:column;align-items:flex-end;gap:3px}
.temp-val{font-family:'Syne',sans-serif;font-size:1rem;font-weight:800}
.temp-val.ok{color:var(--glacier)}.temp-val.crit{color:var(--red)}
.temp-bar{width:70px;height:4px;background:var(--ink-30);border-radius:3px;overflow:hidden}
.temp-fill{height:100%;border-radius:3px}
.temp-fill.ok{background:var(--glacier)}.temp-fill.crit{background:var(--red)}

/* NOTIF */
.notif-item{display:flex;gap:10px;padding:10px 0;border-bottom:1px solid var(--border)}
.notif-item:last-child{border-bottom:none}
.notif-av{width:32px;height:32px;border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:.88rem;flex-shrink:0}
.notif-av.green{background:var(--sage)}.notif-av.blue{background:var(--frost)}.notif-av.amber{background:var(--amber-lt)}.notif-av.red{background:var(--red-lt)}
.notif-msg{font-size:.79rem;color:var(--ink);line-height:1.45}
.notif-msg strong{color:var(--moss)}
.notif-time{font-size:.66rem;color:var(--ink-60);margin-top:2px}
.notif-unread{width:7px;height:7px;border-radius:50%;background:var(--glacier);flex-shrink:0;margin-top:5px}

/* DELIVERY */
.delivery-item{display:flex;gap:12px;padding:12px 0;border-bottom:1px solid var(--border)}
.delivery-item:last-child{border-bottom:none}
.d-step-col{display:flex;flex-direction:column;align-items:center}
.d-bubble{width:24px;height:24px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.68rem;font-weight:700;flex-shrink:0}
.d-bubble.done{background:var(--moss);color:#fff}.d-bubble.transit{background:var(--glacier);color:#fff}.d-bubble.wait{background:var(--ink-30);color:#fff}
.d-line{width:2px;flex:1;background:var(--ink-30);margin:3px 0;min-height:8px}
.d-info{flex:1;display:flex;flex-direction:column;gap:3px}
.d-id{font-size:.68rem;font-weight:600;color:var(--ink-60)}
.d-name{font-size:.82rem;font-weight:600;color:var(--ink)}
.d-steps{display:flex;align-items:center;gap:4px}
.ds{font-size:.65rem;font-weight:600;padding:2px 7px;border-radius:4px}
.ds.done{background:var(--sage);color:var(--forest)}.ds.active{background:var(--frost);color:var(--ice)}.ds.pend{background:var(--ink-30);color:var(--ink-60)}
.d-arrow{font-size:.6rem;color:var(--ink-30)}
.eta-tag{font-size:.67rem;font-weight:600;color:var(--glacier);background:var(--frost);padding:2px 8px;border-radius:20px;align-self:flex-start}

/* ESTIMATOR */
.est-label{font-size:.7rem;font-weight:600;color:var(--ink-60);text-transform:uppercase;letter-spacing:.04em;margin-bottom:4px}
.est-input{width:100%;padding:9px 11px;border:1px solid var(--ink-30);border-radius:8px;font-size:.82rem;font-family:'DM Sans',sans-serif;color:var(--ink);background:var(--paper);outline:none;transition:border-color .18s}
.est-input:focus{border-color:var(--moss)}
.est-row{display:flex;gap:10px;margin-bottom:12px}
.est-result{background:linear-gradient(135deg,var(--forest),var(--moss));border-radius:10px;padding:14px 16px;display:flex;justify-content:space-between;align-items:center;margin-top:12px}
.est-result-label{font-size:.72rem;color:rgba(255,255,255,.75);font-weight:500}
.est-result-val{font-family:Arial,sans-serif;font-size:1.4rem;font-weight:800;color:#fff}

/* BUTTONS */
.btn{display:inline-flex;align-items:center;justify-content:center;gap:7px;padding:10px 18px;border-radius:9px;font-weight:700;font-size:.85rem;cursor:pointer;border:none;font-family:'Syne',sans-serif;transition:all .18s}
.btn-primary{background:var(--moss);color:#fff}.btn-primary:hover{background:var(--forest)}
.btn-amber{background:var(--amber);color:var(--ink)}.btn-amber:hover{background:#d99200}
.btn-ghost{background:var(--paper);color:var(--ink-60);border:1px solid var(--ink-30)}.btn-ghost:hover{background:var(--sage)}
.btn-full{width:100%;padding:12px}
.btn-danger{background:var(--red);color:#fff}.btn-danger:hover{background:#a93226}
.btn-sm{padding:6px 12px;font-size:.76rem;border-radius:7px}

/* FORM */
.form-group{margin-bottom:14px}
.form-label{display:block;font-size:.72rem;font-weight:600;color:var(--ink-60);margin-bottom:5px;text-transform:uppercase;letter-spacing:.04em}
.form-input,.form-select,.form-textarea{width:100%;padding:9px 13px;border:1px solid var(--ink-30);border-radius:8px;font-size:.84rem;font-family:'DM Sans',sans-serif;color:var(--ink);background:var(--paper);outline:none;transition:border-color .18s}
.form-input:focus,.form-select:focus,.form-textarea:focus{border-color:var(--moss)}
.form-textarea{resize:vertical;min-height:80px}
.form-row{display:grid;grid-template-columns:1fr 1fr;gap:12px}

/* MODAL */
.modal-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:200;align-items:center;justify-content:center;backdrop-filter:blur(3px)}
.modal-overlay.open{display:flex}
.modal{background:var(--card-bg);border-radius:16px;padding:26px 28px;width:460px;max-width:95vw;box-shadow:0 8px 40px rgba(0,0,0,.3);animation:fadeUp .3s ease;max-height:90vh;overflow-y:auto}
.modal-title{font-family:'Syne',sans-serif;font-size:1.08rem;font-weight:800;color:var(--ink);margin-bottom:18px}
.modal-btns{display:flex;gap:10px;margin-top:18px}

/* PRODUCTS */
.product-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.product-card{background:var(--card-bg);border-radius:var(--cr);box-shadow:var(--sh);padding:16px;display:flex;flex-direction:column;gap:10px;transition:background .3s}
.product-icon{font-size:2rem;text-align:center;padding:10px;background:var(--sage);border-radius:10px}
.product-name{font-family:'Syne',sans-serif;font-size:.9rem;font-weight:700;color:var(--ink)}
.product-meta{font-size:.75rem;color:var(--ink-60)}
.product-actions{display:flex;gap:8px;margin-top:4px}

/* REPORTS */
.report-stat-row{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-bottom:20px}
.report-stat{background:var(--card-bg);border-radius:var(--cr);padding:18px;box-shadow:var(--sh);text-align:center;transition:background .3s}
.report-stat-val{font-family:'Syne',sans-serif;font-size:1.6rem;font-weight:800;color:var(--forest)}
.report-stat-label{font-size:.72rem;color:var(--ink-60);margin-top:4px}
.bar-chart{display:flex;align-items:flex-end;gap:10px;height:140px;padding:0 4px}
.bar-col{display:flex;flex-direction:column;align-items:center;gap:6px;flex:1}
.bar{width:100%;background:linear-gradient(180deg,var(--moss),var(--forest));border-radius:5px 5px 0 0;transition:height .4s ease}
.bar-label{font-size:.65rem;color:var(--ink-60);font-weight:500}
.bar-val{font-size:.65rem;color:var(--ink);font-weight:700}

/* SETTINGS */
.settings-row{display:flex;align-items:center;justify-content:space-between;padding:11px 0;border-bottom:1px solid var(--border)}
.settings-row:last-child{border-bottom:none}
.settings-label{font-size:.83rem;font-weight:500;color:var(--ink)}
.settings-sub{font-size:.7rem;color:var(--ink-60);margin-top:2px}
.toggle{position:relative;width:40px;height:22px;cursor:pointer;flex-shrink:0}
.toggle input{opacity:0;width:0;height:0}
.toggle-slider{position:absolute;inset:0;background:var(--ink-30);border-radius:22px;transition:.3s}
.toggle-slider::before{content:'';position:absolute;width:16px;height:16px;left:3px;top:3px;background:#fff;border-radius:50%;transition:.3s}
.toggle input:checked+.toggle-slider{background:var(--moss)}
.toggle input:checked+.toggle-slider::before{transform:translateX(18px)}

/* DARK MODE TOGGLE SPECIAL */
.dm-toggle-row{display:flex;align-items:center;justify-content:space-between;padding:14px 18px;background:var(--paper);border-radius:10px;border:2px solid var(--moss);margin-bottom:16px}
.dm-label{font-family:'Syne',sans-serif;font-weight:700;font-size:.88rem;color:var(--ink)}
.dm-sub{font-size:.72rem;color:var(--ink-60);margin-top:2px}

/* TOAST */
.toast{position:fixed;bottom:24px;right:24px;background:var(--forest);color:#fff;padding:12px 20px;border-radius:10px;font-size:.83rem;font-weight:500;box-shadow:0 4px 20px rgba(0,0,0,.3);z-index:999;animation:slideIn .3s ease;display:flex;align-items:center;gap:8px}
@keyframes slideIn{from{transform:translateY(20px);opacity:0}to{transform:translateY(0);opacity:1}}

/* SEARCH OVERLAY */
.search-overlay{display:none;position:fixed;inset:0;background:rgba(0,0,0,.55);z-index:300;align-items:flex-start;justify-content:center;padding-top:80px}
.search-overlay.open{display:flex}
.search-box{background:var(--card-bg);border-radius:14px;width:560px;max-width:95vw;box-shadow:0 8px 40px rgba(0,0,0,.3);overflow:hidden}
.search-input-row{display:flex;align-items:center;gap:10px;padding:14px 18px;border-bottom:1px solid var(--border)}
.search-input-row input{border:none;outline:none;font-size:1rem;font-family:'DM Sans',sans-serif;color:var(--ink);flex:1;background:transparent}
.search-results{padding:12px}
.search-result-item{display:flex;align-items:center;gap:12px;padding:10px 12px;border-radius:9px;cursor:pointer;transition:background .15s}
.search-result-item:hover{background:var(--sage)}
.search-result-icon{width:32px;height:32px;border-radius:8px;background:var(--sage);display:flex;align-items:center;justify-content:center;font-size:.9rem;flex-shrink:0}
.search-result-title{font-size:.84rem;font-weight:600;color:var(--ink)}
.search-result-sub{font-size:.7rem;color:var(--ink-60)}

/* NOTIF PANEL */
.notif-panel{display:none;position:fixed;top:106px;right:28px;width:340px;background:var(--card-bg);border-radius:14px;box-shadow:0 8px 40px rgba(0,0,0,.25);z-index:150;animation:fadeUp .25s ease}
.notif-panel.open{display:block}
.notif-panel-header{padding:14px 18px;border-bottom:1px solid var(--border);display:flex;justify-content:space-between;align-items:center}
.notif-panel-title{font-family:'Syne',sans-serif;font-weight:700;font-size:.92rem;color:var(--ink)}
.notif-panel-body{padding:8px 14px;max-height:340px;overflow-y:auto}
.notif-panel-footer{padding:10px 18px;border-top:1px solid var(--border);text-align:center}
.notif-panel-footer a{font-size:.76rem;color:var(--moss);font-weight:600;cursor:pointer}

/* PROFILE PANEL */
.profile-panel{display:none;position:fixed;top:106px;right:28px;width:240px;background:var(--card-bg);border-radius:14px;box-shadow:0 8px 40px rgba(0,0,0,.25);z-index:150;animation:fadeUp .25s ease;overflow:hidden}
.profile-panel.open{display:block}
.profile-panel-top{padding:18px;background:linear-gradient(135deg,var(--forest),var(--moss));color:#fff;text-align:center}
.profile-big-av{width:52px;height:52px;border-radius:50%;background:rgba(255,255,255,.25);display:flex;align-items:center;justify-content:center;font-family:'Syne',sans-serif;font-weight:800;font-size:1.2rem;color:#fff;margin:0 auto 8px}
.profile-panel-name{font-family:'Syne',sans-serif;font-weight:700;font-size:.95rem}
.profile-panel-role{font-size:.7rem;opacity:.8;margin-top:2px}
.profile-panel-item{display:flex;align-items:center;gap:10px;padding:11px 18px;font-size:.82rem;color:var(--ink);cursor:pointer;transition:background .15s;border-bottom:1px solid var(--border)}
.profile-panel-item:hover{background:var(--sage)}
.profile-panel-item:last-child{border-bottom:none;color:var(--red)}

/* QUICK BOOK */
.quick-book-btn{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;padding:12px;background:linear-gradient(135deg,var(--forest),var(--moss));color:#fff;font-weight:700;font-size:.88rem;border:none;border-radius:10px;cursor:pointer;font-family:'Syne',sans-serif;box-shadow:0 4px 18px rgba(26,92,42,.25);transition:all .2s}
.quick-book-btn:hover{box-shadow:0 6px 24px rgba(26,92,42,.35);transform:translateY(-1px)}

/* LOGOUT SCREEN */
#logoutScreen{display:none;position:fixed;inset:0;background:var(--paper);z-index:999;align-items:center;justify-content:center;flex-direction:column;gap:20px}
#logoutScreen.show{display:flex}
.logout-spinner{width:48px;height:48px;border:4px solid var(--ink-30);border-top-color:var(--moss);border-radius:50%;animation:spin 1s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
</style>
</head>
<body>

<!-- ══════════════ LOGIN PAGE ══════════════ -->
<div id="loginPage">
  <div class="login-left">
    <div class="login-brand">
      <div class="login-logo">
        <svg viewBox="0 0 100 100" width="80" height="80" xmlns="http://www.w3.org/2000/svg">
          <circle cx="50" cy="50" r="50" fill="#c8a96e"/>
          <circle cx="50" cy="50" r="50" fill="#5a9e4e" clip-path="url(#lhL)"/>
          <clipPath id="lhL"><rect x="0" y="0" width="50" height="100"/></clipPath>
          <path d="M28,72 Q32,58 50,52 Q68,58 72,72 Q60,80 50,81 Q40,80 28,72Z" fill="white" opacity="0.92"/>
          <path d="M50,52 Q38,38 36,24 Q44,28 50,40 Q50,46 50,52Z" fill="white" opacity="0.92"/>
          <path d="M50,52 Q62,38 64,24 Q56,28 50,40 Q50,46 50,52Z" fill="white" opacity="0.92"/>
        </svg>
      </div>
      <div class="login-brand-name">AgriCold</div>
      <div class="login-brand-sub">Smart cold chain management for Filipino farmers and merchants</div>
    </div>
    <div class="login-features">
      <div class="login-feature"><div class="login-feature-icon">🌡️</div><div class="login-feature-text"><strong>Real-Time Monitoring</strong>Track storage temperatures 24/7 with instant alerts</div></div>
      <div class="login-feature"><div class="login-feature-icon">🚚</div><div class="login-feature-text"><strong>Delivery Tracking</strong>Live GPS tracking for all your produce deliveries</div></div>
      <div class="login-feature"><div class="login-feature-icon">📦</div><div class="login-feature-text"><strong>Easy Booking</strong>Book cold storage units in under 2 minutes</div></div>
    </div>
  </div>
  <div class="login-right">
    <div style="text-align:center;margin-bottom:28px">
      <div class="login-form-title" id="loginTitle">Welcome back 👋</div>
      <div class="login-form-sub" id="loginSub">Sign in to your AgriCold account</div>
    </div>
    <div class="login-error" id="loginError">❌ Incorrect email or password. Try <strong>admin@agricold.ph</strong> / <strong>1234</strong></div>
    <div class="login-form">
      <div class="login-field">
        <label class="login-label">Email Address</label>
        <input class="login-input" type="email" id="loginEmail" placeholder="your@email.com" value="admin@agricold.ph"/>
      </div>
      <div class="login-field">
        <label class="login-label">Password</label>
        <input class="login-input" type="password" id="loginPassword" placeholder="••••••••" value="1234" onkeydown="if(event.key==='Enter')doLogin()"/>
      </div>
      <div class="login-options">
        <label class="login-remember"><input type="checkbox" checked/> Remember me</label>
        <a class="login-forgot" onclick="showToast('📧 Reset link sent to your email!')">Forgot password?</a>
      </div>
      <button class="login-btn" onclick="doLogin()">Sign In →</button>
      <div class="login-divider"><span>or</span></div>
      <button class="login-demo-btn" onclick="demoLogin()">🚀 Try Demo Account</button>
    </div>
    <div style="margin-top:24px;text-align:center;font-size:.76rem;color:var(--ink-60)">Don't have an account? <a style="color:var(--moss);font-weight:600;cursor:pointer" onclick="showToast('📝 Contact your AgriCold admin to register.')">Register here</a></div>
  </div>
</div>

<!-- ══════════════ APP PAGE ══════════════ -->
<div id="appPage">

<!-- TOPNAV -->
<nav class="topnav">
  <div class="topnav-bar1">
    <div class="logo-mark">
      <div class="logo-icon">
        <svg viewBox="0 0 100 100" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
          <circle cx="50" cy="50" r="50" fill="#c8a96e"/>
          <circle cx="50" cy="50" r="50" fill="#5a9e4e" clip-path="url(#lhA)"/>
          <clipPath id="lhA"><rect x="0" y="0" width="50" height="100"/></clipPath>
          <path d="M28,72 Q32,58 50,52 Q68,58 72,72 Q60,80 50,81 Q40,80 28,72Z" fill="white" opacity="0.92"/>
          <path d="M50,52 Q38,38 36,24 Q44,28 50,40 Q50,46 50,52Z" fill="white" opacity="0.92"/>
          <path d="M50,52 Q62,38 64,24 Q56,28 50,40 Q50,46 50,52Z" fill="white" opacity="0.92"/>
        </svg>
      </div>
      <div><div class="logo-name">AgriCold</div><div class="logo-sub">Connect v1.0</div></div>
    </div>
    <div class="topnav-right">
      <div class="search-bar" onclick="openSearch()"><span>🔍</span><input type="text" placeholder="Search anything…" readonly/></div>
      <button class="topnav-btn" id="notifBtn" onclick="toggleNotifPanel()">🔔<span class="notif-dot" id="notifDot"></span></button>
      <button class="topnav-btn" onclick="showToast('💡 Help: Use the top menu to navigate!')">❓</button>
      <div class="user-card" onclick="toggleProfilePanel()">
        <div class="user-avatar" id="navAvatar">JR</div>
        <div><div class="user-name" id="navName">Juan Reyes</div><div class="user-role" id="navRole">Merchant · Cebu</div></div>
      </div>
    </div>
  </div>
  <div class="topnav-bar2">
    <button class="nav-item active" id="nav-dashboard" onclick="navigate('dashboard')"><span class="nav-icon">🏠</span> <span data-t="dashboard">Dashboard</span></button>
    <button class="nav-item" id="nav-bookings" onclick="navigate('bookings')"><span class="nav-icon">📦</span> <span data-t="my_bookings">My Bookings</span> <span class="nav-badge" id="booking-badge">3</span></button>
    <button class="nav-item" id="nav-delivery" onclick="navigate('delivery')"><span class="nav-icon">🚚</span> <span data-t="delivery">Delivery Tracker</span></button>
    <button class="nav-item" id="nav-products" onclick="navigate('products')"><span class="nav-icon">🌾</span> <span data-t="products">My Products</span></button>
    <div class="nav-divider"></div>
    <button class="nav-item" id="nav-reports" onclick="navigate('reports')"><span class="nav-icon">🧾</span> <span data-t="reports">Reports</span></button>
    <button class="nav-item" id="nav-notifications" onclick="navigate('notifications')"><span class="nav-icon">💬</span> <span data-t="notifications">Notifications</span> <span class="nav-badge" id="notif-badge">5</span></button>
    <button class="nav-item" id="nav-settings" onclick="navigate('settings')"><span class="nav-icon">⚙️</span> <span data-t="settings">Settings</span></button>
  </div>
</nav>

<!-- PAGE HEADER -->
<div class="page-header">
  <div>
    <div class="page-header-title" id="pageTitle">Merchant Dashboard</div>
    <div class="page-header-sub" id="pageSub">Wednesday, May 13, 2026 — Good morning! 👋</div>
  </div>
  <button class="btn btn-primary btn-sm" id="pageActionBtn" onclick="openBookingModal()">➕ <span data-t="new_booking">New Booking</span></button>
</div>

<!-- ════ DASHBOARD ════ -->
<section class="section active" id="sec-dashboard">
  <div class="stats-row">
    <div class="stat-card green"><div class="stat-top"><span class="stat-label" data-t="active_bookings">Active Bookings</span><div class="stat-icon green">📦</div></div><div class="stat-value">7</div><div class="stat-delta delta-up">↑ 2 from last week</div></div>
    <div class="stat-card blue"><div class="stat-top"><span class="stat-label" data-t="storage_units">Storage Units</span><div class="stat-icon blue">🏭</div></div><div class="stat-value">3</div><div class="stat-delta delta-up">↑ 1 new unit rented</div></div>
    <div class="stat-card amber"><div class="stat-top"><span class="stat-label" data-t="in_transit">In Transit</span><div class="stat-icon amber">🚚</div></div><div class="stat-value">2</div><div class="stat-delta delta-up">Avg. ETA 1.5 hrs</div></div>
    <div class="stat-card red"><div class="stat-top"><span class="stat-label" data-t="temp_alerts">Temp Alerts</span><div class="stat-icon red">⚠️</div></div><div class="stat-value">1</div><div class="stat-delta delta-down">Unit C needs attention</div></div>
  </div>
  <div class="grid-2" style="margin-bottom:18px">
    <div class="card">
      <div class="card-header"><span class="card-title">📋 Recent Bookings</span><button class="card-action" onclick="navigate('bookings')">View All</button></div>
      <div class="card-body" style="padding:0">
        <table class="tbl"><thead><tr><th>ID</th><th>Product</th><th>Unit</th><th>Duration</th><th>Status</th></tr></thead>
        <tbody>
          <tr><td style="font-weight:600;color:var(--ink-60);font-size:.7rem">#BK-2041</td><td>Lettuce (80 kg)</td><td>Unit A–2°C</td><td>3 days</td><td><span class="badge active"><span class="badge-dot"></span>Active</span></td></tr>
          <tr><td style="font-weight:600;color:var(--ink-60);font-size:.7rem">#BK-2042</td><td>Tomatoes (50 kg)</td><td>Unit B–8°C</td><td>5 days</td><td><span class="badge active"><span class="badge-dot"></span>Active</span></td></tr>
          <tr><td style="font-weight:600;color:var(--ink-60);font-size:.7rem">#BK-2043</td><td>Mangoes (120 kg)</td><td>Unit C–10°C</td><td>2 days</td><td><span class="badge pending"><span class="badge-dot"></span>Pending</span></td></tr>
          <tr><td style="font-weight:600;color:var(--ink-60);font-size:.7rem">#BK-2039</td><td>Carrots (35 kg)</td><td>Unit A–2°C</td><td>4 days</td><td><span class="badge done"><span class="badge-dot"></span>Done</span></td></tr>
        </tbody></table>
      </div>
    </div>
    <div class="card">
      <div class="card-header"><span class="card-title">🔔 Latest Alerts</span><button class="card-action" onclick="navigate('notifications')">View All</button></div>
      <div class="card-body">
        <div class="notif-item"><div class="notif-av red">⚠️</div><div><div class="notif-msg"><strong>Temperature Alert</strong> — Unit C: 14°C</div><div class="notif-time">2 minutes ago</div></div><div class="notif-unread"></div></div>
        <div class="notif-item"><div class="notif-av green">✅</div><div><div class="notif-msg"><strong>Booking #BK-2043</strong> approved.</div><div class="notif-time">1 hour ago</div></div><div class="notif-unread"></div></div>
        <div class="notif-item"><div class="notif-av blue">🚚</div><div><div class="notif-msg"><strong>DL-0891</strong> in transit — ETA 45 mins.</div><div class="notif-time">3 hours ago</div></div></div>
        <div class="notif-item"><div class="notif-av amber">💰</div><div><div class="notif-msg">Payment confirmed <strong>#BK-2039</strong>.</div><div class="notif-time">Yesterday</div></div></div>
      </div>
    </div>
  </div>
  <div class="grid-3">
    <div class="card">
      <div class="card-header"><span class="card-title">🌡️ Temperature Monitor</span><button class="card-action" onclick="navigate('delivery')">Details</button></div>
      <div class="card-body">
        <div class="temp-unit"><div class="temp-icon ok">❄️</div><div class="temp-details"><div class="temp-name">Unit A</div><div class="temp-sub">Lettuce · 2°C</div></div><div class="temp-gauge"><span class="temp-val ok">2.1°C</span><div class="temp-bar"><div class="temp-fill ok" style="width:22%"></div></div></div></div>
        <div class="temp-unit"><div class="temp-icon ok">🧊</div><div class="temp-details"><div class="temp-name">Unit B</div><div class="temp-sub">Tomatoes · 8°C</div></div><div class="temp-gauge"><span class="temp-val ok">7.8°C</span><div class="temp-bar"><div class="temp-fill ok" style="width:58%"></div></div></div></div>
        <div class="temp-unit" style="border:1px solid #f5c6c6;background:var(--red-lt)"><div class="temp-icon crit">🔴</div><div class="temp-details"><div class="temp-name">Unit C ⚠️</div><div class="temp-sub">Mangoes · 10°C</div></div><div class="temp-gauge"><span class="temp-val crit">14.2°C</span><div class="temp-bar"><div class="temp-fill crit" style="width:85%"></div></div></div></div>
      </div>
    </div>
    <div class="card">
      <div class="card-header"><span class="card-title">🚚 Active Deliveries</span><button class="card-action" onclick="navigate('delivery')">Full Tracker</button></div>
      <div class="card-body">
        <div class="delivery-item"><div class="d-step-col"><div class="d-bubble done">✓</div><div class="d-line"></div><div class="d-bubble transit">→</div></div><div class="d-info"><span class="d-id">#DL-0891</span><span class="d-name">Lettuce Batch — 80 kg</span><div class="d-steps"><span class="ds done">Preparing</span><span class="d-arrow">›</span><span class="ds active">In Transit</span><span class="d-arrow">›</span><span class="ds pend">Delivered</span></div><span class="eta-tag">⏱ ETA: 45 mins</span></div></div>
        <div class="delivery-item"><div class="d-step-col"><div class="d-bubble done">✓</div><div class="d-line"></div><div class="d-bubble transit">→</div></div><div class="d-info"><span class="d-id">#DL-0895</span><span class="d-name">Tomatoes — 50 kg</span><div class="d-steps"><span class="ds done">Preparing</span><span class="d-arrow">›</span><span class="ds active">In Transit</span><span class="d-arrow">›</span><span class="ds pend">Delivered</span></div><span class="eta-tag">⏱ ETA: 2 hrs</span></div></div>
      </div>
    </div>
    <div style="display:flex;flex-direction:column;gap:16px">
      <div class="card">
        <div class="card-header"><span class="card-title">🧮 Cost Estimator</span></div>
        <div class="card-body">
          <div class="form-group"><div class="est-label">Storage Type</div><select class="est-input form-select" id="storageType" onchange="calcCost()"><option value="180">Deep Cold (2°C) — ₱180/day</option><option value="120">Chilled (8°C) — ₱120/day</option><option value="80">Cool Room (12°C) — ₱80/day</option></select></div>
          <div class="est-row"><div style="flex:1"><div class="est-label">Qty (kg)</div><input class="est-input" id="qty" type="number" value="80" min="1" oninput="calcCost()"/></div><div style="flex:1"><div class="est-label">Days</div><input class="est-input" id="days" type="number" value="3" min="1" oninput="calcCost()"/></div></div>
          <div class="est-result"><div><div class="est-result-label">Estimated Cost</div><div class="est-result-val" id="estTotal">₱540.00</div></div><div style="text-align:right"><div class="est-result-label">Delivery Add-on</div><div style="color:rgba(255,255,255,.8);font-size:.8rem;font-weight:600" id="estDelivery">+₱250</div></div></div>
        </div>
      </div>
      <div class="card">
        <div class="card-header"><span class="card-title">➕ Quick Book</span></div>
        <div class="card-body"><p style="font-size:.79rem;color:var(--ink-60);margin-bottom:12px;line-height:1.5">Book cold storage or delivery in under 2 minutes.</p><button class="quick-book-btn" onclick="openBookingModal()">📦 Book Storage / Delivery</button></div>
      </div>
    </div>
  </div>
</section>

<!-- ════ BOOKINGS ════ -->
<section class="section" id="sec-bookings">
  <div style="display:flex;gap:10px;margin-bottom:18px;align-items:center">
    <select class="form-select" id="bookingFilter" onchange="filterBookings()" style="width:160px"><option value="all">All Status</option><option value="active">Active</option><option value="pending">Pending</option><option value="done">Done</option></select>
    <input class="form-input" id="bookingSearch" placeholder="🔍 Search bookings…" oninput="filterBookings()" style="flex:1;max-width:280px"/>
    <select class="form-select" id="bookingSort" onchange="filterBookings()" style="width:160px">
      <option value="default">Sort: Default</option>
      <option value="qty_asc">Qty: Low → High</option>
      <option value="qty_desc">Qty: High → Low</option>
    </select>
    <button class="btn btn-primary btn-sm" onclick="openBookingModal()" style="margin-left:auto">➕ New Booking</button>
  </div>
  <div class="card">
    <div class="card-header"><span class="card-title">📦 All Bookings</span><span id="bookingCount" style="font-size:.75rem;color:var(--ink-60)">6 bookings</span></div>
    <div class="card-body" style="padding:0"><table class="tbl" id="bookingsTable"><thead><tr><th>Booking ID</th><th>Product</th><th>Unit / Temp</th><th>Qty</th><th>Duration</th><th>Cost</th><th>Status</th><th>Actions</th></tr></thead><tbody id="bookingsTbody"></tbody></table></div>
  </div>
</section>

<!-- ════ DELIVERY ════ -->
<section class="section" id="sec-delivery">
  <div class="grid-2" style="margin-bottom:18px">
    <div class="card"><div class="card-header"><span class="card-title">🚚 Active Deliveries</span></div><div class="card-body" id="deliveryList"></div></div>
    <div style="display:flex;flex-direction:column;gap:16px">
      <div class="card">
        <div class="card-header"><span class="card-title">🌡️ Storage Temperatures</span></div>
        <div class="card-body">
          <div class="temp-unit"><div class="temp-icon ok">❄️</div><div class="temp-details"><div class="temp-name">Unit A</div><div class="temp-sub">Lettuce · 2°C</div></div><div class="temp-gauge"><span class="temp-val ok">2.1°C</span><div class="temp-bar"><div class="temp-fill ok" style="width:22%"></div></div></div></div>
          <div class="temp-unit"><div class="temp-icon ok">🧊</div><div class="temp-details"><div class="temp-name">Unit B</div><div class="temp-sub">Tomatoes · 8°C</div></div><div class="temp-gauge"><span class="temp-val ok">7.8°C</span><div class="temp-bar"><div class="temp-fill ok" style="width:58%"></div></div></div></div>
          <div class="temp-unit" style="border:1px solid #f5c6c6;background:var(--red-lt)"><div class="temp-icon crit">🔴</div><div class="temp-details"><div class="temp-name">Unit C ⚠️</div><div class="temp-sub">Mangoes · 10°C</div></div><div class="temp-gauge"><span class="temp-val crit">14.2°C</span><div class="temp-bar"><div class="temp-fill crit" style="width:85%"></div></div></div></div>
        </div>
      </div>
      <div class="card">
        <div class="card-header"><span class="card-title">📦 Request Delivery</span></div>
        <div class="card-body">
          <div class="form-group"><div class="est-label">Booking ID</div><select class="form-select"><option>#BK-2041 — Lettuce</option><option>#BK-2042 — Tomatoes</option><option>#BK-2043 — Mangoes</option></select></div>
          <div class="form-group"><div class="est-label">Destination</div><input class="form-input" placeholder="e.g. Cebu City Market"/></div>
          <div class="form-group"><div class="est-label">Date & Time</div><input class="form-input" type="datetime-local"/></div>
          <button class="btn btn-primary btn-full" onclick="requestDelivery()">🚚 Request Delivery</button>
        </div>
      </div>
    </div>
  </div>
  <div class="card"><div class="card-header"><span class="card-title">📋 Delivery History</span></div><div class="card-body" style="padding:0"><table class="tbl"><thead><tr><th>ID</th><th>Product</th><th>Destination</th><th>Date</th><th>Status</th></tr></thead><tbody><tr><td style="font-weight:600;color:var(--ink-60);font-size:.7rem">#DL-0885</td><td>Carrots 35kg</td><td>Mandaue Market</td><td>May 12</td><td><span class="badge done"><span class="badge-dot"></span>Done</span></td></tr><tr><td style="font-weight:600;color:var(--ink-60);font-size:.7rem">#DL-0870</td><td>Cabbage 90kg</td><td>SM Cebu</td><td>May 10</td><td><span class="badge done"><span class="badge-dot"></span>Done</span></td></tr></tbody></table></div></div>
</section>

<!-- ════ PRODUCTS ════ -->
<section class="section" id="sec-products">
  <div style="display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:18px">
    <input class="form-input" id="productSearch" placeholder="🔍 Search products…" oninput="filterProducts()" style="max-width:240px"/>
    <select class="form-select" id="productSort" onchange="filterProducts()" style="width:180px">
      <option value="default">Sort: Default</option>
      <option value="alpha_asc">Name: A → Z</option>
      <option value="alpha_desc">Name: Z → A</option>
      <option value="kg_asc">Qty: Low → High</option>
      <option value="kg_desc">Qty: High → Low</option>
    </select>
    <button class="btn btn-primary btn-sm" onclick="openProductModal()" style="margin-left:auto">➕ Add Product</button>
  </div>
  <div class="product-grid" id="productGrid"></div>
</section>

<!-- ════ REPORTS ════ -->
<section class="section" id="sec-reports">
  <div class="report-stat-row">
    <div class="report-stat"><div class="report-stat-val">₱8,340</div><div class="report-stat-label">Total Spent (May)</div></div>
    <div class="report-stat"><div class="report-stat-val">23</div><div class="report-stat-label">Total Bookings</div></div>
    <div class="report-stat"><div class="report-stat-val">415 kg</div><div class="report-stat-label">Total Stored</div></div>
  </div>
  <div class="grid-2">
    <div class="card"><div class="card-header"><span class="card-title">📊 Monthly Bookings 2026</span></div><div class="card-body"><div class="bar-chart" id="barChart"></div></div></div>
    <div class="card"><div class="card-header"><span class="card-title">🥬 Storage by Product</span></div><div class="card-body" style="padding:0"><table class="tbl"><thead><tr><th>Product</th><th>Qty</th><th>Unit</th><th>Days</th><th>Cost</th></tr></thead><tbody><tr><td>🥬 Lettuce</td><td>80kg</td><td>Unit A</td><td>3</td><td>₱540</td></tr><tr><td>🍅 Tomatoes</td><td>50kg</td><td>Unit B</td><td>5</td><td>₱600</td></tr><tr><td>🥭 Mangoes</td><td>120kg</td><td>Unit C</td><td>2</td><td>₱160</td></tr><tr><td>🥕 Carrots</td><td>35kg</td><td>Unit A</td><td>4</td><td>₱720</td></tr></tbody></table></div></div>
  </div>
</section>

<!-- ════ NOTIFICATIONS ════ -->
<section class="section" id="sec-notifications">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:18px">
    <div style="display:flex;gap:8px">
      <button class="btn btn-ghost btn-sm" onclick="filterNotifs('all')" id="nf-all" style="background:var(--sage);border-color:var(--moss)">All</button>
      <button class="btn btn-ghost btn-sm" onclick="filterNotifs('unread')" id="nf-unread">Unread</button>
      <button class="btn btn-ghost btn-sm" onclick="filterNotifs('alert')" id="nf-alert">Alerts</button>
    </div>
    <button class="btn btn-ghost btn-sm" onclick="markAllRead()">✅ Mark All Read</button>
  </div>
  <div class="card"><div class="card-body" id="notifFullList"></div></div>
</section>

<!-- ════ SETTINGS ════ -->
<section class="section" id="sec-settings">
  <!-- DARK MODE BANNER -->
  <div class="dm-toggle-row" style="margin-bottom:20px">
    <div><div class="dm-label">🌙 Dark Mode</div><div class="dm-sub" id="dmSubText">Currently using Light Mode</div></div>
    <label class="toggle" style="transform:scale(1.3);margin-left:12px"><input type="checkbox" id="darkModeToggle" onchange="toggleDarkMode(this.checked)"/><span class="toggle-slider"></span></label>
  </div>
  <div class="grid-2">
    <div>
      <div class="card" style="margin-bottom:18px">
        <div class="card-header"><span class="card-title">👤 Profile Settings</span></div>
        <div class="card-body">
          <div class="form-row"><div class="form-group"><label class="form-label">First Name</label><input class="form-input" id="s-fname" value="Juan"/></div><div class="form-group"><label class="form-label">Last Name</label><input class="form-input" id="s-lname" value="Reyes"/></div></div>
          <div class="form-group"><label class="form-label">Email</label><input class="form-input" id="s-email" value="juan@agricold.ph" type="email"/></div>
          <div class="form-group"><label class="form-label">Phone</label><input class="form-input" value="+63 917 555 0123" type="tel"/></div>
          <div class="form-group"><label class="form-label">Business Location</label><input class="form-input" id="s-loc" value="Cebu City, Philippines"/></div>
          <button class="btn btn-primary btn-sm" onclick="saveProfile()">💾 Save Changes</button>
        </div>
      </div>
      <div class="card">
        <div class="card-header"><span class="card-title">🔒 Change Password</span></div>
        <div class="card-body">
          <div class="form-group"><label class="form-label">Current Password</label><input class="form-input" id="s-curpw" type="password" placeholder="••••••••"/></div>
          <div class="form-group"><label class="form-label">New Password</label><input class="form-input" id="s-newpw" type="password" placeholder="••••••••"/></div>
          <div class="form-group"><label class="form-label">Confirm Password</label><input class="form-input" id="s-confpw" type="password" placeholder="••••••••"/></div>
          <button class="btn btn-primary btn-sm" onclick="changePassword()">Update Password</button>
        </div>
      </div>
    </div>
    <div>
      <div class="card" style="margin-bottom:18px">
        <div class="card-header"><span class="card-title">🔔 Notification Preferences</span></div>
        <div class="card-body">
          <div class="settings-row"><div><div class="settings-label">Temperature Alerts</div><div class="settings-sub">Notify when temp exceeds threshold</div></div><label class="toggle"><input type="checkbox" checked/><span class="toggle-slider"></span></label></div>
          <div class="settings-row"><div><div class="settings-label">Booking Confirmations</div><div class="settings-sub">Email & in-app on booking approval</div></div><label class="toggle"><input type="checkbox" checked/><span class="toggle-slider"></span></label></div>
          <div class="settings-row"><div><div class="settings-label">Delivery Updates</div><div class="settings-sub">Real-time delivery status</div></div><label class="toggle"><input type="checkbox" checked/><span class="toggle-slider"></span></label></div>
          <div class="settings-row"><div><div class="settings-label">Payment Receipts</div><div class="settings-sub">Email on payment confirmation</div></div><label class="toggle"><input type="checkbox" checked/><span class="toggle-slider"></span></label></div>
          <div class="settings-row"><div><div class="settings-label">Promotional Offers</div><div class="settings-sub">Discounts and promos</div></div><label class="toggle"><input type="checkbox"/><span class="toggle-slider"></span></label></div>
        </div>
      </div>
      <div class="card">
        <div class="card-body" style="padding:14px 20px">
          <button class="btn btn-danger btn-sm" style="width:100%" onclick="doLogout()">🚪 Logout</button>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ════ MODALS ════ -->
<div class="modal-overlay" id="bookingModal">
  <div class="modal">
    <div class="modal-title">📦 New Booking</div>
    <div class="form-row"><div class="form-group"><label class="form-label">Product</label><input class="form-input" id="bk-product" placeholder="e.g. Lettuce"/></div><div class="form-group"><label class="form-label">Quantity (kg)</label><input class="form-input" id="bk-qty" type="number" placeholder="80" oninput="updateBookingCost()"/></div></div>
    <div class="form-group"><label class="form-label">Storage Type</label><select class="form-select" id="bk-storage" onchange="updateBookingCost()"><option value="180">Deep Cold (2°C) — ₱180/day</option><option value="120">Chilled (8°C) — ₱120/day</option><option value="80">Cool Room (12°C) — ₱80/day</option></select></div>
    <div class="form-row"><div class="form-group"><label class="form-label">Start Date</label><input class="form-input" type="date" id="bk-start"/></div><div class="form-group"><label class="form-label">Duration (Days)</label><input class="form-input" type="number" id="bk-days" placeholder="3" oninput="updateBookingCost()"/></div></div>
    <div class="form-group"><label class="form-label">Delivery?</label><select class="form-select" id="bk-delivery" onchange="updateBookingCost()"><option value="250">Yes — include delivery (+₱250)</option><option value="0">No — drop-off only</option></select></div>
    <div class="form-group"><label class="form-label">Notes</label><textarea class="form-textarea" placeholder="Handling instructions…"></textarea></div>
    <div id="bk-cost-preview" style="background:linear-gradient(135deg,var(--forest),var(--moss));border-radius:10px;padding:12px 16px;display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">
      <div><div style="font-size:.68rem;color:rgba(255,255,255,.75);font-weight:500">Predicted Cost</div><div id="bk-cost-val" style="font-family:Arial,sans-serif;font-size:1.3rem;font-weight:800;color:#fff">₱0.00</div></div>
      <div style="text-align:right"><div style="font-size:.68rem;color:rgba(255,255,255,.75)">Breakdown</div><div id="bk-cost-breakdown" style="font-size:.72rem;color:rgba(255,255,255,.85)">— days × ₱—/day + delivery</div></div>
    </div>
    <div class="modal-btns"><button class="btn btn-ghost" onclick="closeModal('bookingModal')">Cancel</button><button class="btn btn-primary" style="flex:1" onclick="submitBooking()">Submit Booking ✓</button></div>
  </div>
</div>

<div class="modal-overlay" id="productModal">
  <div class="modal">
    <div class="modal-title">🌾 Add New Product</div>
    <div class="form-group"><label class="form-label">Product Name</label><input class="form-input" id="pr-name" placeholder="e.g. Broccoli"/></div>
    <div class="form-row"><div class="form-group"><label class="form-label">Category</label><select class="form-select" id="pr-cat"><option>Leafy Greens</option><option>Fruits</option><option>Root Crops</option><option>Other</option></select></div><div class="form-group"><label class="form-label">Quantity (kg)</label><input class="form-input" id="pr-qty" type="number" placeholder="50"/></div></div>
    <div class="form-group"><label class="form-label">Ideal Temp</label><select class="form-select" id="pr-temp"><option>2°C – Deep Cold</option><option>8°C – Chilled</option><option>12°C – Cool Room</option></select></div>
    <div class="form-group"><label class="form-label">Notes</label><textarea class="form-textarea" id="pr-notes" placeholder="Storage notes…"></textarea></div>
    <div class="modal-btns"><button class="btn btn-ghost" onclick="closeModal('productModal')">Cancel</button><button class="btn btn-primary" style="flex:1" onclick="submitProduct()">Add Product ✓</button></div>
  </div>
</div>

<!-- NOTIF PANEL -->
<div class="notif-panel" id="notifPanel">
  <div class="notif-panel-header"><span class="notif-panel-title">🔔 Notifications</span><button class="btn btn-ghost btn-sm" onclick="markAllRead()">Mark all read</button></div>
  <div class="notif-panel-body" id="notifPanelBody"></div>
  <div class="notif-panel-footer"><a onclick="navigate('notifications');closeAllPanels()">View all →</a></div>
</div>

<!-- PROFILE PANEL -->
<div class="profile-panel" id="profilePanel">
  <div class="profile-panel-top">
    <div class="profile-big-av" id="profileBigAv">JR</div>
    <div class="profile-panel-name" id="profilePanelName">Juan Reyes</div>
    <div class="profile-panel-role" id="profilePanelRole">Merchant · Cebu City</div>
  </div>
  <div class="profile-panel-item" onclick="navigate('settings');closeAllPanels()">⚙️ Account Settings</div>
  <div class="profile-panel-item" onclick="navigate('reports');closeAllPanels()">🧾 My Reports</div>
  <div class="profile-panel-item" onclick="showToast('💡 Help center coming soon!')">❓ Help & Support</div>
  <div class="profile-panel-item" onclick="doLogout()">🚪 Logout</div>
</div>

<!-- SEARCH OVERLAY -->
<div class="search-overlay" id="searchOverlay" onclick="closeSearch(event)">
  <div class="search-box" onclick="event.stopPropagation()">
    <div class="search-input-row"><span>🔍</span><input type="text" id="searchInput" placeholder="Search pages, bookings, products…" oninput="doSearch(this.value)"/><button class="btn btn-ghost btn-sm" onclick="closeSearchOverlay()">✕</button></div>
    <div class="search-results" id="searchResults"></div>
  </div>
</div>

</div><!-- /appPage -->

<!-- LOGOUT SCREEN -->
<div id="logoutScreen">
  <div class="logout-spinner"></div>
  <div style="font-family:'Syne',sans-serif;font-size:1rem;font-weight:700;color:var(--ink)">Signing out…</div>
</div>

<!-- ══════════════ SCRIPT ══════════════ -->
<script>
// ── TRANSLATIONS ──────────────────────────────────────────────
const LANG = {
  en:{
    dashboard:'Dashboard',my_bookings:'My Bookings',delivery:'Delivery Tracker',
    products:'My Products',reports:'Reports',notifications:'Notifications',settings:'Settings',
    new_booking:'New Booking',active_bookings:'Active Bookings',storage_units:'Storage Units',
    in_transit:'In Transit',temp_alerts:'Temp Alerts',
    greeting:'Good morning',role:'Merchant'
  },
  fil:{
    dashboard:'Dashboard',my_bookings:'Mga Booking',delivery:'Tracker ng Delivery',
    products:'Aking Produkto',reports:'Ulat',notifications:'Mga Abiso',settings:'Mga Setting',
    new_booking:'Bagong Booking',active_bookings:'Aktibong Booking',storage_units:'Mga Storage Unit',
    in_transit:'Sa Daan',temp_alerts:'Temp na Alerto',
    greeting:'Magandang umaga',role:'Mangangalakal'
  },
  ceb:{
    dashboard:'Dashboard',my_bookings:'Akong Booking',delivery:'Tracker sa Delivery',
    products:'Akong Produkto',reports:'Taho',notifications:'Mga Abiso',settings:'Mga Setting',
    new_booking:'Bag-ong Booking',active_bookings:'Aktibong Booking',storage_units:'Mga Storage Unit',
    in_transit:'Sa Dalan',temp_alerts:'Temp nga Alerto',
    greeting:'Maayong buntag',role:'Negosyante'
  }
};
let currentLang = 'en';

function changeLanguage(lang) {
  currentLang = lang;
  const t = LANG[lang];
  document.querySelectorAll('[data-t]').forEach(el => {
    const key = el.getAttribute('data-t');
    if(t[key]) el.textContent = t[key];
  });
  const fname = document.getElementById('s-fname')?.value || 'Juan';
  document.getElementById('pageSub').textContent = `Wednesday, May 13, 2026 — ${t.greeting}, ${fname}! 👋`;
  document.getElementById('navRole').textContent = `${t.role} · Cebu`;
  document.getElementById('profilePanelRole').textContent = `${t.role} · Cebu City`;
  showToast('🌐 Language changed to ' + {en:'English',fil:'Filipino',ceb:'Cebuano'}[lang]);
}

// ── AUTH ──────────────────────────────────────────────────────
const VALID_USERS = [
  {email:'admin@agricold.ph',pass:'1234',name:'Juan Reyes',initials:'JR',role:'Merchant'},
  {email:'demo@agricold.ph',pass:'demo',name:'Demo User',initials:'DU',role:'Demo'},
];
let currentUser = null;

function doLogin() {
  const email = document.getElementById('loginEmail').value.trim();
  const pass  = document.getElementById('loginPassword').value;
  const user  = VALID_USERS.find(u => u.email===email && u.pass===pass);
  const err   = document.getElementById('loginError');
  if(!user){ err.classList.add('show'); return; }
  err.classList.remove('show');
  currentUser = user;
  launchApp();
}

function demoLogin() {
  document.getElementById('loginEmail').value = 'demo@agricold.ph';
  document.getElementById('loginPassword').value = 'demo';
  doLogin();
}

function launchApp() {
  document.getElementById('loginPage').classList.add('hidden');
  document.getElementById('appPage').classList.add('visible');
  // Set user info
  const u = currentUser;
  document.getElementById('navAvatar').textContent = u.initials;
  document.getElementById('navName').textContent = u.name;
  document.getElementById('profileBigAv').textContent = u.initials;
  document.getElementById('profilePanelName').textContent = u.name;
  const parts = u.name.split(' ');
  document.getElementById('s-fname').value = parts[0]||'';
  document.getElementById('s-lname').value = parts[1]||'';
  // Init renders
  renderBookings(BOOKINGS);
  renderProducts(PRODUCTS);
  renderNotifFull();
  renderBarChart();
  renderDeliveries();
  renderNotifPanel();
  updateNotifBadge();
  navigate('dashboard');
}

function doLogout() {
  if(!confirm('Are you sure you want to log out?')) return;
  closeAllPanels();
  document.getElementById('logoutScreen').classList.add('show');
  setTimeout(() => {
    document.getElementById('logoutScreen').classList.remove('show');
    document.getElementById('appPage').classList.remove('visible');
    document.getElementById('loginPage').classList.remove('hidden');
    document.getElementById('loginPassword').value = '';
    document.getElementById('loginError').classList.remove('show');
    currentUser = null;
    // reset dark mode
    document.body.classList.remove('dark');
    document.getElementById('darkModeToggle').checked = false;
    document.getElementById('dmSubText').textContent = 'Currently using Light Mode';
  }, 1800);
}

// ── DARK MODE ─────────────────────────────────────────────────
function toggleDarkMode(on) {
  document.body.classList.toggle('dark', on);
  document.getElementById('dmSubText').textContent = on ? 'Currently using Dark Mode 🌙' : 'Currently using Light Mode ☀️';
  showToast(on ? '🌙 Dark Mode enabled!' : '☀️ Light Mode enabled!');
}

// ── DATA ──────────────────────────────────────────────────────
const BOOKINGS = [
  {id:'#BK-2041',product:'Lettuce',qty:80,unit:'Unit A – 2°C',days:3,cost:'₱540',status:'active'},
  {id:'#BK-2042',product:'Tomatoes',qty:50,unit:'Unit B – 8°C',days:5,cost:'₱600',status:'active'},
  {id:'#BK-2043',product:'Mangoes',qty:120,unit:'Unit C – 10°C',days:2,cost:'₱160',status:'pending'},
  {id:'#BK-2039',product:'Carrots',qty:35,unit:'Unit A – 2°C',days:4,cost:'₱720',status:'done'},
  {id:'#BK-2037',product:'Cabbage',qty:90,unit:'Unit B – 8°C',days:6,cost:'₱720',status:'done'},
  {id:'#BK-2035',product:'Onions',qty:60,unit:'Unit C – 10°C',days:3,cost:'₱240',status:'done'},
];
const PRODUCTS = [
  {icon:'🥬',name:'Lettuce',cat:'Leafy Greens',qty:80,temp:'2°C',notes:'Keep dry'},
  {icon:'🍅',name:'Tomatoes',cat:'Fruits',qty:50,temp:'8°C',notes:'Check bruising'},
  {icon:'🥭',name:'Mangoes',cat:'Fruits',qty:120,temp:'10°C',notes:'Slightly ripe'},
  {icon:'🥕',name:'Carrots',cat:'Root Crops',qty:35,temp:'2°C',notes:'Washed & bagged'},
  {icon:'🥬',name:'Cabbage',cat:'Leafy Greens',qty:90,temp:'8°C',notes:'Outer leaves intact'},
  {icon:'🧅',name:'Onions',cat:'Root Crops',qty:60,temp:'12°C',notes:'Cured and dried'},
];
const NOTIFS = [
  {icon:'⚠️',color:'red',msg:'<strong>Temperature Alert</strong> — Unit C rose to 14°C.',time:'2 minutes ago',unread:true,type:'alert'},
  {icon:'✅',color:'green',msg:'<strong>Booking #BK-2043</strong> approved by admin.',time:'1 hour ago',unread:true,type:'booking'},
  {icon:'🚚',color:'blue',msg:'<strong>Delivery DL-0891</strong> in transit — ETA 45 mins.',time:'3 hours ago',unread:true,type:'delivery'},
  {icon:'💰',color:'amber',msg:'Payment confirmed for <strong>#BK-2039</strong>.',time:'Yesterday, 4:12 PM',unread:false,type:'payment'},
  {icon:'📦',color:'green',msg:'<strong>Delivery DL-0885</strong> completed.',time:'Yesterday, 11:30 AM',unread:false,type:'delivery'},
];
const DELIVERIES = [
  {id:'#DL-0891',name:'Lettuce Batch — 80 kg',eta:'⏱ ETA: 45 mins'},
  {id:'#DL-0895',name:'Tomatoes — 50 kg',eta:'⏱ ETA: 2 hrs 10 mins'},
];
const MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
const BAR_DATA = [8,12,10,15,23,0,0,0,0,0,0,0];

// ── NAVIGATE ──────────────────────────────────────────────────
const PAGE_INFO = {
  dashboard:{title:'Merchant Dashboard',sub:'Wednesday, May 13, 2026',btn:'➕ New Booking',action:'openBookingModal()'},
  bookings:{title:'My Bookings',sub:'Manage all your cold storage bookings',btn:'➕ New Booking',action:'openBookingModal()'},
  delivery:{title:'Delivery Tracker',sub:'Track your produce in real-time',btn:'🚚 Request Delivery',action:'requestDelivery()'},
  products:{title:'My Products',sub:'Manage your produce inventory',btn:'➕ Add Product',action:'openProductModal()'},
  reports:{title:'Reports & Analytics',sub:'Usage and cost summary',btn:'🔄 Refresh',action:"showToast('🔄 Data refreshed!')"},
  notifications:{title:'Notifications',sub:'Stay updated on your bookings',btn:'✅ Mark All Read',action:'markAllRead()'},
  settings:{title:'Settings',sub:'Manage your account and preferences',btn:'💾 Save All',action:'saveProfile()'},
};
function navigate(page) {
  document.querySelectorAll('.section').forEach(s=>s.classList.remove('active'));
  document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
  document.getElementById('sec-'+page).classList.add('active');
  document.getElementById('nav-'+page).classList.add('active');
  const info = PAGE_INFO[page];
  document.getElementById('pageTitle').textContent = info.title;
  const t = LANG[currentLang];
  const fname = currentUser ? currentUser.name.split(' ')[0] : 'Juan';
  document.getElementById('pageSub').textContent = page==='dashboard'
    ? `Wednesday, May 13, 2026 — ${t.greeting}, ${fname}! 👋`
    : info.sub;
  const btn = document.getElementById('pageActionBtn');
  btn.innerHTML = info.btn;
  btn.onclick = new Function(info.action);
  closeAllPanels();
}

// ── BOOKING COST PREVIEW ──────────────────────────────────────
function updateBookingCost() {
  const rate     = +document.getElementById('bk-storage').value || 0;
  const days     = +document.getElementById('bk-days').value || 0;
  const delivery = +document.getElementById('bk-delivery').value || 0;
  const storage  = rate * days;
  const total    = storage + delivery;
  document.getElementById('bk-cost-val').textContent = '₱' + total.toFixed(2);
  document.getElementById('bk-cost-breakdown').textContent =
    `${days} day${days!==1?'s':''} × ₱${rate}/day` + (delivery ? ` + ₱${delivery} delivery` : '');
}


function renderBookings(list) {
  document.getElementById('bookingsTbody').innerHTML = list.map(b=>`
    <tr>
      <td style="font-weight:600;color:var(--ink-60);font-size:.7rem">${b.id}</td>
      <td>${b.product}</td><td>${b.unit}</td><td>${b.qty} kg</td><td>${b.days} days</td>
      <td style="font-weight:600;color:var(--moss)">${b.cost}</td>
      <td><span class="badge ${b.status}"><span class="badge-dot"></span>${b.status[0].toUpperCase()+b.status.slice(1)}</span></td>
      <td>${(b.status==='active'||b.status==='pending')?`<button class="btn btn-danger btn-sm" onclick="cancelBooking('${b.id}')">Cancel</button>`:''}</td>
    </tr>`).join('');
  document.getElementById('bookingCount').textContent = `${list.length} bookings`;
}
function filterBookings() {
  const st   = document.getElementById('bookingFilter').value;
  const q    = document.getElementById('bookingSearch').value.toLowerCase();
  const sort = document.getElementById('bookingSort').value;
  let list = BOOKINGS.filter(b=>(st==='all'||b.status===st)&&(b.id.toLowerCase().includes(q)||b.product.toLowerCase().includes(q)));
  if(sort==='qty_asc')  list = list.slice().sort((a,b)=>a.qty-b.qty);
  if(sort==='qty_desc') list = list.slice().sort((a,b)=>b.qty-a.qty);
  renderBookings(list);
}
function cancelBooking(id) {
  if(!confirm(`Cancel booking ${id}?`)) return;
  const b = BOOKINGS.find(x=>x.id===id); if(b) b.status='done';
  filterBookings(); showToast(`❌ Booking ${id} cancelled`);
}
function submitBooking() {
  const product  = document.getElementById('bk-product').value;
  const qty      = document.getElementById('bk-qty').value;
  if(!product||!qty){showToast('⚠️ Fill in required fields');return;}
  const rate     = +document.getElementById('bk-storage').value || 120;
  const days     = +(document.getElementById('bk-days').value)||1;
  const delivery = +document.getElementById('bk-delivery').value || 0;
  const total    = rate * days + delivery;
  const id = '#BK-'+Math.floor(2050+Math.random()*99);
  BOOKINGS.unshift({id,product,qty:+qty,unit:'Unit A – 2°C',days,cost:'₱'+total.toFixed(2),status:'pending'});
  closeModal('bookingModal');
  const badge = document.getElementById('booking-badge');
  badge.textContent = +badge.textContent+1;
  filterBookings();
  showToast(`✅ Booking ${id} submitted! Predicted cost: ₱${total.toFixed(2)}`);
}

// ── PRODUCTS ──────────────────────────────────────────────────
function renderProducts(list) {
  document.getElementById('productGrid').innerHTML = list.map((p,i)=>`
    <div class="product-card">
      <div class="product-icon">${p.icon}</div>
      <div><div class="product-name">${p.name}</div><div class="product-meta">📦 ${p.qty}kg &nbsp;|&nbsp; 🌡 ${p.temp} &nbsp;|&nbsp; ${p.cat}</div><div class="product-meta" style="font-style:italic;margin-top:4px">${p.notes}</div></div>
      <div class="product-actions"><button class="btn btn-primary btn-sm" onclick="openBookingModal()">Book</button><button class="btn btn-ghost btn-sm" onclick="deleteProduct(${i})">🗑</button></div>
    </div>`).join('');
}
function filterProducts() {
  const q    = document.getElementById('productSearch').value.toLowerCase();
  const sort = document.getElementById('productSort').value;
  let list = PRODUCTS.filter(p=>p.name.toLowerCase().includes(q)||p.cat.toLowerCase().includes(q));
  if(sort==='alpha_asc')  list = list.slice().sort((a,b)=>a.name.localeCompare(b.name));
  if(sort==='alpha_desc') list = list.slice().sort((a,b)=>b.name.localeCompare(a.name));
  if(sort==='kg_asc')     list = list.slice().sort((a,b)=>a.qty-b.qty);
  if(sort==='kg_desc')    list = list.slice().sort((a,b)=>b.qty-a.qty);
  renderProducts(list);
}
function deleteProduct(i) {
  if(!confirm('Remove this product?')) return;
  PRODUCTS.splice(i,1); renderProducts(PRODUCTS); showToast('🗑 Product removed');
}
function submitProduct() {
  const name = document.getElementById('pr-name').value;
  const qty  = document.getElementById('pr-qty').value;
  if(!name||!qty){showToast('⚠️ Fill in required fields');return;}
  const icons = {'Leafy Greens':'🧺','Fruits':'🧺','Root Crops':'🧺','Other':'📦'};
  const cat = document.getElementById('pr-cat').value;
  PRODUCTS.push({icon:icons[cat],name,cat,qty:+qty,temp:document.getElementById('pr-temp').value.split('–')[0].trim(),notes:document.getElementById('pr-notes').value||'No notes'});
  closeModal('productModal'); renderProducts(PRODUCTS); showToast(`✅ "${name}" added!`);
}

// ── NOTIFICATIONS ─────────────────────────────────────────────
let notifFilter = 'all';
function updateNotifBadge() {
  const unread = NOTIFS.filter(n=>n.unread).length;
  document.getElementById('notif-badge').textContent = unread;
  const dot = document.getElementById('notifDot');
  dot.style.display = unread > 0 ? '' : 'none';
}
function renderNotifFull() {
  const list = NOTIFS.filter(n=>notifFilter==='all'?true:notifFilter==='unread'?n.unread:n.type==='alert');
  document.getElementById('notifFullList').innerHTML = list.map((n,i)=>`
    <div class="notif-item">
      <div class="notif-av ${n.color}">${n.icon}</div>
      <div style="flex:1"><div class="notif-msg">${n.msg}</div><div class="notif-time">${n.time}</div></div>
      ${n.unread?`<div class="notif-unread" style="cursor:pointer" title="Mark as read" onclick="markOneRead(${NOTIFS.indexOf(n)})"></div>`:''}
      <button class="btn btn-ghost btn-sm" style="margin-left:8px" onclick="dismissNotif(${NOTIFS.indexOf(n)})">✕</button>
    </div>`).join('')||'<div style="text-align:center;padding:24px;color:var(--ink-60)">No notifications</div>';
}
function renderNotifPanel() {
  document.getElementById('notifPanelBody').innerHTML = NOTIFS.slice(0,4).map(n=>`
    <div class="notif-item"><div class="notif-av ${n.color}">${n.icon}</div>
    <div style="flex:1"><div class="notif-msg">${n.msg}</div><div class="notif-time">${n.time}</div></div>
    ${n.unread?'<div class="notif-unread"></div>':''}</div>`).join('');
}
function filterNotifs(f) {
  notifFilter = f;
  ['all','unread','alert'].forEach(x=>{
    const b = document.getElementById('nf-'+x);
    b.style.background = x===f?'var(--sage)':'';
    b.style.borderColor = x===f?'var(--moss)':'';
  });
  renderNotifFull();
}
function markOneRead(i) {
  if(NOTIFS[i]) NOTIFS[i].unread = false;
  updateNotifBadge(); renderNotifFull(); renderNotifPanel();
}
function markAllRead() {
  NOTIFS.forEach(n=>n.unread=false);
  updateNotifBadge();
  renderNotifFull(); renderNotifPanel();
  showToast('✅ All notifications read');
}
function dismissNotif(i) { NOTIFS.splice(i,1); updateNotifBadge(); renderNotifFull(); renderNotifPanel(); showToast('Dismissed'); }

// ── REPORTS ───────────────────────────────────────────────────
function renderBarChart() {
  const max = Math.max(...BAR_DATA);
  document.getElementById('barChart').innerHTML = BAR_DATA.map((v,i)=>`
    <div class="bar-col">
      ${v?`<div class="bar-val">${v}</div>`:''}
      <div class="bar" style="height:${v?(v/max*110)+20:4}px;${!v?'background:var(--ink-30)':''}"></div>
      <div class="bar-label">${MONTHS[i]}</div>
    </div>`).join('');
}

// ── DELIVERIES ────────────────────────────────────────────────
function renderDeliveries() {
  document.getElementById('deliveryList').innerHTML = DELIVERIES.map((d,i)=>`
    <div class="delivery-item">
      <div class="d-step-col"><div class="d-bubble done">✓</div><div class="d-line"></div><div class="d-bubble transit">→</div></div>
      <div class="d-info"><span class="d-id">${d.id}</span><span class="d-name">${d.name}</span>
        <div class="d-steps"><span class="ds done">Preparing</span><span class="d-arrow">›</span><span class="ds active">In Transit</span><span class="d-arrow">›</span><span class="ds pend">Delivered</span></div>
        <span class="eta-tag">${d.eta}</span>
      </div>
      <div style="align-self:flex-start;margin-left:8px">
        <button class="btn btn-danger btn-sm" onclick="removeDelivery(${i})">🗑 Remove</button>
      </div>
    </div>`).join('');
}
function removeDelivery(i) {
  if(!confirm(`Remove delivery ${DELIVERIES[i].id}?`)) return;
  const id = DELIVERIES[i].id;
  DELIVERIES.splice(i,1);
  renderDeliveries();
  showToast(`🗑 Delivery ${id} removed`);
}
function requestDelivery() {
  const id = '#DL-'+Math.floor(900+Math.random()*99);
  DELIVERIES.push({id,name:'New Delivery',eta:'⏱ ETA: Pending'});
  renderDeliveries(); showToast(`🚚 Delivery ${id} requested!`);
}

// ── SETTINGS ──────────────────────────────────────────────────
function saveProfile() {
  const fname = document.getElementById('s-fname').value;
  const lname = document.getElementById('s-lname').value;
  const fullName = `${fname} ${lname}`.trim();
  const initials = (fname[0]||'')+(lname[0]||'');
  if(currentUser){ currentUser.name=fullName; currentUser.initials=initials; }
  document.getElementById('navName').textContent = fullName;
  document.getElementById('navAvatar').textContent = initials;
  document.getElementById('profilePanelName').textContent = fullName;
  document.getElementById('profileBigAv').textContent = initials;
  const t = LANG[currentLang];
  document.getElementById('pageSub').textContent = `Wednesday, May 13, 2026 — ${t.greeting}, ${fname}! 👋`;
  showToast('✅ Profile updated!');
}
function changePassword() {
  const cur = document.getElementById('s-curpw').value;
  const nw  = document.getElementById('s-newpw').value;
  const cf  = document.getElementById('s-confpw').value;
  if(!cur||!nw||!cf){showToast('⚠️ Fill in all password fields');return;}
  if(nw!==cf){showToast('❌ Passwords do not match');return;}
  if(currentUser) currentUser.pass = nw;
  document.getElementById('s-curpw').value='';
  document.getElementById('s-newpw').value='';
  document.getElementById('s-confpw').value='';
  showToast('🔒 Password changed successfully!');
}

// ── ESTIMATOR ─────────────────────────────────────────────────
function calcCost() {
  const rate = +document.getElementById('storageType').value||120;
  const qty  = +document.getElementById('qty').value||0;
  const days = +document.getElementById('days').value||0;
  document.getElementById('estTotal').textContent='₱'+(rate*days).toFixed(2);
  document.getElementById('estDelivery').textContent='+₱'+(qty>100?350:250);
}

// ── MODALS ────────────────────────────────────────────────────
function openBookingModal(){ document.getElementById('bookingModal').classList.add('open'); updateBookingCost(); }
function openProductModal() { document.getElementById('productModal').classList.add('open'); }
function closeModal(id)     { document.getElementById(id).classList.remove('open'); }
document.querySelectorAll('.modal-overlay').forEach(m=>m.addEventListener('click',e=>{if(e.target===m)m.classList.remove('open');}));

// ── SEARCH ────────────────────────────────────────────────────
const SEARCH_ITEMS = [
  {icon:'🏠',title:'Dashboard',sub:'Overview & stats',page:'dashboard'},
  {icon:'📦',title:'My Bookings',sub:'View all bookings',page:'bookings'},
  {icon:'🚚',title:'Delivery Tracker',sub:'Track live deliveries',page:'delivery'},
  {icon:'🌾',title:'My Products',sub:'Manage inventory',page:'products'},
  {icon:'🧾',title:'Reports',sub:'Usage & costs',page:'reports'},
  {icon:'💬',title:'Notifications',sub:'Alerts & updates',page:'notifications'},
  {icon:'⚙️',title:'Settings',sub:'Account & preferences',page:'settings'},
];
function openSearch(){ document.getElementById('searchOverlay').classList.add('open'); doSearch(''); setTimeout(()=>document.getElementById('searchInput').focus(),100); }
function closeSearchOverlay(){ document.getElementById('searchOverlay').classList.remove('open'); document.getElementById('searchInput').value=''; }
function closeSearch(e){ if(e.target===document.getElementById('searchOverlay')) closeSearchOverlay(); }
function doSearch(q) {
  const r = q ? SEARCH_ITEMS.filter(x=>x.title.toLowerCase().includes(q.toLowerCase())||x.sub.toLowerCase().includes(q.toLowerCase())) : SEARCH_ITEMS;
  document.getElementById('searchResults').innerHTML = r.map(x=>`
    <div class="search-result-item" onclick="navigate('${x.page}');closeSearchOverlay()">
      <div class="search-result-icon">${x.icon}</div>
      <div><div class="search-result-title">${x.title}</div><div class="search-result-sub">${x.sub}</div></div>
    </div>`).join('')||'<div style="padding:14px;color:var(--ink-60);font-size:.82rem">No results</div>';
}

// ── PANELS ────────────────────────────────────────────────────
function toggleNotifPanel(){ document.getElementById('notifPanel').classList.toggle('open'); document.getElementById('profilePanel').classList.remove('open'); }
function toggleProfilePanel(){ document.getElementById('profilePanel').classList.toggle('open'); document.getElementById('notifPanel').classList.remove('open'); }
function closeAllPanels(){ document.getElementById('notifPanel').classList.remove('open'); document.getElementById('profilePanel').classList.remove('open'); }
document.addEventListener('click',e=>{ if(!e.target.closest('#notifPanel,#notifBtn,.user-card,#profilePanel')) closeAllPanels(); });

// ── TOAST ─────────────────────────────────────────────────────
function showToast(msg) {
  document.querySelectorAll('.toast').forEach(t=>t.remove());
  const t = document.createElement('div'); t.className='toast'; t.innerHTML=msg;
  document.body.appendChild(t); setTimeout(()=>t.remove(),3000);
}
</script>
</body>
</html>