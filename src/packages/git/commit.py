def commit(stdin: str, msg: str | None = None) -> str:
    if msg is not None:
        cmd: str = 'git add .;'
        cmd += f'git commit -m \"{msg}\";'
        cmd += 'git checkout main;'
        cmd += 'git merge dev;'
        cmd += 'git push;'
        cmd += 'git checkout dev'
        return cmd