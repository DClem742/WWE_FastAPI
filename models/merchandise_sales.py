from .base import Base

class Merchandise_Sale(Base):
    __tablename__ = 'merchandise_sales'

    wrestler_id: int
    sales_amount_usd: int
    sales_rank: int
