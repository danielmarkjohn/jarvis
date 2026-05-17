from core.tools.registry import ToolRegistry
from core.tools.file_manager import FileManagerTool
from core.tools.schema import FILE_MANAGER_SCHEMAS

# Dynamically mount your new environment-aware tool package setup
registry = ToolRegistry()
registry.register(FileManagerTool())  # Class pulls constant natively from config now
registry.tools_schema_pool.extend(FILE_MANAGER_SCHEMAS)  # <-- Clean Schema Injection