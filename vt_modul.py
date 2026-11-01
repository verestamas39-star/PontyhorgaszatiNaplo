
def suly_ellenorzes_VT(suly):
    return suly > 0


class FogasVT:

    def __init__(self, datum, helyszin, halfaj, suly):
        self.datum = datum
        self.helyszin = helyszin
        self.halfaj = halfaj
        self.suly = suly

    def megjelenit(self):
        return f"{self.datum} | {self.helyszin} | {self.halfaj} | {self.suly:.2f} kg"
