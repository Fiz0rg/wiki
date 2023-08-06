from dataclasses import dataclass


@dataclass
class WikiDTO:
    request: str
    language: str