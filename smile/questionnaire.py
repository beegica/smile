#emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
#ex: set sts=4 ts=4 sw=4 et:
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See the COPYING file distributed along with the smile package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##

from kivy.uix.widget import Widget
import kivy.uix.label
from kivy.clock import Clock
import kivy.graphics
from kivy.properties import NumericProperty, ListProperty,
from kivy.properties import ObjectProperty, BooleanProperty
from config import *

MARGIN = 25.
TEXT_COLOR = (0,0,0,1)
TEXT_INPUT_TEXT_HEIGHT = 35
FONT_SIZE = 22

class _Questionnaire(Widget):
    loq = ListProperty([{'type': "TITLE",
                         'question': "SMILE QUESTIONNAIRE"}])
    results = ListProperty([])
    def __init__(self, **kwargs):
        super(type(self), self).__init__(**kwargs)
        self.questions = []
        self.MC_list = []
        self.CA_list = []
        self.TI_list = []
        self.CT_list = []
        self.LI_list = []

    def start(self):
        layout = FloatLayout(width=self.width)
        top_con = layout.top - 10.
        quest_counter = 0.

        for quest in self.loq:
            if quest['type'] != "TITLE":
                qrec = Rectangle(color=(0.2, 0.2, 0.2, 1.0),
                          left=1.5*MARGIN,
                          width=self.width - 3.0*MARGIN,
                          top=top_con - MARGIN)
                layout.add_widget(mcrec)
                qlabel = kivy.uix.label.Label(text=str(quest_counter) + ". " + quest['question'],
                                               left=layout.left + MARGIN,
                                               center_y=qrec.center_y,
                                               text_size=(self.width - 4*MARGIN, None),
                                               color=TEXT_COLOR, halign="left",
                                               font_size=FONT_SIZE)
                layout.add_widget(question_label)
                top_con = qrec.bottom - MARGIN

            if quest['type'] == "MC":
                self.questions.append({"answers_index":len(self.MC_list)+1,
                                  "question":quest['quest'],
                                  "type":"MC",
                                  "index": quest_counter})
                answers = []
                for ans in quest['ans']:
                    ans_but = kivy.uix.togglebutton.ToggleButton(group=quest['question'],
                                                                 name=quest['ans'],
                                                                 left=layout.left + MARGIN,
                                                                 top=top_con,
                                                                 width=MARGIN,
                                                                 height=MARGIN)
                    layout.add_widget(ans_but)
                    answers.append(ans_but)
                    ans_label =kivy.uix.label.Label(left=ans.right + MARGIN, center_y=ans.center_y,
                                         text=quest['ans'], font_size=FONT_SIZE,
                                         color=TEXT_COLOR)

                    layout.add_widget(ans_label)
                    top_con = ans_but.bottom - MARGIN
                self.MC_list.append(answers)
                quest_counter += 1.
                top_con = ans_but.bottom - 1.5*MARGIN

            elif quest['type'] == "CA":

                self.questions.append({"answers_index":len(self.CA_list)+1,
                                  "question":quest['quest'],
                                  "type":"CA",
                                  "index": quest_counter})
                answers = []
                for ans in quest['ans']:
                    ans_but = kivy.uix.togglebutton.ToggleButton(name=quest['ans'],
                                                                 left=layout.left + MARGIN,
                                                                 top=top_con,
                                                                 width=MARGIN,
                                                                 height=MARGIN)
                    layout.add_widget(ans_but)
                    answers.append(ans_but)
                    ans_label =kivy.uix.label.Label(left=ans.right + MARGIN, center_y=ans.center_y,
                                         text=quest['ans'], font_size=FONT_SIZE,
                                         color=TEXT_COLOR)
                    layout.add_widget(ans_label)
                    top_con = ans_but.bottom - MARGIN
                self.CA_list.append(answers)
                quest_counter += 1.
                top_con = ans_but.bottom - 1.5*MARGIN

            elif quest['type'] == "CT":
                self.questions.append({"answers_index":len(self.CA_list)+1,
                                  "question":quest['quest'],
                                  "type":"CA",
                                  "index": quest_counter})
                sl = kivy.uix.slider.Slider(left=MARGIN, width=self.width - 2*MARGIN,
                                            min=quest['min'], max=quest['max'],
                                            top=top_con - 3*MARGIN,
                                            )
                slminlb = kivy.uix.label.Label(text=quest['ans'][0], bottom=sl.top,
                                               left=sl.left, font_size=FONT_SIZE,
                                               color=TEXT_COLOR)
                slmidlb = kivy.uix.label.Label(text=quest['ans'][0], bottom=sl.top,
                                               left=sl.left, font_size=FONT_SIZE,
                                               color=TEXT_COLOR)
                slmaxlb = kivy.uix.label.Label(text=quest['ans'][0], bottom=sl.top,
                                               left=sl.left, font_size=FONT_SIZE,
                                               color=TEXT_COLOR)
                layout.add_widget(sl)
                layout.add_widget(slminlb)
                layout.add_widget(slmidlb)
                layout.add_widget(slmaxlb)
                self.SL_list.append(sl)
                top_con = sl.bottom - 1.5*MARGIN

            elif quest['type'] == "TI":
                self.questions.append({"answers_index":len(self.TI_list)+1,
                                  "question":quest['quest'],
                                  "type":"TI",
                                  "index": quest_counter})
                tif = TextInput(left=MARGIN,
                                font_size=FONT_SIZE,
                                top=top_con,
                                width=self.width - 2*MARGIN,
                                height=self.quest['multiline'] * TEXT_INPUT_TEXT_HEIGHT)
                layout.add_widget(tif)

                self.TI_list.append(tif)
                top_con = tif.bottom - 1.5*MARGIN

            elif quest['type'] == "LI":
                self.questions.append({"answers_index":len(self.LI_list)+1,
                                  "question":quest['quest'],
                                  "type":"LI",
                                  "index": quest_counter})
                curr_x = 0
                li_width_inc = self.width / (len(quest['ans']) + 1)
                answers = []
                for ans in quest['ans']:
                    curr_x = curr_x + li_width_inc
                    libut = kivy.uix.togglebutton.ToggleButton(center_x=curr_x,
                                                               top=top_con - 2*MARGIN,
                                                               width=MARGIN,
                                                               height=MARGIN,
                                                               group=quest['quest'])
                    layout.add_widget(libut)
                    answers.append(libut)
                    lilab = kivy.uix.label.Label(text=ans,
                                                 bottom=libut.top,
                                                 center_x=libut.center_x,
                                                 font_size=FONT_SIZE,
                                                 color=TEXT_COLOR)
                    layout.add_widget(lilab)
                self.LI_list.append(answers)
                top_con = libut.bottom - 1.5*MARGIN

            if quest['type'] == "TITLE":
                titlab = kivy.uix.label.Label(text=str(quest_counter) + ". " + quest['question'],
                                              center_x=layout.center_x,
                                              center_y=top_con - 2*MARGIN,
                                              text_size=(self.width - 5*MARGIN, None),
                                              color=TEXT_COLOR, halign="center",
                                              font_size=2*FONT_SIZE)
                layout.add_widget(titlab)
                top_con = titlab.center_y - 2*MARGIN

        with self.canvas:
            root = ScrollView(size_hint=(1, None),
                              size=(self.width, self.height),
                              x=self.x,
                              y=self.y)
            root.add_widget(layout)
        self.active = True

    def stop(self):
        self.active = False
        self.results = []
        for quest in self.questions:
            if quest['type'] == "TI":
                self.results.append({"question":quest['question'],
                                     "type":"TI",
                                     "index":quest['index'],
                                     "answers":{"ans":"text_input_value",
                                                "value":self.TI_lis[quest['answers_index'].text},
                                     })
            elif quest['type'] == "CT":
                self.results.append({"question": quest['question'],
                                     "type": "CT", "index": quest['index'],
                                     "answers": [{"ans": "slider_value",
                                                  "value": self.CT_list[quest['answers_index']].value}]
                                     })
            elif quest['type'] == "MC":
                answers_list = []
                for ans in self.MC_list[quest['answer_index']]:
                    answers_list.append({"ans": ans.name,
                                         "value": ans.state == 'down'})
                self.results.append({"question": quest['question'],
                                     "type": "MC", "index": quest['index'],
                                     "answers": answers_list})
            elif quest['type'] == "CA":
                answers_list = []
                for ans in self.CA_list[quest['answer_index']]:
                    answers_list.append({"ans": ans.name,
                                         "value": ans.state == 'down'})
                self.results.append({"question": quest['question'],
                                     "type": "CA", "index": quest['index'],
                                     "answers": answers_list})
            elif quest['type'] == "LI":
                answers_list = []
                for ans in self.LI_list[quest['answer_index']]:
                    answers_list.append({"ans": ans.name,
                                         "value": ans.state == 'down'})
                self.results.append({"question": quest['question'],
                                     "type": "LI", "index": quest['index'],
                                     "answers": answers_list})

class Questionnaire(WidgetState.wrap(_Questionnaire)):
    def show(self):
        # custom show so that the widget doesn't run when not onscreen
        self._widget.start()
        super(Enterprise, self).show()

    def unshow(self):
        # custom unshow so that the widget doesn't run when not onscreen
        super(Enterprise, self).unshow()
        self._widget.stop()
"""
if __name__ == "__main__":
    from mouse import MouseCursor
    bob = [{'type': "TITLE",
            'question': "SMILE QUESTIONNAIRE"},
           {'type': "LI",
            'question': "How Happy Are You?",
            'ans': ['Not Happy',
                    '', '',
                    'Meh',
                    '', '',
                    'Happy'],
            'group_id': 'first_question'},
           {'type': "LI",
            'question': "How Old are you?",
            'ans': ['<10', '12', '15', '<20'],
            'group_id':'second_li_question'},
           {'type': "LI",
            'question': "To be or not to be?",
            'ans': ['That is the Question.',
                    'To be is to do.',
                    'To do is to be.'],
            'group_id': 'THIRD_li_question'},
           {'type': "CT",
            'question': "How many years have you lived in your current home?",
            'ans': ['1', '5', '10'],
            'max': 5,
            'min': -5},
           {'type': "CT",
            'question': "Where left is Too much, and right is too little, and middle is just right, how much does your car cost?",
            'ans': ['', '', ''],
            'max': 10,
            'min': -10},
           {'type': "TI",
            'question': "Choose your favorite name.",
            'ans': ['Moe', 'Curly', 'Larry'],
            'group_id': 'second_ans_question'},
           {'type': "TI",
            'question': "If you could do anything in the world right now, what would it be?",
            'multiline': 1},
           {'type': "TI",
            'question': "Tell me about your life.",
            'multiline': 3},
           {'type': "TI",
            'question': "Tell me about your breakfest",
            'multiline': 2},
           {'type': "MC",
            'question': "Choose your Favorite Jim Carry Movie!",
            'ans': ['Eternal Sunshine of the Spotless Mind',
                    'Yes Man',
                    'A Series of Unfortunate Events',
                    'I Love You, Phillip Morris!'],
            'group_id': 'third_ans_question'},
           {'type': "CA",
            'question': "Choose the all that apply!",
            'ans': ['I am an Adult', 'I have a pet', 'I own a house'],
            'group_id': 'choose_question_one'},
           {'type': "TITLE",
            'question': "SMILE QUESTIONNAIRE 2 "},
           {'type': "LI",
            'question': "How Happy is your family?",
            'ans': ['Not Happy',
                    '', '',
                    'Meh',
                    '', '',
                    'Happy'],
            'group_id': 'first_question'},
           {'type': "LI",
            'question': "How Old is your mother?",
            'ans': ['10', '12', '15', '20'],
            'group_id': 'second_li_question'}]

    from experiment import Experiment
    exp = Experiment()
    with Parallel():
        tt = Questionnaire(loq=bob,
                           height=800,
                           width=600,
                           x=50, y=50,)
        MouseCursor(blocking=False)
    exp.run()


"""
