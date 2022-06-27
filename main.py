from controller.tabla_anova_controller import TablaAnovaController

from kivymd.app import MDApp


class CalculadorDiseñoFactorial2x2App(MDApp):
    def build(self):
        tabla_anova_c = TablaAnovaController()

        tabla_anova_c.calculate_datos_tabla_anova()

        tabla_anova_c.create_tabla_anova_widget()

        tabla_anova_c.add_tabla_anova_widget_to_view()

        return tabla_anova_c.get_tabla_anova_v

CalculadorDiseñoFactorial2x2App().run()