import os
from dotenv import load_dotenv

from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

from wordpress_mcp_agent.prompt import PROMPT

load_dotenv()

WP_BASE_URL = os.getenv("WP_BASE_URL")
WP_USERNAME = os.getenv("WP_USERNAME")
WP_APP_PASSWORD = os.getenv("WP_APP_PASSWORD")

root_agent = Agent(
    model="gemini-2.0-flash",
    name="wordpress_mcp_agent",
    instruction=PROMPT,
    tools=[
        MCPToolset(
            connection_params=StdioServerParameters(
                command="npx",
                args=["-y", "@adi.lib/wp-mcp"],
                env={
                    "WP_BASE_URL": WP_BASE_URL,
                    "WP_USERNAME": WP_USERNAME,
                    "WP_APP_PASSWORD": WP_APP_PASSWORD
                },
            )
        ),
    ],
)