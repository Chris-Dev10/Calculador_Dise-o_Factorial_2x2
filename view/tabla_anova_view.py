from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp


class TablaAnovaView(Screen):
    def create_tabla_anova_widget(self, suma_cuadrados, grados_libertad, cuadrados_medios, fs_calculadas, fs_criticas):
        tabla_anova_widget = MDDataTable(
            column_data = [
                ("Fuente de variacion", dp(35)),
                ("Suma de cuadrados", dp(35)),
                ("Grados de libertad", dp(35)),
                ("Cuadrado medio", dp(30)),
                ("F calculada", dp(25)),
                ("F critica", dp(25)),
            ],
            row_data = [
                ("Factor A", str(suma_cuadrados[0]), str(grados_libertad[0]), str(cuadrados_medios[0]), str(fs_calculadas[0]), str(fs_criticas[0])),
                ("Factor B", str(suma_cuadrados[1]), str(grados_libertad[1]), str(cuadrados_medios[1]), str(fs_calculadas[1]), fs_criticas[1]),
                ("Interaccion AB", str(suma_cuadrados[2]), str(grados_libertad[2]), str(cuadrados_medios[2]), str(fs_calculadas[2]), fs_criticas[2]),
                ("Error", str(suma_cuadrados[3]), str(grados_libertad[3]), str(cuadrados_medios[3]), "", ""),
                ("Total", str(suma_cuadrados[4]), str(grados_libertad[4]), "", "", ""),
            ],
        )

        return tabla_anova_widget