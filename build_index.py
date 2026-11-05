# -*- coding: utf-8 -*-
import sys

def build():
    html = r'''<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Chánh Điện Chứng Khoán · Vạn Lệnh Tím Trần (16:9 3D Live)</title>
<meta name="description" content="Chánh điện cầu nguyện cổ phiếu 2.5D: 24 bồ đoàn sen vàng, gieo quẻ Bát Quái, dâng lễ vật nến xanh chuối xanh, bão cảm xúc, Auto-Mõ thiền lofi!">
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🐂</text></svg>">

<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Noto+Serif:ital,wght@0,400;0,600;0,700;1,400&family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=JetBrains+Mono:wght@600;700&display=swap" rel="stylesheet">

<style>
:root {
  --bg: #070305;
  --fg: #f5e8d0;
  --muted: #b89c79;
  --gold: #e5b342;
  --gold-glow: rgba(229, 179, 66, 0.5);
  --purple-ce: #d946ef;
  --purple-glow: rgba(217, 70, 239, 0.6);
  --green-up: #10b981;
  --red-down: #ef4444;
  --yellow-ref: #f59e0b;
  --panel: rgba(18, 9, 15, 0.94);
  --panel-glass: rgba(24, 11, 20, 0.90);
  --line: rgba(229, 179, 66, 0.35);
  --display: "Noto Serif", Georgia, serif;
  --body: "Be Vietnam Pro", system-ui, sans-serif;
  --mono: "JetBrains Mono", monospace;
  color-scheme: dark;
}

* { box-sizing: border-box; margin: 0; padding: 0; user-select: none; -webkit-user-select: none; }
html, body { height: 100%; width: 100%; margin: 0; background: var(--bg); color: var(--fg); font-family: var(--body); overflow: hidden; }

/* Stage wrap filling viewport in landscape 16:9 */
#wrap {
  position: fixed;
  inset: 0;
  display: grid;
  place-items: center;
  background: radial-gradient(circle at 50% 35%, #1f0b18 0%, #060205 100%);
  padding: env(safe-area-inset-top, 0px) env(safe-area-inset-right, 0px) env(safe-area-inset-bottom, 0px) env(safe-area-inset-left, 0px);
}

#stage {
  position: relative;
  aspect-ratio: 16/9;
  width: 100vw;
  height: calc(100vw * 9 / 16);
  max-height: 100vh;
  max-width: calc(100vh * 16 / 9);
  overflow: hidden;
  background: #000;
  box-shadow: 0 0 120px rgba(0, 0, 0, 0.98), 0 0 60px rgba(217, 70, 239, 0.28);
  cursor: grab;
}
#stage.grabbing { cursor: grabbing; }

#stage canvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  display: block;
  touch-action: none;
}

/* Common UI overlays */
.hud {
  position: absolute;
  z-index: 10;
  pointer-events: none;
  display: flex;
  align-items: center;
}
.hud * { pointer-events: auto; }

/* Top Market Ticker Header */
#topHeader {
  top: 8px;
  left: 10px;
  right: 10px;
  justify-content: space-between;
  gap: 8px;
}

.chip {
  background: var(--panel-glass);
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 4px 12px;
  font-size: 11px;
  font-weight: 600;
  backdrop-filter: blur(10px);
  display: inline-flex;
  gap: 6px;
  align-items: center;
  box-shadow: 0 4px 14px rgba(0,0,0,0.6);
  color: var(--fg);
}
.chip b { font-family: var(--display); color: var(--gold); }
.chip.ce { border-color: var(--purple-ce); color: #fff; box-shadow: 0 0 14px var(--purple-glow); }
.chip.ce b { color: var(--purple-ce); font-family: 'Cinzel', serif; }

.index-badge {
  font-family: var(--mono);
  font-size: 10px;
  padding: 2px 6px;
  border-radius: 4px;
  font-weight: 700;
}
.index-badge.up { background: rgba(16, 185, 129, 0.2); color: #34d399; }
.index-badge.ce { background: rgba(217, 70, 239, 0.25); color: #f472b6; border: 1px solid var(--purple-ce); }

/* Center Temple Title */
#templeBanner {
  position: absolute;
  top: 8px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 10;
  text-align: center;
  pointer-events: none;
}
.banner-title {
  display: inline-block;
  background: linear-gradient(180deg, #991b1b, #7f1d1d);
  border: 1px solid var(--gold);
  border-radius: 6px;
  padding: 3px 14px;
  color: #fef08a;
  font-family: var(--display);
  font-weight: 900;
  font-size: 13px;
  letter-spacing: 1px;
  box-shadow: 0 4px 16px rgba(0,0,0,0.7), 0 0 12px rgba(229, 179, 66, 0.3);
}

/* Top Ticker Marquee Strip */
#tickerTape {
  position: absolute;
  top: 42px;
  left: 10px;
  right: 10px;
  height: 26px;
  background: rgba(15, 6, 13, 0.88);
  border: 1px solid rgba(229, 179, 66, 0.25);
  border-radius: 6px;
  backdrop-filter: blur(8px);
  z-index: 10;
  overflow: hidden;
  display: flex;
  align-items: center;
}
#tickerTape .ticker-label {
  background: linear-gradient(90deg, #b45309, #d97706);
  color: #fff;
  font-weight: 700;
  font-size: 10px;
  padding: 0 10px;
  height: 100%;
  display: flex;
  align-items: center;
  letter-spacing: 0.5px;
  white-space: nowrap;
  font-family: var(--display);
}
#tickerTape .ticker-track {
  display: flex;
  gap: 22px;
  animation: scrollTape 35s linear infinite;
  white-space: nowrap;
  font-family: var(--mono);
  font-size: 11px;
  font-weight: 600;
  padding-left: 20px;
}
@keyframes scrollTape {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
.tape-item { display: inline-flex; gap: 5px; align-items: center; cursor: pointer; }
.tape-item:hover { text-decoration: underline; }
.tape-item.ce { color: #f472b6; text-shadow: 0 0 6px var(--purple-glow); }
.tape-item.green { color: #34d399; }

/* TikTok Live Style: Royal Merit Proclamation Banner */
#royalMeritBanner {
  position: absolute;
  top: 74px;
  left: 50%;
  transform: translateX(-50%);
  width: min(580px, 86%);
  background: linear-gradient(180deg, rgba(88, 14, 25, 0.95) 0%, rgba(45, 7, 14, 0.95) 100%);
  border: 1.5px solid var(--gold);
  border-radius: 8px;
  padding: 6px 14px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.9), 0 0 20px rgba(229, 179, 66, 0.35);
  backdrop-filter: blur(10px);
  z-index: 11;
  text-align: center;
  pointer-events: none;
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  display: flex;
  flex-direction: column;
  gap: 2px;
}
#royalMeritBanner.pulse {
  animation: bannerGlow 1.2s ease-out;
}
@keyframes bannerGlow {
  0% { transform: translateX(-50%) scale(1.05); box-shadow: 0 0 40px var(--purple-glow); }
  100% { transform: translateX(-50%) scale(1.0); }
}
.merit-lead {
  font-family: var(--display);
  font-size: 11px;
  color: #fef08a;
  font-weight: 700;
  letter-spacing: 0.5px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
}
.merit-lead span.name { color: #fff; text-shadow: 0 0 8px rgba(255,255,255,0.6); }
.merit-lead span.gold-score { color: var(--gold); font-family: var(--mono); font-weight: 800; }
.merit-quote {
  font-family: var(--body);
  font-size: 10.5px;
  color: #fce7f3;
  font-style: italic;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* Button to Toggle Stock Board */
.board-toggle-btn {
  position: absolute;
  top: 76px;
  left: 10px;
  z-index: 11;
  background: var(--panel);
  border: 1px solid var(--line);
  color: var(--gold);
  border-radius: 8px;
  padding: 6px 12px;
  font-size: 11px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  box-shadow: 0 4px 16px rgba(0,0,0,0.6);
  backdrop-filter: blur(8px);
}
.board-toggle-btn:hover { border-color: var(--gold); background: #230f1b; }

/* Left Bát Quái Bảng Điện Tử */
#stockBoardPanel {
  position: absolute;
  top: 74px;
  bottom: 56px;
  left: 10px;
  width: 370px;
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 12px;
  backdrop-filter: blur(14px);
  z-index: 12;
  display: flex;
  flex-direction: column;
  box-shadow: 0 8px 32px rgba(0,0,0,0.85);
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.35s ease;
}
#stockBoardPanel.collapsed {
  transform: translateX(-390px);
  opacity: 0;
  pointer-events: none;
}
.board-header {
  padding: 8px 12px;
  border-bottom: 1px solid rgba(229, 179, 66, 0.2);
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: rgba(229, 179, 66, 0.08);
}
.board-header h3 {
  font-family: var(--display);
  font-size: 12px;
  color: var(--gold);
  display: flex;
  align-items: center;
  gap: 6px;
}
.board-tabs {
  display: flex;
  gap: 4px;
  padding: 5px 8px;
  background: rgba(0, 0, 0, 0.4);
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  overflow-x: auto;
}
.board-tab {
  padding: 3px 7px;
  font-size: 9.5px;
  font-weight: 600;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid transparent;
  border-radius: 4px;
  color: var(--muted);
  cursor: pointer;
  white-space: nowrap;
}
.board-tab.active {
  background: rgba(217, 70, 239, 0.2);
  border-color: var(--purple-ce);
  color: #fff;
}
.stock-list {
  flex: 1;
  overflow-y: auto;
  padding: 3px;
  font-family: var(--mono);
}
.stock-list::-webkit-scrollbar { width: 5px; }
.stock-list::-webkit-scrollbar-thumb { background: rgba(229, 179, 66, 0.3); border-radius: 4px; }
.stock-row {
  display: grid;
  grid-template-columns: 50px 52px 60px 70px 1fr 46px;
  align-items: center;
  padding: 5px 6px;
  font-size: 10.5px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  border-radius: 4px;
  transition: background 0.15s;
}
.stock-row:hover { background: rgba(229, 179, 66, 0.12); }
.stock-sym { font-weight: 700; color: #fff; }
.stock-price { font-weight: 700; }
.stock-price.ce { color: #f472b6; text-shadow: 0 0 6px var(--purple-glow); }
.stock-price.green { color: #34d399; }
.stock-price.yellow { color: #fbbf24; }
.stock-act-btn {
  background: linear-gradient(135deg, #701a75, #a21caf);
  border: 1px solid var(--purple-ce);
  color: #fff;
  font-size: 8.5px;
  font-weight: 700;
  border-radius: 4px;
  padding: 2px 4px;
  cursor: pointer;
  font-family: var(--body);
}
.stock-act-btn:hover { background: #c026d3; }

.board-footer {
  padding: 6px 10px;
  border-top: 1px solid rgba(229, 179, 66, 0.2);
  display: flex;
  gap: 6px;
}

/* Right Leaderboard */
#rightPanel {
  top: 74px;
  right: 10px;
  width: 210px;
  flex-direction: column;
  gap: 8px;
}
.card-box {
  background: var(--panel-glass);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 8px 10px;
  backdrop-filter: blur(10px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.65);
  width: 100%;
}
.card-box h4 {
  font-family: var(--display);
  font-size: 11px;
  color: var(--gold);
  border-bottom: 1px solid rgba(229, 179, 66, 0.25);
  padding-bottom: 4px;
  margin-bottom: 6px;
  display: flex;
  justify-content: space-between;
}
.merit-list { list-style: none; font-size: 10.5px; display: flex; flex-direction: column; gap: 4px; }
.merit-list li { display: flex; justify-content: space-between; align-items: center; }
.merit-list li span { font-family: var(--mono); color: var(--gold); font-weight: 700; }
.merit-list li:first-child { color: #f472b6; font-weight: 700; }

/* Interactive Big Mõ Gỗ Xả Margin (Image 1 Feature) */
#fishWidget {
  position: absolute;
  bottom: 54px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 11;
  background: rgba(22, 10, 18, 0.94);
  border: 1.5px solid var(--gold);
  border-radius: 16px;
  padding: 5px 14px;
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 8px 30px rgba(0,0,0,0.85), 0 0 20px rgba(229, 179, 66, 0.25);
  backdrop-filter: blur(12px);
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
#fishWidget:hover {
  border-color: var(--purple-ce);
  box-shadow: 0 8px 35px rgba(0,0,0,0.95), 0 0 25px var(--purple-glow);
  transform: translateX(-50%) translateY(-2px);
}
#fishWidget:active {
  transform: translateX(-50%) scale(0.96);
}
.fish-avatar {
  width: 52px;
  height: 44px;
  position: relative;
  display: grid;
  place-items: center;
}
.fish-avatar img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: drop-shadow(0 4px 8px rgba(0,0,0,0.6));
  transition: transform 0.08s;
}
#fishWidget.knock .fish-avatar img {
  transform: scale(0.86) rotate(-4deg);
}
.fish-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.fish-title {
  font-family: var(--display);
  font-size: 11px;
  font-weight: 700;
  color: var(--gold);
  letter-spacing: 0.5px;
  display: flex;
  align-items: center;
  gap: 6px;
}
.fish-stats {
  display: flex;
  gap: 10px;
  font-size: 9.5px;
  color: #d1d5db;
}
.fish-stats b { font-family: var(--mono); color: #fef08a; }
.fish-stats span.margin-stat b { color: #34d399; }
.fish-actions {
  display: flex;
  align-items: center;
  gap: 6px;
}
.fish-tap-prompt {
  background: linear-gradient(135deg, #701a75, #a21caf);
  border: 1px solid var(--purple-ce);
  color: #fff;
  border-radius: 999px;
  padding: 4px 9px;
  font-size: 9.5px;
  font-weight: 700;
  white-space: nowrap;
}
.auto-zen-toggle {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(229, 179, 66, 0.4);
  color: #fef08a;
  border-radius: 999px;
  padding: 4px 9px;
  font-size: 9.5px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}
.auto-zen-toggle.active {
  background: linear-gradient(135deg, #059669, #10b981);
  border-color: #34d399;
  color: #fff;
  box-shadow: 0 0 12px rgba(16, 185, 129, 0.5);
}

/* TikTok Live Danmaku Layer */
#danmakuLayer {
  position: absolute;
  inset: 0;
  pointer-events: none;
  overflow: hidden;
  z-index: 8;
}
.danmaku-item {
  position: absolute;
  white-space: nowrap;
  font-size: 12px;
  font-weight: 600;
  color: rgba(255, 255, 255, 0.9);
  background: rgba(16, 7, 14, 0.65);
  border: 1px solid rgba(229, 179, 66, 0.3);
  border-radius: 999px;
  padding: 3px 12px;
  backdrop-filter: blur(4px);
  text-shadow: 0 1px 3px rgba(0,0,0,0.8);
  animation: floatUpDanmaku 10s linear forwards;
  will-change: transform, opacity;
}
.danmaku-item.special {
  color: #fef08a;
  border-color: var(--purple-ce);
  background: rgba(112, 26, 117, 0.85);
  box-shadow: 0 0 14px var(--purple-glow);
  font-weight: 700;
}
@keyframes floatUpDanmaku {
  0% { transform: translateY(100vh); opacity: 0; }
  10% { opacity: 1; }
  85% { opacity: 1; }
  100% { transform: translateY(-40px); opacity: 0; }
}

/* COMBO FEATURE 3: LIVE EMOTE BURST BAR (RIGHT SIDE) */
#emoteBar {
  position: absolute;
  right: 12px;
  bottom: 195px;
  z-index: 11;
  display: flex;
  flex-direction: column;
  gap: 7px;
  align-items: center;
}
.emote-btn {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: rgba(20, 8, 16, 0.92);
  border: 1.5px solid var(--gold);
  color: #fff;
  font-size: 18px;
  display: grid;
  place-items: center;
  cursor: pointer;
  box-shadow: 0 4px 14px rgba(0,0,0,0.7);
  backdrop-filter: blur(8px);
  transition: all 0.18s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.emote-btn:hover {
  transform: scale(1.18);
  border-color: var(--purple-ce);
  box-shadow: 0 0 18px var(--purple-glow);
}
.emote-btn:active {
  transform: scale(0.9);
}

/* Quick Prayer Bar */
#quickPrayerBar {
  position: absolute;
  bottom: 10px;
  left: 10px;
  width: 250px;
  z-index: 10;
  display: flex;
  gap: 4px;
}
#quickPrayerInput {
  flex: 1;
  background: rgba(18, 9, 15, 0.85);
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 5px 12px;
  font-size: 11px;
  color: #fff;
  backdrop-filter: blur(8px);
}
#quickPrayerInput:focus { outline: none; border-color: var(--purple-ce); }
#sendPrayerBtn {
  background: linear-gradient(135deg, #b45309, #d97706);
  border: 1px solid var(--gold);
  border-radius: 999px;
  color: #fff;
  font-size: 11px;
  font-weight: 700;
  padding: 5px 10px;
  cursor: pointer;
}
#sendPrayerBtn:hover { background: #d97706; }

/* Camera Toolbar */
#camToolbar {
  position: absolute;
  bottom: 54px;
  right: 10px;
  display: flex;
  flex-direction: column;
  gap: 5px;
  z-index: 11;
}
.cam-btn {
  background: var(--panel);
  border: 1px solid var(--line);
  color: var(--fg);
  border-radius: 8px;
  padding: 5px 9px;
  font-size: 10px;
  font-weight: 700;
  display: flex;
  align-items: center;
  gap: 5px;
  cursor: pointer;
  box-shadow: 0 4px 14px rgba(0,0,0,0.6);
  backdrop-filter: blur(8px);
  transition: all 0.2s;
}
.cam-btn:hover {
  background: #2b1122;
  border-color: var(--gold);
  color: #fff;
}
.cam-btn.special {
  background: linear-gradient(135deg, #831843, #c026d3);
  border-color: #f472b6;
  color: #fff;
  box-shadow: 0 0 16px var(--purple-glow);
}
.cam-btn.special:hover {
  background: linear-gradient(135deg, #9d174d, #d946ef);
  transform: translateY(-2px);
}

/* Bottom Action Dock */
#bottomDock {
  position: absolute;
  bottom: 8px;
  right: 10px;
  display: flex;
  gap: 6px;
  align-items: center;
  z-index: 10;
  background: rgba(16, 7, 13, 0.88);
  border: 1px solid var(--line);
  border-radius: 999px;
  padding: 4px 12px;
  backdrop-filter: blur(14px);
  box-shadow: 0 6px 25px rgba(0,0,0,0.85);
}
.btn {
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(229, 179, 66, 0.3);
  color: var(--fg);
  border-radius: 999px;
  padding: 5px 11px;
  font-size: 11px;
  font-weight: 700;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  cursor: pointer;
  transition: all 0.2s;
  white-space: nowrap;
}
.btn:hover { background: rgba(229, 179, 66, 0.2); border-color: var(--gold); }
.btn.primary {
  background: linear-gradient(135deg, #9333ea, #c026d3);
  border-color: #f472b6;
  color: #fff;
  box-shadow: 0 0 16px var(--purple-glow);
}
.btn.primary:hover { background: linear-gradient(135deg, #a855f7, #d946ef); transform: translateY(-1px); }
.btn.fortune {
  background: linear-gradient(135deg, #b45309, #d97706);
  border-color: var(--gold);
  color: #fef08a;
  box-shadow: 0 0 14px rgba(229, 179, 66, 0.4);
}
.btn.fortune:hover { background: linear-gradient(135deg, #d97706, #f59e0b); }
.btn.gift {
  background: linear-gradient(135deg, #047857, #059669);
  border-color: #34d399;
  color: #ecfdf5;
}
.btn.gift:hover { background: linear-gradient(135deg, #059669, #10b981); }

/* Modals */
.modal-backdrop {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.78);
  backdrop-filter: blur(6px);
  display: none;
  place-items: center;
  z-index: 100;
  padding: 16px;
}
.modal-backdrop.active { display: grid; }
.modal-box {
  background: linear-gradient(180deg, #1f0b17 0%, #12050e 100%);
  border: 1px solid var(--gold);
  border-radius: 14px;
  width: 100%;
  max-width: 520px;
  box-shadow: 0 0 50px rgba(0,0,0,0.9), 0 0 25px rgba(217, 70, 239, 0.3);
  padding: 16px 20px;
  position: relative;
  max-height: 90vh;
  overflow-y: auto;
}
.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid rgba(229, 179, 66, 0.25);
  padding-bottom: 8px;
  margin-bottom: 12px;
}
.modal-header h2 {
  font-family: var(--display);
  font-size: 15px;
  color: var(--gold);
  display: flex;
  align-items: center;
  gap: 8px;
}
.close-btn {
  background: none;
  border: none;
  font-size: 22px;
  color: var(--muted);
  cursor: pointer;
}
.close-btn:hover { color: #fff; }

.form-group { margin-bottom: 10px; }
.form-group label {
  display: block;
  font-size: 11px;
  font-weight: 600;
  color: var(--muted);
  margin-bottom: 4px;
}
.form-control {
  width: 100%;
  background: rgba(0, 0, 0, 0.45);
  border: 1px solid rgba(229, 179, 66, 0.3);
  border-radius: 6px;
  padding: 7px 10px;
  color: #fff;
  font-size: 12px;
  font-family: var(--body);
}
.form-control:focus {
  outline: none;
  border-color: var(--purple-ce);
  box-shadow: 0 0 10px var(--purple-glow);
}

.avatar-selector {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 6px;
  margin-top: 4px;
}
.avatar-card {
  background: rgba(0, 0, 0, 0.4);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 8px;
  padding: 6px 4px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 3px;
  cursor: pointer;
  transition: all 0.2s;
}
.avatar-card:hover { border-color: var(--gold); }
.avatar-card.active {
  border-color: var(--purple-ce);
  background: rgba(217, 70, 239, 0.2);
  box-shadow: 0 0 12px var(--purple-glow);
}
.avatar-card .icon { font-size: 22px; }
.avatar-card .title { font-size: 9.5px; font-weight: 700; color: #fff; }

.quick-stocks { display: flex; flex-wrap: wrap; gap: 4px; margin-top: 5px; }
.stock-pill {
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: 999px;
  padding: 2px 8px;
  font-size: 10.5px;
  font-family: var(--mono);
  color: var(--fg);
  cursor: pointer;
}
.stock-pill:hover, .stock-pill.selected {
  background: rgba(217, 70, 239, 0.25);
  border-color: var(--purple-ce);
  color: #fff;
}

.submit-btn {
  width: 100%;
  background: linear-gradient(135deg, #b45309, #d97706);
  border: 1px solid var(--gold);
  border-radius: 8px;
  padding: 9px;
  color: #fff;
  font-family: var(--display);
  font-size: 12.5px;
  font-weight: 700;
  cursor: pointer;
  letter-spacing: 0.5px;
  margin-top: 6px;
  box-shadow: 0 4px 16px rgba(180, 83, 9, 0.4);
}
.submit-btn:hover { background: linear-gradient(135deg, #d97706, #f59e0b); }

/* COMBO FEATURE 1: ỐNG XĂM GIEO QUẺ BÁT QUÁI MODAL STYLING */
#fortuneModal .fortune-stage {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px 0;
  text-align: center;
}
.tube-box {
  width: 110px;
  height: 150px;
  position: relative;
  margin: 10px auto;
  cursor: pointer;
  transition: transform 0.2s;
}
.tube-box:hover { transform: scale(1.05); }
.tube-box.shaking {
  animation: shakeTube 0.8s ease-in-out infinite;
}
@keyframes shakeTube {
  0% { transform: rotate(0deg) translateY(0); }
  20% { transform: rotate(-14deg) translateY(-8px); }
  40% { transform: rotate(14deg) translateY(-8px); }
  60% { transform: rotate(-10deg) translateY(-4px); }
  80% { transform: rotate(10deg) translateY(-4px); }
  100% { transform: rotate(0deg) translateY(0); }
}
.tube-body {
  width: 70px;
  height: 115px;
  background: linear-gradient(180deg, #92400e 0%, #78350f 50%, #451a03 100%);
  border: 2px solid var(--gold);
  border-radius: 8px 8px 18px 18px;
  margin: 0 auto;
  box-shadow: 0 8px 20px rgba(0,0,0,0.8), 0 0 15px rgba(229, 179, 66, 0.3);
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}
.tube-label {
  writing-mode: vertical-rl;
  font-family: var(--display);
  font-size: 11px;
  font-weight: 900;
  color: #fef08a;
  letter-spacing: 2px;
  text-shadow: 0 0 6px rgba(0,0,0,0.9);
}
.fortune-sticks {
  position: absolute;
  top: -24px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 4px;
}
.stick {
  width: 5px;
  height: 40px;
  background: linear-gradient(180deg, #fef08a, #d97706);
  border-radius: 2px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.6);
}
.stick.pop {
  animation: popStick 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
}
@keyframes popStick {
  0% { transform: translateY(0); }
  100% { transform: translateY(-38px) scale(1.15); box-shadow: 0 0 15px var(--purple-glow); }
}

/* Fortune Card Result */
.fortune-card {
  display: none;
  background: linear-gradient(180deg, #2a081c 0%, #170410 100%);
  border: 2px solid var(--gold);
  border-radius: 12px;
  padding: 16px;
  box-shadow: 0 0 35px rgba(217, 70, 239, 0.35);
  animation: cardFadeIn 0.5s ease-out;
}
@keyframes cardFadeIn {
  from { opacity: 0; transform: scale(0.92); }
  to { opacity: 1; transform: scale(1); }
}
.fortune-badge {
  display: inline-block;
  background: linear-gradient(135deg, #b45309, #d97706);
  color: #fff;
  font-family: var(--display);
  font-weight: 700;
  font-size: 11px;
  padding: 3px 12px;
  border-radius: 999px;
  margin-bottom: 6px;
}
.fortune-title {
  font-family: var(--display);
  font-size: 17px;
  font-weight: 900;
  color: #fef08a;
  margin-bottom: 10px;
  text-shadow: 0 0 10px rgba(229, 179, 66, 0.6);
}
.fortune-poem {
  background: rgba(0, 0, 0, 0.45);
  border-left: 3px solid var(--purple-ce);
  padding: 10px 14px;
  border-radius: 6px;
  font-family: var(--display);
  font-size: 12.5px;
  color: #fce7f3;
  line-height: 1.7;
  font-style: italic;
  margin-bottom: 12px;
  text-align: left;
}
.fortune-stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 6px;
  margin-bottom: 14px;
}
.stat-pill {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(229, 179, 66, 0.25);
  border-radius: 6px;
  padding: 6px 4px;
  text-align: center;
}
.stat-pill span { display: block; font-size: 9.5px; color: var(--muted); }
.stat-pill b { font-family: var(--mono); font-size: 11px; color: #34d399; }
.stat-pill b.purple { color: #f472b6; }

/* COMBO FEATURE 2: DÂNG LỄ VẬT MODAL STYLING */
.offerings-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
  gap: 10px;
  margin-top: 10px;
}
.offering-card {
  background: rgba(25, 10, 20, 0.85);
  border: 1.5px solid rgba(229, 179, 66, 0.35);
  border-radius: 10px;
  padding: 12px 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.2s;
}
.offering-card:hover {
  border-color: var(--gold);
  background: rgba(45, 14, 32, 0.95);
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(229, 179, 66, 0.3);
}
.offering-icon { font-size: 34px; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.6)); }
.offering-name { font-family: var(--display); font-size: 11.5px; font-weight: 700; color: #fef08a; }
.offering-desc { font-size: 9.5px; color: #cbd5e1; line-height: 1.3; }
.offering-merit { font-family: var(--mono); font-size: 10px; font-weight: 700; color: #34d399; }

/* Capture Facebook Card Modal */
#fbModal .preview-box {
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
  border: 1px solid var(--gold);
  margin-bottom: 10px;
  background: #000;
}
#fbModal .preview-box img {
  width: 100%;
  display: block;
}
.fb-actions { display: flex; gap: 8px; }
.fb-actions .btn { flex: 1; justify-content: center; }

/* Toast */
#toast {
  position: absolute;
  top: 76px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(18, 9, 15, 0.95);
  border: 1px solid var(--purple-ce);
  border-radius: 999px;
  padding: 6px 16px;
  font-size: 11.5px;
  font-weight: 700;
  color: #fff;
  box-shadow: 0 0 20px var(--purple-glow);
  z-index: 120;
  display: none;
  animation: fadeIn 0.3s;
}
@keyframes fadeIn { from { opacity: 0; transform: translate(-50%, -10px); } to { opacity: 1; transform: translate(-50%, 0); } }
</style>
</head>
<body>

<div id="wrap">
  <div id="stage">
    <canvas id="c" width="1920" height="1080"></canvas>

    <!-- Danmaku Flying Layer -->
    <div id="danmakuLayer"></div>

    <!-- COMBO FEATURE 3: LIVE EMOTE BURST BAR -->
    <div id="emoteBar">
      <button class="emote-btn" id="emoteHeartBtn" title="Thả Bão Tim Tím Cầu Trần">🟣</button>
      <button class="emote-btn" id="emoteBullBtn" title="Thả Đàn Bò Vàng Mini Chạy">🐂</button>
      <button class="emote-btn" id="emoteGoldBtn" title="Thả Mưa Tiền Vàng Lộc Phát">💰</button>
      <button class="emote-btn" id="emoteBoltBtn" title="Sấm Sét Trần CE Đánh Tan Gấu Đỏ">⚡</button>
    </div>

    <!-- Top Market Ticker Header -->
    <div class="hud" id="topHeader">
      <div style="display:flex; gap:6px; align-items:center;">
        <div class="chip ce">
          <span>VN-INDEX:</span>
          <b id="idxVal">1,288.66</b>
          <span class="index-badge ce" id="idxChg">+18.52 (+1.46%) CE</span>
        </div>
        <div class="chip">
          <span>VN30:</span>
          <span class="index-badge up">1,324.50 (+1.52%)</span>
        </div>
        <div class="chip">
          <span>Thanh khoản:</span>
          <b>28,450 Tỷ</b>
        </div>
      </div>

      <div style="display:flex; gap:6px; align-items:center;">
        <button class="chip" id="userProfileBtn" title="Tạo hoặc sửa nhân vật của bạn">
          <span id="userBadgeIcon">🧘‍♂️</span>
          <span id="userBadgeName">BẠN: <b>Cá Mập Đáy [SSI]</b></span>
        </button>
        <div class="chip">
          <span>Đồng thiền:</span>
          <b id="devoteeCount">24/24 chứng sĩ</b>
        </div>
      </div>
    </div>

    <!-- Center Temple Title Banner -->
    <div id="templeBanner">
      <div class="banner-title">CHÁNH ĐIỆN CHỨNG KHOÁN</div>
    </div>

    <!-- Top Ticker Marquee Strip -->
    <div id="tickerTape">
      <div class="ticker-label">⚡ BẢNG ĐIỆN TỬ:</div>
      <div class="ticker-track" id="tickerTrack"></div>
    </div>

    <!-- Royal Merit Proclamation Banner -->
    <div id="royalMeritBanner">
      <div class="merit-lead">
        <span>📜 ĐẠO HỮU</span>
        <span class="name" id="meritBannerUser">Cá Mập Đáy</span>
        <span>THÀNH TÂM DÂNG SỚ [</span>
        <span class="name" id="meritBannerStock" style="color:#f472b6;">SSI</span>
        <span>] · CÔNG ĐỨC:</span>
        <span class="gold-score" id="meritBannerPoints">1,592</span>
        <span>📜</span>
      </div>
      <div class="merit-quote" id="meritBannerWish">
        "Kính nguyện Thần Chứng Khoán độ cho [SSI] tím 7 cây liên tiếp, khối ngoại ngừng xả, lái kéo về bờ đại thắng!"
      </div>
    </div>

    <!-- Button to Toggle Stock Board -->
    <button class="board-toggle-btn" id="toggleBoardBtn">
      <span>📊</span>
      <span id="toggleBoardText">BÁT QUÁI BẢNG ĐIỆN</span>
    </button>

    <!-- Left Bát Quái Bảng Điện Tử -->
    <div id="stockBoardPanel">
      <div class="board-header">
        <h3><span>📈</span> BÁT QUÁI BẢNG ĐIỆN SƠ BỘ</h3>
        <button class="close-btn" id="closeBoardBtn" style="font-size:16px;">&times;</button>
      </div>

      <div class="board-tabs" id="boardTabs">
        <button class="board-tab active" data-filter="all">Tất cả</button>
        <button class="board-tab" data-filter="chungkhoan">Chứng khoán</button>
        <button class="board-tab" data-filter="bds">BĐS & Thép</button>
        <button class="board-tab" data-filter="nganhang">Ngân hàng</button>
        <button class="board-tab" data-filter="ce">Tím Trần (CE)</button>
      </div>

      <div class="stock-list" id="stockListContainer"></div>

      <div class="board-footer">
        <button class="btn primary" id="forceCeBtn" style="flex:1; font-size:11px;" title="Tâm linh kích hoạt toàn sàn tím trần!">🟣 Ép Toàn Sàn Tím Trần</button>
      </div>
    </div>

    <!-- Right Merit Board -->
    <div class="hud" id="rightPanel">
      <div class="card-box">
        <h4><span>✨ BẢNG VÀNG CÔNG ĐỨC</span> <span>Top</span></h4>
        <ol class="merit-list" id="meritList">
          <li>1. Cụ Lái Trưởng <span>99.999</span></li>
          <li>2. Cá Con Đu Đỉnh <span>12.500</span></li>
          <li>3. Bắt Đáy Thành Công <span>8.800</span></li>
          <li>4. Sư FPT Công Nghệ <span>6.200</span></li>
          <li>5. Tàu BĐS Về Bờ <span>5.400</span></li>
        </ol>
      </div>
    </div>

    <!-- Interactive Big Mõ Gỗ Xả Margin (Image 1 Feature) -->
    <div id="fishWidget" title="Chạm mõ gõ tiếng cốc để xả Margin, tích công đức, kéo cổ phiếu tím trần!">
      <div class="fish-avatar">
        <img id="fishImg" src="assets/fx_mo.png" alt="Mõ Gỗ Xả Margin">
      </div>
      <div class="fish-info">
        <div class="fish-title">
          <span>📿 MÕ GỖ XẢ MARGIN</span>
          <span style="font-size:10px; color:#f472b6;">✦ Tiếng Cốc Linh Ứng</span>
        </div>
        <div class="fish-stats">
          <span>Công đức: <b id="userMeritVal">515</b></span>
          <span>Cộng đồng: <b id="commMeritVal">88.376</b></span>
          <span class="margin-stat">Margin: <b id="marginVal">35% (An toàn)</b></span>
        </div>
      </div>
      <div class="fish-actions">
        <div class="fish-tap-prompt">GÕ MÕ (SPACE)</div>
        <button class="auto-zen-toggle" id="autoZenBtn" title="Bật chế độ tự động gõ mõ thiền Lo-fi">🎧 Auto-Mõ: TẮT</button>
      </div>
    </div>

    <!-- Quick Prayer Bar -->
    <form id="quickPrayerBar">
      <input type="text" id="quickPrayerInput" placeholder="Gõ lời khấn để bay lên Chánh Điện..." maxlength="60">
      <button type="submit" id="sendPrayerBtn">Khấn</button>
    </form>

    <!-- Camera Navigation Toolbar -->
    <div id="camToolbar">
      <button class="cam-btn special" id="captureFbBtn" title="Chụp ảnh chứng sĩ dâng sớ để up Facebook">
        <span>📸</span>
        <span>Chụp Ảnh Up FB</span>
      </button>
      <button class="cam-btn" id="focusMeBtn" title="Zoom thẳng vào nhân vật của bạn">
        <span>🎯</span>
        <span>Về Tôi</span>
      </button>
      <button class="cam-btn" id="zoomInBtn" title="Phóng to">
        <span>🔍+</span>
        <span>Phóng to</span>
      </button>
      <button class="cam-btn" id="zoomOutBtn" title="Thu nhỏ">
        <span>🔍-</span>
        <span>Thu nhỏ</span>
      </button>
      <button class="cam-btn" id="resetCamBtn" title="Xem toàn cảnh Chánh Điện">
        <span>🔄</span>
        <span>Toàn cảnh</span>
      </button>
    </div>

    <!-- Bottom Action Dock -->
    <div id="bottomDock">
      <button class="btn fortune" id="openFortuneBtn">🎋 Gieo Quẻ Bát Quái</button>
      <button class="btn gift" id="openGiftBtn">🎁 Dâng Lễ Vật</button>
      <button class="btn primary" id="openPrayBtn">✍️ Dâng Sớ Cầu Trần</button>
      <button class="btn" id="openCharBtn">👤 Nhân Vật</button>
      <button class="btn" id="ringBellBtn" title="Thỉnh Đại Hồng Chung">🔔 Chuông</button>
      <button class="btn" id="soundToggleBtn">🔊 Nhạc: Bật</button>
    </div>

    <!-- Toast Alert -->
    <div id="toast"></div>

    <!-- COMBO FEATURE 1: MODAL GIEO QUẺ BÁT QUÁI -->
    <div class="modal-backdrop" id="fortuneModal">
      <div class="modal-box" style="max-width: 480px;">
        <div class="modal-header">
          <h2>🎋 Gieo Quẻ Bát Quái Thần Tài</h2>
          <button class="close-btn" id="closeFortuneModal">&times;</button>
        </div>
        <div class="fortune-stage">
          <!-- Tube shake phase -->
          <div id="tubePhase">
            <p style="font-size:12px; color:#fef08a; margin-bottom:6px;">Chạm vào Ống Xăm để xin quẻ vận mệnh cho mã <b id="fortuneStockBadge" style="color:#f472b6;">[SSI]</b>:</p>
            <div class="tube-box" id="bambooTube">
              <div class="fortune-sticks">
                <div class="stick"></div>
                <div class="stick pop" id="mainStick"></div>
                <div class="stick"></div>
              </div>
              <div class="tube-body">
                <div class="tube-label">BÁT QUÁI THẦN TÀI</div>
              </div>
            </div>
            <button class="btn fortune" id="shakeBtn" style="font-size:12px; padding:8px 20px; margin-top:10px;">🎋 Lắc Ống Xăm Xin Quẻ</button>
          </div>

          <!-- Fortune result card phase -->
          <div class="fortune-card" id="fortuneCard">
            <div class="fortune-badge" id="fortuneNumber">QUẺ SỐ 01: THUẦN CÀN</div>
            <div class="fortune-title" id="fortuneName">RỒNG BAY VỀ TRỜI · TÍM TOÀN SÀN</div>
            <div class="fortune-poem" id="fortunePoem">
              Bò Vàng xuất trận rực hào quang,<br>
              Mã [SSI] phi nước đại ngút ngàn.<br>
              Bảng điện ngập tràn màu hoa cà,<br>
              Cổ đông ca khúc khải hoàn vang!
            </div>
            <div class="fortune-stats-grid">
              <div class="stat-pill">
                <span>Tỷ Lệ Tím Trần</span>
                <b class="purple" id="fortuneCeRate">100% CE</b>
              </div>
              <div class="stat-pill">
                <span>Vận Khí Lái Kéo</span>
                <b id="fortuneLuck">Đại Cát ⭐⭐⭐⭐⭐</b>
              </div>
              <div class="stat-pill">
                <span>Khuyên Hành Động</span>
                <b id="fortuneAdvice">Gồng Lãi Chặt</b>
              </div>
            </div>
            <div style="display:flex; gap:8px;">
              <button class="btn primary" id="copyFortuneBtn" style="flex:1;">📋 Copy Thơ Quẻ</button>
              <button class="btn" id="reFortuneBtn">🔄 Xin Quẻ Khác</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- COMBO FEATURE 2: MODAL DÂNG LỄ VẬT TÂM LINH -->
    <div class="modal-backdrop" id="giftModal">
      <div class="modal-box" style="max-width: 540px;">
        <div class="modal-header">
          <h2>🎁 Cúng Dường Lễ Vật · Cầu Cổ Phiếu Tím Trần</h2>
          <button class="close-btn" id="closeGiftModal">&times;</button>
        </div>
        <p style="font-size:11.5px; color:#d1d5db; margin-bottom:8px;">Chọn lễ vật tâm linh để dâng lên hương án Thần Chứng Khoán. Cả Chánh Điện sẽ đồng loạt quỳ lạy tiếp dẫn lộc phát!</p>
        <div class="offerings-grid" id="offeringsGrid">
          <div class="offering-card" data-gift="banana" data-merit="100" data-name="Nải Chuối Xanh Tâm Linh">
            <span class="offering-icon">🍌</span>
            <span class="offering-name">Chuối Xanh Tâm Linh</span>
            <span class="offering-desc">Danh mục một màu xanh ngát, xua tan sắc đỏ!</span>
            <span class="offering-merit">+100 Công Đức</span>
          </div>
          <div class="offering-card" data-gift="candle" data-merit="250" data-name="Cây Nến Xanh Marubozu">
            <span class="offering-icon">🕯️</span>
            <span class="offering-name">Nến Xanh Marubozu</span>
            <span class="offering-desc">Kéo nến tuần dựng đứng, thân dài không râu!</span>
            <span class="offering-merit">+250 Công Đức</span>
          </div>
          <div class="offering-card" data-gift="bull" data-merit="500" data-name="Linh Vật Bò Vàng Dát Vàng">
            <span class="offering-icon">🐂</span>
            <span class="offering-name">Bò Vàng Dát Vàng</span>
            <span class="offering-desc">Trấn yểm Gấu Đỏ, rước Bò Tím phi nước đại!</span>
            <span class="offering-merit">+500 Công Đức</span>
          </div>
          <div class="offering-card" data-gift="beer" data-merit="350" data-name="Thùng Bia Ăn Mừng CE">
            <span class="offering-icon">🍺</span>
            <span class="offering-name">Thùng Bia Mừng CE</span>
            <span class="offering-desc">Khao cả đạo tràng Chánh Điện say sưa thắng lớn!</span>
            <span class="offering-merit">+350 Công Đức</span>
          </div>
          <div class="offering-card" data-gift="incense" data-merit="1000" data-name="Nhang Trầm Khói Tím Thần Kê">
            <span class="offering-icon">📿</span>
            <span class="offering-name">Nhang Trầm Khói Tím</span>
            <span class="offering-desc">Khói tím nghi ngút, kích hoạt vạn lệnh tím trần!</span>
            <span class="offering-merit">+1000 Công Đức</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal 1: Tạo/Sửa Nhân Vật -->
    <div class="modal-backdrop" id="charModal">
      <div class="modal-box">
        <div class="modal-header">
          <h2>👤 Thiết Lập Nhân Vật Chứng Sĩ</h2>
          <button class="close-btn" id="closeCharModal">&times;</button>
        </div>
        <form id="charForm">
          <div class="form-group">
            <label>Chọn Hình Tướng / Giới Tính</label>
            <div class="avatar-selector">
              <div class="avatar-card active" data-gender="man">
                <span class="icon">🧘‍♂️</span>
                <span class="title">Nam Phật Tử</span>
              </div>
              <div class="avatar-card" data-gender="woman">
                <span class="icon">🧘‍♀️</span>
                <span class="title">Nữ Cư Sĩ</span>
              </div>
              <div class="avatar-card" data-gender="monk">
                <span class="icon">🧑‍🦲</span>
                <span class="title">Sư Thầy</span>
              </div>
              <div class="avatar-card" data-gender="granny">
                <span class="icon">👵</span>
                <span class="title">Cụ Lái Già</span>
              </div>
            </div>
          </div>

          <div class="form-group">
            <label>Pháp Danh / Tên Của Bạn</label>
            <input type="text" id="charNameInput" class="form-control" placeholder="Ví dụ: Cá Mập Đáy, Tuấn SSI, Hương HPG..." maxlength="22" required>
          </div>

          <div class="form-group">
            <label>Mã Cổ Phiếu Tâm Đắc</label>
            <input type="text" id="charStockInput" class="form-control" placeholder="Ví dụ: SSI, HPG, VND, DIG, FPT..." maxlength="8" style="text-transform: uppercase;" required>
            <div class="quick-stocks" id="charQuickStocks">
              <span class="stock-pill" data-sym="SSI">SSI</span>
              <span class="stock-pill" data-sym="HPG">HPG</span>
              <span class="stock-pill" data-sym="VND">VND</span>
              <span class="stock-pill" data-sym="DIG">DIG</span>
              <span class="stock-pill" data-sym="FPT">FPT</span>
              <span class="stock-pill" data-sym="VIX">VIX</span>
              <span class="stock-pill" data-sym="NVL">NVL</span>
              <span class="stock-pill" data-sym="PDR">PDR</span>
              <span class="stock-pill" data-sym="CEO">CEO</span>
            </div>
          </div>

          <div class="form-group">
            <label>Giá Vốn / Giá Mua (kẹp đỉnh nếu có)</label>
            <input type="number" step="0.1" id="charCostInput" class="form-control" placeholder="Ví dụ: 38.5 (nghìn đồng)">
          </div>

          <button type="submit" class="submit-btn">✨ Xác Nhận Xuất Hiện Trong Chánh Điện</button>
        </form>
      </div>
    </div>

    <!-- Modal 2: Dâng Sớ Cầu Trần -->
    <div class="modal-backdrop" id="prayModal">
      <div class="modal-box">
        <div class="modal-header">
          <h2>✍️ Dâng Sớ Cầu Trần · Đổi Vận Cổ Phiếu</h2>
          <button class="close-btn" id="closePrayModal">&times;</button>
        </div>
        <form id="prayForm">
          <div class="form-group">
            <label>Họ Tên / Pháp Danh Người Dâng</label>
            <input type="text" id="inputUser" class="form-control" placeholder="Tên của bạn..." maxlength="22" required>
          </div>
          <div class="form-group">
            <label>Mã Cổ Phiếu Cầu Nguyện</label>
            <input type="text" id="inputStock" class="form-control" placeholder="Mã CP (ví dụ: SSI, HPG, VND...)" maxlength="8" style="text-transform: uppercase;" required>
            <div class="quick-stocks" id="quickStocks">
              <span class="stock-pill" data-sym="SSI">SSI</span>
              <span class="stock-pill" data-sym="HPG">HPG</span>
              <span class="stock-pill" data-sym="VND">VND</span>
              <span class="stock-pill" data-sym="DIG">DIG</span>
              <span class="stock-pill" data-sym="FPT">FPT</span>
              <span class="stock-pill" data-sym="VIX">VIX</span>
              <span class="stock-pill" data-sym="NVL">NVL</span>
            </div>
          </div>
          <div class="form-group">
            <label>Giá Vốn Kẹp Đỉnh (nghìn đồng)</label>
            <input type="number" step="0.1" id="inputCost" class="form-control" placeholder="Ví dụ: 38.5">
          </div>
          <div class="form-group">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;">
              <label style="margin:0;">Lời Sớ Khấn (Nhúng đúng 100% mã cổ phiếu)</label>
              <button type="button" id="genWishBtn" style="background:none; border:none; color:var(--purple-ce); font-size:11px; font-weight:700; cursor:pointer;">🎲 Soạn sớ đúng mã CP</button>
            </div>
            <textarea id="inputWish" class="form-control" rows="3" required></textarea>
          </div>
          <button type="submit" class="submit-btn">🙏 Thành Tâm Dâng Sớ Lên Thần Chứng Khoán</button>
        </form>
      </div>
    </div>

    <!-- Modal 3: Facebook Capture Certificate Card -->
    <div class="modal-backdrop" id="fbModal">
      <div class="modal-box" style="max-width: 640px;">
        <div class="modal-header">
          <h2>📸 Chứng Nhận Cầu Nguyện Cổ Phiếu (Up FB)</h2>
          <button class="close-btn" id="closeFbModal">&times;</button>
        </div>
        <div class="preview-box">
          <img id="fbPreviewImg" src="" alt="Facebook Card Preview">
        </div>
        <div class="form-group">
          <label>Caption Gợi Ý Đăng Facebook (Bấm nút dưới để sao chép):</label>
          <textarea id="fbCaptionText" class="form-control" rows="3" readonly></textarea>
        </div>
        <div class="fb-actions">
          <button class="btn primary" id="downloadCardBtn">📥 Tải Ảnh Về Máy</button>
          <button class="btn" id="copyFbCaptionBtn">📋 Copy Caption + Hashtags</button>
        </div>
      </div>
    </div>

  </div>
</div>

<script>
/* ==========================================================
   ENGINE CORE SETUP & CANAVS (16:9 Landscape)
   ========================================================== */
const canvas = document.getElementById('c');
const ctx = canvas.getContext('2d');
const SW = 1920;
const SH = 1080;

const A = {};
const ASSETS = {
  hall: 'assets/stock_temple_hall_169.jpg',
  bull: 'assets/golden_bull_mascot.jpg',
  anim_man: 'assets/anim_man.png',
  anim_woman: 'assets/anim_woman.png',
  anim_granny: 'assets/anim_granny.png',
  c_man: 'assets/c_man.png',
  c_woman: 'assets/c_woman.png',
  c_nun: 'assets/c_nun.png',
  c_monk: 'assets/c_monk.png',
  fx_bell: 'assets/fx_bell.png',
  fx_halo: 'assets/fx_halo.png',
  fx_lotus: 'assets/fx_lotus.png',
  fx_mo: 'assets/fx_mo.png',
  fx_petal: 'assets/fx_petal.png'
};

let loadedCount = 0;
const totalAssets = Object.keys(ASSETS).length;
for (const [k, src] of Object.entries(ASSETS)) {
  const img = new Image();
  img.src = src;
  img.onload = () => { loadedCount++; };
  img.onerror = () => { loadedCount++; };
  A[k] = img;
}

/* ==========================================================
   STOCK MARKET DATA (16 Symbols Across Sectors)
   ========================================================== */
const MARKET_STOCKS = [
  { sym: 'SSI', ref: 40.00, cur: 42.80, chg: 7.0, cat: 'chungkhoan', status: 'Dư mua trần CE', vol: '28.4M' },
  { sym: 'HPG', ref: 31.00, cur: 33.15, chg: 6.9, cat: 'bds', status: 'Kéo cực mạnh', vol: '42.1M' },
  { sym: 'VND', ref: 23.80, cur: 25.45, chg: 6.9, cat: 'chungkhoan', status: 'Dư mua trần', vol: '18.9M' },
  { sym: 'DIG', ref: 33.70, cur: 36.05, chg: 7.0, cat: 'bds', status: 'Tím rực rỡ', vol: '15.6M' },
  { sym: 'FPT', ref: 142.00, cur: 151.90, chg: 7.0, cat: 'chungkhoan', status: 'Vượt đỉnh', vol: '8.4M' },
  { sym: 'VIX', ref: 20.20, cur: 21.60, chg: 6.9, cat: 'chungkhoan', status: 'Dư mua trần', vol: '31.2M' },
  { sym: 'NVL', ref: 14.20, cur: 15.15, chg: 6.7, cat: 'bds', status: 'Giải cứu trần', vol: '22.0M' },
  { sym: 'PDR', ref: 27.50, cur: 29.40, chg: 6.9, cat: 'bds', status: 'Tím trần', vol: '11.3M' },
  { sym: 'CEO', ref: 21.00, cur: 23.10, chg: 10.0, cat: 'bds', status: 'CE HNX', vol: '9.8M' },
  { sym: 'VHM', ref: 45.00, cur: 47.80, chg: 6.2, cat: 'bds', status: 'Cá mập gom', vol: '14.2M' },
  { sym: 'VIC', ref: 44.50, cur: 47.20, chg: 6.1, cat: 'bds', status: 'Trụ kéo', vol: '7.8M' },
  { sym: 'TCB', ref: 25.00, cur: 26.75, chg: 7.0, cat: 'nganhang', status: 'Dư mua trần', vol: '19.5M' },
  { sym: 'MBB', ref: 24.80, cur: 26.40, chg: 6.5, cat: 'nganhang', status: 'Kéo ATC', vol: '21.0M' },
  { sym: 'STB', ref: 32.50, cur: 34.75, chg: 6.9, cat: 'nganhang', status: 'Về bờ', vol: '16.7M' },
  { sym: 'MWG', ref: 68.00, cur: 72.50, chg: 6.6, cat: 'bds', status: 'Khối ngoại múc', vol: '8.1M' },
  { sym: 'VCI', ref: 48.00, cur: 51.30, chg: 6.9, cat: 'chungkhoan', status: 'Dư mua trần', vol: '10.4M' }
];

function populateTickerTrack() {
  const track = document.getElementById('tickerTrack');
  const items = [...MARKET_STOCKS, ...MARKET_STOCKS].map(s => {
    return `<div class="tape-item ce" onclick="openPrayForStock('${s.sym}')">
      <b>${s.sym}</b> ${s.cur.toFixed(2)} (+${s.chg.toFixed(1)}% CE)
    </div>`;
  }).join(' ✦ ');
  track.innerHTML = items;
}
populateTickerTrack();

/* ==========================================================
   BÁT QUÁI BẢNG ĐIỆN PANEL
   ========================================================== */
let activeTab = 'all';

function renderStockBoard() {
  const container = document.getElementById('stockListContainer');
  const filtered = activeTab === 'all' ? MARKET_STOCKS :
                   activeTab === 'ce' ? MARKET_STOCKS.filter(s => s.chg >= 6.8) :
                   MARKET_STOCKS.filter(s => s.cat === activeTab);

  container.innerHTML = filtered.map(s => {
    return `
      <div class="stock-row">
        <span class="stock-sym">${s.sym}</span>
        <span style="color:var(--yellow-ref);">${s.ref.toFixed(2)}</span>
        <span class="stock-price ce">${s.cur.toFixed(2)}</span>
        <span class="stock-price ce">+${s.chg.toFixed(1)}%</span>
        <span style="font-size:9.5px; color:#cbd5e1; overflow:hidden; text-overflow:ellipsis; white-space:nowrap;">${s.status}</span>
        <button class="stock-act-btn" onclick="openPrayForStock('${s.sym}')">Dâng Sớ</button>
      </div>
    `;
  }).join('');
}
renderStockBoard();

document.getElementById('boardTabs').addEventListener('click', e => {
  const btn = e.target.closest('.board-tab');
  if (!btn) return;
  document.querySelectorAll('#boardTabs .board-tab').forEach(b => b.classList.remove('active'));
  btn.classList.add('active');
  activeTab = btn.dataset.filter;
  renderStockBoard();
});

const stockBoardPanel = document.getElementById('stockBoardPanel');
const toggleBoardBtn = document.getElementById('toggleBoardBtn');
const closeBoardBtn = document.getElementById('closeBoardBtn');

toggleBoardBtn.addEventListener('click', () => {
  stockBoardPanel.classList.toggle('collapsed');
});
closeBoardBtn.addEventListener('click', () => {
  stockBoardPanel.classList.add('collapsed');
});

// Ép Toàn Sàn Tím Trần
document.getElementById('forceCeBtn').addEventListener('click', () => {
  MARKET_STOCKS.forEach(s => {
    s.cur = +(s.ref * 1.07).toFixed(2);
    s.chg = 7.0;
    s.status = 'Dư mua trần CE';
  });
  renderStockBoard();
  populateTickerTrack();
  playBell(true);
  triggerDanmaku('🟣 TOÀN BỘ BẢNG ĐIỆN ĐÃ ĐƯỢC ÉP TÍM TRẦN! VẠN LỆNH TÍM!', true);
  showToast('🟣 Vạn Lệnh Tím Trần! Toàn bộ bảng điện đã rực sắc tím Thần Tài!');
});

/* ==========================================================
   USER IDENTITY & PROFILE
   ========================================================== */
let currentUser = {
  name: 'Cá Mập Đáy',
  gender: 'man',
  stock: 'SSI',
  cost: 38.5,
  wish: 'Cầu cho mã [SSI] tím 7 cây liên tiếp, khối ngoại ngừng xả ròng, dòng tiền lớn kéo thốc về bờ!',
  merit: 515
};

try {
  const saved = localStorage.getItem('user_profile_stock_temple');
  if (saved) {
    currentUser = { ...currentUser, ...JSON.parse(saved) };
  }
} catch (e) {}

function saveUserProfile() {
  try {
    localStorage.setItem('user_profile_stock_temple', JSON.stringify(currentUser));
  } catch (e) {}
  updateUserBadge();
  updateMeritDisplay();
}

function updateUserBadge() {
  const badgeName = document.getElementById('userBadgeName');
  const badgeIcon = document.getElementById('userBadgeIcon');
  if (badgeName) badgeName.innerHTML = `BẠN: <b>${currentUser.name} [${currentUser.stock}]</b>`;
  if (badgeIcon) badgeIcon.textContent = currentUser.gender === 'woman' ? '🧘‍♀️' : currentUser.gender === 'monk' ? '🧑‍🦲' : currentUser.gender === 'granny' ? '👵' : '🧘‍♂️';
  const fortuneBadge = document.getElementById('fortuneStockBadge');
  if (fortuneBadge) fortuneBadge.textContent = `[${currentUser.stock}]`;
}
updateUserBadge();

/* ==========================================================
   CAMERA TRANSFORMS (ZOOM & PAN)
   ========================================================== */
const camera = {
  zoom: 1.0,
  targetZoom: 1.0,
  minZoom: 1.0,
  maxZoom: 3.5,
  x: 0,
  y: 0,
  targetX: 0,
  targetY: 0,
  isDragging: false,
  dragStartX: 0,
  dragStartY: 0,
  camStartX: 0,
  camStartY: 0
};

function clampCamera() {
  const z = camera.targetZoom;
  const minX = -(z - 1) * SW;
  const minY = -(z - 1) * SH;
  camera.targetX = Math.min(0, Math.max(minX, camera.targetX));
  camera.targetY = Math.min(0, Math.max(minY, camera.targetY));
}

const stage = document.getElementById('stage');

stage.addEventListener('wheel', e => {
  e.preventDefault();
  const rect = stage.getBoundingClientRect();
  const mouseScreenX = (e.clientX - rect.left) * (SW / rect.width);
  const mouseScreenY = (e.clientY - rect.top) * (SH / rect.height);

  const zoomFactor = e.deltaY < 0 ? 1.18 : 1 / 1.18;
  const oldZoom = camera.targetZoom;
  camera.targetZoom = Math.min(camera.maxZoom, Math.max(camera.minZoom, camera.targetZoom * zoomFactor));

  if (camera.targetZoom <= 1.01) {
    camera.targetZoom = 1.0;
    camera.targetX = 0;
    camera.targetY = 0;
  } else {
    const scaleChange = camera.targetZoom / oldZoom;
    camera.targetX = mouseScreenX - (mouseScreenX - camera.targetX) * scaleChange;
    camera.targetY = mouseScreenY - (mouseScreenY - camera.targetY) * scaleChange;
    clampCamera();
  }
}, { passive: false });

stage.addEventListener('mousedown', e => {
  if (e.target.closest('.hud') || e.target.closest('#camToolbar') || e.target.closest('#stockBoardPanel') || e.target.closest('#fishWidget') || e.target.closest('#quickPrayerBar') || e.target.closest('#royalMeritBanner') || e.target.closest('#emoteBar')) return;
  camera.isDragging = true;
  stage.classList.add('grabbing');
  camera.dragStartX = e.clientX;
  camera.dragStartY = e.clientY;
  camera.camStartX = camera.targetX;
  camera.camStartY = camera.targetY;
});

window.addEventListener('mousemove', e => {
  if (!camera.isDragging) return;
  const rect = stage.getBoundingClientRect();
  const dx = (e.clientX - camera.dragStartX) * (SW / rect.width);
  const dy = (e.clientY - camera.dragStartY) * (SH / rect.height);
  camera.targetX = camera.camStartX + dx;
  camera.targetY = camera.camStartY + dy;
  clampCamera();
});

window.addEventListener('mouseup', () => {
  camera.isDragging = false;
  stage.classList.remove('grabbing');
});

document.getElementById('zoomInBtn').addEventListener('click', () => {
  const oldZoom = camera.targetZoom;
  camera.targetZoom = Math.min(camera.maxZoom, camera.targetZoom * 1.3);
  const scaleChange = camera.targetZoom / oldZoom;
  camera.targetX = SW / 2 - (SW / 2 - camera.targetX) * scaleChange;
  camera.targetY = SH / 2 - (SH / 2 - camera.targetY) * scaleChange;
  clampCamera();
});

document.getElementById('zoomOutBtn').addEventListener('click', () => {
  const oldZoom = camera.targetZoom;
  camera.targetZoom = Math.max(camera.minZoom, camera.targetZoom / 1.3);
  if (camera.targetZoom <= 1.01) {
    camera.targetZoom = 1.0;
    camera.targetX = 0;
    camera.targetY = 0;
  } else {
    const scaleChange = camera.targetZoom / oldZoom;
    camera.targetX = SW / 2 - (SW / 2 - camera.targetX) * scaleChange;
    camera.targetY = SH / 2 - (SH / 2 - camera.targetY) * scaleChange;
    clampCamera();
  }
});

document.getElementById('resetCamBtn').addEventListener('click', () => {
  camera.targetZoom = 1.0;
  camera.targetX = 0;
  camera.targetY = 0;
});

function focusOnUser() {
  const userVis = visitors.find(v => v.isUser);
  if (!userVis) return;
  camera.targetZoom = 2.4;
  camera.targetX = SW / 2 - userVis.x * camera.targetZoom;
  camera.targetY = SH * 0.6 - userVis.y * camera.targetZoom;
  clampCamera();
  showToast(`🎯 Đang tiêu điểm vào chứng sĩ [${currentUser.name}]`);
}
document.getElementById('focusMeBtn').addEventListener('click', focusOnUser);

/* ==========================================================
   24 BỒ ĐOÀN SEN VÀNG & SEATING GRID
   ========================================================== */
const FLOOR = { yTop: 880, yBot: 1045, halfTop: 360, halfBot: 740 };
let seats = [];

function layoutSeats() {
  seats = [];
  const rows = 4;
  const cols = 6;
  for (let r = 0; r < rows; r++) {
    const t = rows === 1 ? 0.5 : r / (rows - 1);
    const y = FLOOR.yTop + (FLOOR.yBot - FLOOR.yTop) * t;
    const half = FLOOR.halfTop + (FLOOR.halfBot - FLOOR.halfTop) * t;
    const scale = (0.24 + 0.18 * t);
    for (let k = 0; k < cols; k++) {
      let u = (k - (cols - 1) / 2) / ((cols - 1) / 2);
      u = Math.sign(u || 1) * (0.18 + 0.82 * Math.abs(u));
      const x = 960 + u * half;
      seats.push({ x, y, scale, r, k, taken: null });
    }
  }
  seats.sort((a, b) => (b.r - a.r) || (Math.abs(a.x - 960) - Math.abs(b.x - 960)));
}
layoutSeats();

function freeSeat() {
  return seats.find(s => !s.taken) || null;
}

/* ==========================================================
   CHANTING DAIS & 3 HIGH MASTERS
   ========================================================== */
const HIGH_MASTERS = [
  { id: 'left', name: 'Thầy Khấn CE', title: '📿 Thầy Khấn CE', x: 740, y: 840, scale: 0.28, role: 'chant', skin: 'c_monk', flip: false },
  { id: 'center', name: 'Cụ Lái Trưởng', title: '🏛️ [SƯ TRỤ TRÌ] Cụ Lái Trưởng', x: 960, y: 845, scale: 0.32, role: 'abbot', skin: 'c_monk', flip: false },
  { id: 'right', name: 'Đại Sư Về Bờ', title: '🔔 Đại Sư Về Bờ', x: 1180, y: 840, scale: 0.28, role: 'bell', skin: 'c_monk', flip: true }
];

/* ==========================================================
   DEVOTEE SPRITE & ANIMATION SYSTEM
   ========================================================== */
const visitors = [];
const floaters = [];
const activeOfferings = []; // offerings sitting on altar desk
let screenShake = 0;

function addVisitor(name, stock, gender, instant = false, isUser = false) {
  const primeSeat = seats.find(s => s.r === 3 && (s.k === 2 || s.k === 3) && !s.taken) ||
                    seats.find(s => s.r === 2 && (s.k === 2 || s.k === 3) && !s.taken) ||
                    freeSeat();
  const seat = isUser ? primeSeat : freeSeat();
  if (!seat) return null;

  const skin = gender === 'woman' ? 'c_woman' :
               gender === 'granny' ? 'c_nun' :
               gender === 'monk' ? 'c_monk' : 'c_man';

  const v = {
    name,
    stock,
    gender,
    skin,
    seat,
    x: instant ? seat.x : 960,
    y: instant ? seat.y : 1080,
    state: instant ? 'sit' : 'walk',
    speed: 120 + Math.random() * 30,
    animFrame: Math.floor(Math.random() * 12),
    frameTimer: 0,
    glow: isUser ? 1.0 : 0,
    bow: 0,
    isUser,
    bubble: null,
    flip: seat.x > 960
  };

  seat.taken = v;
  visitors.push(v);
  return v;
}

function spawnOrUpdateUserVisitor() {
  const existingIdx = visitors.findIndex(v => v.isUser);
  if (existingIdx >= 0) {
    const old = visitors[existingIdx];
    if (old.seat) old.seat.taken = null;
    visitors.splice(existingIdx, 1);
  }
  const v = addVisitor(currentUser.name, currentUser.stock, currentUser.gender, true, true);
  if (v) {
    v.bubble = {
      text: currentUser.wish,
      until: performance.now() + 6000
    };
  }
}

spawnOrUpdateUserVisitor();

const DEMO_DEVOTEES = [
  { name: 'Chiến Thần F0', stock: 'HPG', gender: 'man' },
  { name: 'Thích Bắt Đáy', stock: 'VND', gender: 'man' },
  { name: 'Cô Bé Gồng Lãi', stock: 'DIG', gender: 'woman' },
  { name: 'Nữ Hoàng Về Bờ', stock: 'FPT', gender: 'woman' },
  { name: 'Tín Đồ Bò Tím', stock: 'NVL', gender: 'man' },
  { name: 'Cao Tăng Lướt Sóng', stock: 'VIX', gender: 'monk' },
  { name: 'Đại Ca Cá Mập', stock: 'TCB', gender: 'man' },
  { name: 'Mẹ Bỉm Margin', stock: 'PDR', gender: 'woman' },
  { name: 'Thầy Cúng CE', stock: 'CEO', gender: 'monk' },
  { name: 'Tu sĩ Bò Tót', stock: 'VHM', gender: 'man' },
  { name: 'Tiểu Thư Chứng Sĩ', stock: 'VIC', gender: 'woman' },
  { name: 'Cư Sĩ Tím Lịm', stock: 'STB', gender: 'man' },
  { name: 'Đạo Tràng Cổ Đông', stock: 'MWG', gender: 'man' },
  { name: 'Ni Cô Gỡ Lỗ', stock: 'VCI', gender: 'woman' },
  { name: 'Cụ Ông Bắt Đáy', stock: 'MBB', gender: 'granny' }
];

DEMO_DEVOTEES.forEach(d => {
  addVisitor(d.name, d.stock, d.gender, true, false);
});

/* ==========================================================
   AUDIO SYNTHESIZER (Mõ, Chuông, Tiếng Sấm, Gieo Quẻ)
   ========================================================== */
let audioCtx = null;
let soundEnabled = true;

function audioStart() {
  if (!audioCtx) {
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  }
  if (audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
}

function playMok() {
  if (!soundEnabled) return;
  audioStart();
  const t = audioCtx.currentTime;

  const osc1 = audioCtx.createOscillator();
  const gain1 = audioCtx.createGain();
  osc1.type = 'sine';
  osc1.frequency.setValueAtTime(840, t);
  osc1.frequency.exponentialRampToValueAtTime(320, t + 0.08);
  gain1.gain.setValueAtTime(0.85, t);
  gain1.gain.exponentialRampToValueAtTime(0.001, t + 0.12);
  osc1.connect(gain1);
  gain1.connect(audioCtx.destination);
  osc1.start(t);
  osc1.stop(t + 0.13);

  const osc2 = audioCtx.createOscillator();
  const gain2 = audioCtx.createGain();
  osc2.type = 'triangle';
  osc2.frequency.setValueAtTime(420, t);
  osc2.frequency.exponentialRampToValueAtTime(180, t + 0.14);
  gain2.gain.setValueAtTime(0.45, t);
  gain2.gain.exponentialRampToValueAtTime(0.001, t + 0.15);
  osc2.connect(gain2);
  gain2.connect(audioCtx.destination);
  osc2.start(t);
  osc2.stop(t + 0.16);
}

function playBell(deep = false) {
  if (!soundEnabled) return;
  audioStart();
  const t = audioCtx.currentTime;
  const freqs = deep ? [196, 392, 587, 880] : [330, 660, 990, 1320];
  freqs.forEach((f, i) => {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    osc.type = 'sine';
    osc.frequency.setValueAtTime(f, t);
    const dur = 3.5 - i * 0.5;
    gain.gain.setValueAtTime(0.3 / (i + 1), t);
    gain.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start(t);
    osc.stop(t + dur);
  });
}

function playBambooShake() {
  if (!soundEnabled) return;
  audioStart();
  for (let i = 0; i < 4; i++) {
    setTimeout(() => {
      if (!audioCtx) return;
      const t = audioCtx.currentTime;
      const osc = audioCtx.createOscillator();
      const gain = audioCtx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(400 + Math.random() * 200, t);
      gain.gain.setValueAtTime(0.2, t);
      gain.gain.exponentialRampToValueAtTime(0.001, t + 0.04);
      osc.connect(gain);
      gain.connect(audioCtx.destination);
      osc.start(t);
      osc.stop(t + 0.05);
    }, i * 90);
  }
}

function playThunder() {
  if (!soundEnabled) return;
  audioStart();
  const t = audioCtx.currentTime;
  const osc = audioCtx.createOscillator();
  const gain = audioCtx.createGain();
  osc.type = 'sawtooth';
  osc.frequency.setValueAtTime(80, t);
  osc.frequency.exponentialRampToValueAtTime(30, t + 0.4);
  gain.gain.setValueAtTime(0.4, t);
  gain.gain.exponentialRampToValueAtTime(0.001, t + 0.5);
  osc.connect(gain);
  gain.connect(audioCtx.destination);
  osc.start(t);
  osc.stop(t + 0.55);
}

/* ==========================================================
   INTERACTIVE BIG MÕ GỖ & AUTO-MÕ LO-FI (FEATURE 3)
   ========================================================== */
let userMerit = currentUser.merit || 515;
let commMerit = 88376;
let currentMargin = 35;
let knockCombo = 0;
let comboTimeout = null;
let autoZenInterval = null;

function updateMeritDisplay() {
  document.getElementById('userMeritVal').textContent = userMerit.toLocaleString();
  document.getElementById('commMeritVal').textContent = commMerit.toLocaleString();
  document.getElementById('marginVal').textContent = `${Math.max(0, currentMargin)}% (${currentMargin <= 20 ? 'Tuyệt đối an toàn' : 'An toàn'})`;
}
updateMeritDisplay();

function knockWoodFish() {
  playMok();
  userMerit++;
  commMerit++;
  if (currentMargin > 0 && Math.random() < 0.3) currentMargin--;
  currentUser.merit = userMerit;
  saveUserProfile();

  const fishWidget = document.getElementById('fishWidget');
  fishWidget.classList.add('knock');
  setTimeout(() => fishWidget.classList.remove('knock'), 120);

  visitors.forEach(v => { v.bow = 0.3; });

  knockCombo++;
  clearTimeout(comboTimeout);
  comboTimeout = setTimeout(() => { knockCombo = 0; }, 1800);

  const perks = [
    '+1 CÔNG ĐỨC',
    '-1% MARGIN',
    '🟣 VẠN LỆNH TÍM TRẦN',
    '🚀 LÁI KÉO VỀ BỜ',
    '✦ TÂM AN LỘC PHÁT',
    '✦ KHỐI NGOẠI GOM HÀNG'
  ];
  const text = knockCombo >= 10 ? `🔥 COMBO X${knockCombo}: ĐẠI THÀNH TÂM! TÍM RỰC RỠ!` : perks[Math.floor(Math.random() * perks.length)];

  floaters.push({
    x: 960 + (Math.random() - 0.5) * 120,
    y: 860,
    vx: (Math.random() - 0.5) * 30,
    vy: -70 - Math.random() * 40,
    s: 1.0,
    rot: 0,
    vr: 0,
    alpha: 1.0,
    kind: 'text',
    text
  });

  const userVis = visitors.find(v => v.isUser);
  if (userVis && Math.random() < 0.35) {
    userVis.bubble = {
      text: `Cốc! Xả Margin [${currentUser.stock}], tâm an vạn sự thông!`,
      until: performance.now() + 3000
    };
  }
}

document.getElementById('fishWidget').addEventListener('click', e => {
  if (e.target.closest('#autoZenBtn')) return;
  knockWoodFish();
});

window.addEventListener('keydown', e => {
  if (e.code === 'Space' && e.target.tagName !== 'INPUT' && e.target.tagName !== 'TEXTAREA') {
    e.preventDefault();
    knockWoodFish();
  }
});

// Auto-Mõ Lo-fi Toggle
const autoZenBtn = document.getElementById('autoZenBtn');
autoZenBtn.addEventListener('click', e => {
  e.stopPropagation();
  if (autoZenInterval) {
    clearInterval(autoZenInterval);
    autoZenInterval = null;
    autoZenBtn.classList.remove('active');
    autoZenBtn.textContent = '🎧 Auto-Mõ: TẮT';
    showToast('⏸️ Đã tắt chế độ Auto-Mõ thiền.');
  } else {
    autoZenInterval = setInterval(() => {
      knockWoodFish();
    }, 1200);
    autoZenBtn.classList.add('active');
    autoZenBtn.textContent = '🎧 Auto-Mõ: BẬT';
    showToast('🧘 Đã kích hoạt Auto-Mõ Thiền Lo-fi! Thư giãn xả margin tự động.');
  }
});

document.getElementById('ringBellBtn').addEventListener('click', () => {
  playBell(true);
  triggerDanmaku('🔔 Tiếng Đại Hồng Chung ngân vang! Vạn chứng sĩ đồng tâm cầu tím trần!', true);
  showToast('🔔 Boong... Tiếng chuông Chánh Điện cầu tàu về bờ ngân vang!');
});

document.getElementById('soundToggleBtn').addEventListener('click', e => {
  soundEnabled = !soundEnabled;
  e.target.textContent = soundEnabled ? '🔊 Nhạc: Bật' : '🔇 Nhạc: Tắt';
});

/* ==========================================================
   COMBO FEATURE 3: LIVE EMOTE BURSTS
   ========================================================== */
function spawnHeartBurst() {
  audioStart();
  playMok();
  const userVis = visitors.find(v => v.isUser);
  const ox = userVis ? userVis.x : 960;
  const oy = userVis ? userVis.y - 40 : 800;

  for (let i = 0; i < 22; i++) {
    floaters.push({
      x: ox + (Math.random() - 0.5) * 40,
      y: oy,
      vx: (Math.random() - 0.5) * 160,
      vy: -120 - Math.random() * 140,
      s: 0.6 + Math.random() * 0.7,
      rot: (Math.random() - 0.5) * 0.5,
      vr: (Math.random() - 0.5) * 2,
      alpha: 1.0,
      kind: 'heart'
    });
  }
  triggerDanmaku(`🟣 [BÃO TIM] ${currentUser.name} thả tim tím chúc [${currentUser.stock}] CE cứng cựa!`, true);
  showToast('🟣 Bão Tim Tím đã phủ kín Chánh Điện!');
}

function spawnGoldCoins() {
  audioStart();
  playBell(false);
  for (let i = 0; i < 35; i++) {
    floaters.push({
      x: Math.random() * SW,
      y: -20 - Math.random() * 150,
      vx: (Math.random() - 0.5) * 40,
      vy: 180 + Math.random() * 220,
      s: 0.7 + Math.random() * 0.8,
      rot: Math.random() * 6,
      vr: 3 + Math.random() * 4,
      alpha: 1.0,
      kind: 'coin'
    });
  }
  userMerit += 50;
  updateMeritDisplay();
  triggerDanmaku(`💰 [MƯA VÀNG] Lộc phát tràn trề, chúc cả phòng gồng lãi đại thắng!`, true);
  showToast('💰 Cơn mưa tiền vàng lộc phát đã đổ xuống!');
}

function spawnMiniBulls() {
  audioStart();
  playBell(false);
  for (let i = 0; i < 5; i++) {
    setTimeout(() => {
      floaters.push({
        x: -80,
        y: 880 + Math.random() * 120,
        vx: 380 + Math.random() * 100,
        vy: 0,
        s: 0.45 + Math.random() * 0.2,
        rot: 0,
        vr: 0,
        alpha: 1.0,
        kind: 'bull_runner'
      });
    }, i * 280);
  }
  triggerDanmaku(`🐂 [BÒ VÀNG XUẤT TRẬN] Đàn bò vàng mini húc bay phe gấu!`, true);
  showToast('🐂 Đàn Bò Vàng mini đang phi nước đại qua sàn!');
}

function triggerLightningCe() {
  playThunder();
  screenShake = 14;
  floaters.push({ kind: 'lightning_flash', alpha: 0.55 });
  triggerDanmaku('⚡ [SẤM SÉT TRẦN] Luồng năng lượng CE giáng thế! Toàn bộ bảng điện rực tím!', true);
  showToast('⚡ Sấm Sét Tím Trần giáng xuống! Đánh tan áp lực bán tháo!');
}

document.getElementById('emoteHeartBtn').addEventListener('click', spawnHeartBurst);
document.getElementById('emoteGoldBtn').addEventListener('click', spawnGoldCoins);
document.getElementById('emoteBullBtn').addEventListener('click', spawnMiniBulls);
document.getElementById('emoteBoltBtn').addEventListener('click', triggerLightningCe);

/* ==========================================================
   COMBO FEATURE 1: ỐNG XĂM GIEO QUẺ BÁT QUÁI ENGINE
   ========================================================== */
const fortuneModal = document.getElementById('fortuneModal');
const openFortuneBtn = document.getElementById('openFortuneBtn');
const closeFortuneModal = document.getElementById('closeFortuneModal');
const bambooTube = document.getElementById('bambooTube');
const shakeBtn = document.getElementById('shakeBtn');
const tubePhase = document.getElementById('tubePhase');
const fortuneCard = document.getElementById('fortuneCard');
const copyFortuneBtn = document.getElementById('copyFortuneBtn');
const reFortuneBtn = document.getElementById('reFortuneBtn');

const FORTUNE_POEMS = [
  {
    num: 'QUẺ SỐ 01: THUẦN CÀN',
    name: 'RỒNG BAY VỀ TRỜI · TÍM TOÀN SÀN',
    rate: '100% CE',
    luck: 'Đại Phú Quý ⭐⭐⭐⭐⭐',
    advice: 'Gồng Lãi Chặt',
    poem: (s) => `Bò Vàng xuất trận rực hào quang,\nMã [${s}] phi nước đại ngút ngàn.\nBảng điện ngập tràn màu hoa cà,\nCổ đông ca khúc khải hoàn vang!`
  },
  {
    num: 'QUẺ SỐ 14: HỎA THIÊN ĐẠI HỮU',
    name: 'ĐẠI PHÚ ĐẠI QUÝ · TIỀN VÀO NHƯ NƯỚC',
    rate: '96% CE',
    luck: 'Vạn Sự Hanh Thông ⭐⭐⭐⭐⭐',
    advice: 'Nắm Chắc Hàng',
    poem: (s) => `Thiên thời địa lợi hợp nhân hòa,\n[${s}] tiền lớn múc xông pha.\nDư mua triệu cổ trần cứng ngắc,\nTài lộc đong đầy khắp mọi nhà!`
  },
  {
    num: 'QUẺ SỐ 35: HỎA ĐỊA TẤN',
    name: 'RÚT CHÂN THẦN THÁNH · RŨ HẾT CHIM LỢN',
    rate: '92% CE',
    luck: 'Đảo Chiều Cực Mạnh ⭐⭐⭐⭐',
    advice: 'Không Bán Rẻ',
    poem: (s) => `Sáng sớm rung lắc rũ chim lợn,\nChiều về lái kéo nến căng tròn.\nRút chân chữ V kinh điển nhất,\nVững tay chèo lái lộc trường tồn!`
  },
  {
    num: 'QUẺ SỐ 11: ĐỊA THIÊN THÁI',
    name: 'THỜI VẬN HANH THÔNG · PHÁ MỌI KHÁNG CỰ',
    rate: '95% CE',
    luck: 'Phá Đỉnh Cũ ⭐⭐⭐⭐⭐',
    advice: 'Gia Tăng Tỷ Trọng',
    poem: (s) => `Qua cơn bĩ cực tới hồi thái,\n[${s}] bứt phá đỉnh tương lai.\nCản dày cản mỏng đều xuyên thủng,\nVề bờ nhân bội túi tiền tài!`
  },
  {
    num: 'QUẺ SỐ 24: ĐỊA LÔI PHỤC',
    name: 'ĐẢO CHIỀU TẠO ĐÁY · BẬT DẬY NHƯ LÒ XO',
    rate: '89% CE',
    luck: 'Bắt Đáy Trúng ⭐⭐⭐⭐',
    advice: 'Kiên Trì Chờ Đợi',
    poem: (s) => `Tạo đáy hai đáy nén lò xo,\nBung nóc phiên nay hết lắng lo.\nKhối ngoại quay xe ngừng xả rác,\nLệnh mua quét sạch bảng điện to!`
  },
  {
    num: 'QUẺ SỐ 43: TRẠCH THIÊN QUẢI',
    name: 'QUYẾT TỬ GỒNG LÃI · SIÊU CỔ VÀO GUỒNG',
    rate: '98% CE',
    luck: 'Siêu Chu Kỳ ⭐⭐⭐⭐⭐',
    advice: 'Khóa Chặt Tài Khoản',
    poem: (s) => `Siêu cổ vào guồng sóng đại dương,\n[${s}] ngạo nghễ khắp thương trường.\nAi bán mất hàng ngồi tiếc nuối,\nTa cười rạng rỡ đếm tiền lương!`
  },
  {
    num: 'QUẺ SỐ 64: HỎA THỦY VỊ TẾ',
    name: 'TÂM AN VÔ VI · XẢ SẠCH MARGIN',
    rate: '85% CE',
    luck: 'Bình An Đại Cát ⭐⭐⭐⭐',
    advice: 'Tắt App Đi Cafe',
    poem: (s) => `Thị trường biến động mặc phong vân,\nGõ mõ buông lơi mối nợ nần.\nTâm tĩnh lộc tự nhiên tìm đến,\nTím trần sẽ gõ cửa người thân!`
  }
];

let lastFortuneText = '';

function startShakeFortune() {
  audioStart();
  bambooTube.classList.add('shaking');
  shakeBtn.disabled = true;
  shakeBtn.textContent = '🎋 Đang thỉnh quẻ từ Thần...';
  playBambooShake();

  setTimeout(() => {
    bambooTube.classList.remove('shaking');
    const pick = FORTUNE_POEMS[Math.floor(Math.random() * FORTUNE_POEMS.length)];
    const poemTxt = pick.poem(currentUser.stock);

    document.getElementById('fortuneNumber').textContent = pick.num;
    document.getElementById('fortuneName').textContent = pick.name;
    document.getElementById('fortunePoem').innerHTML = poemTxt.replace(/\n/g, '<br>');
    document.getElementById('fortuneCeRate').textContent = pick.rate;
    document.getElementById('fortuneLuck').textContent = pick.luck;
    document.getElementById('fortuneAdvice').textContent = pick.advice;

    lastFortuneText = `🎋 [QUẺ BÁT QUÁI THẦN TÀI: ${pick.name}]\nChiếu mệnh mã: #${currentUser.stock}\n\n${poemTxt}\n\nTỷ lệ Tím: ${pick.rate} | Lời khuyên: ${pick.advice}\n#ChanhDienChungKhoan #GieoQueBatQuai #${currentUser.stock}`;

    tubePhase.style.display = 'none';
    fortuneCard.style.display = 'block';
    shakeBtn.disabled = false;
    shakeBtn.textContent = '🎋 Lắc Ống Xăm Xin Quẻ';

    playBell(true);
    visitors.forEach(v => { v.bow = 0.6; });

    const userVis = visitors.find(v => v.isUser);
    if (userVis) {
      userVis.bubble = { text: `🎋 Đã rút được [${pick.name}]!`, until: performance.now() + 6000 };
    }

    triggerDanmaku(`🎋 [GIEO QUẺ] ${currentUser.name} vừa rút được "${pick.name}" cho mã [${currentUser.stock}]!`, true);
  }, 900);
}

openFortuneBtn.addEventListener('click', () => {
  tubePhase.style.display = 'block';
  fortuneCard.style.display = 'none';
  document.getElementById('fortuneStockBadge').textContent = `[${currentUser.stock}]`;
  fortuneModal.classList.add('active');
});

closeFortuneModal.addEventListener('click', () => fortuneModal.classList.remove('active'));
bambooTube.addEventListener('click', startShakeFortune);
shakeBtn.addEventListener('click', startShakeFortune);

reFortuneBtn.addEventListener('click', () => {
  tubePhase.style.display = 'block';
  fortuneCard.style.display = 'none';
  startShakeFortune();
});

copyFortuneBtn.addEventListener('click', () => {
  navigator.clipboard.writeText(lastFortuneText).then(() => {
    showToast('📋 Đã copy Thơ Quẻ may mắn vào Clipboard!');
  }).catch(() => {
    showToast('📋 Đã copy Thơ Quẻ!');
  });
});

/* ==========================================================
   COMBO FEATURE 2: DÂNG LỄ VẬT TÂM LINH ENGINE
   ========================================================== */
const giftModal = document.getElementById('giftModal');
const openGiftBtn = document.getElementById('openGiftBtn');
const closeGiftModal = document.getElementById('closeGiftModal');

openGiftBtn.addEventListener('click', () => {
  giftModal.classList.add('active');
});
closeGiftModal.addEventListener('click', () => giftModal.classList.remove('active'));

document.getElementById('offeringsGrid').addEventListener('click', e => {
  const card = e.target.closest('.offering-card');
  if (!card) return;

  const giftType = card.dataset.gift;
  const giftName = card.dataset.name;
  const meritAdd = parseInt(card.dataset.merit, 10);

  audioStart();
  playBell(true);
  giftModal.classList.remove('active');

  userMerit += meritAdd;
  commMerit += meritAdd;
  currentUser.merit = userMerit;
  saveUserProfile();

  // All 24 devotees bow in deep reverence!
  visitors.forEach(v => { v.bow = 1.0; });

  // Spawn ascending offering visual towards altar desk (960, 835)
  const userVis = visitors.find(v => v.isUser);
  const startX = userVis ? userVis.x : 960;
  const startY = userVis ? userVis.y : 980;

  floaters.push({
    x: startX,
    y: startY,
    tx: 960 + (Math.random() - 0.5) * 200,
    ty: 835,
    icon: card.querySelector('.offering-icon').textContent,
    s: 1.6,
    alpha: 1.0,
    kind: 'offering_fly',
    t: 0
  });

  // Keep an active offering icon on altar table
  activeOfferings.push({
    x: 880 + Math.random() * 160,
    y: 830,
    icon: card.querySelector('.offering-icon').textContent,
    created: performance.now()
  });
  if (activeOfferings.length > 8) activeOfferings.shift();

  // Royal Banner updates
  showRoyalBanner(currentUser.name, currentUser.stock, userMerit, `Thành tâm cúng dường [${giftName}] cầu mã [${currentUser.stock}] tím 7 cây liên tiếp!`);
  triggerDanmaku(`🎁 [DÂNG LỄ] ${currentUser.name} dâng [${giftName}] lên Thần Chứng Khoán (+${meritAdd} công đức)!`, true);
  showToast(`🎁 Đã cúng dường [${giftName}] thành công! Công đức +${meritAdd}!`);

  focusOnUser();
});

/* ==========================================================
   TIKTOK LIVE DANMAKU & QUICK PRAYER BAR
   ========================================================== */
const DANMAKU_SEEDS = [
  'SSI ơi tím đi em gồng 3 tháng rồi 🙏',
  'Cầu Thần linh độ cho HPG chạm 35 vượt cản!',
  'VND hôm nay nến xanh đẹp quá lái ơi!',
  'Con vừa gõ mõ 50 cái xả margin, nhẹ cả đầu!',
  'Nam mô Bò Vàng Thần Tài! Độ cho DIG tím 5 cây!',
  'Khối ngoại gom ròng rã, anh em kiên trì giữ hàng!',
  'FPT công nghệ bền bỉ, phá đỉnh lịch sử!',
  'VIX bay cao như đại bàng, giải phóng kẹp đỉnh!',
  'Vạn lệnh gom hàng, triệu lệnh CE đón cổ đông về bờ!',
  'Tâm thành khấn nguyện tím toàn sàn!',
  'Lái kéo trần tàu chở về bờ đại thắng!'
];

function triggerDanmaku(text, isSpecial = false) {
  const layer = document.getElementById('danmakuLayer');
  const div = document.createElement('div');
  div.className = `danmaku-item ${isSpecial ? 'special' : ''}`;
  div.textContent = text;
  div.style.left = `${10 + Math.random() * 70}%`;
  div.style.animationDuration = `${8 + Math.random() * 4}s`;
  layer.appendChild(div);
  setTimeout(() => { if (div.parentNode) div.parentNode.removeChild(div); }, 12000);
}

setInterval(() => {
  const quote = DANMAKU_SEEDS[Math.floor(Math.random() * DANMAKU_SEEDS.length)];
  triggerDanmaku(quote, Math.random() < 0.2);
}, 3200);

document.getElementById('quickPrayerBar').addEventListener('submit', e => {
  e.preventDefault();
  const input = document.getElementById('quickPrayerInput');
  const val = input.value.trim();
  if (!val) return;
  triggerDanmaku(`[${currentUser.name} · ${currentUser.stock}]: ${val}`, true);
  input.value = '';

  const userVis = visitors.find(v => v.isUser);
  if (userVis) {
    userVis.bubble = { text: val, until: performance.now() + 4500 };
  }
  showToast('🕊️ Lời khấn đã bay lên Chánh Điện!');
});

/* ==========================================================
   ROYAL MERIT BANNER UPDATER
   ========================================================== */
function showRoyalBanner(user, stock, points, wish) {
  const banner = document.getElementById('royalMeritBanner');
  document.getElementById('meritBannerUser').textContent = user;
  document.getElementById('meritBannerStock').textContent = stock;
  document.getElementById('meritBannerPoints').textContent = points.toLocaleString();
  document.getElementById('meritBannerWish').textContent = `"${wish}"`;
  banner.classList.remove('pulse');
  void banner.offsetWidth;
  banner.classList.add('pulse');
}

setInterval(() => {
  if (Math.random() < 0.5) {
    const d = DEMO_DEVOTEES[Math.floor(Math.random() * DEMO_DEVOTEES.length)];
    const pts = Math.floor(1000 + Math.random() * 9000);
    showRoyalBanner(d.name, d.stock, pts, generateRandomWish(d.stock));
  } else {
    showRoyalBanner(currentUser.name, currentUser.stock, userMerit, currentUser.wish);
  }
}, 14000);

/* ==========================================================
   DÂNG SỚ CẦU TRẦN
   ========================================================== */
const prayModal = document.getElementById('prayModal');
const openPrayBtn = document.getElementById('openPrayBtn');
const closePrayBtn = document.getElementById('closePrayModal');
const prayForm = document.getElementById('prayForm');

function openPrayForStock(symbol) {
  document.getElementById('inputUser').value = currentUser.name;
  document.getElementById('inputStock').value = symbol || currentUser.stock;
  document.getElementById('inputCost').value = currentUser.cost || '';
  generateAndSetWish(symbol || currentUser.stock);
  prayModal.classList.add('active');
}
window.openPrayForStock = openPrayForStock;

openPrayBtn.addEventListener('click', () => {
  openPrayForStock(currentUser.stock);
});
closePrayBtn.addEventListener('click', () => prayModal.classList.remove('active'));

function generateRandomWish(stock, cost) {
  const s = (stock || 'CỔ PHIẾU').trim().toUpperCase();
  const c = cost ? `giá vốn ${cost}` : 'kẹp đỉnh';
  const verses = [
    `Cầu cho mã [${s}] tím 7 cây liên tiếp, khối ngoại ngừng xả ròng, dòng tiền lớn kéo thốc về bờ!`,
    `Nam mô Bò Vàng Tím Trần! Con thành tâm dâng lễ cầu mã [${s}] break đỉnh lịch sử, rũ sạch chim lợn!`,
    `Cụ Lái Trưởng ơi hiển linh kéo [${s}] bay thẳng lên nóc, giải cứu con đang ${c}, nhân đôi tài khoản!`,
    `Khấn nguyện mã [${s}] mỗi phiên khớp lệnh triệu cổ giá trần, nến xanh thẳng tắp, không rung lắc, không call margin!`,
    `Con xin dâng lòng thành, nguyện cho [${s}] phi như tên lửa, vượt mọi kháng cự, anh em cùng thuyền đại thắng!`,
    `Vạn lệnh gom hàng, triệu lệnh tím trần! Cầu cho [${s}] rực sắc hoa cà từ ATO đến ATC!`
  ];
  return verses[Math.floor(Math.random() * verses.length)];
}

function generateAndSetWish(sym) {
  const stock = sym || document.getElementById('inputStock').value.trim().toUpperCase() || currentUser.stock;
  const cost = document.getElementById('inputCost').value;
  document.getElementById('inputWish').value = generateRandomWish(stock, cost);
}

document.getElementById('genWishBtn').addEventListener('click', () => {
  const stock = document.getElementById('inputStock').value.trim().toUpperCase();
  generateAndSetWish(stock);
});

document.getElementById('inputStock').addEventListener('input', e => {
  const newStock = e.target.value.trim().toUpperCase();
  const wishBox = document.getElementById('inputWish');
  if (wishBox.value.includes('[')) {
    wishBox.value = wishBox.value.replace(/\[.*?\]/g, `[${newStock || 'CỔ PHIẾU'}]`);
  }
});

document.getElementById('quickStocks').addEventListener('click', e => {
  const pill = e.target.closest('.stock-pill');
  if (!pill) return;
  document.querySelectorAll('#quickStocks .stock-pill').forEach(p => p.classList.remove('selected'));
  pill.classList.add('selected');
  document.getElementById('inputStock').value = pill.dataset.sym;
  generateAndSetWish(pill.dataset.sym);
});

prayForm.addEventListener('submit', e => {
  e.preventDefault();
  audioStart();
  const user = document.getElementById('inputUser').value.trim();
  const stock = document.getElementById('inputStock').value.trim().toUpperCase();
  const cost = parseFloat(document.getElementById('inputCost').value) || 0;
  const wish = document.getElementById('inputWish').value.trim();

  if (!user || !stock || !wish) return;

  currentUser.name = user;
  currentUser.stock = stock;
  currentUser.cost = cost;
  currentUser.wish = wish;
  saveUserProfile();

  prayModal.classList.remove('active');

  spawnOrUpdateUserVisitor();
  const userVis = visitors.find(v => v.isUser);
  if (userVis) {
    userVis.bubble = { text: wish, until: performance.now() + 7000 };
    userVis.glow = 1.0;
  }

  showRoyalBanner(currentUser.name, currentUser.stock, userMerit, currentUser.wish);
  triggerDanmaku(`📜 [DÂNG SỚ] ${currentUser.name} cầu cho [${stock}]: ${wish}`, true);

  playBell(true);
  showToast(`✍️ Đã dâng sớ cầu nguyện cho mã [${stock}] thành công! Cụ tổ chứng giám!`);
  focusOnUser();
});

/* ==========================================================
   MODAL TẠO / SỬA NHÂN VẬT
   ========================================================== */
const charModal = document.getElementById('charModal');
const openCharBtn = document.getElementById('openCharBtn');
const closeCharModal = document.getElementById('closeCharModal');
const userProfileBtn = document.getElementById('userProfileBtn');
const charForm = document.getElementById('charForm');

function openCharModal() {
  document.getElementById('charNameInput').value = currentUser.name;
  document.getElementById('charStockInput').value = currentUser.stock;
  document.getElementById('charCostInput').value = currentUser.cost || '';
  document.querySelectorAll('.avatar-card').forEach(c => {
    c.classList.toggle('active', c.dataset.gender === currentUser.gender);
  });
  charModal.classList.add('active');
}

openCharBtn.addEventListener('click', openCharModal);
userProfileBtn.addEventListener('click', openCharModal);
closeCharModal.addEventListener('click', () => charModal.classList.remove('active'));

document.querySelector('.avatar-selector').addEventListener('click', e => {
  const card = e.target.closest('.avatar-card');
  if (!card) return;
  document.querySelectorAll('.avatar-card').forEach(c => c.classList.remove('active'));
  card.classList.add('active');
  currentUser.gender = card.dataset.gender;
});

document.getElementById('charQuickStocks').addEventListener('click', e => {
  const pill = e.target.closest('.stock-pill');
  if (!pill) return;
  document.querySelectorAll('#charQuickStocks .stock-pill').forEach(p => p.classList.remove('selected'));
  pill.classList.add('selected');
  document.getElementById('charStockInput').value = pill.dataset.sym;
});

charForm.addEventListener('submit', e => {
  e.preventDefault();
  const name = document.getElementById('charNameInput').value.trim();
  const stock = document.getElementById('charStockInput').value.trim().toUpperCase();
  const cost = parseFloat(document.getElementById('charCostInput').value) || 0;
  const activeCard = document.querySelector('.avatar-card.active');
  const gender = activeCard ? activeCard.dataset.gender : 'man';

  if (!name || !stock) return;

  currentUser.name = name;
  currentUser.stock = stock;
  currentUser.cost = cost;
  currentUser.gender = gender;
  currentUser.wish = generateRandomWish(stock, cost);
  saveUserProfile();

  charModal.classList.remove('active');
  spawnOrUpdateUserVisitor();
  showToast(`✨ Đã tạo hình chứng sĩ [${name}] thành công!`);
  focusOnUser();
});

/* ==========================================================
   CAPTURE FACEBOOK PHOTO CARD ENGINE
   ========================================================== */
const fbModal = document.getElementById('fbModal');
const closeFbModal = document.getElementById('closeFbModal');
const fbPreviewImg = document.getElementById('fbPreviewImg');
const fbCaptionText = document.getElementById('fbCaptionText');
const downloadCardBtn = document.getElementById('downloadCardBtn');
const copyFbCaptionBtn = document.getElementById('copyFbCaptionBtn');

let lastCardBlobUrl = null;

function captureForFacebook() {
  focusOnUser();

  setTimeout(() => {
    const card = document.createElement('canvas');
    card.width = 1280;
    card.height = 720;
    const cctx = card.getContext('2d');

    cctx.drawImage(canvas, 0, 0, 1280, 720);

    const grad = cctx.createRadialGradient(640, 360, 300, 640, 360, 700);
    grad.addColorStop(0, 'rgba(0,0,0,0)');
    grad.addColorStop(1, 'rgba(10,3,8,0.75)');
    cctx.fillStyle = grad;
    cctx.fillRect(0, 0, 1280, 720);

    cctx.strokeStyle = '#e5b342';
    cctx.lineWidth = 10;
    cctx.strokeRect(20, 20, 1240, 680);
    cctx.strokeStyle = '#d946ef';
    cctx.lineWidth = 2;
    cctx.strokeRect(28, 28, 1224, 664);

    cctx.fillStyle = 'rgba(15, 5, 12, 0.92)';
    cctx.fillRect(340, 32, 600, 64);
    cctx.strokeStyle = '#e5b342';
    cctx.lineWidth = 2;
    cctx.strokeRect(340, 32, 600, 64);

    cctx.font = 'bold 22px "Noto Serif", Georgia, serif';
    cctx.fillStyle = '#fef08a';
    cctx.textAlign = 'center';
    cctx.fillText('CHỨNG NHẬN CẦU NGUYỆN CỔ PHIẾU', 640, 62);

    cctx.font = '12px "Be Vietnam Pro", sans-serif';
    cctx.fillStyle = '#f472b6';
    cctx.fillText('✦ VẠN LỆNH TÍM TRẦN · LÁI KÉO TÀU VỀ BỜ ĐẠI THẮNG ✦', 640, 84);

    cctx.fillStyle = 'rgba(20, 8, 16, 0.94)';
    cctx.fillRect(60, 560, 1160, 115);
    cctx.strokeStyle = '#e5b342';
    cctx.lineWidth = 2;
    cctx.strokeRect(60, 560, 1160, 115);

    cctx.textAlign = 'left';
    cctx.font = 'bold 20px "Be Vietnam Pro", sans-serif';
    cctx.fillStyle = '#e5b342';
    cctx.fillText(`Đạo hữu: ${currentUser.name}`, 85, 595);

    cctx.fillStyle = '#f472b6';
    cctx.fillText(`Mã Cầu Trần: [${currentUser.stock}] (Vốn: ${currentUser.cost ? currentUser.cost + 'k' : 'Kẹp đỉnh'})`, 540, 595);

    cctx.fillStyle = '#34d399';
    cctx.font = '14px "JetBrains Mono", monospace';
    cctx.fillText(`Điểm Công Đức: ${userMerit} điểm | Margin: 0%`, 85, 625);

    cctx.font = 'italic 15px "Be Vietnam Pro", sans-serif';
    cctx.fillStyle = '#fff';
    const cleanWish = currentUser.wish.length > 95 ? currentUser.wish.slice(0, 95) + '...' : currentUser.wish;
    cctx.fillText(`"${cleanWish}"`, 85, 655);

    cctx.textAlign = 'right';
    cctx.font = '12px "Be Vietnam Pro", sans-serif';
    cctx.fillStyle = '#9ca3af';
    cctx.fillText(`Chánh Điện Chứng Khoán · ${new Date().toLocaleDateString('vi-VN')}`, 1195, 655);

    if (A.bull && A.bull.naturalWidth > 0) {
      cctx.save();
      cctx.globalAlpha = 0.85;
      cctx.drawImage(A.bull, 1110, 48, 110, 110);
      cctx.restore();
    }

    card.toBlob(blob => {
      if (lastCardBlobUrl) URL.revokeObjectURL(lastCardBlobUrl);
      lastCardBlobUrl = URL.createObjectURL(blob);
      fbPreviewImg.src = lastCardBlobUrl;

      fbCaptionText.value =
        `🙏 Thành tâm dâng sớ tại Chánh Điện Chứng Khoán cầu cho mã #${currentUser.stock} tuần này rực tím trần CE 7 cây liên tiếp! ` +
        `Lái tàu kéo về bờ nhân đôi tài khoản! Anh em cùng thuyền thả tim trợ duyên nhé! 🐂🟣\n\n` +
        `#ChanhDienChungKhoan #VanLenhTimTran #${currentUser.stock} #VeBoDaiThang #ChungKhoanVietNam`;

      fbModal.classList.add('active');
    }, 'image/png');
  }, 350);
}

document.getElementById('captureFbBtn').addEventListener('click', captureForFacebook);
closeFbModal.addEventListener('click', () => fbModal.classList.remove('active'));

downloadCardBtn.addEventListener('click', () => {
  if (!lastCardBlobUrl) return;
  const a = document.createElement('a');
  a.href = lastCardBlobUrl;
  a.download = `ChungNhan_CauTran_${currentUser.stock}_${Date.now()}.png`;
  a.click();
});

copyFbCaptionBtn.addEventListener('click', () => {
  navigator.clipboard.writeText(fbCaptionText.value).then(() => {
    showToast('📋 Đã copy Caption Facebook kèm Hashtag vào Clipboard!');
  }).catch(() => {
    fbCaptionText.select();
    document.execCommand('copy');
    showToast('📋 Đã copy Caption Facebook!');
  });
});

/* ==========================================================
   CANVAS DRAWING: TWO CANVAS-ANCHORED COUPLETS
   ========================================================== */
function drawCoupletPlaque(x, y, chars) {
  ctx.save();
  const pw = 42;
  const ph = 270;

  ctx.shadowColor = 'rgba(0, 0, 0, 0.85)';
  ctx.shadowBlur = 18;
  ctx.shadowOffsetX = 4;
  ctx.shadowOffsetY = 4;

  const grad = ctx.createLinearGradient(x, y, x + pw, y);
  grad.addColorStop(0, '#5a1322');
  grad.addColorStop(0.3, '#991b1b');
  grad.addColorStop(0.7, '#7f1d1d');
  grad.addColorStop(1, '#450a0a');
  ctx.fillStyle = grad;
  ctx.beginPath();
  ctx.roundRect(x, y, pw, ph, 4);
  ctx.fill();

  ctx.shadowColor = 'transparent';

  ctx.strokeStyle = '#e5b342';
  ctx.lineWidth = 2;
  ctx.strokeRect(x + 2, y + 2, pw - 4, ph - 4);
  ctx.strokeStyle = 'rgba(245, 232, 208, 0.4)';
  ctx.lineWidth = 1;
  ctx.strokeRect(x + 5, y + 5, pw - 10, ph - 10);

  ctx.beginPath();
  ctx.arc(x + pw / 2, y - 4, 5, 0, Math.PI * 2);
  ctx.strokeStyle = '#e5b342';
  ctx.lineWidth = 2;
  ctx.stroke();

  ctx.fillStyle = '#b45309';
  ctx.fillRect(x + pw / 2 - 3, y + ph, 6, 24);
  ctx.beginPath();
  ctx.arc(x + pw / 2, y + ph + 24, 5, 0, Math.PI * 2);
  ctx.fill();

  ctx.font = '900 16px "Noto Serif", Georgia, serif';
  ctx.textAlign = 'center';
  ctx.fillStyle = '#fef08a';
  ctx.shadowColor = '#e5b342';
  ctx.shadowBlur = 10;

  const charDist = 34;
  const startY = y + 28;
  for (let i = 0; i < chars.length; i++) {
    ctx.fillText(chars[i], x + pw / 2, startY + i * charDist);
  }

  ctx.restore();
}

/* ==========================================================
   CANVAS DRAWING: 3D CUSHIONS & CHANTING DAIS
   ========================================================== */
function drawCushion(seat, isTaken, isUserSeat, now) {
  const { x, y, scale } = seat;
  const rx = 66 * scale;
  const ry = 28 * scale;

  ctx.save();

  ctx.beginPath();
  ctx.ellipse(x, y + 4 * scale, rx * 1.08, ry * 0.95, 0, 0, Math.PI * 2);
  ctx.fillStyle = 'rgba(8, 3, 6, 0.65)';
  ctx.fill();

  const thick = 14 * scale;
  const skirtGrad = ctx.createLinearGradient(x, y, x, y + thick);
  skirtGrad.addColorStop(0, '#5a1322');
  skirtGrad.addColorStop(0.5, '#7b1c31');
  skirtGrad.addColorStop(1, '#2c0810');

  ctx.beginPath();
  ctx.ellipse(x, y + thick, rx, ry, 0, 0, Math.PI);
  ctx.lineTo(x - rx, y);
  ctx.ellipse(x, y, rx, ry, 0, Math.PI, 0, true);
  ctx.closePath();
  ctx.fillStyle = skirtGrad;
  ctx.fill();
  ctx.strokeStyle = 'rgba(229, 179, 66, 0.4)';
  ctx.lineWidth = 1.5 * scale;
  ctx.stroke();

  const topGrad = ctx.createRadialGradient(x - rx * 0.2, y - ry * 0.3, 2 * scale, x, y, rx);
  if (isUserSeat) {
    topGrad.addColorStop(0, '#be185d');
    topGrad.addColorStop(0.6, '#831843');
    topGrad.addColorStop(1, '#500724');
  } else {
    topGrad.addColorStop(0, '#991b1b');
    topGrad.addColorStop(0.6, '#7f1d1d');
    topGrad.addColorStop(1, '#450a0a');
  }

  ctx.beginPath();
  ctx.ellipse(x, y, rx, ry, 0, 0, Math.PI * 2);
  ctx.fillStyle = topGrad;
  ctx.fill();

  ctx.strokeStyle = isUserSeat ? '#fef08a' : '#e5b342';
  ctx.lineWidth = (isUserSeat ? 3 : 2) * scale;
  ctx.stroke();

  ctx.beginPath();
  ctx.ellipse(x, y, rx * 0.5, ry * 0.5, 0, 0, Math.PI * 2);
  ctx.strokeStyle = 'rgba(229, 179, 66, 0.55)';
  ctx.lineWidth = 1 * scale;
  ctx.stroke();

  if (isUserSeat) {
    const pulse = 1.0 + 0.12 * Math.sin(now * 0.005);
    ctx.save();
    ctx.shadowColor = '#d946ef';
    ctx.shadowBlur = 25 * pulse;
    ctx.strokeStyle = '#e5b342';
    ctx.lineWidth = 2.5 * scale * pulse;
    ctx.beginPath();
    ctx.ellipse(x, y, rx * 1.25 * pulse, ry * 1.25 * pulse, 0, 0, Math.PI * 2);
    ctx.stroke();

    if (A.fx_lotus && A.fx_lotus.naturalWidth > 0) {
      ctx.globalAlpha = 0.75 * pulse;
      const lw = 90 * scale;
      const lh = 75 * scale;
      ctx.drawImage(A.fx_lotus, x - lw / 2, y - lh * 0.8, lw, lh);
    }
    ctx.restore();
  }

  ctx.restore();
}

function drawChantingDais(now) {
  ctx.save();

  const tx = 690;
  const ty = 835;
  const tw = 540;
  const th = 26;

  ctx.beginPath();
  ctx.ellipse(960, ty + th + 4, tw * 0.54, 12, 0, 0, Math.PI * 2);
  ctx.fillStyle = 'rgba(8, 3, 6, 0.7)';
  ctx.fill();

  const tableGrad = ctx.createLinearGradient(tx, ty, tx, ty + th);
  tableGrad.addColorStop(0, '#581c1c');
  tableGrad.addColorStop(0.5, '#7f1d1d');
  tableGrad.addColorStop(1, '#3b0d0d');
  ctx.fillStyle = tableGrad;
  ctx.beginPath();
  ctx.roundRect(tx, ty, tw, th, 4);
  ctx.fill();

  ctx.strokeStyle = '#e5b342';
  ctx.lineWidth = 1.5;
  ctx.strokeRect(tx + 4, ty + 3, tw - 8, th - 6);

  ctx.fillStyle = '#991b1b';
  ctx.beginPath();
  ctx.ellipse(960, ty, tw * 0.5, 7, 0, 0, Math.PI * 2);
  ctx.fill();
  ctx.strokeStyle = '#e5b342';
  ctx.lineWidth = 1;
  ctx.stroke();

  // Ritual Objects
  ctx.fillStyle = '#b45309';
  ctx.beginPath();
  ctx.arc(960, ty - 6, 9, 0, Math.PI * 2);
  ctx.fill();
  ctx.strokeStyle = '#fef08a';
  ctx.lineWidth = 1;
  ctx.stroke();

  ctx.strokeStyle = '#ef4444';
  ctx.lineWidth = 1.5;
  ctx.beginPath();
  ctx.moveTo(960, ty - 6);
  ctx.lineTo(960, ty - 22);
  ctx.moveTo(957, ty - 6);
  ctx.lineTo(955, ty - 20);
  ctx.moveTo(963, ty - 6);
  ctx.lineTo(965, ty - 20);
  ctx.stroke();

  ctx.fillStyle = '#fef08a';
  ctx.beginPath();
  ctx.arc(960, ty - 22, 1.5, 0, Math.PI * 2);
  ctx.arc(955, ty - 20, 1.5, 0, Math.PI * 2);
  ctx.arc(965, ty - 20, 1.5, 0, Math.PI * 2);
  ctx.fill();

  if (A.fx_mo && A.fx_mo.naturalWidth > 0) {
    ctx.drawImage(A.fx_mo, 830, ty - 18, 28, 24);
  }

  if (A.fx_bell && A.fx_bell.naturalWidth > 0) {
    ctx.drawImage(A.fx_bell, 1060, ty - 22, 26, 26);
  }

  // Draw active offerings sitting on desk
  for (const off of activeOfferings) {
    ctx.font = '22px serif';
    ctx.textAlign = 'center';
    ctx.fillText(off.icon, off.x, off.y);
  }

  // Draw High Masters
  for (const m of HIGH_MASTERS) {
    ctx.save();
    ctx.translate(m.x, m.y);

    const mrx = 55 * m.scale;
    const mry = 22 * m.scale;
    ctx.beginPath();
    ctx.ellipse(0, 0, mrx, mry, 0, 0, Math.PI * 2);
    ctx.fillStyle = m.role === 'abbot' ? '#b45309' : '#7f1d1d';
    ctx.fill();
    ctx.strokeStyle = '#e5b342';
    ctx.lineWidth = 2 * m.scale;
    ctx.stroke();

    if (m.role === 'abbot' && A.fx_halo && A.fx_halo.naturalWidth > 0) {
      ctx.save();
      const hw = 120 * m.scale;
      const hh = 120 * m.scale;
      ctx.translate(0, -65 * (m.scale / 0.28));
      ctx.rotate(now * 0.0006);
      ctx.globalAlpha = 0.85;
      ctx.drawImage(A.fx_halo, -hw / 2, -hh / 2, hw, hh);
      ctx.restore();
    }

    const skinImg = A[m.skin] || A.c_monk;
    if (skinImg && skinImg.naturalWidth > 0) {
      ctx.save();
      if (m.flip) ctx.scale(-1, 1);
      const dw = skinImg.naturalWidth * m.scale * 0.82;
      const dh = skinImg.naturalHeight * m.scale * 0.82;
      ctx.drawImage(skinImg, -dw / 2, -dh, dw, dh);
      ctx.restore();
    }

    const tagY = -82 * (m.scale / 0.28);
    ctx.font = 'bold 11px "Be Vietnam Pro", sans-serif';
    const tw = ctx.measureText(m.title).width;
    const pw = tw + 14;

    ctx.fillStyle = m.role === 'abbot' ? 'rgba(180, 83, 9, 0.95)' : 'rgba(24, 11, 20, 0.9)';
    ctx.strokeStyle = '#e5b342';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.roundRect(-pw / 2, tagY - 14, pw, 18, 9);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = '#fef08a';
    ctx.textAlign = 'center';
    ctx.fillText(m.title, 0, tagY);

    ctx.restore();
  }

  ctx.restore();
}

/* ==========================================================
   RENDER LOOP (16:9 Widescreen Landscape)
   ========================================================== */
let lastT = performance.now();

function loop(now) {
  const dt = Math.min(0.1, (now - lastT) / 1000);
  lastT = now;

  camera.zoom += (camera.targetZoom - camera.zoom) * 0.14;
  camera.x += (camera.targetX - camera.x) * 0.14;
  camera.y += (camera.targetY - camera.y) * 0.14;

  ctx.clearRect(0, 0, SW, SH);

  ctx.save();

  // Screen shake if triggered (e.g. by lightning)
  if (screenShake > 0) {
    const sx = (Math.random() - 0.5) * screenShake;
    const sy = (Math.random() - 0.5) * screenShake;
    ctx.translate(sx, sy);
    screenShake = Math.max(0, screenShake - dt * 25);
  }

  ctx.translate(camera.x, camera.y);
  ctx.scale(camera.zoom, camera.zoom);

  // 1. Draw Widescreen Temple Hall Background
  if (A.hall && A.hall.naturalWidth > 0) {
    ctx.drawImage(A.hall, 0, 0, SW, SH);
  } else {
    ctx.fillStyle = '#1c0a17';
    ctx.fillRect(0, 0, SW, SH);
  }

  // 1.2. Two Couplets on Dragon Pillars
  drawCoupletPlaque(260, 320, ['TÂM', 'THÀNH', 'KHẤN', 'NGUYỆN', 'TÍM', 'TOÀN', 'SÀN']);
  drawCoupletPlaque(1640, 320, ['LÁI', 'KÉO', 'TRẦN', 'TÀU', 'CHỞ', 'VỀ', 'BỜ']);

  // 1.5. Chanting Dais & 3 Masters
  drawChantingDais(now);

  // 1.8. 24 3D Cushions
  for (const s of seats) {
    const isUserSeat = s.taken && s.taken.isUser;
    drawCushion(s, !!s.taken, isUserSeat, now);
  }

  // 2. Devotees
  visitors.sort((a, b) => a.y - b.y);

  for (const v of visitors) {
    if (v.state === 'walk' && v.seat) {
      const dx = v.seat.x - v.x;
      const dy = v.seat.y - v.y;
      const dist = Math.hypot(dx, dy);
      if (dist < 4) {
        v.x = v.seat.x;
        v.y = v.seat.y;
        v.state = 'sit';
        v.bubble = { text: `Tín đồ [${v.stock}] an tọa cầu nguyện!`, until: now + 3500 };
      } else {
        v.x += (dx / dist) * v.speed * dt;
        v.y += (dy / dist) * v.speed * dt;
      }
    }

    // Bow animation recovery
    if (v.bow > 0) {
      v.bow = Math.max(0, v.bow - dt * 0.8);
    }

    const scale = v.seat ? v.seat.scale : 0.35;
    const imgKey = v.skin;
    const img = A[imgKey] || A.c_man;

    ctx.save();
    ctx.translate(v.x, v.y + v.bow * 12);

    if (img && img.naturalWidth > 0) {
      ctx.save();
      if (v.flip) ctx.scale(-1, 1);
      const dw = img.naturalWidth * scale * 0.85;
      const dh = img.naturalHeight * scale * (0.85 - v.bow * 0.15);
      ctx.drawImage(img, -dw / 2, -dh, dw, dh);
      ctx.restore();
    }

    const tagY = -85 * (scale / 0.3) + v.bow * 10;
    ctx.save();
    ctx.font = v.isUser ? 'bold 12px "Be Vietnam Pro", sans-serif' : '10px "Be Vietnam Pro", sans-serif';
    const tagText = v.isUser ? `⭐ [BẠN] ${v.name} · ${v.stock} ⭐` : `${v.name} · ${v.stock}`;
    const tw = ctx.measureText(tagText).width;
    const pw = tw + 14;

    ctx.fillStyle = v.isUser ? 'rgba(112, 26, 117, 0.95)' : 'rgba(20, 8, 16, 0.85)';
    ctx.strokeStyle = v.isUser ? '#f472b6' : 'rgba(229, 179, 66, 0.5)';
    ctx.lineWidth = v.isUser ? 2 : 1;
    ctx.beginPath();
    ctx.roundRect(-pw / 2, tagY - 14, pw, 18, 9);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = v.isUser ? '#fef08a' : '#f3f4f6';
    ctx.textAlign = 'center';
    ctx.fillText(tagText, 0, tagY);
    ctx.restore();

    if (v.bubble && v.bubble.until > now) {
      const bText = v.bubble.text;
      ctx.save();
      ctx.font = '11px "Be Vietnam Pro", sans-serif';
      const bw = Math.min(240, ctx.measureText(bText).width + 18);
      const by = tagY - 32;

      ctx.fillStyle = 'rgba(254, 240, 138, 0.96)';
      ctx.strokeStyle = '#b45309';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.roundRect(-bw / 2, by - 12, bw, 22, 6);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = '#1c0a00';
      ctx.textAlign = 'center';
      ctx.fillText(bText, 0, by + 3);
      ctx.restore();
    }

    ctx.restore();
  }

  // 3. Floating FX, Particles, Emotes & Offerings
  for (let i = floaters.length - 1; i >= 0; i--) {
    const f = floaters[i];

    if (f.kind === 'offering_fly') {
      f.t += dt * 1.3;
      f.x += (f.tx - f.x) * 0.1;
      f.y = f.y - (f.y - f.ty) * 0.12 - Math.sin(f.t * Math.PI) * 4;
      ctx.save();
      ctx.font = `${Math.floor(28 * f.s)}px serif`;
      ctx.textAlign = 'center';
      ctx.shadowColor = '#d946ef';
      ctx.shadowBlur = 20;
      ctx.fillText(f.icon, f.x, f.y);
      ctx.restore();

      if (f.t >= 1.0 || Math.hypot(f.x - f.tx, f.y - f.ty) < 15) {
        floaters.splice(i, 1);
      }
      continue;
    }

    if (f.kind === 'lightning_flash') {
      f.alpha -= dt * 2.5;
      if (f.alpha <= 0) { floaters.splice(i, 1); continue; }
      ctx.save();
      ctx.fillStyle = `rgba(217, 70, 239, ${f.alpha})`;
      ctx.fillRect(0, 0, SW, SH);
      ctx.restore();
      continue;
    }

    if (f.kind === 'bull_runner') {
      f.x += f.vx * dt;
      ctx.save();
      ctx.font = '36px serif';
      ctx.fillText('🐂', f.x, f.y);
      ctx.restore();
      if (f.x > SW + 100) floaters.splice(i, 1);
      continue;
    }

    if (f.kind === 'coin') {
      f.x += f.vx * dt;
      f.y += f.vy * dt;
      f.rot += f.vr * dt;
      ctx.save();
      ctx.translate(f.x, f.y);
      ctx.rotate(f.rot);
      ctx.font = '24px serif';
      ctx.fillText('🪙', -12, 12);
      ctx.restore();
      if (f.y > SH + 50) floaters.splice(i, 1);
      continue;
    }

    if (f.kind === 'heart') {
      f.x += f.vx * dt;
      f.y += f.vy * dt;
      f.rot += f.vr * dt;
      f.alpha -= dt * 0.45;
      if (f.alpha <= 0) { floaters.splice(i, 1); continue; }
      ctx.save();
      ctx.globalAlpha = Math.max(0, f.alpha);
      ctx.translate(f.x, f.y);
      ctx.rotate(f.rot);
      ctx.font = '22px serif';
      ctx.shadowColor = '#d946ef';
      ctx.shadowBlur = 15;
      ctx.fillText('💜', -11, 11);
      ctx.restore();
      continue;
    }

    // Standard text or petals
    f.x += f.vx * dt;
    f.y += f.vy * dt;
    f.alpha -= dt * 0.4;
    if (f.alpha <= 0) { floaters.splice(i, 1); continue; }

    ctx.save();
    ctx.globalAlpha = Math.max(0, f.alpha);

    if (f.kind === 'text') {
      ctx.font = 'bold 15px "Cinzel", serif';
      ctx.fillStyle = '#fef08a';
      ctx.shadowColor = '#d946ef';
      ctx.shadowBlur = 12;
      ctx.textAlign = 'center';
      ctx.fillText(f.text, f.x, f.y);
    } else {
      ctx.translate(f.x, f.y);
      ctx.rotate(f.rot);
      const pImg = A['fx_' + f.kind] || A.fx_petal;
      if (pImg && pImg.naturalWidth > 0) {
        const pw = pImg.naturalWidth * f.s;
        const ph = pImg.naturalHeight * f.s;
        ctx.drawImage(pImg, -pw / 2, -ph / 2, pw, ph);
      }
    }
    ctx.restore();
  }

  ctx.restore(); // Restore camera

  if (Math.random() < 0.04) {
    floaters.push({
      x: SW * Math.random(),
      y: SH * 0.65 + Math.random() * 200,
      vx: (Math.random() - 0.5) * 35,
      vy: -40 - Math.random() * 50,
      s: 0.25 + Math.random() * 0.25,
      rot: Math.random() * 6,
      vr: (Math.random() - 0.5) * 2,
      alpha: 0.8,
      kind: Math.random() < 0.3 ? 'lotus' : 'petal'
    });
  }

  requestAnimationFrame(loop);
}

requestAnimationFrame(loop);

let toastTimeout;
function showToast(msg) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.style.display = 'block';
  clearTimeout(toastTimeout);
  toastTimeout = setTimeout(() => { t.style.display = 'none'; }, 3200);
}
</script>
</body>
</html>
'''
    return html

if __name__ == '__main__':
    content = build()
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    with open('update_index_v2.py', 'w', encoding='utf-8') as f:
        f.write(f'''# -*- coding: utf-8 -*-
{content}
''')
    print("Successfully built updated index.html with all 3 combo features!")
