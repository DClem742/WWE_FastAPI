from .base import Base

class Championship(Base, table=True):
    __tablename__ = 'championships'

    title_name: str
    current_champion_id1: int
    current_champion_id2: int