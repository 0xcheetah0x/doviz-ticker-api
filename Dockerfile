FROM nginx:alpine

# DAV (WebDAV) için gerekli paketleri ekle
RUN apk add --no-cache nginx-mod-http-dav-ext

# Kendi nginx.conf dosyamızı kopyala
COPY nginx.conf /etc/nginx/nginx.conf

# Statik dosyalar için klasör
RUN mkdir -p /usr/share/nginx/html/hls

# HLS dosyaları buraya yüklenecek
VOLUME ["/usr/share/nginx/html/hls"]

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
