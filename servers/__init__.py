from klavis import CreateServerResponse, Klavis
from dotenv import load_dotenv
import os
import importlib
import pkgutil
from typing import Dict, Any

load_dotenv()

klavis_client = Klavis(api_key=os.getenv("KLAVIS_API_KEY"))

# Registry to store all server instances
_server_registry: Dict[str, Any] = {}

def register_server(name: str, server_instance: CreateServerResponse):
    """Register a server instance with the unified server."""
    _server_registry[name] = server_instance

def discover_and_load_servers():
    """Automatically discover and load all server modules in this package."""
    # Get the current package directory
    package_dir = os.path.dirname(__file__)
    
    # Import all modules in the servers package
    for _, module_name, is_pkg in pkgutil.iter_modules([package_dir]):
        if not is_pkg and module_name != "__init__":
            try:
                # Import the module
                module = importlib.import_module(f"servers.{module_name}")
                print(f"Loaded server module: {module_name}")
            except Exception as e:
                print(f"Failed to load server module {module_name}: {e}")

def get_all_servers() -> Dict[str, Any]:
    """Get all server instances that have been registered."""
    return _server_registry


