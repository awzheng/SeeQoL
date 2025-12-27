from pydantic import BaseModel

class CityBase(BaseModel):
    name: str
    qol_score: float

class CityCreate(CityBase):
    pass

class City(CityBase):
    id: int

    class Config:
        from_attributes = True
