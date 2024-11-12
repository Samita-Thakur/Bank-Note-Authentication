from pydantic import BaseModel

class Banknotes(BaseModel):
    variance:float
    skewness: float
    kurtosis: float
    entropy: float
