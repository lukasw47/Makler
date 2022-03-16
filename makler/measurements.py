from decimal import Decimal


class LengthInMeters(Decimal):
    pass


class AreaInSquareMeters(Decimal):

    def __format__(self, format_spec, **kwargs) -> str:
        return format(str(self), format_spec)

    def __str__(self) -> str:
        return f'{super().__str__()}m²'
