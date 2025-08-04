# Server Organization

This directory contains all the individual server implementations that are automatically discovered and loaded by the main application.

## How to Add a New Server

1. Create a new Python file in the `servers/` directory (e.g., `my_new_server.py`)
2. Follow the template structure from `server_template.py`:

```python
from servers import klavis_client, register_server
from klavis.types import McpServerName

def create_my_new_server():
    """Create and register your new server instance."""
    my_server = klavis_client.mcp_server.create_server_instance(
        server_name=McpServerName.YOUR_SERVER_NAME,  # Replace with actual server name
        user_id="user123",
        platform_name="samla-mcp",
    )
    
    # Register the server with the registry
    register_server("my_new_server", my_server)
    
    return my_server

# Create the server instance when this module is imported
my_new_server = create_my_new_server()
```

3. The server will be automatically discovered and loaded when you run `main.py`

## Current Servers

- `google_calendar.py` - Google Calendar integration
- `server_template.py` - Template for creating new servers

## How It Works

1. When `main.py` runs, it calls `discover_and_load_servers()` from `servers/__init__.py`
2. This function automatically imports all Python modules in the `servers/` directory
3. Each server module registers itself with the server registry when imported
4. The unified server can then access all registered servers through the registry

## Notes

- Server modules are imported automatically - you don't need to manually import them
- Each server should register itself using `register_server(name, instance)`
- The server name should be unique across all servers
- Any server-specific initialization (like OAuth flows) should be handled within the server module 