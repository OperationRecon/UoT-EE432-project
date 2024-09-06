from database import init_db
from cli.menu import run_cli

def main():
    init_db()
    run_cli()

if name == "main":
    main()