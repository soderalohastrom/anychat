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
