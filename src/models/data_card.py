from datetime import datetime
from typing import Dict, List, Any, Optional

class GameDataCardFile:
    def __init__(
        self,
        name: str
    ):
        self.name: str = name,
        #self.uuid = generate_uuid(),
        self.type: str = "list",
        self.cards: Optional[List[DataCard]] = list(), #list of Data Cards
        self.created_at: str = "some_date", # generate a timestamp
        self.version: str = "2.9.3",
        self.website: str = "https://game-datacards.eu"


class DataCard:
    def __init__(
        self,
        category: str,
    ):
        self.category: str = "", # This should be a new "Category" type
        self.created_at: str = "some_date", # generate a timestamp
        self.version: str = "2.9.3",
        self.website: str = "https://game-datacards.eu"

        self.abilities: list[Any] = list(), #TODO: figure out the data structure for this
        self.cardType = "DataCard",
        self.composition: list[str] = list(), # TODO: description of unit makeup; each index is a line
        self.factions: list[str] = list(),  # TODO: list of factions this belongs to; each index is a line
        self.faction_id: str = "faction_id", # TODO: hardcoded list of possible faction ids
        self.fluff: str = "fluff", # flavor text
        self.id: str = "uuid", # TODO: generate a lower-case UUID


    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DataCard':
        """Create a DataCard instance from a dictionary."""
        return cls(
            id=data['id'],
            name=data['name'],
            description=data['description'],
            type=data['type'],
            status=data['status'],
            created_at=datetime.fromisoformat(data['createdAt'].replace('Z', '+00:00')),
            updated_at=datetime.fromisoformat(data['updatedAt'].replace('Z', '+00:00')),
            created_by=data['createdBy'],
            updated_by=data['updatedBy'],
            tags=data.get('tags', []),
            metadata=data.get('metadata', {})
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert the DataCard instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'type': self.type,
            'status': self.status,
            'createdAt': self.created_at.isoformat() + 'Z',
            'updatedAt': self.updated_at.isoformat() + 'Z',
            'createdBy': self.created_by,
            'updatedBy': self.updated_by,
            'tags': self.tags,
            'metadata': self.metadata
        } 