"""Code execution module for AlgoSmith"""

import re
import ast


def execute_code(code, arguments):
    """
    Execute user code with provided arguments.
    
    Args:
        code (str): Python code containing a function definition
        arguments (str): Pipe-separated arguments (e.g., "11 2 34 5 | 5")
                        Space-separated values are converted to lists.
    
    Returns:
        dict: {"error": str or None, "output": result}
    """
    if not code.strip():
        return {"error": "No code provided.", "output": None}
    
    try:
        # Extract function name from code (first function definition)
        func_match = re.search(r'def\s+(\w+)\s*\(', code)
        if not func_match:
            return {"error": "No function definition found in code.", "output": None}
        
        func_name = func_match.group(1)
        
        # Parse input values into Python arguments
        args_list = []
        if arguments.strip():
            # Split by pipe character
            raw_args = [arg.strip() for arg in arguments.split('|')]
            
            for arg in raw_args:
                # Check if it looks like a space-separated list (contains spaces but no brackets)
                if ' ' in arg and '[' not in arg and '{' not in arg:
                    # Try to parse as space-separated numbers
                    try:
                        # Try to parse all space-separated values as numbers
                        parts = arg.split()
                        parsed_list = []
                        for part in parts:
                            try:
                                # Try int first
                                if '.' not in part:
                                    parsed_list.append(int(part))
                                else:
                                    parsed_list.append(float(part))
                            except ValueError:
                                # If it fails, keep as string
                                parsed_list.append(part)
                        args_list.append(parsed_list)
                    except Exception:
                        # If space-separated parsing fails, treat as string
                        args_list.append(arg)
                else:
                    # Try to parse as Python literal
                    try:
                        parsed = ast.literal_eval(arg)
                        args_list.append(parsed)
                    except (ValueError, SyntaxError):
                        # If literal eval fails, try as string or number
                        if arg.isdigit():
                            args_list.append(int(arg))
                        else:
                            try:
                                args_list.append(float(arg))
                            except ValueError:
                                # Treat as string
                                args_list.append(arg)
        
        # Create execution namespace and execute code
        namespace = {}
        exec(code, namespace)
        
        # Get the function and execute it
        if func_name not in namespace:
            return {"error": f"Function '{func_name}' not found after execution.", "output": None}
        
        func = namespace[func_name]
        result = func(*args_list)
        
        return {"error": None, "output": result}
        
    except TypeError as e:
        return {"error": f"Argument error: {str(e)}", "output": None}
    except Exception as e:
        return {"error": f"Execution error: {str(e)}", "output": None}
