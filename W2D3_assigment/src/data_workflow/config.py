from pathlib import Path
from dataclasses import dataclass

@dataclass (frozen= True)
class Paths:
 root : Path
 raw : Path
 processed : Path




def make_paths(root: Path) -> Paths:
    root = Path(root)
    data = root / "data"
    return Paths (
       root = root,
       raw = data / "raw",
       processed = data / "processed",
       
    )
             