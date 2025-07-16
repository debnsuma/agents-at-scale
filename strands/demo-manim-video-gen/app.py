#!/usr/bin/env python3
from mcp import stdio_client, StdioServerParameters
from strands import Agent
from strands_tools import file_read, file_write, speak
from strands.models import BedrockModel
from strands.tools.mcp import MCPClient
import os
import sys
import subprocess
from pathlib import Path

def check_and_install_packages():
    """Check and install required packages using uv"""
    required_packages = {
        "strands-agents": "latest",
        "manim": "latest",
        "mcp": "latest"
    }
    
    print("Checking and installing required packages...")
    for package, version in required_packages.items():
        try:
            # Check if package is installed
            subprocess.run(
                ["uv", "pip", "show", package],
                capture_output=True,
                check=True
            )
        except subprocess.CalledProcessError:
            print(f"Installing {package}...")
            subprocess.run(
                ["uv", "pip", "install", f"{package}=={version}"],
                check=True
            )
    print("Package installation complete!")

def print_help():
    print("\n=== Manim Video Generation Chat Interface ===")
    print("Available commands:")
    print("  /help     - Show this help message")
    print("  /example  - Show an example Manim animation")
    print("  /samples  - Show sample prompts for demonstrations")
    print("  /install  - Install required packages using uv")
    print("  /status   - Check MCP server status")
    print("  exit/bye  - Exit the program")
    print("\nYou can also:")
    print("  - Ask questions about Manim")
    print("  - Request specific animations")
    print("  - Get help with Manim code")
    print("  - Ask about the generated videos")
    print("\nExample questions:")
    print("  - 'How do I create a circle animation?'")
    print("  - 'Can you show me how to animate text?'")
    print("  - 'What's the difference between Create and Show?'")
    print("  - 'Where are the videos saved?'")
    print("==========================================\n")

def print_sample_prompts():
    print("\n=== Sample Prompts for MCP + Strands + Manim Demo ===")
    print("These prompts demonstrate the power of the integration:")
    print()
    print("1. Cubic Function Visualization:")
    print("   'Create a Manim scene that draws the cubic function (2x^3 - 3x^2 + x - 1) from x = -3 to x = 3 in 9 seconds.'")
    print()
    print("2. Economic Data Visualization:")
    print("   'Create a Manim scene using the most recent available data for the population and GDP of the top 5 economies. Ensure that the animations do not overlap and that the transitions are clear.'")
    print()
    print("3. Basic Animation:")
    print("   'Create a simple animation showing a square transforming into a circle'")
    print()
    print("4. Mathematical Visualization:")
    print("   'Generate an animation showing the sine wave function with a moving point'")
    print()
    print("5. Educational Content:")
    print("   'Create an animation explaining the Pythagorean theorem with visual proof'")
    print()
    print("6. Complex Animations:")
    print("   'Make an animation with multiple objects: a bouncing ball, rotating cube, and growing text'")
    print()
    print("7. Interactive Elements:")
    print("   'Create an animation with a counter that counts from 1 to 10 with visual effects'")
    print()
    print("8. Physics Simulation:")
    print("   'Generate an animation showing projectile motion with trajectory path'")
    print()
    print("9. Data Visualization:")
    print("   'Create a bar chart animation showing sales data for different months'")
    print()
    print("10. Text and Typography:")
    print("    'Make an animation with text that appears letter by letter with a typewriter effect'")
    print()
    print("11. Geometric Patterns:")
    print("    'Generate a fractal animation showing the Sierpinski triangle being constructed'")
    print()
    print("12. Color and Effects:")
    print("    'Create an animation with a rainbow gradient circle that pulses and rotates'")
    print()
    print("13. Quadratic Equations:")
    print("    'Plot the quadratic function f(x) = x² - 4x + 3 with its vertex and roots highlighted'")
    print()
    print("14. Quadratic Comparison:")
    print("    'Create an animation comparing f(x) = x², f(x) = 2x², and f(x) = 0.5x² to show how coefficients affect the parabola'")
    print()
    print("15. Quadratic Transformations:")
    print("    'Animate the transformation of f(x) = x² to f(x) = (x-2)² + 1, showing the shift and translation'")
    print()
    print("16. Quadratic with Moving Point:")
    print("    'Plot f(x) = x² - 6x + 8 and animate a point moving along the curve with tangent line'")
    print()
    print("17. Quadratic Factoring Visualization:")
    print("    'Create an animation showing how f(x) = x² - 5x + 6 factors to (x-2)(x-3) with visual representation of roots'")
    print("==================================================\n")

