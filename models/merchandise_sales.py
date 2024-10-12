from .base import Base

class Merchandise_Sale(Base, table=True):
    __tablename__ = 'merchandise_sales'

    wrestler_id: int
    sales_amount_usd: int
    sales_rank: int
