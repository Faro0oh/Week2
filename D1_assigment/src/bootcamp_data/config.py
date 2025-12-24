from pathlib import Path
from dataclasses import dataclass

@dataclass (frozen= True)
class Paths:
 root : Path
 raw : Path
 cache : Path
 external : Path
 processed : Path



def make_paths(root: Path) -> Paths:
    root = Path(root)
    data = root / "data"
    return Paths (
       root = root,
       raw = data / "raw",
       cache = data/"cache",
       external = data /"external",
       processed = data / "processed"
    )
             