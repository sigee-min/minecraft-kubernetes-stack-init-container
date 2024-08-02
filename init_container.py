import os
import shutil
import requests

def copy_configs():
    src_directory = "/data/config-tmp/"
    dest_directory = "/data/config/"
    root_directory = "/data/"

    os.makedirs(dest_directory, exist_ok=True)
    os.makedirs(dest_plugin_directory, exist_ok=True)

    files = os.listdir(src_directory)

    for file in files:
        src_path = os.path.join(src_directory, file)
        dest_path = os.path.join(dest_directory, file)
        if file == "server.properties":
            dest_path  = os.path.join(root_directory, file)

        try:
            if os.path.exists(dest_path):
                os.remove(dest_path)

            shutil.copy2(src_path, dest_path)
            print(f"Copied {file} to {dest_path}")

        except OSError as e:
            print(f"Error copying {file} from {src_path} to {dest_path}: {str(e)}")

    print(f"Copied configuration files from {src_directory} to {dest_directory}")

def install_plugins():
    plugin_directory = "/data/plugins/"
    plugin_urls = os.getenv("PLUGIN_URLS", "")

    if not plugin_urls:
        print("No PLUGIN_URLS environment variable set.")
        return

    os.makedirs(plugin_directory, exist_ok=True)

    for url in plugin_urls.split(','):
        try:
            response = requests.get(url)
            response.raise_for_status()
            plugin_name = url.split('/')[-1]
            with open(os.path.join(plugin_directory, plugin_name), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded and saved {plugin_name} to {plugin_directory}")
        except requests.RequestException as e:
            print(f"Failed to download {url}: {str(e)}")

if __name__ == "__main__":
    copy_configs()
    install_plugins()
