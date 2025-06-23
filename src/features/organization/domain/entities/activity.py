from dataclasses import dataclass


@dataclass
class Activity:
    activity_id: int
    title: str
    parent_id: int | None = None
