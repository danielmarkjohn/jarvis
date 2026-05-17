from typing import List, Dict, Any

FILE_MANAGER_SCHEMAS: List[Dict[str, Any]] = [
    {
        'type': 'function',
        'function': {
            'name': 'read_file',
            'description': 'Reads text data inside a specific project file path location.',
            'parameters': {
                'type': 'object',
                'properties': {
                    'file_path': {'type': 'string', 'description': 'The relative path of the file to read.'}
                },
                'required': ['file_path']
            }
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'list_files',
            'description': 'Queries directory structures inside storage. Use to discover project names or list items inside folders.',
            'parameters': {
                'type': 'object',
                'properties': {
                    'sub_dir': {'type': 'string', 'description': 'Folder path relative to root storage. Empty string "" for the root folder.'}
                },
                'required': ['sub_dir']
            }
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'open_file',
            'description': 'Launches a specific individual file natively on the Windows desktop using its default registered application (e.g. Notepad, browser).',
            'parameters': {
                'type': 'object',
                'properties': {
                    'file_path': {'type': 'string', 'description': 'The relative path of the file to open.'}
                },
                'required': ['file_path']
            }
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'open_project_in_vscode',
            'description': 'Opens an entire project directory folder explicitly in Visual Studio Code editor layout screen.',
            'parameters': {
                'type': 'object',
                'properties': {
                    'project_name': {'type': 'string', 'description': 'The name of the project folder directory inside root storage to open.'}
                },
                'required': ['project_name']
            }
        }
    },
    {
        'type': 'function',
        'function': {
            'name': 'write_file',
            'description': 'Creates a new file or logs contents inside a specific project path location.',
            'parameters': {
                'type': 'object',
                'properties': {
                    'file_path': {'type': 'string', 'description': 'The relative path where the file should be saved inside its project folder structure.'},
                    'content': {'type': 'string', 'description': 'The exact script code block or text contents to write into the file.'}
                },
                'required': ['file_path', 'content']
            }
        }
    }
]