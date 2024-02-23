from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class QuizApp(App):
    def build(self):
        self.questions = [
            {"question": "What is the capital of France?", "answers": ["Paris", "London", "Berlin", "Madrid"]},
            {"question": "Who wrote 'Hamlet'?", "answers": ["Charles Dickens", "William Shakespeare", "Leo Tolstoy", "Mark Twain"]},
            {"question": "What is the largest ocean?", "answers": ["Atlantic", "Indian", "Arctic", "Pacific"]}
        ]
        self.current_question = 0
        
        self.layout = BoxLayout(orientation='vertical', spacing=5, padding=40, size_hint_y=None)
        
        # Properly initialize the Label with text_size and halign properties
        self.question_label = Label(text=self.questions[0]['question'], size_hint_y=None, height=100, halign='center', valign='middle')
        # This is crucial for multiline text alignment to work
        self.question_label.bind(size=self.question_label.setter('text_size'))
        
        self.layout.add_widget(self.question_label)
        
        # Create buttons for answers
        self.answer_buttons = []
        for _ in range(4):
            btn = Button(size_hint_y=None, height=50, on_press=self.on_answer)
            self.answer_buttons.append(btn)
            self.layout.add_widget(btn)
        
        self.load_question()
        return self.layout

    def load_question(self):
        # Load the current question and answers
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.question_label.text = question["question"]
            for i, btn in enumerate(self.answer_buttons):
                btn.text = question["answers"][i]
        else:
            self.question_label.text = "Quiz finished!"
            for btn in self.answer_buttons:
                btn.disabled = True

    def on_answer(self, instance):
        print(f"You selected: {instance.text}")
        self.current_question += 1
        self.load_question()

if __name__ == '__main__':
    QuizApp().run()
