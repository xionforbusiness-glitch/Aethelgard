/**
 * Aethelgard Sovereign Quick-Switcher HUD
 * Floating executive navigation dock across all templates and Master SPA Hub
 */
(function() {
  // Prevent duplicate injection
  if (document.getElementById('aethelgard-quick-switcher')) return;

  const currentPath = window.location.pathname.replace(/\\/g, '/');

  // Determine relative root for links
  const inSubDir = currentPath.includes('/stitch_ai_agency_platform_website/');
  const prefix = inSubDir ? '' : 'stitch_ai_agency_platform_website/';
  const hubPrefix = inSubDir ? '../' : '';

  const screens = [
    {
      id: 'landing',
      name: 'Vision Landing Page',
      icon: '🌐',
      code: 'I',
      folder: 'aethelgard_product_sovereign_vision_landing_page_celestial_astrolabe_animated',
      url: `${prefix}aethelgard_product_sovereign_vision_landing_page_celestial_astrolabe_animated/code.html`
    },
    {
      id: 'onboarding',
      name: 'Client Onboarding (Rites)',
      icon: '📜',
      code: 'II',
      folder: 'client_onboarding_product_dna_intake_portal',
      url: `${prefix}client_onboarding_product_dna_intake_portal/code.html`
    },
    {
      id: 'cockpit',
      name: 'Command Cockpit',
      icon: '⚔️',
      code: 'III',
      crmView: 'cockpit',
      folder: 'the_sovereign_command_cockpit_master_executive_dashboard',
      url: `${prefix}the_sovereign_command_cockpit_master_executive_dashboard/code.html#cockpit`
    },
    {
      id: 'valerius',
      name: 'Valerius Telephony Studio',
      icon: '📞',
      code: 'IV',
      crmView: 'valerius',
      folder: 'valerius_the_herald_ai_voice_concierge_telephony_studio',
      url: `${prefix}the_sovereign_command_cockpit_master_executive_dashboard/code.html#valerius`
    },
    {
      id: 'daedalus',
      name: 'Daedalus Web Studio',
      icon: '🏛️',
      code: 'V',
      crmView: 'daedalus',
      folder: 'daedalus_the_architect_product_web_studio',
      url: `${prefix}the_sovereign_command_cockpit_master_executive_dashboard/code.html#daedalus`
    },
    {
      id: 'calendar',
      name: 'Omnichannel Chronicle',
      icon: '📅',
      code: 'VI',
      crmView: 'chronicle',
      folder: 'the_omnichannel_chronicle_booked_audiences_calendar',
      url: `${prefix}the_sovereign_command_cockpit_master_executive_dashboard/code.html#chronicle`
    },
    {
      id: 'radar',
      name: 'Argus Attribution Radar',
      icon: '👁️',
      code: 'VII',
      crmView: 'argus',
      folder: 'argus_the_watcher_closed_loop_telemetry_strategic_attribution_radar',
      url: `${prefix}the_sovereign_command_cockpit_master_executive_dashboard/code.html#argus`
    },
    {
      id: 'aurelius',
      name: 'Aurelius Thought Leadership',
      icon: '📜',
      code: 'VIII',
      crmView: 'aurelius',
      folder: 'the_sovereign_command_cockpit_master_executive_dashboard',
      url: `${prefix}the_sovereign_command_cockpit_master_executive_dashboard/code.html#aurelius`
    },
    {
      id: 'slas',
      name: 'Agent SLAs & Tone Tuning',
      icon: '⚙️',
      code: 'IX',
      crmView: 'slas',
      folder: 'the_sovereign_command_cockpit_master_executive_dashboard',
      url: `${prefix}the_sovereign_command_cockpit_master_executive_dashboard/code.html#slas`
    },
    {
      id: 'mobile',
      name: 'Mobile Executive Companion',
      icon: '📱',
      code: 'X',
      folder: 'aethelgard_mobile_executive_companion',
      url: `${prefix}aethelgard_mobile_executive_companion/code.html`
    }
  ];

  // Adjust URLs if we are already inside one of the folders
  const currentFolder = screens.find(s => currentPath.includes(s.folder));

  function getTargetUrl(screen) {
    if (!currentFolder) {
      return screen.url;
    }
    if (screen.crmView) {
      return `../the_sovereign_command_cockpit_master_executive_dashboard/code.html#${screen.crmView}`;
    }
    return `../${screen.folder}/code.html`;
  }

  function getHubUrl() {
    return currentFolder ? '../../index.html' : 'index.html';
  }

  // Create Master Switcher Root (Slide-out Drawer + Edge Trigger)
  const root = document.createElement('div');
  root.id = 'aethelgard-switcher-root';
  root.style.cssText = 'position: relative; z-index: 999999; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;';

  root.innerHTML = `
    <!-- Floating Right-Edge Trigger Pill (Zero Bottom Interference) -->
    <button id="aethelgard-switcher-trigger" 
            title="Open Executive Screen Navigator (Hotkeys: 1-9, Esc to close)"
            style="
              position: fixed;
              top: 50%;
              right: 0;
              transform: translateY(-50%);
              background: rgba(11, 19, 14, 0.94);
              backdrop-filter: blur(16px);
              -webkit-backdrop-filter: blur(16px);
              border: 1px solid rgba(197, 160, 89, 0.4);
              border-right: none;
              border-radius: 12px 0 0 12px;
              padding: 10px 8px 10px 10px;
              display: flex;
              flex-direction: column;
              align-items: center;
              gap: 8px;
              cursor: pointer;
              box-shadow: -4px 0 24px rgba(0, 0, 0, 0.6), 0 0 12px rgba(197, 160, 89, 0.2);
              transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
              z-index: 999999;
            "
            onmouseover="this.style.background='rgba(18, 32, 23, 0.98)'; this.style.transform='translateY(-50%) translateX(-4px)';"
            onmouseout="this.style.background='rgba(11, 19, 14, 0.94)'; this.style.transform='translateY(-50%)';"
    >
      <div style="width: 24px; height: 24px; border-radius: 50%; background: #C5A059; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: bold; color: #070B08;">
        ⚔
      </div>
      <div style="writing-mode: vertical-rl; text-orientation: mixed; font-size: 10px; font-weight: 700; letter-spacing: 0.14em; color: #E5C989; text-transform: uppercase;">
        NAVIGATOR
      </div>
      <div style="width: 6px; height: 6px; border-radius: 50%; background: #2EE59D; box-shadow: 0 0 6px #2EE59D;"></div>
    </button>

    <!-- Backdrop Overlay -->
    <div id="aethelgard-switcher-backdrop" 
         style="
           position: fixed;
           inset: 0;
           background: rgba(4, 7, 5, 0.75);
           backdrop-filter: blur(8px);
           -webkit-backdrop-filter: blur(8px);
           opacity: 0;
           pointer-events: none;
           transition: opacity 0.3s ease;
           z-index: 999998;
         "></div>

    <!-- Slide-Out Navigation Drawer -->
    <div id="aethelgard-switcher-drawer" 
         style="
           position: fixed;
           top: 0;
           right: -420px;
           width: 380px;
           max-width: 90vw;
           height: 100vh;
           background: linear-gradient(180deg, rgba(14, 22, 17, 0.98) 0%, rgba(7, 12, 9, 0.98) 100%);
           border-left: 1px solid rgba(197, 160, 89, 0.3);
           box-shadow: -12px 0 48px rgba(0, 0, 0, 0.85);
           backdrop-filter: blur(24px);
           -webkit-backdrop-filter: blur(24px);
           display: flex;
           flex-direction: column;
           transition: right 0.35s cubic-bezier(0.16, 1, 0.3, 1);
           z-index: 1000000;
         ">
      
      <!-- Drawer Header -->
      <div style="padding: 20px 24px; border-bottom: 1px solid rgba(197, 160, 89, 0.2); display: flex; align-items: center; justify-content: space-between;">
        <div style="display: flex; align-items: center; gap: 10px;">
          <div style="width: 32px; height: 32px; border-radius: 8px; background: rgba(197, 160, 89, 0.15); border: 1px solid rgba(197, 160, 89, 0.4); display: flex; align-items: center; justify-content: center; font-size: 16px;">
            ⚔️
          </div>
          <div>
            <div style="font-size: 14px; font-weight: 700; color: #F3F4F6; letter-spacing: -0.01em;">Aethelgard Conclave</div>
            <div style="font-size: 10px; font-family: monospace; color: #C5A059; text-transform: uppercase; letter-spacing: 0.08em;">Executive Screen Deck</div>
          </div>
        </div>
        <button id="aethelgard-switcher-close" 
                style="background: transparent; border: 1px solid rgba(197, 160, 89, 0.3); border-radius: 6px; width: 28px; height: 28px; display: flex; align-items: center; justify-content: center; color: #E5C989; cursor: pointer; font-size: 14px;"
                title="Close (Esc)">
          ✕
        </button>
      </div>

      <!-- Instructions Bar -->
      <div style="padding: 10px 24px; background: rgba(197, 160, 89, 0.06); border-bottom: 1px solid rgba(197, 160, 89, 0.1); font-size: 11px; color: #9CA3AF; display: flex; align-items: center; justify-content: space-between;">
        <span>Press <strong style="color: #E5C989;">1-9</strong> to jump • <strong style="color: #E5C989;">Esc</strong> to close</span>
        <span style="color: #2EE59D; font-family: monospace; font-weight: 600;">Unified SPA</span>
      </div>

      <!-- Screens List -->
      <div style="flex: 1; overflow-y: auto; padding: 12px 16px; display: flex; flex-direction: column; gap: 6px;">
        ${screens.map((screen, idx) => {
          const isActive = currentFolder && currentFolder.id === screen.id;
          const targetUrl = getTargetUrl(screen);
          return `
            <a href="${targetUrl}" 
               data-crm-view="${screen.crmView || ''}"
               class="aethelgard-screen-link"
               style="
                 display: flex;
                 align-items: center;
                 justify-content: space-between;
                 padding: 10px 14px;
                 border-radius: 10px;
                 text-decoration: none;
                 background: ${isActive ? 'rgba(46, 229, 157, 0.1)' : 'rgba(255, 255, 255, 0.02)'};
                 border: 1px solid ${isActive ? '#2EE59D' : 'rgba(197, 160, 89, 0.15)'};
                 transition: all 0.2s ease;
               "
               onmouseover="if(!${isActive}) { this.style.background='rgba(197, 160, 89, 0.12)'; this.style.borderColor='rgba(197, 160, 89, 0.5)'; }"
               onmouseout="if(!${isActive}) { this.style.background='rgba(255, 255, 255, 0.02)'; this.style.borderColor='rgba(197, 160, 89, 0.15)'; }"
            >
              <div style="display: flex; align-items: center; gap: 12px;">
                <span style="font-size: 18px;">${screen.icon}</span>
                <div>
                  <div style="font-size: 13px; font-weight: 600; color: ${isActive ? '#2EE59D' : '#E5E7EB'};">${screen.name}</div>
                  <div style="font-size: 10px; font-family: monospace; color: #9CA3AF;">Node // ${screen.code}</div>
                </div>
              </div>
              <div style="display: flex; align-items: center; gap: 8px;">
                ${isActive ? '<span style="font-size: 10px; font-family: monospace; color: #2EE59D; background: rgba(46,229,157,0.15); padding: 2px 6px; border-radius: 4px; font-weight: bold;">ACTIVE</span>' : ''}
                <kbd style="font-family: monospace; font-size: 11px; font-weight: bold; padding: 3px 7px; border-radius: 4px; background: rgba(0, 0, 0, 0.5); border: 1px solid rgba(197, 160, 89, 0.4); color: #E5C989;">
                  ${idx + 1}
                </kbd>
              </div>
            </a>
          `;
        }).join('')}
      </div>

      <!-- Drawer Footer -->
      <div style="padding: 16px 20px; border-top: 1px solid rgba(197, 160, 89, 0.2); background: rgba(17, 26, 20, 0.7); display: flex; align-items: center; justify-content: space-between;">
        <a href="${getHubUrl()}" 
           style="
             display: flex;
             align-items: center;
             gap: 8px;
             padding: 8px 14px;
             border-radius: 8px;
             background: rgba(197, 160, 89, 0.15);
             border: 1px solid rgba(197, 160, 89, 0.4);
             color: #E5C989;
             text-decoration: none;
             font-size: 12px;
             font-weight: 600;
             font-family: monospace;
             transition: all 0.2s ease;
           "
           onmouseover="this.style.background='#C5A059'; this.style.color='#070B08';"
           onmouseout="this.style.background='rgba(197, 160, 89, 0.15)'; this.style.color='#E5C989';"
        >
          <span>🏛️</span>
          <span>Master Hub</span>
          <kbd style="font-size: 10px; padding: 1px 4px; background: rgba(0,0,0,0.4); border-radius: 3px;">H</kbd>
        </a>

        <span style="font-size: 10px; font-family: monospace; color: #6B7280;">Aethelgard OS v2.4</span>
      </div>
    </div>
  `;

  document.body.appendChild(root);

  const trigger = document.getElementById('aethelgard-switcher-trigger');
  const drawer = document.getElementById('aethelgard-switcher-drawer');
  const backdrop = document.getElementById('aethelgard-switcher-backdrop');
  const closeBtn = document.getElementById('aethelgard-switcher-close');

  let isOpen = false;

  function openDrawer() {
    isOpen = true;
    drawer.style.right = '0';
    backdrop.style.opacity = '1';
    backdrop.style.pointerEvents = 'auto';
  }

  function closeDrawer() {
    isOpen = false;
    drawer.style.right = '-420px';
    backdrop.style.opacity = '0';
    backdrop.style.pointerEvents = 'none';
  }

  trigger.addEventListener('click', () => {
    if (isOpen) closeDrawer();
    else openDrawer();
  });

  closeBtn.addEventListener('click', closeDrawer);
  backdrop.addEventListener('click', closeDrawer);

  // Intercept links inside drawer if on Unified SPA
  document.querySelectorAll('.aethelgard-screen-link').forEach(link => {
    link.addEventListener('click', (e) => {
      const crmView = link.getAttribute('data-crm-view');
      if (crmView && typeof window.switchView === 'function') {
        e.preventDefault();
        window.switchView(crmView);
        closeDrawer();
      }
    });
  });

  // Global Keyboard Shortcuts (1-9, H, Esc)
  window.addEventListener('keydown', (e) => {
    const tag = e.target.tagName.toLowerCase();
    if (tag === 'input' || tag === 'textarea' || e.target.isContentEditable) return;

    if (e.key === 'Escape') {
      if (isOpen) closeDrawer();
      return;
    }

    if (e.key.toLowerCase() === 'h') {
      window.location.href = getHubUrl();
      return;
    }

    const digit = parseInt(e.key, 10);
    if (!isNaN(digit) && digit >= 1 && digit <= screens.length) {
      const targetScreen = screens[digit - 1];
      if (targetScreen) {
        if (targetScreen.crmView && typeof window.switchView === 'function') {
          window.switchView(targetScreen.crmView);
          closeDrawer();
        } else {
          window.location.href = getTargetUrl(targetScreen);
        }
      }
    }
  });

})();
