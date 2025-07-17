import os

os.environ["STRANDS_OTEL_ENABLE_CONSOLE_EXPORT"] = "true"
os.environ["BYPASS_TOOL_CONSENT"]="true"

from strands import Agent
from strands.models import BedrockModel
from strands_tools import file_read, file_write, speak
from bedrock_agentcore import BedrockAgentCoreApp

# Step 1: Define the app 
app = BedrockAgentCoreApp()

# Step 2: Define the system prompt
system_prompt = """
You are a helpful personal assistant capable of performing local file actions and simple tasks for the user.

Your key capabilities:
1. Read, understand, and summarize files.
2. Create and write to files.
3. List directory contents and provide information on the files.
4. Summarize text content

You can use the following tools to perform these actions:
- file_read: Read a file and return the content.
- file_write: Write to a file.
- file_list: List the contents of a directory.
- 'speak': Speak a message to the user.
"""

# Step 3: Define the agent
model_id = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    max_tokens=64000,
    additional_request_fields={
        "thinking": {
            "type":"disabled",
        }
    },
)

agent = Agent(
    model=model_id,
    system_prompt=system_prompt,
    tools=[
        file_read,
        file_write,
        speak,
    ],
)

# Step 4: Run the agent
@app.entrypoint
def invoke(payload):
    """Process user input and return a response"""
    
    user_message = payload.get("prompt", "Hello")
    result = agent(user_message)
    
    return {"result": result.message}

if __name__ == "__main__":
    app.run()

