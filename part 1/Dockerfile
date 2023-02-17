FROM nginx
COPY default.conf /etc/nginx/conf.d/default.conf
COPY *.html /usr/share/nginx/html/
COPY *.css /usr/share/nginx/html/
COPY *.svg /usr/share/nginx/html/
COPY scripts/*.js /usr/share/nginx/html/scripts/
COPY assets/* /usr/share/nginx/html/assets/