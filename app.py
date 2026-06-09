<!DOCTYPE html>
<html lang="az">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Mood AI — Premium Restoran</title>
    <meta name="description" content="Mood AI restoran — rəqəmsal menyu və AI ilə sifariş sistemi">
    <meta name="description" content="Mood AI — Rəqəmsal menyu və AI ilə premium sifariş sistemi">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400;1,500&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
    <style>
        /* ═══════════════════════════════════════════
           RESET & VARIABLES
           ═══════════════════════════════════════════ */
        /* ══════════════════════════════════════════════════════════
           ██  RESET & CUSTOM PROPERTIES
           ══════════════════════════════════════════════════════════ */
        *, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }
        :root {
            --bg-deep: #07070c;
            --bg-primary: #0c0c14;
            --bg-secondary: #13131f;
            --bg-card: rgba(255, 255, 255, 0.025);
            --bg-glass: rgba(255, 255, 255, 0.04);
            --gold: #c9a96e;
            --gold-light: #e0c992;
            --gold-glow: rgba(201, 169, 110, 0.25);
            --gold-subtle: rgba(201, 169, 110, 0.08);
            --text-primary: #f0ebe4;
            --text-secondary: #9a9498;
            --text-muted: #5e5862;
            --border: rgba(201, 169, 110, 0.1);
            --border-strong: rgba(201, 169, 110, 0.2);
            --danger: #e05555;
            --success: #55b87a;
            --shadow-lg: 0 16px 48px rgba(0, 0, 0, 0.5);
            --shadow-gold: 0 0 30px rgba(201, 169, 110, 0.15);
            --radius-sm: 10px;
            --radius-md: 16px;
            --radius-lg: 24px;
            --radius-xl: 32px;
            --font-display: 'Playfair Display', Georgia, serif;
            --font-body: 'Inter', -apple-system, sans-serif;
            --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
            /* Backgrounds */
            --bg-void:     #050508;
            --bg-deep:     #08080e;
            --bg-primary:  #0c0c15;
            --bg-elevated: #111119;
            --bg-surface:  #16161f;
            --bg-glass:    rgba(255, 255, 255, 0.025);
            --bg-glass-2:  rgba(255, 255, 255, 0.045);
            /* Gold Palette */
            --gold-50:   #fdf8ef;
            --gold-100:  #f5e6c8;
            --gold-200:  #e8d0a0;
            --gold-300:  #d4b577;
            --gold-400:  #c9a55e;
            --gold-500:  #b8944d;
            --gold-600:  #9a7a3e;
            --gold-glow: rgba(201, 165, 94, 0.20);
            /* Text */
            --text-white:     #f8f4ef;
            --text-primary:   #e8e0d6;
            --text-secondary: #8e8890;
            --text-muted:     #55515a;
            --text-ghost:     #363240;
            /* Accents */
            --red:       #e85454;
            --red-glow:  rgba(232, 84, 84, 0.2);
            --green:     #4ecb71;
            --green-glow: rgba(78, 203, 113, 0.15);
            /* Borders */
            --border-subtle:   rgba(201, 165, 94, 0.07);
            --border-default:  rgba(201, 165, 94, 0.12);
            --border-strong:   rgba(201, 165, 94, 0.22);
            --border-glow:     rgba(201, 165, 94, 0.35);
            /* Effects */
            --shadow-sm:   0 2px 8px rgba(0, 0, 0, 0.3);
            --shadow-md:   0 8px 24px rgba(0, 0, 0, 0.4);
            --shadow-lg:   0 16px 48px rgba(0, 0, 0, 0.5);
            --shadow-xl:   0 24px 64px rgba(0, 0, 0, 0.6);
            --shadow-gold: 0 4px 30px rgba(201, 165, 94, 0.12);
            /* Radii */
            --r-xs: 6px;  --r-sm: 10px;  --r-md: 14px;
            --r-lg: 20px; --r-xl: 28px;  --r-full: 9999px;
            /* Fonts */
            --f-display: 'Cormorant Garamond', 'Georgia', serif;
            --f-body:    'Inter', -apple-system, sans-serif;
            --f-mono:    'JetBrains Mono', monospace;
            /* Motion */
            --ease:        cubic-bezier(0.16, 1, 0.3, 1);
            --ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1);
            --ease-smooth: cubic-bezier(0.4, 0, 0.2, 1);
        }
        html, body {
            height: 100%; width: 100%;
            font-family: var(--font-body);
            background: var(--bg-deep);
            font-family: var(--f-body);
            background: var(--bg-void);
            color: var(--text-primary);
            overflow: hidden;
            -webkit-tap-highlight-color: transparent;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }
        /* ═══════════════════════════════════════════
           BACKGROUND PATTERN
           ═══════════════════════════════════════════ */
        body::before {
            content: '';
            position: fixed;
            inset: 0;
        /* ══════════════════════════════════════════════════════════
           ██  ANIMATED BACKGROUND
           ══════════════════════════════════════════════════════════ */
        .bg-layer {
            position: fixed; inset: 0;
            pointer-events: none; z-index: 0;
            overflow: hidden;
        }
        /* Animated aurora gradient */
        .bg-aurora {
            position: absolute; inset: -50%;
            background:
                radial-gradient(ellipse 80% 60% at 50% 0%, rgba(201, 169, 110, 0.06) 0%, transparent 60%),
                radial-gradient(circle at 20% 80%, rgba(201, 169, 110, 0.03) 0%, transparent 40%),
                radial-gradient(circle at 80% 70%, rgba(120, 100, 70, 0.03) 0%, transparent 35%);
            pointer-events: none;
            z-index: 0;
                radial-gradient(ellipse 60% 40% at 30% 20%, rgba(201, 165, 94, 0.06) 0%, transparent 70%),
                radial-gradient(ellipse 50% 50% at 70% 60%, rgba(180, 140, 70, 0.04) 0%, transparent 60%),
                radial-gradient(ellipse 80% 30% at 50% 90%, rgba(160, 120, 60, 0.03) 0%, transparent 50%);
            animation: auroraFloat 20s ease-in-out infinite alternate;
        }
        /* ═══════════════════════════════════════════
           TABLE SELECTION MODAL
           ═══════════════════════════════════════════ */
        @keyframes auroraFloat {
            0%   { transform: translate(0, 0) rotate(0deg) scale(1); }
            33%  { transform: translate(3%, -2%) rotate(1deg) scale(1.02); }
            66%  { transform: translate(-2%, 3%) rotate(-1deg) scale(0.98); }
            100% { transform: translate(1%, -1%) rotate(0.5deg) scale(1.01); }
        }
        /* Floating particles */
        .particle {
            position: absolute;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(201, 165, 94, 0.3) 0%, transparent 70%);
            animation: particleFloat linear infinite;
            filter: blur(1px);
        }
        @keyframes particleFloat {
            0%   { transform: translateY(100vh) scale(0); opacity: 0; }
            10%  { opacity: 1; }
            90%  { opacity: 1; }
            100% { transform: translateY(-20vh) scale(1); opacity: 0; }
        }
        /* Noise texture overlay */
        .bg-noise {
            position: absolute; inset: 0;
            opacity: 0.015;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
            background-repeat: repeat;
            background-size: 256px 256px;
        }
        /* ══════════════════════════════════════════════════════════
           ██  TABLE SELECTION MODAL
           ══════════════════════════════════════════════════════════ */
        .modal-overlay {
            position: fixed; inset: 0;
            background: rgba(5, 5, 10, 0.92);
            backdrop-filter: blur(20px);
            background: rgba(3, 3, 6, 0.94);
            backdrop-filter: blur(30px) saturate(120%);
            -webkit-backdrop-filter: blur(30px) saturate(120%);
            display: flex; align-items: center; justify-content: center;
            z-index: 1000;
            animation: fadeIn 0.5s var(--ease-out);
            animation: fadeIn 0.6s var(--ease);
        }
        .modal-overlay.hidden { display: none; }
        .modal-overlay.hidden {
            display: none !important;
        }
        .modal-card {
            background: linear-gradient(145deg, rgba(20, 20, 32, 0.95), rgba(12, 12, 20, 0.98));
            background: linear-gradient(160deg, rgba(22, 22, 32, 0.92) 0%, rgba(10, 10, 18, 0.96) 100%);
            border: 1px solid var(--border-strong);
            border-radius: var(--radius-xl);
            padding: 48px 40px;
            max-width: 560px; width: 90%;
            border-radius: var(--r-xl);
            padding: 52px 44px 44px;
            max-width: 580px; width: 92%;
            text-align: center;
            box-shadow: var(--shadow-lg), var(--shadow-gold);
            animation: modalSlideUp 0.6s var(--ease-spring);
            position: relative;
            box-shadow: var(--shadow-xl), 0 0 80px rgba(201, 165, 94, 0.06);
            animation: modalEnter 0.7s var(--ease-spring);
            overflow: hidden;
        }
        .modal-card::before {
            content: '';
            position: absolute; top: 0; left: 20%; right: 20%; height: 1px;
            background: linear-gradient(90deg, transparent, var(--gold-400), transparent);
        }
        .modal-card::after {
            content: '';
            position: absolute; inset: 0;
            border-radius: var(--r-xl);
            background: radial-gradient(ellipse 80% 60% at 50% 0%, rgba(201, 165, 94, 0.04) 0%, transparent 60%);
            pointer-events: none;
        }
        .modal-icon {
            font-size: 48px;
            margin-bottom: 12px;
            display: block;
            animation: gentleBounce 2s ease-in-out infinite;
        .modal-ornament {
            display: flex; align-items: center; justify-content: center; gap: 16px;
            margin-bottom: 20px;
            color: var(--gold-400);
        }
        .modal-ornament .line {
            width: 48px; height: 1px;
            background: linear-gradient(90deg, transparent, var(--gold-400));
        }
        .modal-ornament .line:last-child {
            background: linear-gradient(90deg, var(--gold-400), transparent);
        }
        .modal-ornament .diamond {
            width: 8px; height: 8px;
            border: 1px solid var(--gold-400);
            transform: rotate(45deg);
            animation: diamondPulse 3s ease-in-out infinite;
        }
        .modal-card h2 {
            font-family: var(--font-display);
            font-size: 36px; font-weight: 600;
            color: var(--gold);
            letter-spacing: 1px;
        @keyframes diamondPulse {
            0%, 100% { opacity: 0.5; transform: rotate(45deg) scale(1); }
            50%      { opacity: 1;   transform: rotate(45deg) scale(1.2); }
        }
        .modal-brand {
            font-family: var(--f-display);
            font-size: 44px; font-weight: 300;
            color: var(--gold-100);
            letter-spacing: 6px;
            margin-bottom: 4px;
        }
        .modal-card .modal-subtitle {
            font-size: 13px; font-weight: 300;
        .modal-tagline {
            font-size: 11px; font-weight: 400;
            color: var(--text-muted);
            letter-spacing: 6px; text-transform: uppercase;
            margin-bottom: 36px;
        }
        .modal-prompt {
            font-family: var(--f-display);
            font-size: 20px; font-weight: 400; font-style: italic;
            color: var(--text-secondary);
            letter-spacing: 4px; text-transform: uppercase;
            margin-bottom: 32px;
            margin-bottom: 28px;
        }
        .modal-card .modal-prompt {
            font-size: 15px; color: var(--text-secondary);
            margin-bottom: 24px;
        }
        .table-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 10px;
            margin-bottom: 8px;
            margin-bottom: 16px;
            position: relative; z-index: 1;
        }
        .table-btn {
            background: var(--bg-glass);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            color: var(--text-primary);
            font-family: var(--font-body);
            border: 1px solid var(--border-subtle);
            border-radius: var(--r-sm);
            color: var(--text-secondary);
            font-family: var(--f-body);
            font-size: 16px; font-weight: 500;
            padding: 14px 0;
            padding: 16px 0;
            cursor: pointer;
            transition: all 0.3s var(--ease-out);
            transition: all 0.4s var(--ease);
            position: relative;
            overflow: hidden;
        }
        .table-btn:hover, .table-btn:focus {
            background: var(--gold-subtle);
            border-color: var(--gold);
            color: var(--gold);
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(201, 169, 110, 0.15);
        .table-btn::before {
            content: '';
            position: absolute; inset: 0;
            background: radial-gradient(circle at center, var(--gold-glow) 0%, transparent 70%);
            opacity: 0;
            transition: opacity 0.4s var(--ease);
        }
        .table-btn:active { transform: scale(0.95); }
        .table-btn:hover::before { opacity: 1; }
        .table-btn:hover {
            border-color: var(--gold-400);
            color: var(--gold-100);
            transform: translateY(-3px);
            box-shadow: 0 8px 24px rgba(201, 165, 94, 0.12);
        }
        .table-btn:active {
            transform: translateY(0) scale(0.96);
            transition-duration: 0.1s;
        }
        /* ═══════════════════════════════════════════
           MAIN APP LAYOUT
           ═══════════════════════════════════════════ */
        /* ══════════════════════════════════════════════════════════
           ██  MAIN APP LAYOUT
           ══════════════════════════════════════════════════════════ */
        .app {
            display: flex; flex-direction: column;
            height: 100vh;
            height: 100vh; height: 100dvh;
            position: relative; z-index: 1;
        }
        .app.hidden { display: none; }
        .app.hidden { display: none !important; }
        /* ═══════════════════════════════════════════
           HEADER
           ═══════════════════════════════════════════ */
        /* ══════════════════════════════════════════════════════════
           ██  HEADER
           ══════════════════════════════════════════════════════════ */
        .header {
            display: flex; align-items: center; justify-content: space-between;
            padding: 16px 28px;
            background: linear-gradient(180deg, rgba(12, 12, 20, 0.98) 0%, rgba(12, 12, 20, 0.85) 100%);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--border);
            padding: 14px 28px;
            background: rgba(8, 8, 14, 0.85);
            backdrop-filter: blur(20px) saturate(130%);
            -webkit-backdrop-filter: blur(20px) saturate(130%);
            border-bottom: 1px solid var(--border-subtle);
            flex-shrink: 0;
            z-index: 10;
            position: relative;
        }
        .header::after {
            content: '';
            position: absolute; bottom: -1px; left: 10%; right: 10%; height: 1px;
            background: linear-gradient(90deg, transparent, rgba(201, 165, 94, 0.15), transparent);
        }
        .header-brand {
            display: flex; align-items: center; gap: 14px;
        }
        .header-logo {
            width: 44px; height: 44px;
            background: linear-gradient(135deg, var(--gold), var(--gold-light));
            border-radius: 12px;
            width: 42px; height: 42px;
            border-radius: var(--r-sm);
            display: flex; align-items: center; justify-content: center;
            font-size: 20px;
            box-shadow: 0 4px 16px rgba(201, 169, 110, 0.25);
            position: relative;
            background: linear-gradient(135deg, var(--gold-400) 0%, var(--gold-300) 50%, var(--gold-500) 100%);
            box-shadow: 0 4px 20px rgba(201, 165, 94, 0.25);
        }
        .header-brand h1 {
            font-family: var(--font-display);
        .header-logo span {
            font-family: var(--f-display);
            font-size: 22px; font-weight: 600;
            color: var(--gold);
            line-height: 1.1;
            color: var(--bg-void);
        }
        .header-brand span {
            font-size: 11px; font-weight: 300;
        .header-title {
            font-family: var(--f-display);
            font-size: 24px; font-weight: 400;
            color: var(--gold-100);
            letter-spacing: 3px;
            line-height: 1;
        }
        .header-subtitle {
            font-size: 10px; font-weight: 400;
            color: var(--text-muted);
            letter-spacing: 3px; text-transform: uppercase;
            letter-spacing: 4px; text-transform: uppercase;
            margin-top: 2px;
        }
        .header-right {
            display: flex; align-items: center; gap: 14px;
            display: flex; align-items: center; gap: 12px;
        }
        .table-badge {
            background: var(--gold-subtle);
            border: 1px solid var(--border-strong);
            border-radius: 20px;
            padding: 6px 16px;
            display: flex; align-items: center; gap: 8px;
            background: rgba(201, 165, 94, 0.06);
            border: 1px solid var(--border-default);
            border-radius: var(--r-full);
            padding: 7px 18px;
            font-size: 13px; font-weight: 500;
            color: var(--gold);
            color: var(--gold-300);
        }
        .table-badge .dot {
            width: 6px; height: 6px;
            background: var(--green);
            border-radius: 50%;
            box-shadow: 0 0 8px var(--green-glow);
            animation: liveDot 2s ease-in-out infinite;
        }
        @keyframes liveDot {
            0%, 100% { opacity: 1; } 50% { opacity: 0.4; }
        }
        .new-customer-btn {
        .btn-reset {
            background: transparent;
            border: 1px solid var(--border);
            border-radius: 20px;
            padding: 8px 18px;
            font-family: var(--font-body);
            font-size: 12px; font-weight: 500;
            color: var(--text-secondary);
            border: 1px solid var(--border-subtle);
            border-radius: var(--r-full);
            padding: 7px 16px;
            font-family: var(--f-body);
            font-size: 11px; font-weight: 500;
            color: var(--text-muted);
            cursor: pointer;
            transition: all 0.3s var(--ease-out);
            transition: all 0.3s var(--ease);
            letter-spacing: 0.5px;
        }
        .new-customer-btn:hover {
            border-color: var(--danger);
            color: var(--danger);
            background: rgba(224, 85, 85, 0.08);
        .btn-reset:hover {
            border-color: var(--red);
            color: var(--red);
            background: rgba(232, 84, 84, 0.06);
        }
        /* ═══════════════════════════════════════════
           CHAT AREA
           ═══════════════════════════════════════════ */
        /* ══════════════════════════════════════════════════════════
           ██  CHAT AREA
           ══════════════════════════════════════════════════════════ */
        .chat-area {
            flex: 1;
            overflow-y: auto;
            padding: 24px 28px;
            overflow-x: hidden;
            padding: 20px 28px 8px;
            scroll-behavior: smooth;
        }
        .chat-area::-webkit-scrollbar { width: 4px; }
        .chat-area::-webkit-scrollbar { width: 3px; }
        .chat-area::-webkit-scrollbar-track { background: transparent; }
        .chat-area::-webkit-scrollbar-thumb {
            background: rgba(201, 169, 110, 0.2);
            border-radius: 4px;
            background: rgba(201, 165, 94, 0.15);
            border-radius: 10px;
        }
        /* Welcome Card */
        .welcome-card {
        /* ── Welcome Section ── */
        .welcome {
            text-align: center;
            padding: 48px 24px 32px;
            animation: fadeInUp 0.8s var(--ease-out);
            padding: 36px 16px 20px;
            animation: welcomeFadeIn 1s var(--ease) both;
        }
        .welcome-icon {
            font-size: 56px;
            display: block;
            margin-bottom: 16px;
            animation: gentleBounce 3s ease-in-out infinite;
        @keyframes welcomeFadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to   { opacity: 1; transform: translateY(0); }
        }
        .welcome-card h2 {
            font-family: var(--font-display);
            font-size: 28px; font-weight: 600;
            color: var(--gold);
            margin-bottom: 12px;
        .welcome-emblem {
            width: 80px; height: 80px;
            margin: 0 auto 20px;
            border-radius: 50%;
            background: linear-gradient(135deg, rgba(201, 165, 94, 0.08), rgba(201, 165, 94, 0.02));
            border: 1px solid var(--border-default);
            display: flex; align-items: center; justify-content: center;
            font-size: 36px;
            position: relative;
            animation: emblemFloat 4s ease-in-out infinite;
        }
        .welcome-card p {
            font-size: 15px; color: var(--text-secondary);
            line-height: 1.7;
            max-width: 400px; margin: 0 auto;
        .welcome-emblem::before {
            content: '';
            position: absolute; inset: -8px;
            border-radius: 50%;
            border: 1px dashed var(--border-subtle);
            animation: emblemSpin 30s linear infinite;
        }
        .quick-actions {
        @keyframes emblemFloat {
            0%, 100% { transform: translateY(0); }
            50%      { transform: translateY(-8px); }
        }
        @keyframes emblemSpin {
            from { transform: rotate(0deg); } to { transform: rotate(360deg); }
        }
        .welcome h2 {
            font-family: var(--f-display);
            font-size: 30px; font-weight: 400;
            color: var(--gold-100);
            margin-bottom: 10px;
            letter-spacing: 1px;
        }
        .welcome p {
            font-size: 14px; font-weight: 300;
            color: var(--text-secondary);
            line-height: 1.8;
            max-width: 440px; margin: 0 auto;
        }
        /* Quick action chips */
        .quick-chips {
            display: flex; flex-wrap: wrap;
            justify-content: center; gap: 8px;
            margin-top: 24px;
            margin-top: 28px;
        }
        .quick-action-btn {
        .chip {
            display: inline-flex; align-items: center; gap: 6px;
            background: var(--bg-glass);
            border: 1px solid var(--border);
            border-radius: 20px;
            border: 1px solid var(--border-subtle);
            border-radius: var(--r-full);
            padding: 10px 20px;
            font-family: var(--font-body);
            font-family: var(--f-body);
            font-size: 13px; font-weight: 400;
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.3s var(--ease-out);
            transition: all 0.35s var(--ease);
            position: relative;
            overflow: hidden;
        }
        .quick-action-btn:hover {
            background: var(--gold-subtle);
            border-color: var(--gold);
            color: var(--gold);
            transform: translateY(-1px);
        .chip::before {
            content: '';
            position: absolute; inset: 0;
            background: linear-gradient(135deg, rgba(201, 165, 94, 0.08), transparent);
            opacity: 0;
            transition: opacity 0.35s;
        }
        .chip:hover::before { opacity: 1; }
        .chip:hover {
            border-color: var(--gold-400);
            color: var(--gold-200);
            transform: translateY(-2px);
            box-shadow: 0 4px 16px rgba(201, 165, 94, 0.08);
        }
        .chip:active { transform: scale(0.96); }
        .chip .chip-icon { font-size: 15px; }
        /* Chat Messages */
        .message-row {
        /* ── Message Rows ── */
        .msg {
            display: flex; gap: 12px;
            margin-bottom: 20px;
            animation: messageSlideIn 0.4s var(--ease-out);
            max-width: 85%;
            margin-bottom: 22px;
            max-width: 80%;
            animation: msgIn 0.45s var(--ease) both;
        }
        .message-row.user {
        .msg.user {
            flex-direction: row-reverse;
            margin-left: auto;
        }
        .message-avatar {
            width: 36px; height: 36px;
            border-radius: 12px;
        @keyframes msgIn {
            from { opacity: 0; transform: translateY(14px) scale(0.97); }
            to   { opacity: 1; transform: translateY(0) scale(1); }
        }
        .msg-avatar {
            width: 38px; height: 38px;
            border-radius: var(--r-sm);
            flex-shrink: 0;
            display: flex; align-items: center; justify-content: center;
            font-size: 16px;
            font-size: 15px;
            margin-top: 2px;
        }
        .message-row.ai .message-avatar {
            background: linear-gradient(135deg, var(--gold), var(--gold-light));
            box-shadow: 0 2px 12px rgba(201, 169, 110, 0.2);
        .msg.ai .msg-avatar {
            background: linear-gradient(135deg, var(--gold-400), var(--gold-300));
            box-shadow: 0 3px 14px rgba(201, 165, 94, 0.2);
            color: var(--bg-void);
            font-family: var(--f-display);
            font-weight: 600; font-size: 18px;
        }
        .message-row.user .message-avatar {
            background: var(--bg-glass);
            border: 1px solid var(--border);
        .msg.user .msg-avatar {
            background: var(--bg-glass-2);
            border: 1px solid var(--border-default);
        }
        .message-bubble {
            padding: 14px 18px;
            border-radius: var(--radius-md);
        .msg-body { min-width: 0; }
        .msg-bubble {
            padding: 15px 20px;
            font-size: 14.5px;
            line-height: 1.7;
            line-height: 1.75;
            word-wrap: break-word;
            white-space: pre-wrap;
            border-radius: var(--r-md);
            position: relative;
        }
        .message-row.ai .message-bubble {
            background: linear-gradient(135deg, rgba(201, 169, 110, 0.06), rgba(201, 169, 110, 0.02));
            border: 1px solid var(--border);
        .msg.ai .msg-bubble {
            background: linear-gradient(160deg, rgba(201, 165, 94, 0.055), rgba(201, 165, 94, 0.015));
            border: 1px solid var(--border-subtle);
            border-top-left-radius: var(--r-xs);
            color: var(--text-primary);
            border-top-left-radius: 4px;
        }
        .message-row.user .message-bubble {
            background: linear-gradient(135deg, rgba(201, 169, 110, 0.15), rgba(201, 169, 110, 0.08));
            border: 1px solid var(--border-strong);
            color: var(--text-primary);
            border-top-right-radius: 4px;
        .msg.user .msg-bubble {
            background: linear-gradient(160deg, rgba(201, 165, 94, 0.12), rgba(201, 165, 94, 0.05));
            border: 1px solid var(--border-default);
            border-top-right-radius: var(--r-xs);
            color: var(--text-white);
        }
        .message-meta {
            display: flex; align-items: center; gap: 6px;
        .msg-time {
            font-size: 10.5px;
            color: var(--text-ghost);
            margin-top: 6px;
            font-size: 11px;
            color: var(--text-muted);
            display: flex; align-items: center; gap: 5px;
        }
        .message-row.user .message-meta { justify-content: flex-end; }
        .msg.user .msg-time { justify-content: flex-end; }
        .voice-badge {
            display: inline-flex; align-items: center; gap: 4px;
            font-size: 11px; color: var(--gold);
            margin-bottom: 6px;
        .msg-voice-tag {
            display: inline-flex; align-items: center; gap: 5px;
            font-size: 11px; color: var(--gold-400);
            margin-bottom: 8px;
            font-weight: 500;
        }
        /* Typing Indicator */
        /* ── Typing Indicator ── */
        .typing-row {
            display: flex; gap: 12px;
            margin-bottom: 20px;
            animation: fadeIn 0.3s var(--ease-out);
            margin-bottom: 22px;
            animation: fadeIn 0.3s var(--ease);
        }
        .typing-dots {
            display: flex; gap: 5px;
            padding: 16px 20px;
            background: linear-gradient(135deg, rgba(201, 169, 110, 0.06), rgba(201, 169, 110, 0.02));
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            border-top-left-radius: 4px;
        .typing-row .msg-avatar {
            background: linear-gradient(135deg, var(--gold-400), var(--gold-300));
            box-shadow: 0 3px 14px rgba(201, 165, 94, 0.2);
            color: var(--bg-void);
            font-family: var(--f-display);
            font-weight: 600; font-size: 18px;
            width: 38px; height: 38px;
            border-radius: var(--r-sm);
            display: flex; align-items: center; justify-content: center;
        }
        .typing-dots span {
            width: 7px; height: 7px;
            background: var(--gold);
        .typing-bubble {
            display: flex; align-items: center; gap: 5px;
            padding: 18px 22px;
            background: linear-gradient(160deg, rgba(201, 165, 94, 0.055), rgba(201, 165, 94, 0.015));
            border: 1px solid var(--border-subtle);
            border-radius: var(--r-md);
            border-top-left-radius: var(--r-xs);
        }
        .typing-bubble span {
            width: 6px; height: 6px;
            background: var(--gold-400);
            border-radius: 50%;
            animation: typingPulse 1.4s ease-in-out infinite;
            animation: typingDance 1.4s ease-in-out infinite;
        }
        .typing-dots span:nth-child(2) { animation-delay: 0.2s; }
        .typing-dots span:nth-child(3) { animation-delay: 0.4s; }
        .typing-bubble span:nth-child(2) { animation-delay: 0.15s; }
        .typing-bubble span:nth-child(3) { animation-delay: 0.3s; }
        /* ═══════════════════════════════════════════
           INPUT AREA
           ═══════════════════════════════════════════ */
        @keyframes typingDance {
            0%, 60%, 100% { transform: translateY(0); opacity: 0.3; }
            30%            { transform: translateY(-8px); opacity: 1; }
        }
        /* ══════════════════════════════════════════════════════════
           ██  INPUT AREA
           ══════════════════════════════════════════════════════════ */
        .input-area {
            flex-shrink: 0;
            padding: 16px 28px 24px;
            background: linear-gradient(0deg, rgba(12, 12, 20, 0.98) 0%, rgba(12, 12, 20, 0.85) 100%);
            backdrop-filter: blur(16px);
            border-top: 1px solid var(--border);
            padding: 14px 28px 26px;
            position: relative;
        }
        .input-area::before {
            content: '';
            position: absolute; top: 0; left: 10%; right: 10%; height: 1px;
            background: linear-gradient(90deg, transparent, var(--border-subtle), transparent);
        }
        .input-container {
            display: flex; align-items: center; gap: 10px;
        .input-wrap {
            display: flex; align-items: center; gap: 8px;
            background: var(--bg-glass);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 6px 6px 6px 20px;
            transition: border-color 0.3s var(--ease-out), box-shadow 0.3s var(--ease-out);
            border: 1px solid var(--border-subtle);
            border-radius: var(--r-xl);
            padding: 5px 5px 5px 22px;
            transition: all 0.4s var(--ease);
            position: relative;
        }
        .input-container:focus-within {
            border-color: var(--gold);
            box-shadow: 0 0 0 3px rgba(201, 169, 110, 0.08);
        .input-wrap:focus-within {
            border-color: var(--gold-500);
            box-shadow: 0 0 0 4px rgba(201, 165, 94, 0.05), var(--shadow-gold);
        }
        .input-container input {
        .input-wrap input {
            flex: 1;
            background: transparent;
            border: none; outline: none;
            font-family: var(--font-body);
            background: none; border: none; outline: none;
            font-family: var(--f-body);
            font-size: 15px; font-weight: 400;
            color: var(--text-primary);
            padding: 10px 0;
            color: var(--text-white);
            padding: 12px 0;
            min-width: 0;
        }
        .input-container input::placeholder {
            color: var(--text-muted);
        .input-wrap input::placeholder {
            color: var(--text-ghost);
            font-weight: 300;
        }
        .btn-icon {
            width: 44px; height: 44px;
            border-radius: 14px;
        .btn-circle {
            width: 46px; height: 46px;
            border-radius: var(--r-md);
            border: none;
            display: flex; align-items: center; justify-content: center;
            cursor: pointer;
            transition: all 0.3s var(--ease-out);
            transition: all 0.35s var(--ease);
            flex-shrink: 0;
            position: relative;
            overflow: hidden;
        }
        .btn-circle svg {
            width: 20px; height: 20px;
            stroke: currentColor;
            stroke-width: 2; fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
            position: relative; z-index: 1;
        }
        .send-btn {
            background: linear-gradient(135deg, var(--gold), var(--gold-light));
            color: var(--bg-deep);
            box-shadow: 0 4px 16px rgba(201, 169, 110, 0.3);
        /* Mic Button */
        .btn-mic {
            background: var(--bg-glass-2);
            border: 1px solid var(--border-subtle) !important;
            color: var(--text-secondary);
        }
        .send-btn:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 24px rgba(201, 169, 110, 0.4);
        .btn-mic:hover {
            border-color: var(--gold-400) !important;
            color: var(--gold-300);
            background: rgba(201, 165, 94, 0.06);
        }
        .send-btn:active { transform: scale(0.95); }
        .send-btn:disabled {
            opacity: 0.3;
            cursor: not-allowed;
            transform: none;
            box-shadow: none;
        .btn-mic.recording {
            color: var(--red);
            border-color: var(--red) !important;
            background: rgba(232, 84, 84, 0.08);
            animation: micPulse 1.5s ease-in-out infinite;
        }
        @keyframes micPulse {
            0%, 100% { box-shadow: 0 0 0 0 var(--red-glow); }
            50%      { box-shadow: 0 0 0 10px rgba(232, 84, 84, 0); }
        }
        .mic-btn {
            background: var(--bg-glass);
            border: 1px solid var(--border) !important;
            color: var(--text-secondary);
        /* Send Button */
        .btn-send {
            background: linear-gradient(135deg, var(--gold-400), var(--gold-500));
            color: var(--bg-void);
            box-shadow: 0 4px 20px rgba(201, 165, 94, 0.25);
        }
        .mic-btn:hover {
            border-color: var(--gold) !important;
            color: var(--gold);
            background: var(--gold-subtle);
        .btn-send::before {
            content: '';
            position: absolute; inset: 0;
            border-radius: var(--r-md);
            background: linear-gradient(135deg, var(--gold-300), var(--gold-400));
            opacity: 0;
            transition: opacity 0.35s;
        }
        .mic-btn.recording {
            background: rgba(224, 85, 85, 0.15);
            border-color: var(--danger) !important;
            color: var(--danger);
            animation: recordPulse 1.5s ease-in-out infinite;
        .btn-send:hover::before { opacity: 1; }
        .btn-send:hover {
            transform: scale(1.06);
            box-shadow: 0 6px 28px rgba(201, 165, 94, 0.35);
        }
        /* SVG Icons */
        .btn-icon svg {
            width: 20px; height: 20px;
            stroke: currentColor;
            stroke-width: 2;
            fill: none;
            stroke-linecap: round;
            stroke-linejoin: round;
        .btn-send:active { transform: scale(0.95); }
        .btn-send:disabled {
            opacity: 0.25;
            cursor: default;
            transform: none !important;
            box-shadow: none !important;
        }
        .btn-send:disabled::before { display: none; }
        /* ═══════════════════════════════════════════
           RECORDING OVERLAY
           ═══════════════════════════════════════════ */
        .recording-overlay {
        /* ══════════════════════════════════════════════════════════
           ██  RECORDING OVERLAY
           ══════════════════════════════════════════════════════════ */
        .rec-overlay {
            position: fixed; inset: 0;
            background: rgba(5, 5, 10, 0.88);
            backdrop-filter: blur(24px);
            display: flex; align-items: center; justify-content: center;
            background: rgba(3, 3, 6, 0.90);
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            display: flex; align-items: center; justify-content: center; flex-direction: column;
            z-index: 500;
            animation: fadeIn 0.3s var(--ease-out);
            animation: fadeIn 0.3s var(--ease);
        }
        .recording-overlay.hidden { display: none; }
        .rec-overlay.hidden { display: none !important; }
        .recording-content {
            text-align: center;
        }
        .recording-visual {
        .rec-rings {
            position: relative;
            width: 140px; height: 140px;
            margin: 0 auto 28px;
            width: 160px; height: 160px;
            margin-bottom: 32px;
        }
        .recording-circle {
            position: absolute;
            inset: 0;
        .rec-ring {
            position: absolute; inset: 0;
            border-radius: 50%;
            border: 2px solid var(--danger);
            animation: recordRipple 2s ease-out infinite;
            border: 1.5px solid var(--red);
            animation: ringExpand 2.5s ease-out infinite;
        }
        .recording-circle:nth-child(2) { animation-delay: 0.5s; }
        .recording-circle:nth-child(3) { animation-delay: 1s; }
        .recording-core {
        .rec-ring:nth-child(2) { animation-delay: 0.6s; }
        .rec-ring:nth-child(3) { animation-delay: 1.2s; }
        @keyframes ringExpand {
            0%   { transform: scale(0.4); opacity: 0.7; }
            100% { transform: scale(1.5); opacity: 0; }
        }
        .rec-core {
            position: absolute;
            top: 50%; left: 50%;
            transform: translate(-50%, -50%);
            width: 60px; height: 60px;
            background: linear-gradient(135deg, var(--danger), #c44);
            width: 72px; height: 72px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--red), #c44040);
            display: flex; align-items: center; justify-content: center;
            box-shadow: 0 0 40px rgba(224, 85, 85, 0.3);
            box-shadow: 0 0 50px rgba(232, 84, 84, 0.25);
        }
        .recording-core svg {
            width: 28px; height: 28px;
            stroke: white; fill: none;
            stroke-width: 2;
        .rec-core svg {
            width: 32px; height: 32px;
            stroke: white; fill: none; stroke-width: 1.8;
        }
        .recording-timer {
            font-family: var(--font-body);
            font-size: 32px; font-weight: 300;
            color: var(--text-primary);
            margin-bottom: 8px;
            font-variant-numeric: tabular-nums;
        /* Waveform bars */
        .rec-wave {
            display: flex; align-items: center; gap: 3px;
            height: 40px;
            margin-bottom: 24px;
        }
        .recording-label {
            font-size: 13px; color: var(--danger);
            letter-spacing: 2px; text-transform: uppercase;
            margin-bottom: 32px;
        .rec-wave .bar {
            width: 3px;
            background: var(--red);
            border-radius: 2px;
            animation: waveBar 0.8s ease-in-out infinite alternate;
        }
        .stop-btn {
            background: rgba(224, 85, 85, 0.12);
            border: 1px solid rgba(224, 85, 85, 0.3);
            border-radius: 28px;
            padding: 14px 36px;
            font-family: var(--font-body);
            font-size: 14px; font-weight: 500;
            color: var(--danger);
            cursor: pointer;
            transition: all 0.3s var(--ease-out);
        @keyframes waveBar {
            0%   { height: 6px; opacity: 0.4; }
            100% { height: 36px; opacity: 1; }
        }
        .stop-btn:hover {
            background: rgba(224, 85, 85, 0.2);
            transform: scale(1.02);
        }
        /* ═══════════════════════════════════════════
           ANIMATIONS
           ═══════════════════════════════════════════ */
        @keyframes fadeIn {
            from { opacity: 0; } to { opacity: 1; }
        .rec-timer {
            font-family: var(--f-mono);
            font-size: 36px; font-weight: 400;
            color: var(--text-white);
            letter-spacing: 4px;
            margin-bottom: 6px;
        }
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(24px); }
            to { opacity: 1; transform: translateY(0); }
        .rec-label {
            font-size: 12px; color: var(--red);
            letter-spacing: 3px; text-transform: uppercase;
            font-weight: 500;
            margin-bottom: 36px;
            display: flex; align-items: center; gap: 8px;
        }
        @keyframes modalSlideUp {
            from { opacity: 0; transform: translateY(40px) scale(0.96); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        .rec-label .blink {
            width: 7px; height: 7px;
            background: var(--red);
            border-radius: 50%;
            animation: blink 1s step-end infinite;
        }
        @keyframes messageSlideIn {
            from { opacity: 0; transform: translateY(12px); }
            to { opacity: 1; transform: translateY(0); }
        @keyframes blink {
            0%, 100% { opacity: 1; } 50% { opacity: 0; }
        }
        @keyframes gentleBounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-6px); }
        .btn-stop {
            background: rgba(232, 84, 84, 0.1);
            border: 1px solid rgba(232, 84, 84, 0.25);
            border-radius: var(--r-full);
            padding: 15px 40px;
            font-family: var(--f-body);
            font-size: 14px; font-weight: 500;
            color: var(--text-white);
            cursor: pointer;
            transition: all 0.3s var(--ease);
            letter-spacing: 1px;
        }
        @keyframes typingPulse {
            0%, 60%, 100% { opacity: 0.3; transform: scale(0.8); }
            30% { opacity: 1; transform: scale(1); }
        .btn-stop:hover {
            background: rgba(232, 84, 84, 0.18);
            border-color: var(--red);
            transform: scale(1.03);
        }
        @keyframes recordPulse {
            0%, 100% { box-shadow: 0 0 0 0 rgba(224, 85, 85, 0.3); }
            50% { box-shadow: 0 0 0 8px rgba(224, 85, 85, 0); }
        /* ══════════════════════════════════════════════════════════
           ██  ANIMATIONS
           ══════════════════════════════════════════════════════════ */
        @keyframes fadeIn {
            from { opacity: 0; } to { opacity: 1; }
        }
        @keyframes recordRipple {
            0% { transform: scale(0.5); opacity: 0.6; }
            100% { transform: scale(1.4); opacity: 0; }
        @keyframes modalEnter {
            from { opacity: 0; transform: translateY(30px) scale(0.95); }
            to   { opacity: 1; transform: translateY(0) scale(1); }
        }
        /* ═══════════════════════════════════════════
           RESPONSIVE
           ═══════════════════════════════════════════ */
        @media (max-width: 600px) {
            .modal-card { padding: 32px 24px; }
        /* ══════════════════════════════════════════════════════════
           ██  RESPONSIVE
           ══════════════════════════════════════════════════════════ */
        @media (max-width: 640px) {
            .modal-card { padding: 36px 24px 32px; }
            .modal-brand { font-size: 34px; letter-spacing: 4px; }
            .table-grid { grid-template-columns: repeat(4, 1fr); }
            .header { padding: 12px 16px; }
            .chat-area { padding: 16px; }
            .input-area { padding: 12px 16px 20px; }
            .welcome-card { padding: 32px 16px 24px; }
            .message-row { max-width: 92%; }
            .header-title { font-size: 20px; letter-spacing: 2px; }
            .chat-area { padding: 16px 16px 8px; }
            .input-area { padding: 10px 16px 20px; }
            .msg { max-width: 90%; }
            .welcome { padding: 24px 8px 16px; }
        }
        @media (min-width: 1024px) {
            .chat-area { padding: 32px 10%; }
            .input-area { padding: 16px 10% 28px; }
            .chat-area { padding: 28px 12% 8px; }
            .input-area { padding: 14px 12% 28px; }
        }
        /* ══════════════════════════════════════════════════════════
           ██  SELECTION & FOCUS
           ══════════════════════════════════════════════════════════ */
        ::selection {
            background: rgba(201, 165, 94, 0.25);
            color: var(--gold-100);
        }
    </style>
</head>
<body>
    <!-- ═══════════ ANIMATED BACKGROUND ═══════════ -->
    <div class="bg-layer" id="bgLayer" aria-hidden="true">
        <div class="bg-aurora"></div>
        <div class="bg-noise"></div>
    </div>
    <!-- ═══════════ TABLE SELECTION MODAL ═══════════ -->
    <div id="tableModal" class="modal-overlay">
        <div class="modal-card">
            <span class="modal-icon">✦</span>
            <h2>Mood AI</h2>
            <p class="modal-subtitle">Premium Restoran</p>
            <p class="modal-prompt">Masa nömrənizi seçin</p>
            <div class="modal-ornament">
                <span class="line"></span>
                <span class="diamond"></span>
                <span class="line"></span>
            </div>
            <div class="modal-brand">MOOD AI</div>
            <div class="modal-tagline">premium restoran</div>
            <p class="modal-prompt">Masanızı seçin</p>
            <div class="table-grid" id="tableGrid"></div>
        </div>
    </div>
    <!-- ═══════════ MAIN APP ═══════════ -->
    <div id="app" class="app hidden">
        <!-- Header -->
        <header class="header">
            <div class="header-brand">
                <div class="header-logo">✦</div>
                <div class="header-logo"><span>M</span></div>
                <div>
                    <h1>Mood AI</h1>
                    <span>premium restoran</span>
                    <div class="header-title">MOOD AI</div>
                    <div class="header-subtitle">premium restoran</div>
                </div>
            </div>
            <div class="header-right">
                <div class="table-badge">🍽 Masa <span id="tableDisplay">1</span></div>
                <button class="new-customer-btn" id="newCustomerBtn" title="Sessiyanı sıfırla">Yeni Müştəri</button>
                <div class="table-badge">
                    <span class="dot"></span>
                    Masa <strong id="tableDisplay">1</strong>
                </div>
                <button class="btn-reset" id="btnReset">Yeni Müştəri</button>
            </div>
        </header>
        <!-- Chat Area -->
        <!-- Chat -->
        <main class="chat-area" id="chatArea">
            <div class="welcome-card" id="welcomeCard">
                <span class="welcome-icon">👨‍🍳</span>
            <div class="welcome" id="welcomeSection">
                <div class="welcome-emblem">👨‍🍳</div>
                <h2>Xoş gəlmisiniz!</h2>
                <p>Mən sizin rəqəmsal Baş Şefinizəm. Menyumuzu nəzərdən keçirin, tövsiyə alın və ya birbaşa sifariş verin — yazılı və ya səsli!</p>
                <div class="quick-actions">
                    <button class="quick-action-btn" data-msg="Menyunu göstər">📋 Menyu</button>
                    <button class="quick-action-btn" data-msg="Şefin məsləhəti nədir?">👨‍🍳 Şefin tövsiyəsi</button>
                    <button class="quick-action-btn" data-msg="Günün xüsusi yeməyi nədir?">⭐ Günün xüsusi</button>
                    <button class="quick-action-btn" data-msg="Veqan seçimləriniz var?">🌱 Veqan</button>
                <p>Mən sizin rəqəmsal Baş Şefinizəm. Menyumuzu araşdırın, tövsiyə alın və ya birbaşa sifariş verin — həm yazılı, həm də səsli.</p>
                <div class="quick-chips">
                    <button class="chip" data-msg="Menyunu göstər"><span class="chip-icon">📋</span> Menyu</button>
                    <button class="chip" data-msg="Şefin məsləhəti nədir?"><span class="chip-icon">⭐</span> Şef tövsiyəsi</button>
                    <button class="chip" data-msg="Günün xüsusi yeməyi nədir?"><span class="chip-icon">🔥</span> Günün xüsusi</button>
                    <button class="chip" data-msg="Veqan seçimləriniz var?"><span class="chip-icon">🌿</span> Veqan</button>
                    <button class="chip" data-msg="Desertləri göstər"><span class="chip-icon">🍰</span> Desertlər</button>
                    <button class="chip" data-msg="İçkilər siyahısı"><span class="chip-icon">🥂</span> İçkilər</button>
                </div>
            </div>
        </main>
        <!-- Input Area -->
        <!-- Input -->
        <footer class="input-area">
            <div class="input-container">
                <input type="text" id="messageInput" placeholder="Mesajınızı yazın..." autocomplete="off" />
                <button class="btn-icon mic-btn" id="micBtn" title="Səsli mesaj">
                    <svg viewBox="0 0 24 24"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>
            <div class="input-wrap">
                <input type="text" id="inputField" placeholder="Mesajınızı yazın..." autocomplete="off" />
                <button class="btn-circle btn-mic" id="btnMic" title="Səsli mesaj">
                    <svg viewBox="0 0 24 24">
                        <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
                        <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
                        <line x1="12" y1="19" x2="12" y2="23"/>
                        <line x1="8" y1="23" x2="16" y2="23"/>
                    </svg>
                </button>
                <button class="btn-icon send-btn" id="sendBtn" title="Göndər" disabled>
                    <svg viewBox="0 0 24 24"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                <button class="btn-circle btn-send" id="btnSend" title="Göndər" disabled>
                    <svg viewBox="0 0 24 24">
                        <path d="M22 2L11 13"/>
                        <path d="M22 2L15 22L11 13L2 9L22 2Z"/>
                    </svg>
                </button>
            </div>
        </footer>
    </div>
    <!-- ═══════════ RECORDING OVERLAY ═══════════ -->
    <div id="recordingOverlay" class="recording-overlay hidden">
        <div class="recording-content">
            <div class="recording-visual">
                <div class="recording-circle"></div>
                <div class="recording-circle"></div>
                <div class="recording-circle"></div>
                <div class="recording-core">
                    <svg viewBox="0 0 24 24"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/></svg>
                </div>
    <div id="recOverlay" class="rec-overlay hidden">
        <div class="rec-rings">
            <div class="rec-ring"></div>
            <div class="rec-ring"></div>
            <div class="rec-ring"></div>
            <div class="rec-core">
                <svg viewBox="0 0 24 24">
                    <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
                </svg>
            </div>
            <div class="recording-timer" id="recordingTimer">00:00</div>
            <div class="recording-label">● Səs yazılır</div>
            <button class="stop-btn" id="stopRecordBtn">Dayandır və Göndər</button>
        </div>
        <div class="rec-wave" id="recWave"></div>
        <div class="rec-timer" id="recTimer">00:00</div>
        <div class="rec-label"><span class="blink"></span> Səs yazılır</div>
        <button class="btn-stop" id="btnStop">Dayandır və Göndər</button>
    </div>
    <!-- ═══════════════════════════════════════════
         JAVASCRIPT
         ═══════════════════════════════════════════ -->
    <!-- ══════════════════════════════════════════════════════════
         ██  JAVASCRIPT
         ══════════════════════════════════════════════════════════ -->
    <script>
    (() => {
        'use strict';
        /* ─── CONFIG ─── */
        /* ═══ CONFIG ═══ */
        const WEBHOOK_URL = 'https://o2nynum8.rcsrv.net/webhook/6eb72414-2f64-45bb-88e9-e58000725f9d';
        const MAX_TABLES = 15;
        const TABLE_COUNT = 15;
        /* ─── STATE ─── */
        let sessionId = localStorage.getItem('mood_session_id') || generateUUID();
        let tableNo = localStorage.getItem('mood_table_no') || null;
        let isRecording = false;
        let mediaRecorder = null;
        /* ═══ STATE ═══ */
        let sessionId   = localStorage.getItem('mood_sid') || uuid();
        let tableNo     = localStorage.getItem('mood_table') || null;
        let sending     = false;
        let recording   = false;
        let recorder    = null;
        let audioChunks = [];
        let recordingInterval = null;
        let recordingStartTime = 0;
        let isSending = false;
        let recInterval = null;
        let recStart    = 0;
        /* ─── DOM ─── */
        const $tableModal   = document.getElementById('tableModal');
        const $tableGrid    = document.getElementById('tableGrid');
        const $app          = document.getElementById('app');
        const $chatArea     = document.getElementById('chatArea');
        const $welcomeCard  = document.getElementById('welcomeCard');
        const $messageInput = document.getElementById('messageInput');
        const $sendBtn      = document.getElementById('sendBtn');
        const $micBtn       = document.getElementById('micBtn');
        const $tableDisplay = document.getElementById('tableDisplay');
        const $newCustomer  = document.getElementById('newCustomerBtn');
        const $recordOverlay = document.getElementById('recordingOverlay');
        const $recordTimer  = document.getElementById('recordingTimer');
        const $stopRecord   = document.getElementById('stopRecordBtn');
        /* ═══ DOM ═══ */
        const $ = id => document.getElementById(id);
        const dom = {
            modal:      $('tableModal'),
            grid:       $('tableGrid'),
            app:        $('app'),
            chat:       $('chatArea'),
            welcome:    $('welcomeSection'),
            input:      $('inputField'),
            btnSend:    $('btnSend'),
            btnMic:     $('btnMic'),
            btnReset:   $('btnReset'),
            tableDisp:  $('tableDisplay'),
            recOverlay: $('recOverlay'),
            recTimer:   $('recTimer'),
            recWave:    $('recWave'),
            btnStop:    $('btnStop'),
            bgLayer:    $('bgLayer'),
        };
        /* ─── UTILITIES ─── */
        function generateUUID() {
        /* ═══ UTILITIES ═══ */
        function uuid() {
            return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, c => {
                const r = Math.random() * 16 | 0;
                return (c === 'x' ? r : (r & 0x3 | 0x8)).toString(16);
            });
        }
        function getTimestamp() {
        function timeNow() {
            return new Date().toLocaleTimeString('az-AZ', { hour: '2-digit', minute: '2-digit' });
        }
        function scrollToBottom() {
            requestAnimationFrame(() => {
                $chatArea.scrollTop = $chatArea.scrollHeight;
            });
        function scrollEnd() {
            requestAnimationFrame(() => dom.chat.scrollTo({ top: dom.chat.scrollHeight, behavior: 'smooth' }));
        }
        /* ─── TABLE SELECTION ─── */
        function buildTableGrid() {
            for (let i = 1; i <= MAX_TABLES; i++) {
        /* ═══ PARTICLES ═══ */
        function spawnParticles(count = 18) {
            for (let i = 0; i < count; i++) {
                const p = document.createElement('div');
                p.className = 'particle';
                const size = 2 + Math.random() * 4;
                p.style.cssText = `
                    width: ${size}px; height: ${size}px;
                    left: ${Math.random() * 100}%;
                    animation-duration: ${12 + Math.random() * 20}s;
                    animation-delay: ${Math.random() * 15}s;
                `;
                dom.bgLayer.appendChild(p);
            }
        }
        /* ═══ WAVE BARS ═══ */
        function buildWave(count = 24) {
            dom.recWave.innerHTML = '';
            for (let i = 0; i < count; i++) {
                const bar = document.createElement('div');
                bar.className = 'bar';
                bar.style.animationDelay = `${(i * 0.07).toFixed(2)}s`;
                bar.style.animationDuration = `${0.5 + Math.random() * 0.6}s`;
                dom.recWave.appendChild(bar);
            }
        }
        /* ═══ TABLE SELECTION ═══ */
        function buildGrid() {
            for (let i = 1; i <= TABLE_COUNT; i++) {
                const btn = document.createElement('button');
                btn.className = 'table-btn';
                btn.textContent = i;
                btn.addEventListener('click', () => selectTable(i));
                $tableGrid.appendChild(btn);
                btn.addEventListener('click', () => pickTable(i));
                dom.grid.appendChild(btn);
            }
        }
        function selectTable(num) {
            tableNo = num;
            localStorage.setItem('mood_table_no', num);
            localStorage.setItem('mood_session_id', sessionId);
            $tableDisplay.textContent = num;
            $tableModal.classList.add('hidden');
            $app.classList.remove('hidden');
            $messageInput.focus();
        function pickTable(n) {
            tableNo = n;
            localStorage.setItem('mood_table', n);
            localStorage.setItem('mood_sid', sessionId);
            dom.tableDisp.textContent = n;
            dom.modal.classList.add('hidden');
            dom.app.classList.remove('hidden');
            dom.input.focus();
        }
        /* ─── CHAT MESSAGES ─── */
        function addMessage(text, type, isVoice = false) {
            // Hide welcome card after first message
            if ($welcomeCard) $welcomeCard.style.display = 'none';
        /* ═══ MESSAGES ═══ */
        function addMsg(text, who, voice = false) {
            if (dom.welcome) dom.welcome.style.display = 'none';
            const row = document.createElement('div');
            row.className = `message-row ${type}`;
            row.className = `msg ${who}`;
            const avatar = document.createElement('div');
            avatar.className = 'message-avatar';
            avatar.textContent = type === 'ai' ? '✦' : '😊';
            const av = document.createElement('div');
            av.className = 'msg-avatar';
            av.textContent = who === 'ai' ? 'M' : '😊';
            const content = document.createElement('div');
            const body = document.createElement('div');
            body.className = 'msg-body';
            if (isVoice && type === 'user') {
                const badge = document.createElement('div');
                badge.className = 'voice-badge';
                badge.innerHTML = '🎤 Səsli mesaj';
                content.appendChild(badge);
            if (voice && who === 'user') {
                const tag = document.createElement('div');
                tag.className = 'msg-voice-tag';
                tag.textContent = '🎤 Səsli mesaj';
                body.appendChild(tag);
            }
            const bubble = document.createElement('div');
            bubble.className = 'message-bubble';
            bubble.className = 'msg-bubble';
            bubble.textContent = text;
            content.appendChild(bubble);
            body.appendChild(bubble);
            const meta = document.createElement('div');
            meta.className = 'message-meta';
            meta.textContent = getTimestamp();
            content.appendChild(meta);
            const time = document.createElement('div');
            time.className = 'msg-time';
            time.textContent = timeNow();
            body.appendChild(time);
            row.appendChild(avatar);
            row.appendChild(content);
            $chatArea.appendChild(row);
            scrollToBottom();
            row.appendChild(av);
            row.appendChild(body);
            dom.chat.appendChild(row);
            scrollEnd();
        }
        function showTypingIndicator() {
        function showTyping() {
            const row = document.createElement('div');
            row.className = 'typing-row';
            row.id = 'typingIndicator';
            const avatar = document.createElement('div');
            avatar.className = 'message-avatar';
            avatar.style.background = 'linear-gradient(135deg, var(--gold), var(--gold-light))';
            avatar.style.boxShadow = '0 2px 12px rgba(201,169,110,0.2)';
            avatar.textContent = '✦';
            const dots = document.createElement('div');
            dots.className = 'typing-dots';
            dots.innerHTML = '<span></span><span></span><span></span>';
            row.appendChild(avatar);
            row.appendChild(dots);
            $chatArea.appendChild(row);
            scrollToBottom();
            row.id = 'typing';
            row.innerHTML = `
                <div class="msg-avatar">M</div>
                <div class="typing-bubble">
                    <span></span><span></span><span></span>
                </div>
            `;
            dom.chat.appendChild(row);
            scrollEnd();
        }
        function removeTypingIndicator() {
            const el = document.getElementById('typingIndicator');
        function hideTyping() {
            const el = $('typing');
            if (el) el.remove();
        }
        /* ─── SEND TEXT MESSAGE ─── */
        async function sendTextMessage(message) {
            if (!message.trim() || isSending) return;
            isSending = true;
            $sendBtn.disabled = true;
            $messageInput.value = '';
        /* ═══ SEND TEXT ═══ */
        async function sendText(msg) {
            if (!msg.trim() || sending) return;
            sending = true;
            dom.btnSend.disabled = true;
            dom.input.value = '';
            addMessage(message, 'user');
            showTypingIndicator();
            addMsg(msg, 'user');
            showTyping();
            try {
                const response = await fetch(WEBHOOK_URL, {
                const res = await fetch(WEBHOOK_URL, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        message: message,
                        message: msg,
                        session_id: sessionId,
                        table_no: `Masa ${tableNo}`,
                        type: 'text'
                    })
                });
                removeTypingIndicator();
                if (!response.ok) throw new Error(`HTTP ${response.status}`);
                const data = await response.json();
                const aiText = data.ai_response || data.output || 'Cavab alına bilmədi.';
                addMessage(aiText, 'ai');
            } catch (err) {
                removeTypingIndicator();
                addMessage('⚠️ Bağlantı xətası. Zəhmət olmasa yenidən cəhd edin.', 'ai');
                console.error('Send error:', err);
                hideTyping();
                if (!res.ok) throw new Error(res.status);
                const data = await res.json();
                addMsg(data.ai_response || data.output || 'Cavab alına bilmədi.', 'ai');
            } catch (e) {
                hideTyping();
                addMsg('⚠️ Bağlantı xətası baş verdi. Yenidən cəhd edin.', 'ai');
                console.error(e);
            } finally {
                isSending = false;
                updateSendButton();
                sending = false;
                syncSendBtn();
            }
        }
        /* ─── SEND AUDIO MESSAGE ─── */
        async function sendAudioMessage(audioBlob) {
            if (isSending) return;
            isSending = true;
            $sendBtn.disabled = true;
        /* ═══ SEND AUDIO ═══ */
        async function sendAudio(blob) {
            if (sending) return;
            sending = true;
            dom.btnSend.disabled = true;
            addMessage('🎤 Səsli mesaj göndərildi...', 'user', true);
            showTypingIndicator();
            addMsg('🎤 Səsli mesaj göndərildi...', 'user', true);
            showTyping();
            try {
                const formData = new FormData();
                formData.append('type', 'audio');
                formData.append('session_id', sessionId);
                formData.append('table_no', `Masa ${tableNo}`);
                formData.append('data', audioBlob, 'recording.webm');
                const fd = new FormData();
                fd.append('type', 'audio');
                fd.append('session_id', sessionId);
                fd.append('table_no', `Masa ${tableNo}`);
                fd.append('data', blob, 'recording.webm');
                const response = await fetch(WEBHOOK_URL, {
                    method: 'POST',
                    body: formData
                });
                removeTypingIndicator();
                if (!response.ok) throw new Error(`HTTP ${response.status}`);
                const data = await response.json();
                const aiText = data.ai_response || data.output || 'Cavab alına bilmədi.';
                addMessage(aiText, 'ai');
            } catch (err) {
                removeTypingIndicator();
                addMessage('⚠️ Səsli mesaj göndərilə bilmədi. Yazılı mesaj yaza bilərsiniz.', 'ai');
                console.error('Audio send error:', err);
                const res = await fetch(WEBHOOK_URL, { method: 'POST', body: fd });
                hideTyping();
                if (!res.ok) throw new Error(res.status);
                const data = await res.json();
                addMsg(data.ai_response || data.output || 'Cavab alına bilmədi.', 'ai');
            } catch (e) {
                hideTyping();
                addMsg('⚠️ Səsli mesaj göndərilə bilmədi.', 'ai');
                console.error(e);
            } finally {
                isSending = false;
                updateSendButton();
                sending = false;
                syncSendBtn();
            }
        }
        /* ─── VOICE RECORDING ─── */
        async function startRecording() {
        /* ═══ RECORDING ═══ */
        async function startRec() {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                let mime = ['audio/webm;codecs=opus', 'audio/webm', 'audio/mp4', '']
                    .find(m => !m || MediaRecorder.isTypeSupported(m));
                // Determine a supported MIME type
                let mimeType = 'audio/webm;codecs=opus';
                if (!MediaRecorder.isTypeSupported(mimeType)) {
                    mimeType = 'audio/webm';
                }
                if (!MediaRecorder.isTypeSupported(mimeType)) {
                    mimeType = 'audio/mp4';
                }
                if (!MediaRecorder.isTypeSupported(mimeType)) {
                    mimeType = ''; // let browser pick default
                }
                mediaRecorder = new MediaRecorder(stream, mimeType ? { mimeType } : {});
                recorder = new MediaRecorder(stream, mime ? { mimeType: mime } : {});
                audioChunks = [];
                mediaRecorder.ondataavailable = e => {
                    if (e.data.size > 0) audioChunks.push(e.data);
                };
                mediaRecorder.onstop = () => {
                recorder.ondataavailable = e => { if (e.data.size) audioChunks.push(e.data); };
                recorder.onstop = () => {
                    stream.getTracks().forEach(t => t.stop());
                    const blob = new Blob(audioChunks, { type: mediaRecorder.mimeType || 'audio/webm' });
                    if (blob.size > 0) sendAudioMessage(blob);
                    const blob = new Blob(audioChunks, { type: recorder.mimeType || 'audio/webm' });
                    if (blob.size > 0) sendAudio(blob);
                };
                mediaRecorder.start(100); // collect data every 100ms
                isRecording = true;
                $micBtn.classList.add('recording');
                $recordOverlay.classList.remove('hidden');
                recordingStartTime = Date.now();
                updateRecordingTimer();
                recordingInterval = setInterval(updateRecordingTimer, 1000);
            } catch (err) {
                console.error('Microphone error:', err);
                addMessage('⚠️ Mikrofona giriş icazəsi verilmədi. Cihaz parametrlərindən icazəni yoxlayın.', 'ai');
                recorder.start(100);
                recording = true;
                dom.btnMic.classList.add('recording');
                dom.recOverlay.classList.remove('hidden');
                recStart = Date.now();
                tickTimer();
                recInterval = setInterval(tickTimer, 1000);
            } catch (e) {
                console.error(e);
                addMsg('⚠️ Mikrofon icazəsi verilmədi. Cihaz parametrlərini yoxlayın.', 'ai');
            }
        }
        function stopRecording() {
            if (mediaRecorder && isRecording) {
                mediaRecorder.stop();
                isRecording = false;
                $micBtn.classList.remove('recording');
                $recordOverlay.classList.add('hidden');
                clearInterval(recordingInterval);
                $recordTimer.textContent = '00:00';
        function stopRec() {
            if (recorder && recording) {
                recorder.stop();
                recording = false;
                dom.btnMic.classList.remove('recording');
                dom.recOverlay.classList.add('hidden');
                clearInterval(recInterval);
                dom.recTimer.textContent = '00:00';
            }
        }
        function updateRecordingTimer() {
            const elapsed = Math.floor((Date.now() - recordingStartTime) / 1000);
            const mins = String(Math.floor(elapsed / 60)).padStart(2, '0');
            const secs = String(elapsed % 60).padStart(2, '0');
            $recordTimer.textContent = `${mins}:${secs}`;
        function tickTimer() {
            const s = Math.floor((Date.now() - recStart) / 1000);
            dom.recTimer.textContent =
                String(Math.floor(s / 60)).padStart(2, '0') + ':' +
                String(s % 60).padStart(2, '0');
        }
        /* ─── UI HELPERS ─── */
        function updateSendButton() {
            $sendBtn.disabled = !$messageInput.value.trim() || isSending;
        /* ═══ UI ═══ */
        function syncSendBtn() {
            dom.btnSend.disabled = !dom.input.value.trim() || sending;
        }
        function resetSession() {
            if (!confirm('Sessiyanı sıfırlamaq istəyirsiniz?\nYeni müştəri üçün söhbət təmizlənəcək.')) return;
            sessionId = generateUUID();
            localStorage.setItem('mood_session_id', sessionId);
            // Clear chat
            const messages = $chatArea.querySelectorAll('.message-row, .typing-row');
            messages.forEach(m => m.remove());
            if ($welcomeCard) $welcomeCard.style.display = '';
            scrollToBottom();
            sessionId = uuid();
            localStorage.setItem('mood_sid', sessionId);
            dom.chat.querySelectorAll('.msg, .typing-row').forEach(n => n.remove());
            if (dom.welcome) dom.welcome.style.display = '';
            scrollEnd();
        }
        /* ─── EVENT LISTENERS ─── */
        $messageInput.addEventListener('input', updateSendButton);
        $messageInput.addEventListener('keydown', e => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                sendTextMessage($messageInput.value);
            }
        /* ═══ EVENTS ═══ */
        dom.input.addEventListener('input', syncSendBtn);
        dom.input.addEventListener('keydown', e => {
            if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendText(dom.input.value); }
        });
        dom.btnSend.addEventListener('click', () => sendText(dom.input.value));
        dom.btnMic.addEventListener('click', () => recording ? stopRec() : startRec());
        dom.btnStop.addEventListener('click', stopRec);
        dom.btnReset.addEventListener('click', resetSession);
        $sendBtn.addEventListener('click', () => {
            sendTextMessage($messageInput.value);
        document.querySelectorAll('.chip').forEach(c => {
            c.addEventListener('click', () => sendText(c.dataset.msg));
        });
        $micBtn.addEventListener('click', () => {
            if (isRecording) {
                stopRecording();
            } else {
                startRecording();
            }
        });
        $stopRecord.addEventListener('click', () => {
            stopRecording();
        });
        $newCustomer.addEventListener('click', resetSession);
        // Quick action buttons
        document.querySelectorAll('.quick-action-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const msg = btn.getAttribute('data-msg');
                if (msg) sendTextMessage(msg);
            });
        });
        /* ─── INIT ─── */
        function init() {
            buildTableGrid();
            if (tableNo) {
                selectTable(tableNo);
            }
        }
        init();
        /* ═══ INIT ═══ */
        buildGrid();
        buildWave();
        spawnParticles();
        if (tableNo) pickTable(tableNo);
    })();
    </script>
</body>
</html>
