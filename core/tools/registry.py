from typing import Dict, Any, List, Callable
from core.tools.base import BaseTool

class ToolRegistry:
    def __init__(self):
        self.tools_schema_pool: List[Dict[str, Any]] = []
        self.execution_router: Dict[str, Callable] = {}

    def register(self, tool_instance: BaseTool) -> None:
        """Dynamically binds a modular capability group to the central engine core."""
        print(f"[REGISTRY] Mounting capability package: {tool_instance.name}")
        
        # Aggregate Ollama API Schemas
        self.tools_schema_pool.extend(tool_instance.get_schemas())
        
        # Bind executable Python function mappings
        self.execution_router.update(tool_instance.get_execution_map())

    def get_all_schemas(self) -> List[Dict[str, Any]]:
        return self.tools_schema_pool

    def execute(self, function_name: str, arguments: Dict[str, Any]) -> Any:
        """Routes dynamic tool calls directly to their targeted modules."""
        if function_name in self.execution_router:
            return self.execution_router[function_name](**arguments)
        raise NotImplementedError(f"Requested tool execution path '{function_name}' is unregistered.")