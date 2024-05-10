import os


def generate_gitignore():
    gitignore_content = '''
    # Byte-compiled / optimized / DLL files
    __pycache__/
    *.py[cod]
    *$py.class

    # Distribution / packaging
    .venv*
    .vscode*
    _*.ps1
    Pipfile.lock
    __pycache__/
    build/
    dist/
    .Python
    develop-eggs/
    eggs/
    .eggs/
    sdist/
    *.egg-info/
    '''

    with open('.gitignore', 'w') as gitignore_file:
        gitignore_file.write(gitignore_content)
    print('gitignore file generated successfully!')

generate_gitignore()