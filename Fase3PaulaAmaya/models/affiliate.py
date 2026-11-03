
class Affiliate:
    """
    Represents a person affiliated with the compensation fund.
    """

    def __init__(
        self,
        id_type: str,
        id_number: str,
        full_name: str,
        current_income: float,
        desired_service: str,
        employment_type: str,
        membership_fee: float,
        registration_date: str
    ):
        self.id_type = id_type
        self.id_number = id_number
        self.full_name = full_name
        self.current_income = current_income
        self.desired_service = desired_service
        self.employment_type = employment_type
        self.membership_fee = membership_fee
        self.registration_date = registration_date

    def get_details(self) -> tuple:
        """
        Returns all affiliate information as a tuple.
        """
        return (
            self.id_type,
            self.id_number,
            self.full_name,
            self.current_income,
            self.desired_service,
            self.employment_type,
            self.membership_fee,
            self.registration_date
        )

    def __str__(self) -> str:
        return f"{self.full_name} - {self.id_number}"
