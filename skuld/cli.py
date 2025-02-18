import os
import click
from .config import load_config
from .migration import create_migration_file

@click.command()
@click.argument("name")
def create_migration(name: str):
    """Create a new migration file with the given name."""
    config = load_config()
    migration_dir = config.migration_dir

    # Ensure the migration directory exists
    os.makedirs(migration_dir, exist_ok=True)

    # Create the migration file
    filepath = create_migration_file(migration_dir, name)
    click.echo(f"Created migration file: {filepath}")

if __name__ == "__main__":
    create_migration()