from servers import klavis_client, discover_and_load_servers, get_all_servers

"""
Discover and load all server modules
"""
print("Discovering and loading server modules...")
discover_and_load_servers()

"""
Create the unified server
"""
unified_server = klavis_client.mcp_server.create_unified_mcp_server_instance(
    user_id="user123",
    platform_name="samla-mcp",
)

"""
Get all registered servers and relate them to the unified server
"""
all_servers = get_all_servers()
print(f"Found {len(all_servers)} server(s): {list(all_servers.keys())}")

print(f"Unified server URL: {unified_server.server_url}")

input("Press Enter to continue...")