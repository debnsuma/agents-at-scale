import ipywidgets as widgets
from IPython.display import display, HTML, Markdown, display
import json

def select_agent_runtime(agent_runtimes):
    """
    Display a dropdown of agent ARNs and let the user pick one.
    Returns a widgets.Text widget holding the selected ARN.
    """
    agent_arns = [agent['agentRuntimeArn'] for agent in agent_runtimes]

    display(HTML("""
        <div style="
            background-color: #4CAF50; 
            color: white; 
            font-weight: bold; 
            font-size: 16px; 
            padding: 10px; 
            border-radius: 5px; 
            margin-bottom: 10px;
            width: fit-content;">
            🎯 Select an Agent Runtime ARN
        </div>
    """))

    dropdown = widgets.Dropdown(
        options=agent_arns,
        description='',
        layout=widgets.Layout(width='90%')
    )

    dropdown_box = widgets.VBox(
        [dropdown],
        layout=widgets.Layout(
            border='2px solid #4CAF50', 
            padding='10px', 
            border_radius='8px',
            width='95%'
        )
    )

    output = widgets.Output()

    selected_arn = widgets.Text(value='', description='')

    def on_change(change):
        if change['type'] == 'change' and change['name'] == 'value':
            selected_arn.value = change['new']
            with output:
                output.clear_output()
                display(HTML(f"""
                    <div style="
                        background-color: #e7f4e4; 
                        border-left: 5px solid #4CAF50; 
                        padding: 8px; 
                        font-weight: bold;">
                        ✅ Selected ARN: <span style='color: #2e7d32'>{change['new']}</span>
                    </div>
                """))

    dropdown.observe(on_change)

    display(dropdown_box, output)

    return selected_arn


def process_output(response, chat_mode=False):
    """
    Process Bedrock Agent response and display only the text content in Markdown.
    """
    text_output = ""

    if "text/event-stream" in response.get("contentType", ""):
        # Streaming response
        content = []
        for line in response["response"].iter_lines(chunk_size=10):
            if line:
                line = line.decode("utf-8")
                if line.startswith("data: "):
                    line = line[6:]
                    content.append(line)
        try:
            parsed = [json.loads(c) for c in content]
            for part in parsed:
                result = part.get("result", {})
                if isinstance(result, dict):
                    for c in result.get("content", []):
                        text_output += c.get("text", "")
        except Exception as e:
            print("⚠️ Failed to parse streaming content:", e)

    elif response.get("contentType") == "application/json":
        # JSON response
        content = []
        for chunk in response.get("response", []):
            content.append(chunk.decode('utf-8'))
        try:
            parsed = json.loads(''.join(content))
            result = parsed.get("result", {})
            if isinstance(result, dict):
                for c in result.get("content", []):
                    text_output += c.get("text", "")
        except Exception as e:
            print("⚠️ Failed to parse JSON content:", e)

    if text_output and chat_mode:
        html_text = text_output.strip().replace('\n', '<br>')
        display(Markdown(
            f"""<div style="background-color:#f0f8ff; padding:10px; border-radius:8px; border-left:4px solid #4682B4;">
🤖 <strong>Bedrock AgentCore</strong>:<br><br>{html_text}
</div>"""
        ))
    elif text_output:
        display(Markdown(f"### 🤖 Bedrock AgentCore Response\n{text_output.strip()}"))
    else:
        print("⚠️ No text output found in the response.")