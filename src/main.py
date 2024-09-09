from database import init_db
from CLI.menu import run_cli

def main():
    init_db()
    run_cli()

if __name__ == "__main__":
    main()
