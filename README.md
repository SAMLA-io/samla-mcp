# SAMLA MCP Server

A unified Model Context Protocol (MCP) server for SAMLA systems that enables centralized resource sharing and tool management across all SAMLA components.

## Overview

The SAMLA MCP Server acts as a central hub that allows all SAMLA systems to share the same resources, tools, and services through a single unified interface. This eliminates the need for individual system configurations and provides a consistent experience across the entire SAMLA ecosystem.

## Features

- **Unified Server Architecture**: Single MCP server that manages all connected services
- **Automatic Service Discovery**: Automatically detects and loads all available server modules
- **Centralized Resource Management**: Shared resources, authentication, and tool access
- **Scalable Design**: Easy to add new services and tools without modifying core infrastructure
- **Cross-System Compatibility**: Consistent API and tool access across all SAMLA systems

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    SAMLA MCP Server                        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │ Google      │  │ Other       │  │ Custom      │      │
│  │ Calendar    │  │ Services    │  │ Services    │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
├─────────────────────────────────────────────────────────────┤
│              Unified MCP Interface                         │
└─────────────────────────────────────────────────────────────┘
```

## Quick Start

### Prerequisites

1. Python 3.8+
2. Klavis API key (set as `KLAVIS_API_KEY` environment variable)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/samla-io/samla-mcp.git
cd samla-mcp
```

2. Install dependencies:
```bash
uv sync
```

3. Set up your environment:
```bash
KLAVIS_API_KEY=your_klavis_api_key
```

### Running the Server

```bash
uv run main.py
```

The server will:
1. Automatically discover and load all available service modules
2. Create a unified MCP server instance
3. Register all services with the unified server
4. Display the server URL for client connections

## Adding New Services

To add a new service to the SAMLA MCP Server:

1. Create a new Python file in the `servers/` directory
2. Follow the template pattern (see `servers/README.md` for details)
3. The service will be automatically discovered and loaded

Example service structure:
```python
from servers import klavis_client, register_server
from klavis.types import McpServerName

def create_my_service():
    service = klavis_client.mcp_server.create_server_instance(
        server_name=McpServerName.YOUR_SERVICE,
        user_id="user123",
        platform_name="samla-mcp",
    )
    
    register_server("my_service", service)
    return service

my_service = create_my_service()
```

## Current Services

- **Google Calendar**: Calendar integration and scheduling tools
- *More services can be easily added*

## Configuration

### Environment Variables

- `KLAVIS_API_KEY`: Your Klavis API key for service authentication

### Server Configuration

The server uses the following default configuration:
- User ID: `user123`
- Platform Name: `samla-mcp`

These can be modified in the individual service files or main configuration.

## Integration with SAMLA Systems

SAMLA systems can connect to this MCP server to access:

- **Shared Tools**: Common utilities and functions
- **Centralized Resources**: Database connections, API keys, etc.
- **Unified Authentication**: Single sign-on across all services
- **Consistent APIs**: Standardized interfaces for all operations

## Development

### Project Structure

```
samla-mcp/
├── main.py                 # Main server entry point
├── servers/                # Service modules
│   ├── __init__.py        # Server registry and discovery
│   ├── google_calendar.py # Google Calendar service
│   └── README.md          # Service development guide
├── pyproject.toml         # Project configuration
└── README.md              # This file
```

### Adding New Features

1. **New Services**: Add Python files to the `servers/` directory
2. **Core Functionality**: Modify `main.py` for server-wide changes
3. **Configuration**: Update environment variables or configuration files

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your service or enhancement
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under a propietary license.

## Contributors

- [@jpgtz](https://github.com/jpgtz)