def get_example_animation():
    return """
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        self.play(Create(circle))
        self.wait(2)
"""

def ensure_output_directory():
    """Ensure the output directory exists"""
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    return output_dir

def main():
    try:
        # Check and install required packages
        check_and_install_packages()
        
        # Ensure output directory exists
        output_dir = ensure_output_directory()
        
        # Get the path to the manim_server.py
        current_dir = os.path.dirname(os.path.abspath(__file__))
        manim_server_path = os.path.join(current_dir, "src", "manim_server.py")
        os.chdir(current_dir)

        # Connect to the Manim MCP server using stdio transport
        manim_mcp_client = MCPClient(lambda: stdio_client(
            StdioServerParameters(command="uv", args=["run", manim_server_path])
        ))

        print("Checking MCP server status...")
        # Try to open the context to check if the server is running
        try:
            with manim_mcp_client:
                tools = manim_mcp_client.list_tools_sync()
        except Exception as e:
            print("\nError: MCP server is not running!")
            print("Please start the MCP server first using:")
            print("uv run start_mcp_server.py")
            sys.exit(1)

        print("Initializing Manim Video Generation Chat Interface...")
        # Now open the context for the actual chat loop
        with manim_mcp_client:
            tools = manim_mcp_client.list_tools_sync()
            
            # Show which model is being used
            print("🔍 Attempting to use default Strands model (usually AWS Bedrock)")
            print("💡 If you get permission errors, you may need to:")
            print("   - Configure AWS credentials for Bedrock access")
            print("   - Or run Ollama locally (ollama run llama3.2:latest)")
            # Step 1: Define the model
            model_id = BedrockModel(
                model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
                max_tokens=64000,
                additional_request_fields={
                    "thinking": {
                        "type":"disabled",
                    }
                },
            ) 
            agent = Agent(model=model_id, tools=tools + [file_write, file_read, speak])
            print("✅ Initialization complete!")
            print(f"🤖 Using model: {agent.model}")
            print_help()
            
            print("\n🤖 Welcome to the Manim Video Generation Chat!")
            print("💡 Type '/samples' to see demonstration prompts")
            print("❓ Type '/help' for available commands")
            print("🚪 Type 'exit' or 'bye' to quit\n")
            
            while True:
                try:
                    # Get user input
                    user_input = input("👤 You: ").strip()
                    
                    # Check for exit commands
                    if user_input.lower() in ['exit', 'bye', 'quit']:
                        print("👋 Goodbye! Thanks for using the Manim Video Generator!")
                        break
                    
                    # Handle empty input
                    if not user_input:
                        continue
                    
                    # Handle commands
                    if user_input.lower() == '/help':
                        print_help()
                        continue
                    elif user_input.lower() == '/example':
                        print("\n📝 Here's an example Manim animation:")
                        print(get_example_animation())
                        print("\n🤔 Would you like me to execute this example? (yes/no)")
                        if input("👤 You: ").lower().startswith('y'):
                            print("\n🤖 Agent: Processing your request...")
                            result = agent(f"Please execute this Manim code to create a simple animation: {get_example_animation()}")
                            print(f"\n🤖 Agent: {result}")
                        continue
                    elif user_input.lower() == '/samples':
                        print_sample_prompts()
                        continue
                    elif user_input.lower() == '/install':
                        check_and_install_packages()
                        continue
                    elif user_input.lower() == '/status':
                        # Check status by trying to list tools
                        try:
                            manim_mcp_client.list_tools_sync()
                            print("✅ MCP server is running")
                        except Exception:
                            print("❌ MCP server is not running")
                        continue
                    
                    # Process user input with the agent
                    print("\n🤖 Agent: Processing your request...")
                    result = agent(user_input)
                    print(f"\n🤖 Agent: {result}")
                    
                except KeyboardInterrupt:
                    print("\n👋 Exiting...")
                    break
                except Exception as e:
                    print(f"\n❌ Error: {str(e)}")
                    print("💡 Please try again or type /help for assistance.")
    except Exception as e:
        print(f"💥 Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
