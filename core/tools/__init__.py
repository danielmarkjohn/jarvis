from core.tools.registry import ToolRegistry
from core.tools.file_manager import FileManagerTool
from core.tools.system_control import SystemControlTool # <-- New import

# Package entry registry compilation layer
registry = ToolRegistry()

# Mount feature modules independently
registry.register(FileManagerTool())
registry.register(SystemControlTool()) # <-- Mount system automation hooks