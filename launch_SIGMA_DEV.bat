
@echo off
cd /d %~dp0
start cmd /k "cd backend && uvicorn parser_engine.main_api:app --reload"
start cmd /k "cd frontend && python -m http.server 8080"
