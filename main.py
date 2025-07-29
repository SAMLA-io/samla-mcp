from klavis.types import McpServerName, ToolFormat
from datetime import datetime, timedelta
from dotenv import load_dotenv
from klavis import Klavis
from openai import OpenAI
import webbrowser
import json
import os

load_dotenv()

klavis_client = Klavis(api_key=os.getenv("KLAVIS_API_KEY"))
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

google_calendar_server = klavis_client.mcp_server.create_server_instance(
    server_name=McpServerName.GOOGLE_CALENDAR,
    user_id="mcp-user",
    platform_name="SamlaTest",
)

webbrowser.open(google_calendar_server.oauth_url)

input("Press Enter to continue...")

tools = klavis_client.mcp_server.list_tools(
    server_url=google_calendar_server.server_url,
    format=ToolFormat.OPENAI,
)

# Get available tools in OpenAI format
tools = klavis_client.mcp_server.list_tools(
    server_url=google_calendar_server.server_url,
    format=ToolFormat.OPENAI,
)


# Initial conversation
today = datetime.now().strftime("%Y-%m-%d")
wednesday = (datetime.now() + timedelta(days=2)).strftime("%Y-%m-%d")

messages = [{
    "role": "system",
    "content": "You are a helpful assistant that can help with Google Calendar events. You can create, update, and delete events. You can also get the events for a given day."
}]
while True:
    user_input = input("Enter a command: ")
    if user_input == "exit":
        break
    else:
        user_input = f"Today is {today}. {user_input}"
        messages.append({
            "role": "user",
            "content": user_input
        })

    # First OpenAI call with function calling
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools.tools
    )

    messages.append(response.choices[0].message)

    # Handle tool calls
    if response.choices[0].message.tool_calls:
        for tool_call in response.choices[0].message.tool_calls:
            result = klavis_client.mcp_server.call_tools(
                server_url=google_calendar_server.server_url,
                tool_name=tool_call.function.name,
                tool_args=json.loads(tool_call.function.arguments),
            )
            
            # Add tool result to conversation
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })

    # Second OpenAI call to process tool results and generate final response
    final_response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    print(final_response.choices[0].message.content)