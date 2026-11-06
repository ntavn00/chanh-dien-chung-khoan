import http from 'http';
import https from 'https';
import zlib from 'zlib';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { WebSocketServer, WebSocket } from 'ws';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const PORT = process.env.PORT || 3000;
const HOST = process.env.HOST || '0.0.0.0';

// In-memory state for real-time stock prayers
const state = {
  activeUsers: 0,
  totalMerit: 86860,
  recentPrayers: [
    { id: 1, user: 'Thích Bắt Đáy', stock: 'HPG', cost: 28.5, offering: 'nhang-tim', wish: 'Cầu cụ Tây lông ngừng xả, lái kéo 3 cây CE về bờ ăn Tết!', time: '14:02', merits: 500 },
    { id: 2, user: 'Trưởng Tàu Bất Động Sản', stock: 'DIG', cost: 26.8, offering: 'chuoi-xanh', wish: 'Cầu giải cứu sàn, tiền lớn vào đỡ giá giải cứu anh em!', time: '14:00', merits: 100 },
    { id: 3, user: 'Cá Con Full Margin', stock: 'SSI', cost: 35.0, offering: 'bo-tim', wish: 'Xin Cụ Tổ ban cho một phiên tím lịm, thanh khoản tỷ đô!', time: '13:58', merits: 1000 },
    { id: 4, user: 'Tín Chủ Kẹp Đỉnh', stock: 'NVL', cost: 16.5, offering: 'chuoi-xanh', wish: 'Thành tâm xin thoát kẹp giá 16.5, không mong lãi chỉ mong hòa vốn!', time: '13:55', merits: 100 },
    { id: 5, user: 'Sư Huynh FPT', stock: 'FPT', cost: 130.0, offering: 'dai-hong-chung', wish: 'Cầu công nghệ số vươn tầm, cổ phiếu phá đỉnh 150!', time: '13:50', merits: 5000 },
  ],
  topStocks: {
    'HPG': 1420,
    'DIG': 1180,
    'SSI': 950,
    'NVL': 820,
    'FPT': 610,
    'VIX': 490,
    'VND': 420,
    'PDR': 380,
    'SHS': 310,
    'MWG': 290
  },
  topBelievers: [
    { name: 'Cá Con Full Margin', stock: 'SSI', merits: 12500 },
    { name: 'Thích Bắt Đáy', stock: 'HPG', merits: 8800 },
    { name: 'Sư Huynh FPT', stock: 'FPT', merits: 6200 },
    { name: 'Trưởng Tàu Bất Động Sản', stock: 'DIG', merits: 5400 },
    { name: 'Pháp Danh Về Bờ', stock: 'NVL', merits: 3900 }
  ],
  donations: [
    { id: 'd1', user: 'Đại Ca SSI', stock: 'SSI', amount: 18888, gift: 'Bò Vàng Sen Vàng VIP', merits: 188880, time: '14:10' },
    { id: 'd2', user: 'Bà Trùm FPT', stock: 'FPT', amount: 9999, gift: 'Heo Quay Tím Trần', merits: 99990, time: '14:05' },
    { id: 'd3', user: 'Chứng Sĩ Đu Đỉnh', stock: 'HPG', amount: 5000, gift: 'Chuối Xanh Về Bờ', merits: 50000, time: '13:50' },
    { id: 'd4', user: 'Bắt Đáy NVL', stock: 'NVL', amount: 2000, gift: 'Nhang Xanh Cắt Lỗ', merits: 20000, time: '13:42' }
  ]
};

// Bank Configuration for VietQR & SePay Webhook
const bankConfig = {
  bankId: process.env.BANK_ID || 'TCB',
  accountNo: process.env.ACCOUNT_NO || '6891456789',
  accountName: process.env.ACCOUNT_NAME || 'NGUYEN TUAN ANH',
  webhookSecret: process.env.WEBHOOK_SECRET || ''
};

