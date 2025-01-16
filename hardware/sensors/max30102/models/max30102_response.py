from dataclasses import dataclass


@dataclass
class MAX30102_response:
    heart_rate: int = None
    spo2_level: float = None
