# Minecraft Server Configuration and Plugin Installer

This project provides a Dockerized solution for initializing Minecraft server configurations and dynamically installing plugins based on environment variables. It uses Python to manage file operations and downloads, ensuring that your Minecraft server setup is ready with the necessary configurations and plugins before starting.

## Features

- **Configuration Management:** Automatically copies configuration files from a temporary location to the main configuration directory.
- **Plugin Installation:** Downloads and installs Minecraft plugins specified via environment variables directly into the plugin directory of the server.

## Getting Started

### Prerequisites

- Docker
- Python 3.9+
- Internet access for downloading plugins

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sigee-min/minecraft-kubernetes-stack-init-container
   cd minecraft-kubernetes-stack-init-container
   ```

2. **Build the Docker image:**

   ```bash
   docker build -t minecraft-init-container .
   ```

3. **Run the container:**
Ensure to replace <plugin_urls> with the actual URLs of the plugins, comma-separated.

   ```bash
   docker run -e PLUGIN_URLS="<plugin_urls>" -v /path/to/config:/data/config -v /path/to/config-tmp:/data/config-tmp -v /path/to/plugins:/data/plugins minecraft-init-container
   ```