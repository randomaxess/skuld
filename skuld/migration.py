from datetime import datetime
import os

def create_migration_file(migration_dir: str, name: str) -> str:
    # Generate the filename
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{name}.sql"
    filepath = os.path.join(migration_dir, filename)

    # Create the migration file with the required template
    with open(filepath, "w") as f:
        f.write(
            "-- up begin\n\n-- up end\n\n-- down begin\n\n-- down end\n"
        )

    return filepath