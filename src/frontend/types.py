from dataclasses import dataclass, field

@dataclass(slots=True)
class Chunk:
    link: str
    name: str
    args: tuple[str] = field(default_factory=tuple[str])

    def __init__(self, link: str, name: str, *args: str) -> None:
        self.link = link
        self.name = name
        self.args = args