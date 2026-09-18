@echo off
title Aethelgard 1300s Gothic AI Sovereign - Local Server
echo ========================================================
echo   Aethelgard Sovereign AI Agency Platform
echo   Starting Local HTTP Server on http://localhost:8000 ...
echo ========================================================
echo.
echo Opening browser to Aethelgard Landing Page...
start http://localhost:8000/stitch_ai_agency_platform_website/aethelgard_1300s_gothic_ai_sovereign_landing_page.html
echo.
echo Press Ctrl+C in this window to stop the server at any time.
python -m http.server 8000