function sanitizeClean(str, maxLen = 30) {
  if (typeof str !== 'string') return '';
  return str.replace(/<[^>]*>/g, '').replace(/[^\p{L}\p{N}\s_.,!?#\-\[\]]/gu, '').trim().slice(0, maxLen);
}

const ALLOWED_GIFTS = new Set([
  'Bò Vàng Sen Vàng VIP',
  'Heo Quay Tím Trần',
  'Chuối Xanh Về Bờ',
  'Nhang Xanh Cắt Lỗ',
  'Cà Phê Dev',
  'Trà Đá Server',
  'Nhang Tím Trần',
  'Lễ Vật Tâm Linh'
]);

// Process incoming donation (from SePay, Casso, or Test simulator)
function processDonation({ id, user, stock, amount, gift, content }) {
  const cleanAmount = Math.max(1000, Number(amount) || 5000);
  let cleanUser = sanitizeClean(user, 25);
  let cleanStock = sanitizeClean(stock, 8).toUpperCase();

  // If content is provided from bank transfer memo e.g. "CDCK ChienThan HPG"
  if (content) {
    const rawContent = sanitizeClean(content, 60).replace(/^CDCK\s+/i, '');
    const parts = rawContent.split(/\s+/);
    if (parts.length >= 2) {
      if (!cleanUser) cleanUser = parts[0];
      if (!cleanStock) cleanStock = parts[1].toUpperCase();
    } else if (parts.length === 1 && parts[0]) {
      if (parts[0].length === 3 && parts[0] === parts[0].toUpperCase()) {
        if (!cleanStock) cleanStock = parts[0];
      } else {
        if (!cleanUser) cleanUser = parts[0];
      }
    }
  }

  if (!cleanUser) cleanUser = 'Thí Chủ Hảo Tâm';
  if (!cleanStock) cleanStock = 'VNI';

  let giftName = ALLOWED_GIFTS.has(gift) ? gift : null;
  if (!giftName) {
    if (cleanAmount >= 18888) giftName = 'Bò Vàng Sen Vàng VIP';
    else if (cleanAmount >= 9999) giftName = 'Heo Quay Tím Trần';
    else if (cleanAmount >= 5000) giftName = 'Chuối Xanh Về Bờ';
    else giftName = 'Nhang Xanh Cắt Lỗ';
  }

  const meritBoost = Math.floor(cleanAmount * 10);
  state.totalMerit += meritBoost;

  const donationItem = {
    id: id || ('d_' + Date.now()),
    user: cleanUser,
    stock: cleanStock,
    amount: cleanAmount,
    gift: giftName,
    merits: meritBoost,
    time: new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' })
  };

  state.donations.unshift(donationItem);
  if (state.donations.length > 50) state.donations.pop();

  // Add or update top believers
  const bIdx = state.topBelievers.findIndex(b => b.name === cleanUser);
  if (bIdx >= 0) {
    state.topBelievers[bIdx].merits += meritBoost;
  } else {
    state.topBelievers.push({ name: cleanUser, stock: cleanStock, merits: meritBoost });
  }
  state.topBelievers.sort((a, b) => b.merits - a.merits);
  state.topBelievers = state.topBelievers.slice(0, 5);

  // Broadcast to all connected clients
  broadcast({
    type: 'DONATE_VIP',
    donation: donationItem,
    totalMerit: state.totalMerit,
    topBelievers: state.topBelievers
  });

  return donationItem;
}

// MIME types dictionary
const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'application/javascript; charset=utf-8',
  '.mjs': 'application/javascript; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.mp3': 'audio/mpeg',
  '.wav': 'audio/wav',
  '.woff2': 'font/woff2'
};

// In-memory cache for TTS audio buffers (max 200 items)
const ttsCache = new Map();

// HTTP Server
const server = http.createServer((req, res) => {
  const parsedUrl = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
  let pathname = decodeURIComponent(parsedUrl.pathname);

  // Default to index.html
  if (pathname === '/' || pathname === '') {
    pathname = '/index.html';
  }

  // API endpoints
  if (pathname === '/api/state') {
    res.writeHead(200, { 'Content-Type': 'application/json; charset=utf-8' });
    return res.end(JSON.stringify(state));
  }

  // TTS Proxy endpoint (Google Translate Vietnamese voice)
  if (pathname === '/api/tts') {
    const rawText = parsedUrl.searchParams.get('text') || '';
    const text = rawText.trim();
    if (!text) {
      res.writeHead(400, { 'Content-Type': 'text/plain; charset=utf-8' });
      return res.end('Thiếu tham số text');
    }

    // Limit chunk to 200 characters max for Google Translate TTS API
    const chunk = text.slice(0, 200);

    // Check in-memory cache
    if (ttsCache.has(chunk)) {
      const cached = ttsCache.get(chunk);
      res.writeHead(200, {
        'Content-Type': 'audio/mpeg',
        'Content-Length': cached.length,
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'public, max-age=86400'
      });
      return res.end(cached);
    }

    const ttsUrl = `https://translate.google.com/translate_tts?ie=UTF-8&tl=vi&client=tw-ob&q=${encodeURIComponent(chunk)}`;
    const reqOptions = {
      headers: {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Referer': 'https://translate.google.com/'
      }
    };

    https.get(ttsUrl, reqOptions, (ttsRes) => {
      if (ttsRes.statusCode === 200) {
        const chunks = [];
        ttsRes.on('data', d => chunks.push(d));
        ttsRes.on('end', () => {
          const buffer = Buffer.concat(chunks);
          if (ttsCache.size < 200) {
            ttsCache.set(chunk, buffer);
          }
          res.writeHead(200, {
            'Content-Type': 'audio/mpeg',
            'Content-Length': buffer.length,
            'Access-Control-Allow-Origin': '*',
            'Cache-Control': 'public, max-age=86400'
          });
          res.end(buffer);
        });
      } else {
        res.writeHead(ttsRes.statusCode || 500, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('TTS Proxy Error');
      }
    }).on('error', (err) => {
      console.error('TTS request error:', err.message);
      res.writeHead(500, { 'Content-Type': 'text/plain; charset=utf-8' });
      res.end('TTS Proxy Failed');
    });
    return;
  }

  // Bank config endpoint (Read-only for security)
  if (pathname === '/api/config/bank') {
    res.writeHead(200, {
      'Content-Type': 'application/json; charset=utf-8',
      'Access-Control-Allow-Origin': '*'
    });
    return res.end(JSON.stringify(bankConfig));
  }

  // Get donations list
  if (pathname === '/api/donations') {
    res.writeHead(200, {
      'Content-Type': 'application/json; charset=utf-8',
      'Access-Control-Allow-Origin': '*'
    });
    return res.end(JSON.stringify(state.donations));
  }

  // SePay Webhook Endpoint
  if (pathname === '/api/webhook/sepay' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
      try {
        const payload = JSON.parse(body || '{}');
        console.log('⚡ [SePay Webhook Received]:', payload);
        const amount = payload.transferAmount || payload.amount || 0;
        const content = payload.content || payload.description || '';
        
        if (amount > 0) {
          const donation = processDonation({ amount, content });
          res.writeHead(200, {
            'Content-Type': 'application/json; charset=utf-8',
            'Access-Control-Allow-Origin': '*'
          });
          return res.end(JSON.stringify({ success: true, donation }));
        } else {
          res.writeHead(200, {
            'Content-Type': 'application/json; charset=utf-8',
            'Access-Control-Allow-Origin': '*'
          });
          return res.end(JSON.stringify({ success: false, message: 'Amount <= 0' }));
        }
      } catch (err) {
        console.error('SePay webhook parse error:', err);
        res.writeHead(400, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('Bad Request');
      }
    });
    return;
  }

  // Casso Webhook Endpoint
  if (pathname === '/api/webhook/casso' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
      try {
        const payload = JSON.parse(body || '{}');
        console.log('⚡ [Casso Webhook Received]:', payload);
        if (Array.isArray(payload.data)) {
          for (const item of payload.data) {
            if (item.amount > 0) {
              processDonation({
                amount: item.amount,
                content: item.description
              });
            }
          }
        }
        res.writeHead(200, {
          'Content-Type': 'application/json; charset=utf-8',
          'Access-Control-Allow-Origin': '*'
        });
        res.end(JSON.stringify({ error: 0, message: 'Success' }));
      } catch (err) {
        res.writeHead(400, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('Bad Request');
      }
    });
    return;
  }

  // Test Webhook Simulation Endpoint (for immediate live testing)
  if (pathname === '/api/webhook/test-donate' && req.method === 'POST') {
    const authKey = parsedUrl.searchParams.get('key') || req.headers['x-admin-key'];
    if (authKey !== 'chanhdien_admin_2026') {
      res.writeHead(403, { 'Content-Type': 'text/plain; charset=utf-8' });
      return res.end('Forbidden');
    }
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', () => {
      try {
        const data = JSON.parse(body || '{}');
        const donation = processDonation({
          id: data.id,
          user: data.user,
          stock: data.stock,
          amount: data.amount,
          gift: data.gift,
          content: data.content
        });
        res.writeHead(200, {
          'Content-Type': 'application/json; charset=utf-8',
          'Access-Control-Allow-Origin': '*'
        });
        res.end(JSON.stringify({ success: true, donation }));
      } catch (e) {
        res.writeHead(400, { 'Content-Type': 'text/plain; charset=utf-8' });
        res.end('Bad Request');
      }
    });
    return;
  }

  // Security: prevent path traversal
  const safePath = path.normalize(pathname).replace(/^(\.\.[\/\\])+/, '');
  const filePath = path.join(__dirname, safePath);

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      res.writeHead(404, { 'Content-Type': 'text/plain; charset=utf-8' });
      return res.end('404 Không tìm thấy trang');
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';

    const acceptEncoding = req.headers['accept-encoding'] || '';
    const isCompressible = ['.html', '.js', '.css', '.json', '.svg'].includes(ext);
    const headers = {
      'Content-Type': contentType,
      'Vary': 'Accept-Encoding',
      'Cache-Control': ext === '.html' ? 'no-cache' : 'public, max-age=86400, stale-while-revalidate=604800'
    };

    if (isCompressible && acceptEncoding.includes('gzip')) {
      headers['Content-Encoding'] = 'gzip';
      res.writeHead(200, headers);
      fs.createReadStream(filePath).pipe(zlib.createGzip({ level: 6 })).pipe(res);
    } else {
      res.writeHead(200, headers);
      fs.createReadStream(filePath).pipe(res);
    }
  });
});

