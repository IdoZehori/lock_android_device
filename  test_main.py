import unittest
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
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

class MyAppTest(unittest.TestCase):
    def test_build(self):
        app = MyApp()
        layout = app.build()
        self.assertIsInstance(layout, BoxLayout)
        self.assertEqual(len(layout.children), 5)
        self.assertIsInstance(layout.children[0], Label)
        self.assertEqual(layout.children[0].text, "What is the capital of France?")
        self.assertIsInstance(layout.children[1], Button)
        self.assertIsInstance(layout.children[2], Button)
        self.assertIsInstance(layout.children[3], Button)
        self.assertIsInstance(layout.children[4], Button)

if __name__ == '__main__':
    unittest.main()