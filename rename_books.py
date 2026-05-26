from ebooklib import epub
from pathlib import Path
import re

for file in Path(".").glob("*.epub"):
    try:
        book = epub.read_epub(str(file))

        title_meta = book.get_metadata("DC", "title")
        creator_meta = book.get_metadata("DC", "creator")

        title = title_meta[0][0] if title_meta else "Unknown Title"
        author = creator_meta[0][0] if creator_meta else "Unknown Author"

        clean = lambda s: re.sub(r'[<>:"/\\|?*]', '', s)

        new_name = f"{clean(author)} - {clean(title)}.epub"

        file.rename(file.with_name(new_name))

        print(f"{file.name} -> {new_name}")

    except Exception:
        print(f"Failed: {file.name}")