import subprocess
import os
import shutil
import glob
import time
from pathlib import Path
from mcp.server.fastmcp import FastMCP

# MCP server
mcp = FastMCP()

# Get Manim executable path from environment variables or assume it's in the system PATH
MANIM_EXECUTABLE = os.getenv("MANIM_EXECUTABLE", "manim")   

# Manim output directory
TEMP_DIRS = {}
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "output")
os.makedirs(BASE_DIR, exist_ok=True)  

def find_generated_videos(directory: str) -> list:
    """Find all generated video files in the directory"""
    video_extensions = ['*.mp4', '*.mov', '*.avi', '*.mkv']
    video_files = []
    
    for ext in video_extensions:
        video_files.extend(glob.glob(os.path.join(directory, ext)))
    
    return sorted(video_files, key=os.path.getctime, reverse=True)

def validate_manim_code(manim_code: str) -> tuple[bool, str]:
    """Basic validation of Manim code"""
    if not manim_code.strip():
        return False, "Empty code provided"
    
    required_imports = ["from manim import", "import manim"]
    has_import = any(import_stmt in manim_code for import_stmt in required_imports)
    
    if not has_import:
        return False, "Missing Manim import statement"
    
    if "class" not in manim_code or "Scene" not in manim_code:
        return False, "Code should contain a Scene class"
    
    return True, "Code validation passed"

@mcp.tool()
def execute_manim_code(manim_code: str, quality: str = "medium_quality", renderer: str = "cairo") -> str:
    """
    Execute the Manim code and generate video
    
    Args:
        manim_code: The Manim Python code to execute
        quality: Video quality (low_quality, medium_quality, high_quality, production_quality)
        renderer: Rendering engine (cairo, opengl)
    """
    # Validate input
    is_valid, validation_msg = validate_manim_code(manim_code)
    if not is_valid:
        return f"Code validation failed: {validation_msg}"
    
    # Create unique temporary directory
    timestamp = int(time.time())
    tmpdir = os.path.join(BASE_DIR, f"manim_tmp_{timestamp}")
    os.makedirs(tmpdir, exist_ok=True)
    
    script_path = os.path.join(tmpdir, "scene.py")
    
    try:
        # Write the Manim script to the temp directory
        with open(script_path, "w") as script_file:
            script_file.write(manim_code)
        
        # Build Manim command with quality and renderer options
        manim_cmd = [
            MANIM_EXECUTABLE,
            "-p",  # Preview
            "-q", quality,  # Quality setting
            "-r", renderer,  # Renderer
            script_path
        ]
        
        print(f"Executing Manim with command: {' '.join(manim_cmd)}")
        
        # Execute Manim with the correct path
        result = subprocess.run(
            manim_cmd,
            capture_output=True,
            text=True,
            cwd=tmpdir,
            timeout=300  # 5 minute timeout
        )

        if result.returncode == 0:
            # Find generated videos
            video_files = find_generated_videos(tmpdir)
            
            if video_files:
                latest_video = video_files[0]
                video_size = os.path.getsize(latest_video) / (1024 * 1024)  # Size in MB
                
                TEMP_DIRS[tmpdir] = True
                
                success_msg = f"✅ Execution successful!\n"
                success_msg += f"📁 Output directory: {tmpdir}\n"
                success_msg += f"🎥 Generated video: {os.path.basename(latest_video)}\n"
                success_msg += f"📊 Video size: {video_size:.2f} MB\n"
                success_msg += f"🔧 Quality: {quality}, Renderer: {renderer}\n"
                success_msg += f"💡 You can find the video file in the output directory."
                
                return success_msg
            else:
                return f"⚠️ Execution completed but no video files found in {tmpdir}"
        else:
            error_msg = f"❌ Execution failed with return code {result.returncode}\n"
            error_msg += f"📝 Error output:\n{result.stderr}\n"
            error_msg += f"📝 Standard output:\n{result.stdout}"
            return error_msg

    except subprocess.TimeoutExpired:
        return f"⏰ Execution timed out after 5 minutes. The animation might be too complex."
    except Exception as e:
        return f"💥 Error during execution: {str(e)}"

