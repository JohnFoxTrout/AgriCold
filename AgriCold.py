<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>AgriCold Connect — Dashboard</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet"/>
<style>
  /* ── RESET & TOKENS ─────────────────────────────────────── */
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --forest:   #1a5c2a;
    --moss:     #2e8b57;
    --mint:     #a8d5b5;
    --sage:     #d6efd8;
    --ice:      #1b4f72;
    --glacier:  #2e86c1;
    --frost:    #d4e6f1;
    --amber:    #f0a500;
    --amber-lt: #fef3d0;
    --red:      #c0392b;
    --red-lt:   #fdecea;
    --ink:      #1a1f2e;
    --ink-60:   #5a6070;
    --ink-30:   #c2c7d0;
    --paper:    #f4f6f2;
    --white:    #ffffff;
    --card-r:   14px;
    --shadow:   0 2px 16px rgba(26,92,42,.10);
    --shadow-lg:0 8px 40px rgba(26,92,42,.16);
  }

  html { font-size: 15px; }
  body {
    font-family: 'DM Sans', sans-serif;
    background: var(--paper);
    color: var(--ink);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  /* ── SIDEBAR ────────────────────────────────────────────── */
  .layout { display: flex; min-height: 100vh; }

  .sidebar {
    width: 240px;
    flex-shrink: 0;
    background: var(--forest);
    display: flex;
    flex-direction: column;
    padding: 0;
    position: fixed;
    top: 0; left: 0; bottom: 0;
    z-index: 100;
    overflow: hidden;
  }

  .sidebar-logo {
    padding: 28px 24px 20px;
    border-bottom: 1px solid rgba(255,255,255,.10);
  }
  .logo-mark {
    display: flex; align-items: center; gap: 10px;
  }
  .logo-icon {
    width: 36px; height: 36px;
    background: linear-gradient(135deg, var(--amber), #e8960a);
    border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    font-size: 18px;
    box-shadow: 0 2px 8px rgba(240,165,0,.40);
  }
  .logo-text { display: flex; flex-direction: column; }
  .logo-name {
    font-family: Arial, sans-serif;
    font-weight: 700; font-size: 1rem;
    color: var(--white); line-height: 1;
    text-transform: uppercase;
  }
  .logo-sub {
    font-size: .68rem; color: var(--mint);
    font-weight: 400; margin-top: 2px;
  }

  .sidebar-nav { padding: 18px 12px; flex: 1; }
  .nav-section-label {
    font-size: .65rem; font-weight: 600; letter-spacing: .1em;
    text-transform: uppercase; color: var(--mint);
    padding: 0 12px; margin: 14px 0 6px;
  }

  .nav-item {
    display: flex; align-items: center; gap: 11px;
    padding: 10px 14px; border-radius: 9px;
    color: rgba(255,255,255,.7);
    font-size: .88rem; font-weight: 400;
    cursor: pointer;
    transition: background .18s, color .18s;
    margin-bottom: 2px;
    text-decoration: none;
  }
  .nav-item:hover { background: rgba(255,255,255,.08); color: #fff; }
  .nav-item.active {
    background: rgba(255,255,255,.14);
    color: #fff; font-weight: 600;
  }
  .nav-item.active .nav-icon { opacity: 1; }
  .nav-icon { font-size: 1rem; opacity: .7; }
  .nav-badge {
    margin-left: auto;
    background: var(--amber);
    color: var(--ink);
    font-size: .65rem; font-weight: 700;
    padding: 1px 7px; border-radius: 20px;
  }

  .sidebar-footer {
    padding: 16px 18px;
    border-top: 1px solid rgba(255,255,255,.10);
  }
  .user-card {
    display: flex; align-items: center; gap: 10px;
  }
  .user-avatar {
    width: 36px; height: 36px; border-radius: 50%;
    background: linear-gradient(135deg, var(--glacier), var(--ice));
    display: flex; align-items: center; justify-content: center;
    color: #fff; font-family: 'Syne', sans-serif;
    font-weight: 700; font-size: .85rem;
    flex-shrink: 0;
  }
  .user-info { display: flex; flex-direction: column; }
  .user-name { font-size: .82rem; font-weight: 600; color: #fff; }
  .user-role { font-size: .68rem; color: var(--mint); }

  /* ── MAIN CONTENT ───────────────────────────────────────── */
  .main {
    margin-left: 240px;
    flex: 1;
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }

  /* ── TOPBAR ─────────────────────────────────────────────── */
  .topbar {
    background: var(--white);
    border-bottom: 1px solid rgba(0,0,0,.07);
    padding: 0 32px;
    height: 64px;
    display: flex; align-items: center; justify-content: space-between;
    position: sticky; top: 0; z-index: 50;
    backdrop-filter: blur(10px);
  }
  .topbar-left { display: flex; flex-direction: column; }
  .topbar-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.08rem; font-weight: 700; color: var(--ink);
  }
  .topbar-sub { font-size: .75rem; color: var(--ink-60); }
  .topbar-right { display: flex; align-items: center; gap: 12px; }

  .topbar-btn {
    width: 38px; height: 38px; border-radius: 10px;
    border: 1px solid var(--ink-30);
    background: var(--white);
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem; cursor: pointer;
    position: relative;
    transition: border-color .18s, background .18s;
  }
  .topbar-btn:hover { background: var(--sage); border-color: var(--moss); }
  .notif-dot {
    position: absolute; top: 6px; right: 6px;
    width: 8px; height: 8px; background: var(--red);
    border-radius: 50%; border: 2px solid #fff;
  }

  .search-bar {
    display: flex; align-items: center; gap: 8px;
    background: var(--paper); border: 1px solid var(--ink-30);
    border-radius: 10px; padding: 8px 14px;
    font-size: .83rem; color: var(--ink-60);
    width: 220px; transition: border-color .18s;
  }
  .search-bar:focus-within { border-color: var(--moss); }
  .search-bar input {
    border: none; background: transparent; outline: none;
    font-size: .83rem; color: var(--ink); font-family: 'DM Sans', sans-serif;
    width: 100%;
  }

  /* ── PAGE CONTENT ───────────────────────────────────────── */
  .page { padding: 28px 32px; flex: 1; }

  /* ── STAT CARDS ─────────────────────────────────────────── */
  .stats-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-bottom: 24px;
  }
  .stat-card {
    background: var(--white);
    border-radius: var(--card-r);
    padding: 20px 22px;
    box-shadow: var(--shadow);
    display: flex; flex-direction: column; gap: 12px;
    position: relative; overflow: hidden;
    animation: fadeUp .5s ease both;
  }
  .stat-card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0;
    height: 3px;
  }
  .stat-card.green::before  { background: linear-gradient(90deg, var(--forest), var(--moss)); }
  .stat-card.blue::before   { background: linear-gradient(90deg, var(--ice), var(--glacier)); }
  .stat-card.amber::before  { background: linear-gradient(90deg, #c87900, var(--amber)); }
  .stat-card.red::before    { background: linear-gradient(90deg, #8e1c13, var(--red)); }

  .stat-top { display: flex; align-items: center; justify-content: space-between; }
  .stat-label { font-size: .75rem; font-weight: 500; color: var(--ink-60); text-transform: uppercase; letter-spacing: .04em; }
  .stat-icon {
    width: 36px; height: 36px; border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem;
  }
  .stat-icon.green { background: var(--sage); }
  .stat-icon.blue  { background: var(--frost); }
  .stat-icon.amber { background: var(--amber-lt); }
  .stat-icon.red   { background: var(--red-lt); }
  .stat-value {
    font-family: 'Syne', sans-serif;
    font-size: 1.9rem; font-weight: 800; color: var(--ink);
    line-height: 1;
  }
  .stat-delta {
    font-size: .72rem; font-weight: 500;
    display: flex; align-items: center; gap: 4px;
  }
  .delta-up   { color: var(--moss); }
  .delta-down { color: var(--red); }

  /* ── GRID ───────────────────────────────────────────────── */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 340px;
    gap: 20px;
    margin-bottom: 20px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
  }

  /* ── CARD ───────────────────────────────────────────────── */
  .card {
    background: var(--white);
    border-radius: var(--card-r);
    box-shadow: var(--shadow);
    overflow: hidden;
    animation: fadeUp .5s ease both;
  }
  .card-header {
    padding: 18px 22px 12px;
    display: flex; align-items: center; justify-content: space-between;
    border-bottom: 1px solid rgba(0,0,0,.05);
  }
  .card-title {
    font-family: 'Syne', sans-serif;
    font-size: .95rem; font-weight: 700; color: var(--ink);
  }
  .card-action {
    font-size: .75rem; color: var(--moss);
    font-weight: 600; cursor: pointer;
    padding: 4px 10px; border-radius: 7px;
    border: 1px solid var(--moss);
    transition: background .18s;
  }
  .card-action:hover { background: var(--sage); }
  .card-body { padding: 18px 22px; }

  /* ── BOOKING TABLE ──────────────────────────────────────── */
  .booking-table { width: 100%; border-collapse: collapse; }
  .booking-table th {
    font-size: .7rem; font-weight: 600; text-transform: uppercase;
    letter-spacing: .06em; color: var(--ink-60);
    padding: 8px 14px; text-align: left;
    border-bottom: 1px solid rgba(0,0,0,.06);
    background: var(--paper);
  }
  .booking-table td {
    padding: 12px 14px;
    font-size: .83rem;
    border-bottom: 1px solid rgba(0,0,0,.04);
    vertical-align: middle;
  }
  .booking-table tr:last-child td { border-bottom: none; }
  .booking-table tr:hover td { background: rgba(168,213,181,.08); }

  .status-badge {
    display: inline-flex; align-items: center; gap: 5px;
    padding: 3px 10px; border-radius: 20px;
    font-size: .7rem; font-weight: 600;
  }
  .status-badge.active  { background: var(--sage);    color: var(--forest); }
  .status-badge.pending { background: var(--amber-lt); color: #7a5000; }
  .status-badge.done    { background: #f0f0f0;          color: var(--ink-60); }
  .status-dot {
    width: 6px; height: 6px; border-radius: 50%;
  }
  .status-badge.active  .status-dot { background: var(--moss); }
  .status-badge.pending .status-dot { background: var(--amber); }
  .status-badge.done    .status-dot { background: #bbb; }

  /* ── TEMPERATURE WIDGET ─────────────────────────────────── */
  .temp-row {
    display: flex; flex-direction: column; gap: 14px;
  }
  .temp-unit {
    display: flex; align-items: center; gap: 14px;
    padding: 12px 14px; border-radius: 10px;
    background: var(--paper);
    border: 1px solid rgba(0,0,0,.06);
  }
  .temp-icon {
    width: 40px; height: 40px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.2rem; flex-shrink: 0;
  }
  .temp-icon.ok   { background: var(--frost); }
  .temp-icon.warn { background: var(--amber-lt); }
  .temp-icon.crit { background: var(--red-lt); }
  .temp-details { flex: 1; }
  .temp-name { font-size: .82rem; font-weight: 600; color: var(--ink); }
  .temp-sub  { font-size: .71rem; color: var(--ink-60); margin-top: 2px; }
  .temp-gauge {
    display: flex; flex-direction: column; align-items: flex-end; gap: 4px;
  }
  .temp-val {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem; font-weight: 800;
  }
  .temp-val.ok   { color: var(--glacier); }
  .temp-val.warn { color: var(--amber); }
  .temp-val.crit { color: var(--red); }
  .temp-bar {
    width: 80px; height: 5px;
    background: var(--ink-30); border-radius: 3px;
    overflow: hidden;
  }
  .temp-fill { height: 100%; border-radius: 3px; }
  .temp-fill.ok   { background: var(--glacier); }
  .temp-fill.warn { background: var(--amber); }
  .temp-fill.crit { background: var(--red); }

  /* ── DELIVERY TRACKER ───────────────────────────────────── */
  .delivery-item {
    display: flex; gap: 14px;
    padding: 14px 0;
    border-bottom: 1px solid rgba(0,0,0,.05);
  }
  .delivery-item:last-child { border-bottom: none; }
  .delivery-step-col { display: flex; flex-direction: column; align-items: center; gap: 0; }
  .step-bubble {
    width: 28px; height: 28px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: .75rem; font-weight: 700; flex-shrink: 0;
  }
  .step-bubble.done    { background: var(--moss);    color: #fff; }
  .step-bubble.transit { background: var(--glacier); color: #fff; }
  .step-bubble.waiting { background: var(--ink-30);  color: #fff; }
  .step-line { width: 2px; flex: 1; background: var(--ink-30); margin: 3px 0; min-height: 12px; }
  .delivery-info { flex: 1; }
  .delivery-id   { font-size: .72rem; font-weight: 600; color: var(--ink-60); }
  .delivery-name { font-size: .85rem; font-weight: 600; color: var(--ink); margin: 2px 0; }
  .delivery-steps { display: flex; align-items: center; gap: 6px; margin-top: 6px; }
  .d-step {
    font-size: .68rem; font-weight: 600;
    padding: 2px 8px; border-radius: 4px;
  }
  .d-step.done    { background: var(--sage);   color: var(--forest); }
  .d-step.active  { background: var(--frost);  color: var(--ice); }
  .d-step.pending { background: #f0f0f0; color: var(--ink-60); }
  .d-arrow { font-size: .65rem; color: var(--ink-30); }
  .eta-tag {
    font-size: .7rem; font-weight: 600; color: var(--glacier);
    background: var(--frost); padding: 3px 9px; border-radius: 20px;
    white-space: nowrap; align-self: flex-start; margin-top: 2px;
  }

  /* ── NOTIFICATIONS ──────────────────────────────────────── */
  .notif-item {
    display: flex; gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid rgba(0,0,0,.05);
  }
  .notif-item:last-child { border-bottom: none; }
  .notif-avatar {
    width: 34px; height: 34px; border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: .95rem; flex-shrink: 0;
  }
  .notif-avatar.green { background: var(--sage); }
  .notif-avatar.blue  { background: var(--frost); }
  .notif-avatar.amber { background: var(--amber-lt); }
  .notif-avatar.red   { background: var(--red-lt); }
  .notif-text { flex: 1; }
  .notif-msg  { font-size: .81rem; color: var(--ink); line-height: 1.45; }
  .notif-msg strong { color: var(--forest); }
  .notif-time { font-size: .68rem; color: var(--ink-60); margin-top: 3px; }
  .notif-unread { width: 7px; height: 7px; border-radius: 50%; background: var(--glacier); flex-shrink: 0; margin-top: 6px; }

  /* ── COST ESTIMATOR ─────────────────────────────────────── */
  .estimator { display: flex; flex-direction: column; gap: 14px; }
  .est-label { font-size: .75rem; font-weight: 600; color: var(--ink-60); text-transform: uppercase; letter-spacing: .04em; margin-bottom: 4px; }
  .est-input-row { display: flex; gap: 10px; }
  .est-input {
    flex: 1; padding: 10px 12px;
    border: 1px solid var(--ink-30); border-radius: 8px;
    font-size: .83rem; font-family: 'DM Sans', sans-serif;
    color: var(--ink); background: var(--paper);
    outline: none; transition: border-color .18s;
  }
  .est-input:focus { border-color: var(--moss); }
  select.est-input { cursor: pointer; }
  .est-result {
    background: linear-gradient(135deg, var(--forest), var(--moss));
    border-radius: 10px; padding: 16px 18px;
    display: flex; justify-content: space-between; align-items: center;
  }
  .est-result-label { font-size: .78rem; color: rgba(255,255,255,.75); font-weight: 500; }
  .est-result-val {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem; font-weight: 800; color: #fff;
  }
  .est-calc-btn {
    width: 100%; padding: 11px;
    background: var(--amber);
    color: var(--ink); font-weight: 700; font-size: .88rem;
    border: none; border-radius: 9px; cursor: pointer;
    font-family: 'Syne', sans-serif;
    transition: background .18s, transform .1s;
  }
  .est-calc-btn:hover { background: #e09200; transform: translateY(-1px); }
  .est-calc-btn:active { transform: translateY(0); }

  /* ── ANIMATION ──────────────────────────────────────────── */
  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
  }
  .stat-card:nth-child(1) { animation-delay: .05s; }
  .stat-card:nth-child(2) { animation-delay: .10s; }
  .stat-card:nth-child(3) { animation-delay: .15s; }
  .stat-card:nth-child(4) { animation-delay: .20s; }

  /* ── QUICK BOOK BUTTON ──────────────────────────────────── */
  .quick-book-btn {
    display: flex; align-items: center; justify-content: center; gap: 8px;
    width: 100%; padding: 13px;
    background: linear-gradient(135deg, var(--forest), var(--moss));
    color: #fff; font-weight: 700; font-size: .9rem;
    border: none; border-radius: 10px; cursor: pointer;
    font-family: 'Syne', sans-serif;
    margin-top: 4px;
    box-shadow: 0 4px 18px rgba(26,92,42,.25);
    transition: box-shadow .2s, transform .1s;
  }
  .quick-book-btn:hover { box-shadow: 0 6px 24px rgba(26,92,42,.35); transform: translateY(-1px); }

  /* ── MODAL OVERLAY ──────────────────────────────────────── */
  .modal-overlay {
    display: none;
    position: fixed; inset: 0;
    background: rgba(0,0,0,.45);
    z-index: 200;
    align-items: center; justify-content: center;
    backdrop-filter: blur(3px);
  }
  .modal-overlay.open { display: flex; }
  .modal {
    background: var(--white);
    border-radius: 18px;
    padding: 30px 32px;
    width: 420px; max-width: 95vw;
    box-shadow: var(--shadow-lg);
    animation: fadeUp .3s ease;
  }
  .modal-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem; font-weight: 800; color: var(--ink);
    margin-bottom: 20px;
  }
  .modal-field { margin-bottom: 14px; }
  .modal-field label { display: block; font-size: .75rem; font-weight: 600; color: var(--ink-60); margin-bottom: 5px; text-transform: uppercase; letter-spacing: .04em; }
  .modal-field input,
  .modal-field select {
    width: 100%; padding: 10px 14px;
    border: 1px solid var(--ink-30); border-radius: 8px;
    font-size: .85rem; font-family: 'DM Sans', sans-serif;
    color: var(--ink); background: var(--paper); outline: none;
    transition: border-color .18s;
  }
  .modal-field input:focus,
  .modal-field select:focus { border-color: var(--moss); }
  .modal-btns { display: flex; gap: 10px; margin-top: 20px; }
  .modal-submit {
    flex: 1; padding: 11px;
    background: var(--moss); color: #fff;
    font-weight: 700; font-size: .88rem;
    border: none; border-radius: 9px; cursor: pointer;
    font-family: 'Syne', sans-serif;
    transition: background .18s;
  }
  .modal-submit:hover { background: var(--forest); }
  .modal-cancel {
    padding: 11px 20px;
    background: var(--paper); color: var(--ink-60);
    font-weight: 600; font-size: .88rem;
    border: 1px solid var(--ink-30); border-radius: 9px; cursor: pointer;
    font-family: 'DM Sans', sans-serif;
  }

  /* ── RESPONSIVE HINT ────────────────────────────────────── */
  @media (max-width: 1100px) {
    .stats-row { grid-template-columns: repeat(2,1fr); }
    .grid-2 { grid-template-columns: 1fr; }
    .grid-3 { grid-template-columns: 1fr 1fr; }
  }
</style>
</head>
<body>
<div class="layout">

  <!-- ── SIDEBAR ── -->
  <aside class="sidebar">
    <div class="sidebar-logo">
      <div class="logo-mark">
        <div class="logo-icon" style="background:none;box-shadow:none;padding:0;overflow:hidden;">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Placeholder_view_vector.svg/120px-Placeholder_view_vector.svg.png" alt="Logo" style="display:none;" />
          <svg viewBox="0 0 100 100" width="36" height="36" xmlns="http://www.w3.org/2000/svg">
            <circle cx="50" cy="50" r="50" fill="#c8a96e"/>
            <circle cx="50" cy="50" r="50" fill="#5a9e4e" clip-path="url(#leftHalf)"/>
            <clipPath id="leftHalf">
              <rect x="0" y="0" width="50" height="100"/>
            </clipPath>
            <!-- Hand/leaf base -->
            <path d="M28,72 Q32,58 50,52 Q68,58 72,72 Q60,80 50,81 Q40,80 28,72Z" fill="white" opacity="0.92"/>
            <!-- Left leaf -->
            <path d="M50,52 Q38,38 36,24 Q44,28 50,40 Q50,46 50,52Z" fill="white" opacity="0.92"/>
            <!-- Right leaf -->
            <path d="M50,52 Q62,38 64,24 Q56,28 50,40 Q50,46 50,52Z" fill="white" opacity="0.92"/>
          </svg>
        </div>
        <div class="logo-text">
          <span class="logo-name">AgriCold</span>
          <span class="logo-sub">Connect v1.0</span>
        </div>
      </div>
    </div>

    <nav class="sidebar-nav">
      <div class="nav-section-label">Main</div>
      <a class="nav-item active">
        <span class="nav-icon">🏠</span> Dashboard
      </a>
      <a class="nav-item">
        <span class="nav-icon">📦</span> My Bookings
        <span class="nav-badge">3</span>
      </a>
      <a class="nav-item">
        <span class="nav-icon">🚚</span> Delivery Tracker
      </a>
      <a class="nav-item">
        <span class="nav-icon">🌾</span> My Products
      </a>

      <div class="nav-section-label">Management</div>
      <a class="nav-item">
        <span class="nav-icon">🧾</span> Reports
      </a>
      <a class="nav-item">
        <span class="nav-icon">💬</span> Notifications
        <span class="nav-badge">5</span>
      </a>
    </nav>

    <div class="sidebar-footer">
      <div class="user-card">
        <div class="user-avatar">JR</div>
        <div class="user-info">
          <span class="user-name">Juan Reyes</span>
          <span class="user-role">Merchant · Cebu</span>
        </div>
      </div>
    </div>
  </aside>

  <!-- ── MAIN ── -->
  <main class="main">

    <!-- TOPBAR -->
    <header class="topbar">
      <div class="topbar-left">
        <span class="topbar-title">Merchant Dashboard</span>
        <span class="topbar-sub">Wednesday, May 6, 2026 — Good morning, Juan! 👋</span>
      </div>
      <div class="topbar-right">
        <div class="search-bar">
          <span>🔍</span>
          <input type="text" placeholder="Search bookings, products…" />
        </div>
        <button class="topbar-btn" title="Notifications">
          🔔
          <span class="notif-dot"></span>
        </button>
        <button class="topbar-btn" title="Help">❓</button>
      </div>
    </header>

    <!-- PAGE -->
    <div class="page">

      <!-- STAT CARDS -->
      <div class="stats-row">
        <div class="stat-card green">
          <div class="stat-top">
            <span class="stat-label">Active Bookings</span>
            <div class="stat-icon green">📦</div>
          </div>
          <div class="stat-value">7</div>
          <div class="stat-delta delta-up">↑ 2 from last week</div>
        </div>
        <div class="stat-card blue">
          <div class="stat-top">
            <span class="stat-label">Storage Units Used</span>
            <div class="stat-icon blue">🏭</div>
          </div>
          <div class="stat-value">3</div>
          <div class="stat-delta delta-up">↑ 1 new unit rented</div>
        </div>
        <div class="stat-card amber">
          <div class="stat-top">
            <span class="stat-label">In Transit</span>
            <div class="stat-icon amber">🚚</div>
          </div>
          <div class="stat-value">2</div>
          <div class="stat-delta delta-up">Avg. ETA 1.5 hrs</div>
        </div>
        <div class="stat-card red">
          <div class="stat-top">
            <span class="stat-label">Temp Alerts</span>
            <div class="stat-icon red">⚠️</div>
          </div>
          <div class="stat-value">1</div>
          <div class="stat-delta delta-down">Unit C needs attention</div>
        </div>
      </div>

      <!-- ROW 1: Bookings + Notifications -->
      <div class="grid-2" style="margin-bottom:20px;">

        <!-- Booking Table -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">📋 Recent Bookings</span>
            <span class="card-action">View All</span>
          </div>
          <div class="card-body" style="padding:0;">
            <table class="booking-table">
              <thead>
                <tr>
                  <th>Booking ID</th>
                  <th>Product</th>
                  <th>Unit</th>
                  <th>Duration</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td style="font-weight:600;color:var(--ink-60);font-size:.72rem;">#BK-2041</td>
                  <td>Lettuce (80 kg)</td>
                  <td>Unit A – 2°C</td>
                  <td>3 days</td>
                  <td><span class="status-badge active"><span class="status-dot"></span>Active</span></td>
                </tr>
                <tr>
                  <td style="font-weight:600;color:var(--ink-60);font-size:.72rem;">#BK-2042</td>
                  <td>Tomatoes (50 kg)</td>
                  <td>Unit B – 8°C</td>
                  <td>5 days</td>
                  <td><span class="status-badge active"><span class="status-dot"></span>Active</span></td>
                </tr>
                <tr>
                  <td style="font-weight:600;color:var(--ink-60);font-size:.72rem;">#BK-2043</td>
                  <td>Mangoes (120 kg)</td>
                  <td>Unit C – 10°C</td>
                  <td>2 days</td>
                  <td><span class="status-badge pending"><span class="status-dot"></span>Pending</span></td>
                </tr>
                <tr>
                  <td style="font-weight:600;color:var(--ink-60);font-size:.72rem;">#BK-2039</td>
                  <td>Carrots (35 kg)</td>
                  <td>Unit A – 2°C</td>
                  <td>4 days</td>
                  <td><span class="status-badge done"><span class="status-dot"></span>Done</span></td>
                </tr>
                <tr>
                  <td style="font-weight:600;color:var(--ink-60);font-size:.72rem;">#BK-2037</td>
                  <td>Cabbage (90 kg)</td>
                  <td>Unit B – 8°C</td>
                  <td>6 days</td>
                  <td><span class="status-badge done"><span class="status-dot"></span>Done</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>

        <!-- Notifications -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">🔔 Notifications</span>
            <span class="card-action">Mark All Read</span>
          </div>
          <div class="card-body">
            <div class="notif-item">
              <div class="notif-avatar red">⚠️</div>
              <div class="notif-text">
                <div class="notif-msg"><strong>Temperature Alert</strong> — Unit C rose to 14°C, above your 12°C limit.</div>
                <div class="notif-time">2 minutes ago</div>
              </div>
              <div class="notif-unread"></div>
            </div>
            <div class="notif-item">
              <div class="notif-avatar green">✅</div>
              <div class="notif-text">
                <div class="notif-msg"><strong>Booking #BK-2043</strong> approved by facility admin.</div>
                <div class="notif-time">1 hour ago</div>
              </div>
              <div class="notif-unread"></div>
            </div>
            <div class="notif-item">
              <div class="notif-avatar blue">🚚</div>
              <div class="notif-text">
                <div class="notif-msg"><strong>Delivery DL-0891</strong> is now in transit — ETA 45 mins.</div>
                <div class="notif-time">3 hours ago</div>
              </div>
              <div class="notif-unread"></div>
            </div>
            <div class="notif-item">
              <div class="notif-avatar amber">💰</div>
              <div class="notif-text">
                <div class="notif-msg">Payment confirmed for <strong>#BK-2039</strong>. Receipt sent to your email.</div>
                <div class="notif-time">Yesterday, 4:12 PM</div>
              </div>
            </div>
            <div class="notif-item">
              <div class="notif-avatar green">📦</div>
              <div class="notif-text">
                <div class="notif-msg"><strong>Delivery DL-0885</strong> successfully completed and received.</div>
                <div class="notif-time">Yesterday, 11:30 AM</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- ROW 2: Temp Monitor + Delivery + Cost Estimator -->
      <div class="grid-3">

        <!-- Temperature Monitor -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">🌡️ Temperature Monitor</span>
            <span class="card-action">Details</span>
          </div>
          <div class="card-body">
            <div class="temp-row">
              <div class="temp-unit">
                <div class="temp-icon ok">❄️</div>
                <div class="temp-details">
                  <div class="temp-name">Unit A</div>
                  <div class="temp-sub">Lettuce · Target: 2°C</div>
                </div>
                <div class="temp-gauge">
                  <span class="temp-val ok">2.1°C</span>
                  <div class="temp-bar"><div class="temp-fill ok" style="width:22%"></div></div>
                </div>
              </div>
              <div class="temp-unit">
                <div class="temp-icon ok">🧊</div>
                <div class="temp-details">
                  <div class="temp-name">Unit B</div>
                  <div class="temp-sub">Tomatoes · Target: 8°C</div>
                </div>
                <div class="temp-gauge">
                  <span class="temp-val ok">7.8°C</span>
                  <div class="temp-bar"><div class="temp-fill ok" style="width:58%"></div></div>
                </div>
              </div>
              <div class="temp-unit" style="border:1px solid #f5c6c6;background:#fff8f8;">
                <div class="temp-icon crit">🔴</div>
                <div class="temp-details">
                  <div class="temp-name">Unit C</div>
                  <div class="temp-sub">Mangoes · Target: 10°C</div>
                </div>
                <div class="temp-gauge">
                  <span class="temp-val crit">14.2°C</span>
                  <div class="temp-bar"><div class="temp-fill crit" style="width:85%"></div></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Delivery Tracker -->
        <div class="card">
          <div class="card-header">
            <span class="card-title">🚚 Delivery Tracker</span>
            <span class="card-action">Full Map</span>
          </div>
          <div class="card-body">
            <div class="delivery-item">
              <div class="delivery-step-col">
                <div class="step-bubble done">✓</div>
                <div class="step-line"></div>
                <div class="step-bubble transit">→</div>
              </div>
              <div class="delivery-info" style="display:flex;flex-direction:column;gap:4px;">
                <span class="delivery-id">#DL-0891</span>
                <span class="delivery-name">Lettuce Batch — 80 kg</span>
                <div class="delivery-steps">
                  <span class="d-step done">Preparing</span>
                  <span class="d-arrow">›</span>
                  <span class="d-step active">In Transit</span>
                  <span class="d-arrow">›</span>
                  <span class="d-step pending">Delivered</span>
                </div>
                <span class="eta-tag">⏱ ETA: 45 mins</span>
              </div>
            </div>
            <div class="delivery-item">
              <div class="delivery-step-col">
                <div class="step-bubble done">✓</div>
                <div class="step-line"></div>
                <div class="step-bubble transit">→</div>
              </div>
              <div class="delivery-info" style="display:flex;flex-direction:column;gap:4px;">
                <span class="delivery-id">#DL-0895</span>
                <span class="delivery-name">Tomatoes — 50 kg</span>
                <div class="delivery-steps">
                  <span class="d-step done">Preparing</span>
                  <span class="d-arrow">›</span>
                  <span class="d-step active">In Transit</span>
                  <span class="d-arrow">›</span>
                  <span class="d-step pending">Delivered</span>
                </div>
                <span class="eta-tag">⏱ ETA: 2 hrs 10 mins</span>
              </div>
            </div>
            <div class="delivery-item">
              <div class="delivery-step-col">
                <div class="step-bubble done">✓</div>
                <div class="step-line"></div>
                <div class="step-bubble done">✓</div>
              </div>
              <div class="delivery-info" style="display:flex;flex-direction:column;gap:4px;">
                <span class="delivery-id">#DL-0885</span>
                <span class="delivery-name">Carrots — 35 kg</span>
                <div class="delivery-steps">
                  <span class="d-step done">Preparing</span>
                  <span class="d-arrow">›</span>
                  <span class="d-step done">In Transit</span>
                  <span class="d-arrow">›</span>
                  <span class="d-step done">Delivered</span>
                </div>
                <span style="font-size:.7rem;color:var(--moss);font-weight:600;">✅ Completed yesterday</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Cost Estimator + Quick Book -->
        <div style="display:flex;flex-direction:column;gap:16px;">
          <div class="card">
            <div class="card-header">
              <span class="card-title">🧮 Cost Estimator</span>
            </div>
            <div class="card-body">
              <div class="estimator">
                <div>
                  <div class="est-label">Storage Type</div>
                  <select class="est-input" id="storageType" onchange="calcCost()">
                    <option value="2">Deep Cold (2°C) — ₱180/day</option>
                    <option value="8">Chilled (8°C) — ₱120/day</option>
                    <option value="12">Cool Room (12°C) — ₱80/day</option>
                  </select>
                </div>
                <div class="est-input-row">
                  <div style="flex:1;">
                    <div class="est-label">Quantity (kg)</div>
                    <input class="est-input" id="qty" type="number" value="80" min="1" oninput="calcCost()" />
                  </div>
                  <div style="flex:1;">
                    <div class="est-label">Days</div>
                    <input class="est-input" id="days" type="number" value="3" min="1" oninput="calcCost()" />
                  </div>
                </div>
                <div class="est-result">
                  <div>
                    <div class="est-result-label">Estimated Cost</div>
                    <div class="est-result-val" id="estTotal">₱540.00</div>
                  </div>
                  <div style="text-align:right;">
                    <div class="est-result-label">Delivery Add-on</div>
                    <div style="color:rgba(255,255,255,.8);font-size:.85rem;font-weight:600;" id="estDelivery">+₱250</div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="card">
            <div class="card-header">
              <span class="card-title">➕ Quick Book</span>
            </div>
            <div class="card-body">
              <p style="font-size:.81rem;color:var(--ink-60);margin-bottom:14px;line-height:1.5;">
                Need cold storage or a delivery slot? Book in under 2 minutes.
              </p>
              <button class="quick-book-btn" onclick="openModal()">
                📦 Book Storage / Delivery
              </button>
            </div>
          </div>
        </div>

      </div>
    </div><!-- /page -->
  </main>
</div>

<!-- BOOKING MODAL -->
<div class="modal-overlay" id="bookingModal">
  <div class="modal">
    <div class="modal-title">📦 New Booking</div>
    <div class="modal-field">
      <label>Product Name</label>
      <input type="text" placeholder="e.g. Lettuce, Tomatoes, Mangoes" />
    </div>
    <div class="modal-field">
      <label>Quantity (kg)</label>
      <input type="number" placeholder="e.g. 80" />
    </div>
    <div class="modal-field">
      <label>Storage Type</label>
      <select>
        <option>Deep Cold (2°C)</option>
        <option>Chilled (8°C)</option>
        <option>Cool Room (12°C)</option>
      </select>
    </div>
    <div class="modal-field">
      <label>Duration (Days)</label>
      <input type="number" placeholder="e.g. 3" />
    </div>
    <div class="modal-field">
      <label>Delivery Needed?</label>
      <select>
        <option>Yes — include delivery</option>
        <option>No — drop-off only</option>
      </select>
    </div>
    <div class="modal-btns">
      <button class="modal-cancel" onclick="closeModal()">Cancel</button>
      <button class="modal-submit" onclick="submitBooking()">Submit Booking ✓</button>
    </div>
  </div>
</div>

<script>
  const RATES = { "2": 180, "8": 120, "12": 80 };

  function calcCost() {
    const type  = document.getElementById("storageType").value;
    const qty   = parseFloat(document.getElementById("qty").value) || 0;
    const days  = parseFloat(document.getElementById("days").value) || 0;
    const rate  = RATES[type] || 120;
    const base  = rate * days;
    const delivery = qty > 100 ? 350 : 250;
    document.getElementById("estTotal").textContent    = "₱" + base.toFixed(2);
    document.getElementById("estDelivery").textContent = "+₱" + delivery;
  }

  function openModal()  { document.getElementById("bookingModal").classList.add("open"); }
  function closeModal() { document.getElementById("bookingModal").classList.remove("open"); }

  function submitBooking() {
    closeModal();
    alert("✅ Booking submitted! Admin will confirm within 30 minutes.");
  }

  document.getElementById("bookingModal").addEventListener("click", function(e) {
    if (e.target === this) closeModal();
  });
</script>
</body>
</html>
