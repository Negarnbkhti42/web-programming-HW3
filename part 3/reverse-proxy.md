note: we also need to change our apis to match this new format

```bash
sudo nano /etc/nginx/sites-available/example.com.conf
```

```
server {
{
    listen 443;
    server_name localhost;

    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $remote_addr;

    location /bank/ {
        proxy_pass https://localhost:8000;
    }
    location /auth/ {
        proxy_pass https://localhost:9000;
    }
    location = /ticket/ {
        proxy_pass https://localhost:3000;
    }
}
```

now our requests are proxied to the desired port.
