import sys
import os
from dotenv import load_dotenv
from groq import Groq
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from ui_py.main_window import Ui_MainWindow

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.output_box.setReadOnly(True)
        self.ui.submit_btn.clicked.connect(self.process_notes)

    def build_prompt(self, notes):
        extras = []

        if self.ui.concepts_box.isChecked():
            extras.append("- Simplify and explain the key concepts clearly")
        if self.ui.analogy_box.isChecked():
            extras.append("- Provide relatable analogies to explain ideas")
        if self.ui.example_box.isChecked():
            extras.append("- Give real-world examples for better understanding")
        if self.ui.definitions_box.isChecked():
            extras.append("- Define all important terms and keywords")
        if self.ui.practice_box.isChecked():
            extras.append("- Add practice questions at the end")

        if not extras:
            extras.append("- Summarize the notes clearly and concisely")

        extras_text = "\n".join(extras)

        prompt = f"""You are a helpful study assistant.
Given the following notes, please do the following:
{extras_text}

Notes:
{notes}
"""
        return prompt

    def process_notes(self):
        notes = self.ui.input_box.toPlainText().strip()

        if not notes:
            self.ui.output_box.setPlainText("⚠️ Please paste your notes first.")
            return

        self.ui.output_box.setPlainText("⏳ Processing your notes, please wait...")
        self.ui.submit_btn.setEnabled(False)
        QApplication.processEvents()

        try:
            prompt = self.build_prompt(notes)
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}]
            )
            output = response.choices[0].message.content
            self.ui.output_box.setPlainText(output)

        except Exception as e:
            error = str(e)
            if "429" in error or "quota" in error.lower() or "rate" in error.lower():
                self.ui.output_box.setPlainText(
                    "⚠️ You've hit the rate limit.\n\n"
                    "Please wait 1 minute and try again."
                )
            else:
                self.ui.output_box.setPlainText(f"❌ Error: {error}")
        finally:
            self.ui.submit_btn.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())