@mcp.tool()
def list_manim_scenes(manim_code: str) -> str:
    """List all available scenes in the provided Manim code"""
    try:
        # Create temporary file to analyze
        tmpdir = os.path.join(BASE_DIR, "temp_analysis")
        os.makedirs(tmpdir, exist_ok=True)
        script_path = os.path.join(tmpdir, "temp_scene.py")
        
        with open(script_path, "w") as script_file:
            script_file.write(manim_code)
        
        # Use Manim to list scenes
        result = subprocess.run(
            [MANIM_EXECUTABLE, "-l", script_path],
            capture_output=True,
            text=True,
            cwd=tmpdir
        )
        
        # Clean up temp file
        shutil.rmtree(tmpdir)
        
        if result.returncode == 0:
            return f"📋 Available scenes:\n{result.stdout}"
        else:
            return f"❌ Failed to list scenes: {result.stderr}"
            
    except Exception as e:
        return f"💥 Error listing scenes: {str(e)}"

@mcp.tool()
def get_manim_help() -> str:
    """Get help information about Manim usage and available options"""
    help_info = """
🤖 Manim Video Generation Help

📚 Available Quality Options:
- low_quality: Fast rendering, lower quality
- medium_quality: Balanced speed and quality (default)
- high_quality: Higher quality, slower rendering
- production_quality: Best quality, slowest rendering

🎨 Available Renderers:
- cairo: 2D vector graphics (default)
- opengl: 3D graphics and advanced effects

📝 Code Requirements:
- Must import manim: 'from manim import *'
- Must define a Scene class
- Must have a construct() method

💡 Tips:
- Keep animations under 30 seconds for faster rendering
- Use simple shapes for quick previews
- Complex 3D scenes work best with opengl renderer
- Check the output directory for generated videos

🔧 Example usage:
execute_manim_code(manim_code="your code here", quality="medium_quality", renderer="cairo")
"""
    return help_info

@mcp.tool()
def cleanup_manim_temp_dir(directory: str = None) -> str:
    """
    Clean up Manim temporary directories.
    
    Args:
        directory: Specific directory to clean (optional). If None, cleans all temp dirs.
    """
    try:
        if directory:
            # Clean specific directory
            if os.path.exists(directory):
                shutil.rmtree(directory)
                if directory in TEMP_DIRS:
                    del TEMP_DIRS[directory]
                return f"✅ Cleanup successful for directory: {directory}"
            else:
                return f"❌ Directory not found: {directory}"
        else:
            # Clean all temp directories
            cleaned_count = 0
            for temp_dir in list(TEMP_DIRS.keys()):
                if os.path.exists(temp_dir):
                    shutil.rmtree(temp_dir)
                    cleaned_count += 1
            
            TEMP_DIRS.clear()
            return f"✅ Cleanup successful! Removed {cleaned_count} temporary directories."
            
    except Exception as e:
        return f"💥 Failed to clean up directories. Error: {str(e)}"

@mcp.tool()
def get_output_directory_info() -> str:
    """Get information about the output directory and generated files"""
    try:
        if not os.path.exists(BASE_DIR):
            return f"📁 Output directory does not exist: {BASE_DIR}"
        
        # Count files in output directory
        files = os.listdir(BASE_DIR)
        video_files = find_generated_videos(BASE_DIR)
        
        info = f"📁 Output Directory: {BASE_DIR}\n"
        info += f"📊 Total files: {len(files)}\n"
        info += f"🎥 Video files: {len(video_files)}\n"
        
        if video_files:
            info += "\n📹 Recent videos:\n"
            for i, video in enumerate(video_files[:5], 1):
                size_mb = os.path.getsize(video) / (1024 * 1024)
                info += f"  {i}. {os.path.basename(video)} ({size_mb:.2f} MB)\n"
        
        return info
        
    except Exception as e:
        return f"💥 Error getting directory info: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")




