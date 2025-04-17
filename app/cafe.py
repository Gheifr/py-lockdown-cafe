import datetime


from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Vaccine:
    def __init__(self, data: dict = None) -> None:
        self.expiration = None
        if data:
            self.expiration = data.get("expiration_date", None)


class Person:
    def __init__(self, data: dict) -> None:
        self.name = ""
        self.is_in_mask = False
        self.vaccine = Vaccine()
        if data:
            self.name = data.get("name", "")
            self.is_in_mask = data.get("wearing_a_mask", False)
            self.vaccine = Vaccine(data.get("vaccine", None))


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        guest = Person(visitor)
        if guest.vaccine.expiration is None:
            raise NotVaccinatedError()

        if guest.vaccine.expiration < datetime.date.today():
            raise OutdatedVaccineError()

        if not guest.is_in_mask:
            raise NotWearingMaskError()

        return f"Welcome to {self.name}"
