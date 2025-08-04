from servers import klavis_client, register_server
from klavis.types import McpServerName
from webbrowser import open

def create_google_calendar_server():
    """Create and register the Google Calendar server instance."""
    google_calendar_server = klavis_client.mcp_server.create_server_instance(
        server_name=McpServerName.GOOGLE_CALENDAR,
        user_id="user123",
        platform_name="samla-mcp",
    )
    
    open(google_calendar_server.oauth_url)
    
    # Register the server with the registry
    register_server("google_calendar", google_calendar_server)
    
    return google_calendar_server

# Create the server instance when this module is imported
google_calendar_server = create_google_calendar_server()
