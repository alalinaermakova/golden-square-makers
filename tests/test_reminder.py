from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"

def test_reminds_the_user_to_do_a_task1():
    reminder = Reminder("Alina")
    reminder.remind_me_to("Make dinner")
    result = reminder.remind()
    assert result == "Make dinner, Alina!"