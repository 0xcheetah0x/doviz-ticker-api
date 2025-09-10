FROM alfg/nginx-rtmp:latest

# Nginx config dosyasını kopyala
COPY nginx.conf /etc/nginx/nginx.conf

# RTMP (1935) ve HTTP (80) portlarını aç
EXPOSE 1935 80
