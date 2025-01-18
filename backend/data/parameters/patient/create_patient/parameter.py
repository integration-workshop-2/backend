from typing import List, NamedTuple


class CreatePatientParameter(NamedTuple):
    name: str
    face_embeddings: List[List[float]]
