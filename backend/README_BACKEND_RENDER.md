# Backend en Render
Fecha: 2025-10-27

1) Supabase → ejecutá db/schema_supabase.sql y db/seed_supabase.sql
2) Subí tu código backend + este folder `backend/` a un repo
3) Render → Web Service usando blueprint backend/cloud/render/render.yaml
4) Variables: DATABASE_URL (sslmode=require), JWT_SECRET, CORS_ORIGINS
5) Start: uvicorn app:app --host 0.0.0.0 --port $PORT
6) Probar: https://<TU-BACKEND>.onrender.com/docs
