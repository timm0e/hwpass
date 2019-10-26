from pykeepass.group import Group
from pykeepass.entry import Entry

from pi.rotaryEncoder import Callback, RotaryInput
from pi.display import *

back_text = "<<"


class Nav(Callback):
    def __init__(self, kp):
        self.kp = kp
        self.back = [kp.root_group]
        self.index = 0
        self.dir = self.__select_group(kp.root_group)
        self.display_selected()

        # Implement Callback
        self.next = self.step_next
        self.prev = self.step_prev
        self.press = self.step_into

    def get_selected(self):
        return self.dir[self.index]

    def display_selected(self):
        line_1 = "/"
        if len(self.back) > 1:
            line_1 += self.back[-1].path
            if len(line_1) > 16:
                if line_1[-1] == "/":
                    curr_dir = line_1.split('/')[-2] + '/'
                else:
                    curr_dir = line_1.split('/')[-1]
                if len(curr_dir) > 12:
                    curr_dir = curr_dir[:10] + "..."
                line_1 = ".../" + curr_dir
        line_2 = ""
        current = self.get_selected()
        if self.index == 0:
            line_2 = current
        else:
            if type(current) is Group:
                line_2 = current.name
            elif type(current) is Entry:
                title = current._get_string_field("Title")
                if title == "" or title is None:
                    title = current.username
                    if title == "" or title is None:
                        title = "<no name>"
                line_2 = title
            elif type(current) is str:
                line_2 = current
        print_first_line(line_1)
        print_second_line(line_2)
        print("1:", line_1)
        print("2:", line_2)
        print("-----")

    def step_next(self):
        self.index = (self.index + 1) % len(self.dir)
        self.display_selected()

    def step_prev(self):
        self.index = (self.index - 1) % len(self.dir)
        self.display_selected()

    def step_into(self):
        if self.index == 0:
            self.__step_out()
        else:
            selected = self.get_selected()
            if type(selected) is Group:
                self.back.append(selected)
                self.index = 0
                self.dir = self.__select_group(selected)
            elif type(selected) is Entry:
                self.back.append(selected)
                self.index = 0
                self.dir = self.__select_entry(selected)
            elif type(selected) is str:
                username = self.back[-1].username
                password = self.back[-1].password
                print("sending to client")
                # send to client
        self.display_selected()

    def __step_out(self):
        if len(self.back) > 1:
            self.dir = self.__select_group(self.back[-2])
            self.back.pop()
            self.index = 0

    # returns array of all direct entries, groups and a 'back' option of a group
    def __select_group(self, group):
        result = [back_text]

        for g in group.subgroups:
            result.append(g)

        for e in group.entries:
            result.append(e)

        return result

    def __select_entry(self, entry):
        return [back_text, "un: " + entry.username, "pw: " + entry.password]


def act(nav, input):
    if len(input) == 1:
        if input == "w":
            nav.step_prev()
        elif input == "s":
            nav.step_next()
        elif input == "d":
            nav.step_into()
