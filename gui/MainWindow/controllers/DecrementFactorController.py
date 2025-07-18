from .BaseController import BaseController
from . import Validation as validation

class DecrementFactorController(BaseController):
    def __init__(self, parent):

        super().__init__(parent)
        
        self.ui = parent.ui

        self.parent = parent

        # Calculate Decrement Factor according to IEEE Std 80

        # Make error labels invisible
        self.ui.label_62.setVisible(False)
        self.ui.label_87.setVisible(False)
        self.ui.label_88.setVisible(False)

        # Show options based on comboBox_16
        self.setup_toggle_behavior(
            self.ui.comboBox_16,
            show_on_yes = [
                self.ui.label_74, self.ui.label_75, self.ui.lineEdit_45, self.ui.toolButton_60,
                self.ui.label_76, self.ui.label_77, self.ui.lineEdit_46, self.ui.toolButton_61
            ],
            show_on_no = [
                self.ui.label_78, self.ui.label_79, self.ui.lineEdit_38, self.ui.toolButton_62
            ]
        )
        
        # Validate Inductive Reactance inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_45,
            error_label=self.ui.label_88,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

        # Validate System resistance at fault inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_46,
            error_label=self.ui.label_87,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

        # Validate Decrement Factor inputs
        validation.setup_live_validation(
            self,
            line_edit=self.ui.lineEdit_38,
            error_label=self.ui.label_62,
            validator_func=validation.is_valid_number,
            error_message="Enter a valid number"
        )

    def extractParametersFromGui(self):
        def safe_float(text, default=0.0):
            try:
                return float(text)
            except (ValueError, TypeError):
                return default
        def safe_str(text, default=""):
            return text if text is not None else default
        return {
            "calcDecrementFactor": safe_str(self.ui.comboBox_16.currentIndex()),
            "inductiveReactance": safe_float(self.ui.lineEdit_45.text()),
            "resistanceAtFault": safe_float(self.ui.lineEdit_46.text()),
            "decrementFactor": safe_float(self.ui.lineEdit_38.text())
        }

    def resetParameters(self):
        self.ui.comboBox_16.setCurrentIndex(0)
        self.ui.lineEdit_45.setText("")
        self.ui.lineEdit_46.setText("")
        self.ui.lineEdit_38.setText("")