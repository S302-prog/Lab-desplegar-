from pydantic import BaseModel

class DataModel(BaseModel):
    u: float
    g: float
    r: float
    redshift: float
    rowv: float
    colv: float
    STAR: int
    GALAXY: int

    def columns(self):
        return ["u", "g", "r", "redshift", "rowv", "colv", "STAR", "GALAXY"]
