import os
import subprocess
from pathlib import Path
from typing import Optional, List, Dict, Any, Callable
from config import JARVIS_STORAGE_ROOT, VSCODE_CMD
from core.tools.base import BaseTool
from .schema import FILE_MANAGER_SCHEMAS
class FileManagerTool(BaseTool):
    def __init__(self):
        self.root = Path(JARVIS_STORAGE_ROOT).resolve()
        self.root.mkdir(parents=True, exist_ok=True)

    @property
    def name(self) -> str:
        return "Workspace_Project_File_IO"

    def _safe_path(self, relative_path: str) -> Path:
        target_path = Path(os.path.normpath(self.root / relative_path)).resolve()
        if not target_path.is_relative_to(self.root):
            raise PermissionError("Access Denied: Target path is outside Jarvis storage boundaries.")
        return target_path

    def read_file(self, file_path: str) -> Optional[str]:
        try:
            safe_target = self._safe_path(file_path)
            if not safe_target.is_file(): return f"Error: '{file_path}' does not exist."
            return safe_target.read_text(encoding="utf-8")
        except Exception as e: return f"Error reading file: {str(e)}"

    def list_files(self, sub_dir: str = "") -> List[str]:
        try:
            if sub_dir.strip().lower() in ["storage", "root", "storage0", "."]: sub_dir = ""
            safe_target = self._safe_path(sub_dir)
            if not safe_target.is_dir(): return [f"Error: Subdirectory '{sub_dir}' does not exist."]
            found_items = [str(p.relative_to(self.root)) for p in safe_target.rglob("*")]
            return found_items if found_items else ["The target workspace directory is currently empty, Sir."]
        except Exception as e: return [f"Error listing files: {str(e)}"]

    def open_file(self, file_path: str) -> str:
        try:
            safe_target = self._safe_path(file_path)
            if not safe_target.exists(): return f"Error: Target '{file_path}' not found."
            os.startfile(str(safe_target))
            return f"SUCCESS: '{safe_target.name}' opened natively on desktop screen."
        except Exception as e: return f"Failed to execute native OS open layer: {str(e)}"

    def open_project_in_vscode(self, project_name: str) -> str:
        try:
            project_target = self._safe_path(project_name)
            if not project_target.is_dir(): return f"Error: '{project_name}' is not an active folder directory, Sir."
            subprocess.Popen([VSCODE_CMD, str(project_target)], shell=True)
            return f"SUCCESS: Project folder '{project_name}' has been successfully launched inside VS Code, Sir."
        except Exception as e: return f"Failed to open project workspace folder in VS Code: {str(e)}"

    def write_file(self, file_path: str, content: str) -> str:
        try:
            safe_target = self._safe_path(file_path)
            safe_target.parent.mkdir(parents=True, exist_ok=True)
            safe_target.write_text(content, encoding="utf-8")
            return f"SUCCESS: File '{safe_target.name}' written completely."
        except Exception as e: return f"Failed to write file to disk layout: {str(e)}"

    def get_execution_map(self) -> Dict[str, Callable]:
        return {
            'read_file': self.read_file,
            'list_files': self.list_files,
            'open_file': self.open_file,
            'open_project_in_vscode': self.open_project_in_vscode,
            'write_file': self.write_file
        }

    def get_schemas(self) -> List[Dict[str, Any]]:
        return FILE_MANAGER_SCHEMAS # <-- Point directly to the imported list