// WebSocket Server for live syncing prayers and wooden fish clicks
const wss = new WebSocketServer({ server, maxPayload: 64 * 1024 });

// Clean up stale or zombie connections every 30s
const pingInterval = setInterval(() => {
  for (const client of wss.clients) {
    if (client.isAlive === false) {
      client.terminate();
      continue;
    }
    client.isAlive = false;
    try {
      client.ping();
    } catch (e) {
      client.terminate();
    }
  }
}, 30000);

wss.on('close', () => clearInterval(pingInterval));

function broadcast(msgObj) {
  const data = JSON.stringify(msgObj);
  for (const client of wss.clients) {
    if (client.readyState === WebSocket.OPEN) {
      try {
        client.send(data);
      } catch (err) {
        // ignore send error on closing client
      }
    }
  }
}

wss.on('connection', (ws) => {
  if (wss.clients.size > 150) {
    ws.close(1013, 'Server busy');
    return;
  }

  ws.isAlive = true;
  ws.on('pong', () => { ws.isAlive = true; });
  ws.on('error', () => {
    try { ws.terminate(); } catch (e) {}
  });

  state.activeUsers = wss.clients.size;
  broadcast({ type: 'USER_COUNT', count: state.activeUsers });

  // Send initial state
  ws.send(JSON.stringify({
    type: 'INIT_STATE',
    state: state
  }));

  ws.on('message', (message) => {
    try {
      const data = JSON.parse(message.toString());

      if (data.type === 'PRAY') {
        const { user, stock, cost, offering, wish, merits } = data;
        const cleanStock = (stock || 'VNI').toUpperCase().trim().slice(0, 10);
        const cleanUser = (user || 'Chứng Sĩ Vô Danh').trim().slice(0, 25);
        const prayerMerit = Number(merits) || 100;

        const newPrayer = {
          id: Date.now(),
          user: cleanUser,
          stock: cleanStock,
          cost: cost || '',
          offering: offering || 'chuoi-xanh',
          wish: wish || 'Cầu tím trần 3 phiên về bờ!',
          time: new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' }),
          merits: prayerMerit
        };

        // Update state
        state.recentPrayers.unshift(newPrayer);
        if (state.recentPrayers.length > 50) state.recentPrayers.pop();

        state.topStocks[cleanStock] = (state.topStocks[cleanStock] || 0) + 1;
        state.totalMerit += prayerMerit;

        // Update top believers
        const believerIdx = state.topBelievers.findIndex(b => b.name === cleanUser);
        if (believerIdx >= 0) {
          state.topBelievers[believerIdx].merits += prayerMerit;
        } else {
          state.topBelievers.push({ name: cleanUser, stock: cleanStock, merits: prayerMerit });
        }
        state.topBelievers.sort((a, b) => b.merits - a.merits);
        state.topBelievers = state.topBelievers.slice(0, 5);

        // Broadcast to everyone
        broadcast({
          type: 'NEW_PRAYER',
          prayer: newPrayer,
          topStocks: state.topStocks,
          totalMerit: state.totalMerit,
          topBelievers: state.topBelievers
        });
      } else if (data.type === 'TAP_MO') {
        // Individual tapped wooden fish
        state.totalMerit += 1;
        broadcast({
          type: 'MO_TAPPED',
          user: data.user || 'Chứng sĩ',
          stock: (data.stock || 'VNI').toUpperCase(),
          totalMerit: state.totalMerit
        });
      }
    } catch (err) {
      console.error('Error handling WS message:', err);
    }
  });

  ws.on('close', () => {
    state.activeUsers = wss.clients.size;
    broadcast({ type: 'USER_COUNT', count: state.activeUsers });
  });
});

server.listen(PORT, HOST, () => {
  console.log(`====================================================`);
  console.log(`🐂 ĐIỆN THỜ CHỨNG KHOÁN - CẦU NGUYỆN CỔ PHIẾU VỀ BỜ 🐂`);
  console.log(`👉 Server đang chạy tại: http://localhost:${PORT}`);
  console.log(`====================================================`);
});
