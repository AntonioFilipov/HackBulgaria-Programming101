from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from expresion import Expression
from sqlalchemy import desc
from player import Player
from connect import Base
import random
import math


def set_expression(session):
    signs = ['+', '-', '*', '/', '^']
    second_operand = 0
    sign_char = '/'
    while second_operand == 0 and sign_char == '/':
        first_operand = random.randrange(10)
        second_operand = random.randrange(10)
        sign_char = random.choice(signs)

    new_expression = Expression(left_operand=first_operand, sign=sign_char, right_operand=second_operand, result="")
    result = resolve_expression(new_expression)
    new_expression.result = result
    session.add(new_expression)
    session.commit()
    return new_expression


def resolve_expression(new_expression):
    if new_expression.sign == '+':
        answer = new_expression.left_operand + new_expression.right_operand
    elif new_expression.sign == '-':
        answer = new_expression.left_operand - new_expression.right_operand
    elif new_expression.sign == '*':
        answer = new_expression.left_operand * new_expression.right_operand
    elif new_expression.sign == '^':
        answer = int(math.pow(new_expression.left_operand, new_expression.right_operand))
    elif new_expression.sign == '/':
        answer = new_expression.left_operand / float(new_expression.right_operand)

    answer = str(answer)
    if '.' in answer:
        split_answer = answer.split('.')
        if split_answer[1] == '0':
            answer = split_answer[0]
        else:
            answer = "{}.{}".format(split_answer[0], split_answer[1][:2])
    return answer


def start(session):
    points_for_correct_answer = 0
    print("Enter your playername:")
    player_name = input(">")
    player = Player(name=player_name, high_score=0)
    print("Hello %s! Let the game begin!" % player.name)

    while(True):
        expression = set_expression(session)
        print("What is the answer to " + str(expression))
        player_answer = input("?>")

        if expression.result == player_answer:
            print("Correct")
            points_for_correct_answer += 1
        else:
            if player.high_score < points_for_correct_answer * points_for_correct_answer:
                player.high_score = points_for_correct_answer * points_for_correct_answer
            print("Incorrect! Ending game. Your score is: %s" % (points_for_correct_answer * points_for_correct_answer))
            break
    session.add(player)
    session.commit()


def highscores(session):
    print("This is the current top10:")
    result = session.query(Player).order_by(Player.high_score.desc()).limit(10)
    for player in result:
        print (player)


def menu(session):
    game_menu = {'highscores': highscores, 'start': start}
    print("Welcome to the \"Do you even math\"?")
    print("Floating point numbers are rounded up to 2 digits after '.'! (0.12345 = 0.12)")
    print("Here are your options:")
    print("- start")
    print("- highscores")

    while(True):
        answer = input("?>")
        if answer in game_menu.keys():
            game_menu[answer](session)
            break
        else:
            print("Wrong command! Try again")




def main():
    engine = create_engine("sqlite:///math.db")
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    menu(session)
    # print(set_expression(session))
if __name__ == '__main__':
    main()