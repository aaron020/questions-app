from dataclasses import dataclass, field, asdict
from typing import List, Tuple, Optional

@dataclass
class Question:
    comp_id: Optional[str] = None
    question: Optional[str] = None
    answers: Optional[List[Tuple[str, bool]]] = field(default_factory=list)
    explanation: Optional[str] = None
    difficulty: Optional[int] = None
    random: Optional[int] = None

    def to_dict(self) -> dict:
        return asdict(self)