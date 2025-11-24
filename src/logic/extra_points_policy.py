class ExtraPointsPolicy:
    EXTRA_POINT_VALUE = 1.0

    def calculate_extra_points(self, all_years_teachers: bool) -> float:
        """
        Calcula los puntos extra.
        Si los profesores están de acuerdo, se otorga 1 punto extra.
        """
        if all_years_teachers:
            return self.EXTRA_POINT_VALUE
        return 0.0
