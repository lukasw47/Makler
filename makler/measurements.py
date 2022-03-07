from decimal import Decimal


class LengthInMeters(Decimal):
    pass


class AreaInSquareMeters(Decimal):

    def __str__(self) -> str:
        return f'{super().__str__()}m²'
