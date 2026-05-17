import os
import winreg
import subprocess
from pathlib import Path
from typing import List, Dict, Any, Callable, Optional
from core.tools.base import BaseTool

class SystemControlTool(BaseTool):
    @property
    def name(self) -> str:
        return "OS_System_Automation_Control"

    def _find_app_in_registry(self, app_name: str) -> Optional[str]:
        """Queries the Windows Registry to find the absolute executable path of an app."""
        reg_paths = [
            r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths",
            r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\App Paths"
        ]
        
        search_names = [f"{app_name}.exe", app_name]
        
        for root_key in [winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER]:
            for reg_path in reg_paths:
                for name in search_names:
                    try:
                        sub_key = f"{reg_path}\\{name}"
                        with winreg.OpenKey(root_key, sub_key) as key:
                            exe_path, _ = winreg.QueryValueEx(key, "")
                            if os.path.exists(exe_path):
                                return exe_path
                    except OSError:
                        continue
        return None

    def _find_app_in_start_menu(self, app_name: str) -> Optional[str]:
        """Scans the Windows Start Menu directory links for a matching shortcut."""
        start_menu_paths = [
            Path(os.environ.get("PROGRAMDATA", r"C:\ProgramData")) / r"Microsoft\Windows\Start Menu\Programs",
            Path(os.environ.get("APPDATA", "")) / r"Microsoft\Windows\Start Menu\Programs"
        ]
        
        for base_path in start_menu_paths:
            if not base_path.exists():
                continue
            for shortcut in base_path.rglob("*.lnk"):
                if app_name in shortcut.name.lower():
                    return str(shortcut)
        return None

    def launch_application(self, app_name: str) -> str:
        """Dynamically discovers and launches any Windows application with zero hardcoded paths."""
        app_clean = app_name.strip().lower()
        
        print(f"[SYSTEM CONTROL] Attempting to dynamically locate: {app_clean}")
        
        # 1. Step One: Check Windows App Paths Registry
        exe_path = self._find_app_in_registry(app_clean)
        if exe_path:
            subprocess.Popen([exe_path], shell=True)
            return f"SUCCESS: Located and launched '{app_name}' via Windows Registry paths."

        # 2. Step Two: Check Start Menu Shortcuts
        shortcut_path = self._find_app_in_start_menu(app_clean)
        if shortcut_path:
            os.startfile(shortcut_path)
            return f"SUCCESS: Located and launched '{app_name}' via Start Menu shortcuts."

        # 3. Step Three: Blind global shell deployment fallback
        try:
            subprocess.Popen([f"start {app_clean}"], shell=True)
            return f"SUCCESS: Dispatched global system shell execution command for '{app_name}'."
        except Exception as e:
            return f"Failed to open application '{app_name}'. Software could not be auto-discovered on this machine. Error: {str(e)}"

    def manage_power_state(self, state: str) -> str:
        """Handles hardware power configurations natively via Windows shell."""
        state = state.strip().lower()
        try:
            if state == "shutdown":
                subprocess.Popen(["shutdown", "/s", "/f", "/t", "1"], shell=True)
                return "SUCCESS: Initializing full system shutdown sequence."
            elif state == "restart":
                subprocess.Popen(["shutdown", "/r", "/f", "/t", "1"], shell=True)
                return "SUCCESS: Initializing hardware reboot sequence."
            elif state == "sleep":
                subprocess.Popen(["rundll32.exe", "powrprof.dll,SetSuspendState", "0", "1", "0"], shell=True)
                return "SUCCESS: Entering system sleep mode immediately."
            return f"Error: Power state '{state}' is unrecognized."
        except Exception as e:
            return f"Failed to execute system power action: {str(e)}"

    # --- Tool Registrations ---
    def get_execution_map(self) -> Dict[str, Callable]:
        return {
            'manage_power_state': self.manage_power_state,
            'launch_application': self.launch_application
        }

    def get_schemas(self) -> List[Dict[str, Any]]:
        return [
            {
                'type': 'function',
                'function': {
                    'name': 'manage_power_state',
                    'description': 'Executes system-level power actions like shutting down, restarting, or putting the PC to sleep.',
                    'parameters': {
                        'type': 'object',
                        'properties': {
                            'state': {'type': 'string', 'enum': ['shutdown', 'restart', 'sleep']}
                        },
                        'required': ['state']
                    }
                }
            },
            {
                'type': 'function',
                'function': {
                    'name': 'launch_application',
                    'description': 'Launches any application, tool, game launcher, or window program installed on the Windows host machine dynamically.',
                    'parameters': {
                        'type': 'object',
                        'properties': {
                            'app_name': {'type': 'string', 'description': 'The name of the program to launch (e.g. "steam", "battle.net", "discord").'}
                        },
                        'required': ['app_name']
                    }
                }
            }
        ]