# AnyChat Web Application Setup

This document outlines the steps taken to set up the AnyChat web application on an Ubuntu server.

## Directory Setup

1.  The application was cloned into the `/home/scott/anychat` directory.
2.  A Python virtual environment was created in `/home/scott/anychat/venv`.
3.  The application's dependencies were installed using `pip install -r requirements.txt`.

## Systemd Service Setup

1.  A systemd service file was created at `/etc/systemd/system/anychat.service` with the following content:

    ```
    [Unit]
    Description=AnyChat Web Application
    After=network.target

    [Service]
    User=scott
    WorkingDirectory=/home/scott/anychat
    ExecStart=/home/scott/anychat/venv/bin/python /home/scott/anychat/app.py
    Restart=always
    EnvironmentFile=/home/scott/anychat/.env

    [Install]
    WantedBy=multi-user.target
    ```
2.  The systemd daemon was reloaded using `sudo systemctl daemon-reload`.
3.  The service was enabled to start on boot with `sudo systemctl enable anychat`.
4.  The service was started with `sudo systemctl start anychat`.

## Starting and Verifying the Service

-   To start the service, use:
    ```bash
    sudo systemctl start anychat
    ```
-   To restart the service, use:
    ```bash
    sudo systemctl restart anychat
    ```
-   To check the service status, use:
    ```bash
    sudo systemctl status anychat
    ```

## Remote Service Management

To manage the service from your local machine using SSH:

```bash
# Reload systemd, restart service, and check status in one command:
ssh scott@147.93.45.244 "sudo systemctl daemon-reload && sudo systemctl restart anychat && sudo systemctl status anychat"

# View logs remotely:
ssh scott@147.93.45.244 "journalctl -u anychat.service -b"
```

This works because:
1. SSH key authentication allows passwordless login
2. The 'scott' user has sudo privileges
3. Commands can be chained with && to execute in sequence

## Viewing Logs

-   To view the service logs, use:
    ```bash
    journalctl -u anychat.service -b
    ```

## API Keys

The following API keys are required in the `/home/scott/anychat/.env` file:

```
GEMINI_API_KEY=your_gemini_key
OPENAI_API_KEY=your_openai_key
COHERE_API_KEY=your_cohere_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_key
REPLICATE_API_TOKEN=your_replicate_key
PERPLEXITY_API_KEY=your_perplexity_key
FIREWORKS_API_KEY=your_fireworks_key
TOGETHER_API_KEY=your_together_key
ANTHROPIC_API_KEY=your_anthropic_key
GROQ_API_KEY=your_groq_key

## Web Server Configuration

### Nginx Setup
The application uses Nginx to serve both a static landing page and the Gradio interface:

1. Install Nginx:
    ```bash
    sudo apt update && sudo apt install -y nginx
    ```

2. Create a basic landing page:
    ```bash
    echo '<html><body><h1>Under Construction</h1><p>Coming Soon: Paumalu Innovations</p></body></html>' | sudo tee /var/www/html/index.html
    ```

3. Configure Nginx to serve both the landing page and proxy to the Gradio app:
    ```bash
    # Create Nginx configuration
    cat > /etc/nginx/sites-available/paumalu-innovations.online << 'EOL'
    server {
        listen 80;
        server_name paumalu-innovations.online;

        # Serve static landing page at root
        location / {
            root /var/www/html;
            index index.html;
        }

        # Proxy /anychat/ to Gradio interface
        location /anychat/ {
            proxy_pass http://127.0.0.1:7860/;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
    }
    EOL

    # Enable the site
    ln -sf /etc/nginx/sites-available/paumalu-innovations.online /etc/nginx/sites-enabled/
    
    # Test and restart Nginx
    nginx -t && systemctl restart nginx
    ```

### Gradio Interface Configuration
The Gradio interface is configured in app.py to be externally accessible:

```python
if __name__ == "__main__":
    demo.queue(api_open=False).launch(
        server_name="0.0.0.0",  # Make server externally visible
        server_port=7860,       # Default Gradio port
        share=False,            # Don't use Gradio's sharing service
        show_api=False
    )
```

This configuration makes the interface available at:
- Landing Page: http://paumalu-innovations.online/
- Gradio Interface: http://paumalu-innovations.online/anychat/

## Git Commands for Remote Server

### Viewing Changes
- To view changes in a file:
    ```bash
    git diff filename
    ```
    (Press 'q' to exit the diff view)

### Handling Remote Conflicts
If you get conflicts when pulling on the remote server, you have several options:

1. To preserve remote changes:
    ```bash
    # Save remote changes
    git add .
    git commit -m "Save remote changes"
    git pull origin main
    ```

2. To overwrite remote changes with GitHub version:
    ```bash
    # Discard all local changes and pull from GitHub
    git reset --hard HEAD
    git fetch origin
    git reset --hard origin/main
    ```

3. To stash remote changes temporarily:
    ```bash
    # Save changes to stash
    git stash save "Description of changes"
    git pull origin main
    # Optionally reapply stashed changes
    git stash pop
    ```

Choose option 2 if you want to completely overwrite the remote server files with the version from GitHub.
