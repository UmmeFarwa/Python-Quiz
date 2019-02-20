import random
import MySQLdb
from turtle import Turtle,Screen,mainloop
def graphics():
    #from turtle import Turtle, Screen, mainloop
    t = Turtle()
    t.screen.bgcolor("red")
    t.hideturtle()
    t.screen.bgpic("good-luck-Horse-Nail-Wallpaper.gif")
    t.color("red")#t.write("Please close the current window to proceed..!",move=True, align="center", font=("copper black", 15, "normal"))
    t.goto(200, -150)
    t.color("white")
    t.write("Please close the current window to proceed!", move=True, align="right", font=("copper black", 10, "normal"))
    mainloop()
def thanks():
    c = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")    # from turtle import Turtle, Screen, mainloop
    clear()
    clear()
    clear()


    t = Turtle()
    t.screen.bgcolor("red")

    t.hideturtle()
    t.color("red")
    t.screen.bgpic("X93L.gif")
    t.color("black")
    #t.write("Please close the current window to proceed..!", move=True, align="center",
    #font=("copper black", 15, "normal"))
    t.goto(200, -150)
    t.color("white")
    t.write("Please close the current window to proceed!", move=True, align="right", font=("copper black", 10, "normal"))

    mainloop()
    clear()
    clear()
    clear()



def congrats_graphics():
        z = raw_input("PRESS ENTER TO PROCEED..!!")
        t = Turtle()
        t.screen.bgcolor("black")
        t.hideturtle()

        t.screen.bgpic("fr.gif")
        t.color("white")
        t.write("YOU QUALIFIED FOR THE NEXT LEVEL.....!!!", move=True, align="center", font=("copper black", 17, "normal"))
        t.color("black")
        t.goto(200, -150)
        t.color("white")
        t.write("Please close the current window to proceed!", move=True, align="right",
                font=("copper black", 10, "normal"))

        mainloop()


def clear():
    print "\n" * 5

                  ########################### class quiz_result#######################
class quiz_results():
    def create_table(self):
        db = MySQLdb.connect("localhost", "root", "", "test")
        cursor = db.cursor()
        cursor.execute("SET sql_notes = 0")
        sql = """CREATE TABLE IF NOT EXISTS player (
                 Name_of_player  CHAR(50) NOT NULL,
                 player_num VARCHAR(11) NOT NULL,
                 Player_ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
                 easy_score INT DEFAULT NULL,
                 med_score INT DEFAULT NULL,
                 high_score INT DEFAULT NULL)"""
        cursor.execute(sql)
        sql = """SELECT * FROM player """
        cursor.execute(sql)
        db.close()

    def write_in_sql_table(self, name, phone_num):
        db = MySQLdb.connect("localhost", "root", "", "test")
        cursor = db.cursor()
        # name = str(raw_input('Please Enter your full name .. :'))
        sql = "INSERT INTO player(Name_of_pLayer,player_num,Player_ID)\
               VALUES ('%s','%s',NULL)" % \
              (name, phone_num)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        sql = """SELECT * FROM player"""
        cursor.execute(sql)
        db.close()
        return name
       ##########################class end###################

        ########################### class high_score#######################
class highscore():
    def view_easyhighscore(self):
       # print'\n' * 100
        clear()
        clear()
        clear()
        print'\033[1;43m\t\t\t\t\t\t\t\t\t***************HIGHCORE OF EASY LEVEL************\n\033[1;m\n'
        db = MySQLdb.connect("localhost", "root", "", "test")
        cursor = db.cursor()
        sql = "SELECT MAX(easy_score) AS maximum FROM player"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print'\n\n\t\t\t\t\t\t\t\033[1;31m====================================================================\033[1;m'
            print"\t\t\t\t\t\t\t\033[1;35m*******HIGHSCORE OF EASY LEVEL:\033[1;m ", row[0],"\033[1;35m*********\033[1;m"
            print'\t\t\t\t\t\t\t\033[1;31m====================================================================\033[1;m'
        db.close()
        clear()
    def view_medhs(self):
        clear()
        clear()
        clear()
        print'\033[1;43m\t\t\t\t\t\t\t********************HIGHCORE OF MEDIUM LEVEL************\n\033[1;m'
        db = MySQLdb.connect("localhost", "root", "", "test")
        cursor = db.cursor()
        sql = "SELECT  MAX(med_score)AS maximum FROM player"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print'\t\t\t\t\t\033[1;31m====================================================================\033[1;m'
            print"\t\t\t\t\t\t\t\033[1;35m*******HIGHSCORE OF MEDIUM LEVEL:\033[1;m ", row[0], "\033[1;35m*********\033[1;m"
            print'\t\t\t\t\t\033[1;31m====================================================================\033[1;m'
        db.close()
        clear()

    def view_hardhs(self):
        clear()
        clear()
        clear()

        print'\033[1;43m\t\t\t\t\t\t\t\t***************HIGHCORE OF HARD LEVEL************\n\033[1;m'
        db = MySQLdb.connect("localhost", "root", "", "test")
        cursor = db.cursor()
        sql = "SELECT  MAX(high_score)AS MAX FROM player"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print'\t\t\t\t\t\t\033[1;31m====================================================================\033[1;m'
            print"\t\t\t\t\t\t\t\t\033[1;35m*******HIGHSCORE OF EASY LEVEL:\033[1;m ", row[0], "\033[1;35m*********\033[1;m"
            print'\t\t\t\t\t\t\033[1;31m====================================================================\033[1;m'
        db.close()
        clear()

        ########################### class end#######################

        ########################### class playerreport #######################
class playerreport():
    def view_progress(self, newphone_num):
        db = MySQLdb.connect("localhost", "root", "", "test")

        cursor = db.cursor()
        sql = "SELECT Name_of_player,player_num, Player_ID, easy_score, med_score , high_score FROM player WHERE player_num = '%s'" % \
              (newphone_num)

        cursor.execute(sql)
        row = cursor.fetchone()
        while row is not None:
                print"\t\t\t\t\t\t\t\t\t\t\t\t\033[1;45m********************************\033[1;m"
                print '\n\t\t\t\t\t\t\t\t\t\t\t\t\033[1;31mNAME: \033[1;m', row[0]
                print '\t\t\t\t\t\t\t\t\t\t\t\t\033[1;31mMOBILE NUMBER: \033[1;m', row[1]
                print '\t\t\t\t\t\t\t\t\t\t\t\t\033[1;31mPLAYER ID: \033[1;m', row[2]
                print "\t\t\t\t\t\t\t\t\t\t\t\t\033[1;31mPOINTS SECURED IN EASY LEVEl: \033[1;m", row[3]
                print '\t\t\t\t\t\t\t\t\t\t\t\t\033[1;31mPOINTS SECURED IN MEDIUM LEVEL : \033[1;m', row[4]
                print '\t\t\t\t\t\t\t\t\t\t\t\t\033[1;31mPOINTS SECURED IN HIGH LEVEl: \033[1;m', row[5]
                print"\n"
                print"\t\t\t\t\t\t\t\t\t\t\t\t\033[1;45m****" \
                     "*******************************\033[1;m"
                row = cursor.fetchone()
        #cursor = db.cursor()
        db.close()
        return newphone_num

        ########################### class end #######################

        ########################### class hard_level ######################
class hard_level():

    def hard_quiz(self, phone_num, name):
        graphics()
        clear()
        clear()
        z=raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO CONTINUE :\033[1;m")
        print"\n\033[1;42m\t\t\t\t\t\t\t\t\t\t\t******HARD LEVEL***************\n\033[1;m"
        questions_hard = [
            'Q : What will be the output ? \n\nvar=[[0] for k in range (6)]\ntmp=[[1] for k in range (3)]\nvar[0:6:2]=tmp\nprint var\n\na.[[0],[0],[0],[0],[0],[0]]\nb.[[1],[0],[1],[0],[1],[0]]\nc.[[0],[1],[0],[1],[0],[1]]\nd.[1,0,1,0,1,0,]',
            'Q :What does the following function do?\nmath.floor(foo)\na.Return the absolute value of foo\nb.Return the floor of foo as a float\nc.Return the mantissa and exponent of foo\nd.Return the ceiling of foo as  float',
            'Q :What is equivalent for this expression?\nlambda *args:None\na.def do_nothing (*args):pass\nb.def do_nothing(*args):pass()\nc.lambda *args:pass\nd.def do_nothing():pass',
            'Q :What is the correct way to print the letter T from the string PYTHON?\na.print "PYTHON"[2]\nb.print "PYTHON"(3)\nc.print PYTHON{2}\nd.print "PYTHON"(2)',
            'Q :What will be the output?\nfrom functions import partial\nfrom operator import mul\n\ndef foo():\n\treturn[partial(mul,k) for k in range(4)]\n\nprint[var(2) for var in foo()]\na.[6,6,6,6]\nb.[0,2,4,6]\nc.[0,0,0,0]\nd.[]',
            'Q :If you have a variable \"example\", how do you check to see what type of variable you are working with?\na. getType(example)\nb.Type(example)\nc.type(example)\nd. example.type',
            'Q :If you had a statement like, \"f = open(\"test.txt\",\"w\")\", what would happen to the file as soon asthat statement is executed?\na.Nothing, unless the code following it writes to the file\nb.The file\'s contents will be erased\nc.Nothing\nd.Python will save the file\'s contents and append whatever the code following says to write.',
            'Q :What is the output of the following code?\ndef make_pretty(func):\n\tdef inner():\n\t\tprint(\"I got decorated\")\n\t\tfunc()\n\t return inner\n def ordinary():\n\tprint(\"I am ordinary\")\npretty = make_pretty(ordinary)\npretty()\na.I got decorated\nb.I am pretty\nc.I got decorated\nI am ordinary\nd.I am ordinary\nI got decorated',
            'Q :What is the more pythonic way to use getters and setters?\na.Decorators\nb.generators\nc.iterators\nd.@property',
            'Q :What is the output of the following?\nx = [12, 34]\nprint(len(''.join(list(map(str, x)))))\na.4\nb.5\nc.6\nd.ERROR'
        ]
        random.shuffle(questions_hard)
        q = 0
        hcount = 0
        while q < 10:
            if questions_hard[
                0] == 'Q : What will be the output ? \n\nvar=[[0] for k in range (6)]\ntmp=[[1] for k in range (3)]\nvar[0:6:2]=tmp\nprint var\n\na.[[0],[0],[0],[0],[0],[0]]\nb.[[1],[0],[1],[0],[1],[0]]\nc.[[0],[1],[0],[1],[0],[1]]\nd.[1,0,1,0,1,0,]':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ : What will be the output ? \n\n\t\t\t\t\t\tvar=[[0] for k in range (6)]\n\t\t\t\t\t\ttmp=[[1] for k in range (3)]\n\t\t\t\t\t\tvar[0:6:2]=tmp\n\t\t\t\t\t\tprint var\n\n\t\t\t\t\t\ta.[[0],[0],[0],[0],[0],[0]]\n\t\t\t\t\t\tb.[[1],[0],[1],[0],[1],[0]]\n\t\t\t\t\t\tc.[[0],[1],[0],[1],[0],[1]]\n\t\t\t\t\t\td.[1,0,1,0,1,0,]\033[1;m'
                hard_q1 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if hard_q1 == 'b':
                    hcount += 1
                del questions_hard[0]
                q += 1
                clear()
            elif questions_hard[
                0] == 'Q :What does the following function do?\nmath.floor(foo)\na.Return the absolute value of foo\nb.Return the floor of foo as a float\nc.Return the mantissa and exponent of foo\nd.Return the ceiling of foo as  float':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ :What does the following function do?\n\t\t\t\t\t\tmath.floor(foo)\n\t\t\t\t\t\ta.Return the absolute value of foo\n\t\t\t\t\t\tb.Return the floor of foo as a float\n\t\t\t\t\t\tc.Return the mantissa and exponent of foo\n\t\t\t\t\t\td.Return the ceiling of foo as  float\033[1;m'
                hard_q2 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if hard_q2 == 'b':
                    hcount += 1
                del questions_hard[0]
                q += 1
                clear()
            elif questions_hard[
                0] == 'Q :What is equivalent for this expression?\nlambda *args:None\na.def do_nothing (*args):pass\nb.def do_nothing(*args):pass()\nc.lambda *args:pass\nd.def do_nothing():pass':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ :What is equivalent for this expression?\n\t\t\t\t\t\tlambda *args:None\n\t\t\t\t\t\ta.def do_nothing (*args):pass\n\t\t\t\t\t\tb.def do_nothing(*args):pass()\n\t\t\t\t\t\tc.lambda *args:pass\n\t\t\t\t\t\td.def do_nothing():pass\033[1;m'
                hard_q3 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if hard_q3 == 'a':
                    hcount += 1
                del questions_hard[0]
                q += 1
            elif questions_hard[
                0] == 'Q :What is the correct way to print the letter T from the string PYTHON?\na.print "PYTHON"[2]\nb.print "PYTHON"(3)\nc.print PYTHON{2}\nd.print "PYTHON"(2)':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ :What is the correct way to print the letter T from the string PYTHON?\n\t\t\t\t\t\ta.print "PYTHON"[2]\n\t\t\t\t\t\tb.print "PYTHON"(3)\n\t\t\t\t\t\tc.print PYTHON{2}\n\t\t\t\t\t\td.print "PYTHON"(2)\033[1;m'
                hard_q4 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if hard_q4 == 'a':
                    hcount += 1
                del questions_hard[0]
                q += 1
                clear()
            elif questions_hard[
                0] == 'Q :What will be the output?\nfrom functions import partial\nfrom operator import mul\n\ndef foo():\n\treturn[partial(mul,k) for k in range(4)]\n\nprint[var(2) for var in foo()]\na.[6,6,6,6]\nb.[0,2,4,6]\nc.[0,0,0,0]\nd.[]':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ :What will be the output?\n\t\t\t\t\t\tfrom functions import partial\n\t\t\t\t\t\tfrom operator import mul\n\n\t\t\t\t\t\tdef foo():\n\t\t\t\t\t\t\treturn[partial(mul,k) for k in range(4)]\n\n\t\t\t\t\t\tprint[var(2) for var in foo()]\n\t\t\t\t\t\ta.[6,6,6,6]\n\t\t\t\t\t\tb.[0,2,4,6]\n\t\t\t\t\t\tc.[0,0,0,0]\n\t\t\t\t\t\td.[]\033[1;m'
                hard_q5 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if hard_q5 == 'b':
                    hcount += 1
                del questions_hard[0]
                q += 1
                clear()
            elif questions_hard[
                0] == 'Q :If you have a variable \"example\", how do you check to see what type of variable you are working with?\na. getType(example)\nb.Type(example)\nc.type(example)\nd. example.type':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ :If you have a variable \"example\", how do you check to see what type of variable you are working with?\n\t\t\t\t\t\ta. getType(example)\n\t\t\t\t\t\tb.Type(example)\n\t\t\t\t\t\tc.type(example)\n\t\t\t\t\t\td. example.type\033[1;m'
                hard_q6 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if hard_q6 == 'd':
                    hcount += 1
                del questions_hard[0]
                q += 1
                clear()
            elif questions_hard[
                0] == 'Q :If you had a statement like, \"f = open(\"test.txt\",\"w\")\", what would happen to the file as soon asthat statement is executed?\na.Nothing, unless the code following it writes to the file\nb.The file\'s contents will be erased\nc.Nothing\nd.Python will save the file\'s contents and append whatever the code following says to write.':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34mQ :If you had a statement like, \"f = open(\"test.txt\",\"w\")\", what would happen to the file as soon as\nthat statement is executed?\n\t\t\t\t\t\ta.Nothing, unless the code following it writes to the file\n\t\t\t\t\t\tb.The file\'s contents will be erased\n\t\t\t\t\t\tc.Nothing\n\t\t\t\t\t\td.Python will save the file\'s contents and append whatever the code following says to write.\033[1;m'
                hard_q7 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if hard_q7 == 'b':
                    hcount += 1
                del questions_hard[0]
                q += 1
                clear()
            elif questions_hard[
                0] == 'Q :What is the output of the following code?\ndef make_pretty(func):\n\tdef inner():\n\t\tprint(\"I got decorated\")\n\t\tfunc()\n\t return inner\n def ordinary():\n\tprint(\"I am ordinary\")\npretty = make_pretty(ordinary)\npretty()\na.I got decorated\nb.I am pretty\nc.I got decorated\nI am ordinary\nd.I am ordinary\nI got decorated':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ :What is the output of the following code?\n\t\t\t\t\t\tdef make_pretty(func):\n\t\t\t\t\t\t\tdef inner():\n\t\t\t\t\t\t\t\tprint(\"I got decorated\")\n\t\t\t\t\t\t\t\tfunc()\n\t\t\t\t\t\t\t return inner\n\t\t\t\t\t\t def ordinary():\n\t\t\t\t\t\t\tprint(\"I am ordinary\")\n\t\t\t\t\t\tpretty = make_pretty(ordinary)\n\t\t\t\t\t\tpretty()\n\t\t\t\t\t\ta.I got decorated\n\t\t\t\t\t\tb.I am pretty\n\t\t\t\t\t\tc.I got decorated\n\t\t\t\t\t\t  I am ordinary\n\t\t\t\t\t\td.I am ordinary\n\t\t\t\t\t\t  I got decorated\033[1;m'
                hard_q8 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if hard_q8 == 'c':
                    hcount += 1
                del questions_hard[0]
                q += 1
                clear()
            elif questions_hard[
                0] == 'Q :What is the more pythonic way to use getters and setters?\na.Decorators\nb.generators\nc.iterators\nd.@property':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ :What is the more pythonic way to use getters and setters?\n\t\t\t\t\t\ta.Decorators\n\t\t\t\t\t\tb.generators\n\t\t\t\t\t\tc.iterators\n\t\t\t\t\t\td.@property\033[1;m'
                hard_q9 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if hard_q9 == 'd':
                    hcount += 1
                    q += 1
                del questions_hard[0]
                q += 1
                clear()
            elif questions_hard[
                0] == 'Q :What is the output of the following?\nx = [12, 34]\nprint(len(''.join(list(map(str, x)))))\na.4\nb.5\nc.6\nd.ERROR':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ :What is the output of the following?\n\t\t\t\t\t\tx = [12, 34]\n\t\t\t\t\t\tprint(len(''.join(list(map(str, x)))))\n\t\t\t\t\t\ta.4\n\t\t\t\t\t\tb.5\n\t\t\t\t\t\tc.6\n\t\t\t\t\t\td.ERROR\033[1;m'
                hard_q10 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if hard_q10 == 'a':
                    hcount += 1
                del questions_hard[0]
                q += 1
                clear()
        choice = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO SEE YOUR SCORE :\033[1;m")
        clear()
        print"\033[1;45m\t\t\t\t\t\t********************************\n\033[1;m"
        print'\033[1;34m\t\t\t\t\t\t\t\t\tYOUR SCORE IS :\033[1;m ', hcount
        print"\033[1;45m\t\t\t\t\t\t********************************\n\033[1;m"

        db = MySQLdb.connect("localhost", "root", "", "test")
        cursor = db.cursor()
        sql = "UPDATE player \
               SET high_score = '%d' \
                WHERE player_num = '%s'" % \
              (hcount, phone_num)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        sql = """SELECT * FROM player"""
        cursor.execute(sql)
        db.close()
        print"\n" * 10
        if hcount >= 7 :
            thanks()
            t = Turtle()
            t.screen.bgcolor("black")

            t.hideturtle()

            t.screen.bgpic("fr.gif")
            t.color("purple")
            t.write("CONGRATULATIONS..!!YOU CLEARED ALL LEVELS!!!", move=True, align="center",
                    font=("copper black", 15, "normal"))
            t.color("black")
            t.goto(235, -140)
            t.color("white")
            t.write("Please close the current window to proceed", move=True, align="right",
                    font=("copper black", 10, "normal"))

            mainloop()
            print"\033[1;31m\t\t\t\t\t\t\t\t\t\t\t********************************************\033[1;m"
            print"\t\t\t\t\t\t\t\t\t\t\t\033[1;33m----------*******----------\033[1;m"
            print"\t\t\t\t\t\t\t\t\t\t\t\033[1;34mCERTIFICATE OF ACHIEVEMENT\033[1;m"
            print"\t\t\t\t\t\t\t\t\t\t\t\033[1;34mMany Congratulations :)\033[1;m", name
            print"\t\t\t\t\t\t\t\t\t\t\t\033[1;33m----------*******----------\033[1;m"
            print"\t\t\t\t\t\t\t\t\t\t\t\033[1;34mOn Successfully Completing the PYTHON QUIZ\033[1;m"
            print"\t\t\t\t\t\t\t\t\t\t\t\033[1;34mKeep Participating.....!!!!\033[1;m"
            print"\t\t\t\t\t\t\t\t\t\t\t\033[1;33m----------*******----------\033[1;m"
            print"\033[1;31m\t\t\t\t\t\t\t\t\t\t\t*******************************************\033[1;m"
            z = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ENTER TO PROCEED :\033[1;m")
            choice = raw_input("\033[1;35m\n\n\t\t\t\t\tBACK TO THE MAIN MENU?(y/n) :\033[1;m")
            if choice == 'y':
                menu(phone_num, name)
            else:
                main()
        elif hcount <= 6:
            #z = raw_input("Press any key to continue")  # from turtle import Turtle, Screen, mainloop
            t = Turtle()
            t.screen.bgcolor("black")

            t.hideturtle()

            #t.screen.bgpic("X93L.gif")
            t.color("RED")
            t.write("OOPS... YOU DID NOT QUALFY THE ROUND..\nBETTER LUCK NEXT TIME", move=True, align="center",
                    font=("copper black", 10, "normal"))
            t.color("black")
            t.goto(235, -140)
            t.color("white")
            t.write("Please close the current window to proceed!", move=True, align="right",
                    font=("copper black", 15, "normal"))

            mainloop()

            thanks()
            z = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO CONTINUE :\033[1;m")
            menu(phone_num,name)
            ########################### class end #######################

            ########################### class medium_level #######################
class medium_level(hard_level):
    obj2 = hard_level()

    def med_quiz(self, phone_num, name):
        graphics()
        z = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ENTER TO START THE LEVEL..!! :\033[1;m")
        print"\n\033[1;42m\t\t\t\t\t\t\t\t\t\t\t******MEDIUM LEVEL***************\n\033[1;m"
        questions_medium = [
            'Q : What is the output of the following?\nx = [\'ab\', \'cd\']\nprint(len(list(map(list, x))))))\na- 2\nb- 4\nc- error\nd- none of the mentioned',
            'Q : Which of the following function convert a String to a tuple in python?\na - repr(x)\nb - eval(str)\nc - tuple(s)\nd - list(s)',
            'Q : What is the output of the following?\nx = [12, 34]\nprint(len(list(map(len, x))))\na- 2\nb- 1\nc- error\nd- none of the mentioned',
            'Q : What is the output of print tinytuple * 2 if tinytuple = (123, \'john\')?\na - (123, \'john\', 123, \'john\')\nb - (123, \'john\') * 2\nc - Error\nd - None of the above',
            'Q : Which of the following function convert an integer to a character in python?\na - set(x)\nb - dict(d)\nc - frozenset(s)\nd - chr(x)',
            'Q : Which of the following function returns a random float r, such that 0 is less than or equal to r and r is less than 1?\na - choice(seq)\nb - randrange([start, ] stop[, step])\nc - random()\nd - seed([x])',
            'Q : Which of the following function checks in a string that all characters are in uppercase?\na - isupper()\nb - join(seq)\nc - len(string)\nd - ljust(width[, fillchar]',
            'Q : Which of the following function converts a string to all lowercase?\na - lower()\nb - lstrip()\nc - max(str)\nd - min(str)',
            'Q : What is the following function reverses objects of list in place?\na - list.reverse()\nb - list.sort([func])\nc - list.pop(obj=list[-1])\nd - list.remove(obj)',
            'Q : What is the output of print str[0] if str = \'Hello World!\'?\n\na - Hello World!\nb - H\nc - ello World!\nd - None of the above.',
        ]
        random.shuffle(questions_medium)
        j = 0
        medium_score = 0
        while j < 10:
            if questions_medium[
                0] == 'Q : What is the output of the following?\nx = [\'ab\', \'cd\']\nprint(len(list(map(list, x))))))\na- 2\nb- 4\nc- error\nd- none of the mentioned':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ : What is the output of the following?\n\t\t\t\t\t\tx = [\'ab\', \'cd\']\n\t\t\t\t\t\tprint(len(list(map(list, x))))))\n\t\t\t\t\t\ta- 2\n\t\t\t\t\t\tb- 4\n\t\t\t\t\t\tc- error\n\t\t\t\t\t\td- none of the mentioned\033[1;m'
                med_q1 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if med_q1 == 'c':
                    medium_score += 1
                del questions_medium[0]
                j += 1
                clear()
            elif questions_medium[
                0] == 'Q : Which of the following function convert a String to a tuple in python?\na - repr(x)\nb - eval(str)\nc - tuple(s)\nd - list(s)':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ : Which of the following function convert a String to a tuple in python?\n\t\t\t\t\t\ta - repr(x)\n\t\t\t\t\t\tb - eval(str)\n\t\t\t\t\t\tc - tuple(s)\n\t\t\t\t\t\td - list(s)\033[1;m'
                med_q2 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if med_q2 == 'c':
                    medium_score += 1
                del questions_medium[0]
                j += 1
                clear()
            elif questions_medium[0] == 'Q : What is the output of the following?\nx = [12, 34]\nprint(len(list(map(len, x))))\na- 2\nb- 1\nc- error\nd- none of the mentioned':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ : What is the output of the following?\n\t\t\t\t\t\tx = [12, 34]\n\t\t\t\t\t\tprint(len(list(map(len, x))))\n\t\t\t\t\t\ta- 2\n\t\t\t\t\t\tb- 1\n\t\t\t\t\t\tc- Error\n\t\t\t\t\t\td- none of the mentioned\033[1;m'
                med_q3 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if med_q3 == 'c':
                    medium_score += 1
                del questions_medium[0]
                j += 1
                clear()
            elif questions_medium[
                0] == 'Q : What is the output of print tinytuple * 2 if tinytuple = (123, \'john\')?\na - (123, \'john\', 123, \'john\')\nb - (123, \'john\') * 2\nc - Error\nd - None of the above':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ : What is the output of print tinytuple * 2 if tinytuple = (123, \'john\')?\n\t\t\t\t\t\ta - (123, \'john\', 123, \'john\')\n\t\t\t\t\t\tb - (123, \'john\') * 2\n\t\t\t\t\t\tc - Error\n\t\t\t\t\t\td - None of the above\033[1;m'
                med_q4 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if med_q4 == 'a':
                    medium_score += 1
                del questions_medium[0]
                j += 1
                clear()
            elif questions_medium[
                0] == 'Q : Which of the following function convert an integer to a character in python?\na - set(x)\nb - dict(d)\nc - frozenset(s)\nd - chr(x)':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ : Which of the following function convert an integer to a character in python?\n\t\t\t\t\t\ta - set(x)\n\t\t\t\t\t\tb - dict(d)\n\t\t\t\t\t\tc - frozenset(s)\n\t\t\t\t\t\td - chr(x)\033[1;m'
                med_q5 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if med_q5 == 'd':
                    medium_score += 1
                del questions_medium[0]
                j += 1
                clear()
            elif questions_medium[
                0] == 'Q : Which of the following function returns a random float r, such that 0 is less than or equal to r and r is less than 1?\na - choice(seq)\nb - randrange([start, ] stop[, step])\nc - random()\nd - seed([x])':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ : Which of the following function returns a random float r, such that 0 is less than or equal to r and r is less than 1?\n\t\t\t\t\t\ta - choice(seq)\n\t\t\t\t\t\tb - randrange([start, ] stop[, step])\n\t\t\t\t\t\tc - random()\n\t\t\t\t\t\td - seed([x])\033[1;m'
                med_q6 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if med_q6 == 'c':
                    medium_score += 1
                del questions_medium[0]
                j += 1
                clear()
            elif questions_medium[
                0] == 'Q : Which of the following function checks in a string that all characters are in uppercase?\na - isupper()\nb - join(seq)\nc - len(string)\nd - ljust(width[, fillchar]':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ : Which of the following function checks in a string that all characters are in uppercase?\n\t\t\t\t\t\ta - isupper()\n\t\t\t\t\t\tb - join(seq)\n\t\t\t\t\t\tc - len(string)\n\t\t\t\t\t\td - ljust(width[, fillchar]\033[1;m'
                med_q7 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if med_q7 == 'a':
                    medium_score += 1
                del questions_medium[0]
                j += 1
                clear()
            elif questions_medium[
                0] == 'Q : Which of the following function converts a string to all lowercase?\na - lower()\nb - lstrip()\nc - max(str)\nd - min(str)':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ : Which of the following function converts a string to all lowercase?\n\t\t\t\t\t\ta - lower()\n\t\t\t\t\t\tb - lstrip()\n\t\t\t\t\t\tc - max(str)\n\t\t\t\t\t\td - min(str)\033[1;m'
                med_q8 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if med_q8 == 'a':
                    medium_score += 1
                del questions_medium[0]
                j += 1
                clear()
            elif questions_medium[
                0] == 'Q : What is the following function reverses objects of list in place?\na - list.reverse()\nb - list.sort([func])\nc - list.pop(obj=list[-1])\nd - list.remove(obj)':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ : What is the following function reverses objects of list in place?\n\t\t\t\t\t\ta - list.reverse()\n\t\t\t\t\t\tb - list.sort([func])\n\t\t\t\t\t\tc - list.pop(obj=list[-1])\n\t\t\t\t\t\td - list.remove(obj)\033[1;m'
                med_q9 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if med_q9 == 'a':
                    medium_score += 1
                del questions_medium[0]
                j += 1
                clear()
            elif questions_medium[
                0] == 'Q : What is the output of print str[0] if str = \'Hello World!\'?\n\na - Hello World!\nb - H\nc - ello World!\nd - None of the above.':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ : What is the output of print str[0] if str = \'Hello World!\'?\n\t\t\t\t\t\ta - Hello World!\n\t\t\t\t\t\tb - H\n\t\t\t\t\t\tc - ello World!\n\t\t\t\t\t\td - None of the above.\033[1;m'
                med_q10 = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if med_q10 == 'b':
                    medium_score += 1
                del questions_medium[0]
                j += 1
                clear()
        userchoice = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO SEE YOUR SCORE :\033[1;m")
        clear()
        print"\033[1;45m\t\t\t\t\t\t********************************\n\033[1;m"
        print'\033[1;34m\t\t\t\t\t\t\t\t\tYOUR SCORE IS :\033[1;m ', medium_score
        print"\033[1;45m\t\t\t\t\t\t********************************\n\033[1;m"

        db = MySQLdb.connect("localhost", "root", "", "test")
        cursor = db.cursor()
        sql = "UPDATE player \
                SET med_score = '%d' \
                 WHERE player_num = '%s'" % \
              (medium_score, phone_num)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        sql = """SELECT * FROM player"""
        cursor.execute(sql)
        db.close()

        if medium_score >= 8:
            congrats_graphics()
            user_choice = raw_input("\033[1;35m\n\n\t\t\t\t\tDO YOU WANT TO CONTINUE?(y/n) :\033[1;m")
            if user_choice == 'y':
                medium_level.obj2.hard_quiz( phone_num, name)
            elif user_choice == 'n':
                print"\n" * 10
                print"\033[1;31m\t\t\t\t\t\t\t\t\t\t\t********************************************\033[1;m"
                print"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\033[1;33m----------*******----------\033[1;m"
                print"\t\t\t\t\t\t\t\t\t\t\t\t\033[1;34mCERTIFICATE OF ACHIEVEMENT\033[1;m"
                print"\t\t\t\t\t\t\t\t\t\t\t\t\033[1;34mMany Congratulations :)\033[1;m", name
                print"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\033[1;33m----------*******----------\033[1;m"
                print"\t\t\t\t\t\t\t\t\t\033[1;34mOn Successfully Completing the second round of PYTHON QUIZ\033[1;m"
                print"\t\t\t\t\t\t\t\t\t\t\t\t\033[1;34mKeep Participating.....!!!!\033[1;m"
                print"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\033[1;33m----------*******----------\033[1;m"
                print"\033[1;31m\t\t\t\t\t\t\t\t\t\t\t*******************************************\033[1;m"
                thanks()
                c = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")
                menu(phone_num, name)
                z = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ENTER TO PROCEED :\033[1;m")
                choice = raw_input("\033[1;35m\n\n\t\t\t\t\tBACK TO THE MAIN MENU? (y/n) :\033[1;m")
                if choice == 'y':
                    menu(phone_num, name)
                else:
                    main()
            else:
                print"\033[1;35m\n\n\t\t\t\t\tPLEASE ENTER APPROPRIATE OPTION :\033[1;m"
        else:
            print"\033[1;35m\n\n\t\t\t\t\tOOPS..!!YOU ARE NOT ELIGIBLE FOR THE NEXT ROUND :\033[1;m"
            thanks()
            #z = raw_input("PRESS ENTER TO PROCEED..!!")
            select = raw_input("\033[1;35m\n\n\t\t\t\t\tDO YOU WANT TO PLAY AGAIN?(y/n) :\033[1;m")
            if select == 'y':
                menu(phone_num,name)
            else:
                main()

                ########################### class end#######################

                ########################### class easy_level#######################

class easy_level(medium_level):
    obj1 = medium_level()
    def easy_quiz(self, phone_num, name):
        graphics()
        clear()
        clear()
        clear()
        z = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ENTER TO START THE LEVEL..!!\033[1;m")
        clear()
        clear()
        clear()
        clear()

        print"\n\033[1;42m\t\t\t\t\t\t\t\t\t\t\t******EASY LEVEL***************\n\033[1;m"
        #z = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ENTER TO START THE LEVEL..!!\033[1;m")
        questions = [
            'Q: Which of the following statements is true ? \na.Python is a High level programming language \nb.Python is an interpreted language \nc.Python is an object oriented language \nd.All of the above',
            'Q:Which is used to define a block of code (body of loop, function etc) in python?\na.Curly braces\nb.Parenthesis \nc.Indentation \nd.Quotation',
            'Q :In the following code,n is a/an ---------? \n n=\'5\'\na.Integer\nb.String\nc.Tuple\nd.Operator',
            'Q : Which is used to take input from the user in python?\na.scanf()\nb.input()\nc.cin\nd.<>',
            'Q: What is the output of the following code ?\n print(3>=3)\na.3>=3\nb.True\nc.False\nd.None\n',
            'Q:Which of the following is correct?\na.Variable name can start with an underscore\nb.Variable name can start with a digit\nc.Keywords can be used as variables name\nd.Variables name can have symbols like @,#,$ etc\n',
            'Q:The statement using and operator results true if -------\na.Both operands are true\nb.Both operands are false\nc.Either of the operand is true\nd.First of the operand is true',
            'Q: What is the output of following code ?\n numbers = [2, 3, 4]\nprint(numbers)\na.2, 3, 4\nb.2 3 4\nc.[2 , 3, 4]\nd.[2 3 4]',
            'Q : What is the output of the following code??\nprint(1, 2, 3, 4, sep=*)\na.1 2 3 4\nb.1234\nc.1*2*3*4\nd.24',
            'Q : What will be the output?\na = []\nfor k in range(10):\n\ta.append(lambda:k)\n\nprinta[1]()\na.0\nb.1\nc.9\nd.Error']
        random.shuffle(questions)
        que = 0
        count = 0
        while que < 10:
            if questions[
                0] == 'Q: Which of the following statements is true ? \na.Python is a High level programming language \nb.Python is an interpreted language \nc.Python is an object oriented language \nd.All of the above':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ: Which of the following statements is true ? \n\t\t\t\t\t\ta.Python is a High level programming language \n\t\t\t\t\t\tb.Python is an interpreted language \n\t\t\t\t\t\tc.Python is an object oriented language \n\t\t\t\t\t\td.All of the above\033[1;m'
                chosen = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if chosen == 'd':
                    count += 1
                del questions[0]
                que += 1
                clear()
            elif questions[
                0] == 'Q:Which is used to define a block of code (body of loop, function etc) in python?\na.Curly braces\nb.Parenthesis \nc.Indentation \nd.Quotation':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ:Which is used to define a block of code (body of loop, function etc) in python?\n\t\t\t\t\t\ta.Curly braces\n\t\t\t\t\t\tb.Parenthesis \n\t\t\t\t\t\tc.Indentation \n\t\t\t\t\t\td.Quotation\033[1;m'
                chosen = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if chosen == 'c':
                    count += 1
                del questions[0]
                que += 1
                clear()
            elif questions[
                0] == 'Q :In the following code,n is a/an ---------? \n n=\'5\'\na.Integer\nb.String\nc.Tuple\nd.Operator':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ :In the following code,n is a/an ---------? \n\t\t\t\t\t\t n=\'5\'\n\t\t\t\t\t\ta.Integer\n\t\t\t\t\t\tb.String\n\t\t\t\t\t\tc.Tuple\n\t\t\t\t\t\td.Operator\033[1;m'
                chosen = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if chosen == 'b':
                    count += 1
                del questions[0]
                que += 1
                clear()
            elif questions[
                0] == 'Q : Which is used to take input from the user in python?\na.scanf()\nb.input()\nc.cin\nd.<>':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ : Which is used to take input from the user in python?\n\t\t\t\t\t\ta.scanf()\n\t\t\t\t\t\tb.input()\n\t\t\t\t\t\tc.cin\n\t\t\t\t\t\td.<>\033[1;m'
                chosen = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if chosen == 'b':
                    count += 1
                del questions[0]
                que += 1
                clear()
            elif questions[
                0] == 'Q: What is the output of the following code ?\n print(3>=3)\na.3>=3\nb.True\nc.False\nd.None\n':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ: What is the output of the following code ?\n\t\t\t\t\t\t print(3>=3)\n\t\t\t\t\t\ta.3>=3\n\t\t\t\t\t\tb.True\n\t\t\t\t\t\tc.False\n\t\t\t\t\t\td.None\033[1;m'
                chosen = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if chosen == 'c':
                    count += 1
                del questions[0]
                que += 1
                clear()
            elif questions[
                0] == 'Q:Which of the following is correct?\na.Variable name can start with an underscore\nb.Variable name can start with a digit\nc.Keywords can be used as variables name\nd.Variables name can have symbols like @,#,$ etc\n':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ:Which of the following is correct?\n\t\t\t\t\t\ta.Variable name can start with an underscore\n\t\t\t\t\t\tb.Variable name can start with a digit\n\t\t\t\t\t\tc.Keywords can be used as variables name\n\t\t\t\t\t\td.Variables name can have symbols like @,#,$ etc\033[1;m'
                chosen = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if chosen == 'a':
                    count += 1
                del questions[0]
                que += 1
                clear()
            elif questions[
                0] == 'Q:The statement using and operator results true if -------\na.Both operands are true\nb.Both operands are false\nc.Either of the operand is true\nd.First of the operand is true':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ:The statement using and operator results true if -------\n\t\t\t\t\t\ta.Both operands are true\n\t\t\t\t\t\tb.Both operands are false\n\t\t\t\t\t\tc.Either of the operand is true\n\t\t\t\t\t\td.First of the operand is true\033[1;m'
                chosen = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m:")
                if chosen == 'a':
                    count += 1
                del questions[0]
                que += 1
                clear()
            elif questions[
                0] == 'Q: What is the output of following code ?\n numbers = [2, 3, 4]\nprint(numbers)\na.2, 3, 4\nb.2 3 4\nc.[2 , 3, 4]\nd.[2 3 4]':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ: What is the output of following code ?\n\t\t\t\t\t\tnumbers = [2, 3, 4]\n\t\t\t\t\t\tprint(numbers)\n\t\t\t\t\t\ta.2, 3, 4\n\t\t\t\t\t\tb.2 3 4\n\t\t\t\t\t\tc.[2 , 3, 4]\n\t\t\t\t\t\td.[2 3 4]\033[1;m'
                chosen = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if chosen == 'c':
                    count += 1
                del questions[0]
                que += 1
                clear()
            elif questions[
                0] == 'Q : What is the output of the following code??\nprint(1, 2, 3, 4, sep=*)\na.1 2 3 4\nb.1234\nc.1*2*3*4\nd.24':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ : What is the output of the following code??\n\t\t\t\t\t\tprint(1, 2, 3, 4, sep=*)\n\t\t\t\t\t\ta.1 2 3 4\n\t\t\t\t\t\tb.1234\n\t\t\t\t\t\tc.1*2*3*4\n\t\t\t\t\t\td.24\033[1;m'
                chosen = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if chosen == 'c':
                    count += 1

                del questions[0]
                que += 1
                clear()
            elif questions[
                0] == 'Q : What will be the output?\na = []\nfor k in range(10):\n\ta.append(lambda:k)\n\nprinta[1]()\na.0\nb.1\nc.9\nd.Error':
                print"\n\n\n\n\n\033[1;31m\t\t\t\t\t\t\t\t\t----QUESTION------\033[1;m"
                print'\033[1;34m\n\t\t\t\t\tQ : What will be the output?\n\t\t\t\t\t\ta = []\n\t\t\t\t\t\tfor k in range(10):\n\t\t\t\t\t\t\ta.append(lambda:k)\n\n\t\t\t\t\t\tprinta[1]()\n\t\t\t\t\t\ta.0\n\t\t\t\t\t\tb.1\n\t\t\t\t\t\tc.9\n\t\t\t\t\t\td.Error\033[1;m'
                chosen = raw_input("\033[1;35m\n\n\t\t\t\t\tENTER YOUR ANSWER :\033[1;m")
                if chosen == 'c':
                    count += 1
                del questions[0]
                que += 1
                clear()
        userchoice = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO SEE YOUR SCORE :\033[1;m")
        clear()
        print"\033[1;45m\t\t\t\t\t\t********************************\n\033[1;m"
        print'\033[1;34m\t\t\t\t\t\t\t\t\tYOUR SCORE IS :\033[1;m ', count
        print"\033[1;45m\t\t\t\t\t\t********************************\n\033[1;m"
        db = MySQLdb.connect("localhost", "root", "", "test")
        cursor = db.cursor()
        sql = "UPDATE player \
               SET easy_score = '%d'  \
               WHERE player_num = '%s'" % \
              (count, phone_num)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
        sql = """SELECT * FROM player"""
        cursor.execute(sql)
        db.close()

        if count >= 7:
            congrats_graphics()
            #print"*****YOU QUALIFIED FOR THE NEXT LEVEL*******"
            user_choice = raw_input("\033[1;35m\n\n\t\t\t\t\tDO YOU WANT TO CONTINUE?(y/n) :\033[1;m")
            clear()
            clear()
            clear()
            if user_choice == 'y':
                easy_level.obj1.med_quiz(phone_num, name)
            elif user_choice == 'n':
                c = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")
                print"\033[1;31m\t\t\t\t\t\t\t\t\t\t\t********************************************\033[1;m"
                print"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\033[1;33m----------*******----------\033[1;m"
                print"\t\t\t\t\t\t\t\t\t\t\t\t\033[1;34mCERTIFICATE OF ACHIEVEMENT\033[1;m"
                print"\t\t\t\t\t\t\t\t\t\t\t\t\033[1;34mMany Congratulations :)\033[1;m", name
                print"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\033[1;33m----------*******----------\033[1;m"
                print"\t\t\t\t\t\t\t\t\t\t\t\t\033[1;34mOn Successfully Completing the FIRST round of PYTHON QUIZ\033[1;m"
                print"\t\t\t\t\t\t\t\t\t\t\t\t\033[1;34mKeep Participating.....!!!!\033[1;m"
                print"\t\t\t\t\t\t\t\t\t\t\t\t\t\t\033[1;33m----------*******----------\033[1;m"
                print"\033[1;31m\t\t\t\t\t\t\t\t\t\t\t*******************************************\033[1;m"
                thanks()
                c=raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")
                menu(phone_num,name)
                z = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ENTER TO PROCEED :\033[1;m")
                choice = raw_input("\033[1;35m\n\n\t\t\t\t\tBACK TO THE MAIN MENU?(y/n) :\033[1;m")
                if choice == 'y':
                    menu(phone_num, name)
                else:
                    main()
            else:
                print"\033[1;35m\n\n\t\t\t\t\tPLEASE ENTER APPROPRITE OPTION :\033[1;m"
        else:
            print"\033[1;35m\n\n\t\t\t\t\tOOPS..!!YOU ARE NOT ELIGIBLE FOR THE NEXT ROUND :\033[1;m"
            thanks()
            z = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ENTER TO PROCEED :\033[1;m")
            select=raw_input("\033[1;35m\n\n\t\t\t\t\tDO YOU WANT TO PLAY AGAIN?(y/n) :\033[1;m")
            if select == 'y':
                menu(phone_num,name)
            else:
                main()
        return phone_num, name

        ########################### class end#######################

        ########################### menu #######################
def menu(phone_num,name) :
    clear()
    clear()
    print'\t\t\t\t\t\t\t\t\t\t\033[1;31m*********MAIN MENU***********\033[1;m'
    print "\n"
    x = input( "\033[1;33m\n\t\t\t\t\t\t\t\t\t\t1.TAKE QUIZ\n\t\t\t\t\t\t\t\t\t\t2.HELP\n\t\t\t\t\t\t\t\t\t\t3.VIEW HIGH SCORE\n\t\t\t\t\t\t\t\t\t\t4.VIEW PROGRESS\n\t\t\t\t\t\t\t\t\t\t5.ABOUT PROGRAM\n\t\t\t\t\t\t\t\t\t\t6.EXIT\n\n\n\t\t\t\t\t\t\t\t\tENTER YOUR CHOICE....!!\033[1;m")
    x = int(x)
    clear()
    if x == 1:
        t = Turtle()
        t.screen.bgcolor("black")

        t.hideturtle()
        t.color("purple")
        t.write("NOTE : BEFORE STARTING THE GAME PLEASE READ THE HELP CAREFULLY", move=True, align="center",
                font=("copper black", 10, "normal"))
        t.color("black")
        t.goto(260, -180)
        t.color("white")
        t.write("Please close the current window to proceed", move=True, align="right",
                font=("copper black", 10, "normal"))

        mainloop()
        clear()
        clear()
        print'\t\t\t\t\t\t\t\t\t\t*************************************************\n'
        print"\033[1;45m\t\t\t\t\t\t\t\t\t\tPROGRAM DEVELOPERS WISH YOU A GOOD LUCK..!!!\n\033[1;m"
        print'\t\t\t\t\t\t\t\t\t\t**************************************************\n'
        y = input(
            "\033[1;33m\n\t\t\t\t\t\t\t\t\t\t1.EASY LEVEL\n\t\t\t\t\t\t\t\t\t\t2.MEDIUM LEVEL\n\t\t\t\t\t\t\t\t\t\t3.HARD\033[1;m "
            "\033[1;33mLEVEL\n\t\t\t\t\t\t\t\t\t\t4.BACK TO THE MAIN MENU\n\n\n\t\t\t\t\t\t\t\t\t\tENTER YOUR CHOICE..!!\033[1;m")
        y = int(y)
        if y == 1:
            obj = easy_level()
            obj.easy_quiz(phone_num, name)

        elif y == 2:
            clear()
            print"\033[1;31m\t\t\t\t\t\t\t\tLOCKED...\n\t\t\t\t\t\tFIRST YOU HAVE TO QUALIFY EASY LEVEL..\033[1;m"
            clear()
            clear()
            z=raw_input("PRESS ANY KEY TO PROCEED..!!")
            clear()
            clear()
            clear()
            menu(phone_num,name)
        elif y == 3:
            clear()
            print"\033[1;31m\t\t\t\t\t\t\t\tLOCKED...\n\t\t\t\t\t\t\tFIRST YOU HAVE TO QUALIFY MEDIUM LEVEL..\033[1;m"
            clear()
            clear()
            z = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")
            clear()
            clear()
            clear()
            menu(phone_num, name)
        elif y == 4 :
            clear()
            menu(phone_num,name)
        else :
            print"\033[1;35m\n\n\t\t\t\t\tPLEASE ENTER VALID OPTION!!\033[1;m"
            clear()
            clear()
            clear()
            x = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")

            menu(phone_num, name)


    elif x == 2:
        clear()
        print"\033[1;46m\t\t\t\t\t\t\t\t*********************HELP**********************\n\033[1;m"
        print'''\033[1;35m\t\t\t\"In this game you will be ask some general questions about python.There will be 3
                  \n\t\t\tlevels(easy,medium,hard). each level have 10 questions with four options in each.You have to
                  \n\t\t\tselect one of them correct answer will add +1 to your score and there will be no negative
                  \n\t\t\tmarking In every level this is necessary for the player to score as per requirement in order
                  \n\t\t\tto unlock the next level.your score will be calculated at the end of the level and displayed.\"
                  \033[1;m'''
        print'\033[1;31m\n\n\t\t\t\t\t\tIMPORTANT : Please keep your CAPS LOCK OFF.. !\033[1;m'

        z = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")
        clear()
        clear()
        clear()

        menu(phone_num, name)
    elif x == 3:
        clear()
        clear()
        clear()
        print'\t\t\t\t\t\t\t\t\t\t\t\033[1;33m========================================\033[1;m'
        print"\t\t\t\t\t\t\t\t\t\t\t\t\033[1;46m********HIGH SCORE***********\033[1;m"
        print'\t\t\t\t\t\t\t\t\t\t\t\033[1;33m========================================\033[1;m'

        i = raw_input( "\n\033[1;31m\n\n\t\t\t\t\t\t\t\t\t\ta)EASY LEVEL\n\n\t\t\t\t\t\t\t\t\t\tb)MEDIUM LEVEL\n\n\t\t\t\t\t\t\t\t\t\tc)HARD LEVEL\n\n\t\t\t\t\t\t\t\t\t\td)BACK TO THE MAIN MENU\n\n\t\t\t\t\t\t\t\t\t\tSELECT A VALID OPTION TO SEE THE HIGH SCORE OF THE LEVEL:\033[1;m")
        if i == 'a':
            clear()
            h1 = highscore()
            h1.view_easyhighscore()
            x = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")
            clear()

            menu(phone_num,name)
        elif i == 'b':
            clear()
            h1 = highscore()
            h1.view_medhs()
            x = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")
            clear()
            menu(phone_num,name)
        elif i == 'c':
            clear()
            h1 = highscore()
            h1.view_hardhs()
            x = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")
            clear()
            menu(phone_num,name)
        elif i == 'd':
            clear()
            menu(phone_num, name)
        else:
            print"\033[1;35m\n\n\t\t\t\t\tPLEASE ENTER VALID OPTION!!\033[1;m"
            clear()
            clear()
            clear()
            x = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")

            menu(phone_num, name)

    elif x == 4:
        clear()
        clear()
        clear()
        print"\t\t\t\t\t\t\t\t\t\033[1;33m*********************************\033[1;m"
        print"\t\t\t\t\t\t\t\t\t\033[1;46m*******VIEW YOUR PROGRESS*******\033[1;m"
        print"\t\t\t\t\t\t\t\t\t\033[1;33m*********************************\033[1;m"
        print"\n"*2
        newphone_num = str(raw_input("\t\t\t\033[1;35mENTER YOUR MOBILE NUMBER(that you have entered at the time of play)  : \033[1;m"))

        clear()
        o = playerreport()
        o.view_progress(newphone_num)
        z = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED:\033[1;m")
        clear()
        clear()
        clear()
        menu(phone_num, name)
    elif x == 5:
        print"\033[1;42m\t\t\t\t\t\t\t\t\t\t*************ABOUT PROGRAM***************\n\033[1;m"
        print"\033[1;35m\t\t\t\t\t\t\t\t\t\tDEVELOPED BY :\033[1;m"
        print"\033[1;34m\t\t\t\t\t\t\t\t\t\t\tUMM E FARWA (CT -010)\n\t\t\t\t\t\t\t\t\t\t\tSYEDA MISBAH (CT - 006)"
        print"\033[1;35m\t\t\t\t\t\t\t\t\t\t\t*******DESCRIPTION*********\033[1;m"
        print   '''\033[1;34mTHIS QUIZ GAME IS SPECIALLY DESIGN FOR THE PURPOSE OF PLAYING QUIZ CONTEST.IN THIS QUIZ
                \nFIRSTLY PLAYER HAS TO REGITER HIS NAME THERE ARE THREE LEVELS IN THE  GAME (EASY,MEDIUM AND HARD).
                \nAFTER FINISHING EACH LEVEL THERE WILL BE A CERTIFICATE FOR SUCCESSFULL PLAYERS WHO MADE IT TO THE
                \nEND.THE QUESTIONS COME IN RANDOM SO THERE IS ALWAYS LITTLE BIT MIXING OF EXCITEMENT FOR PLAYER.IN
                \nEVERY LEVEL THERE IS TEN QUESTIONS AND THIS IS NECESSARY FOR THE PLAYER TO SCORE AS PER THE
                \nREQUIREMENT IN ORDER TO UNLOCK THE NEXT LEVEL.IF PLAYER FINDS DIFFICULTY IN PLAYINGT HE QUIZ SO
                \nTHERE IS HELP TO GUIDE THEM.PROGRAM CAN ALSO SAVE THE HIGH SCORE OF THE PLAYER FOR EACH LEVEL IT
                \nCAN SAVE RECORD OF INDIVIDUAL PLAYER SO EVERY INDIVIDUAL PLAYER CAN CHECK THEIR PROGRESS AT ANY TIME.\033[1;m'''
        z = raw_input("\033[1;35m\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")
        clear()
        clear()
        clear()
        menu(phone_num, name)
    elif x == 6 :
        exit(1)
    else:
        print"\t\t\t\t\t\t\t\t\t\t\033[1;34mPlease enter valid option\033[1;m"
        z = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")

        menu(phone_num,name)
    return phone_num, name

########################### main #######################
def main():
    clear()
    clear()
    clear()
    print'\t\t\t\t\t\t\t\t\t\t\033[1;42mFIRST REGISTER YOURSELF..!!\033[1;m'
    clear()
    name = str(raw_input('\t\t\t\t\t\t\t\t\t\t\033[1;31mENTER YOUR NAME:\033[1;m'))
    phone_num = str(raw_input("\n\n\n\t\t\t\t\t\t\t\t\t\t\033[1;31mENTER YOUR MOBILE NUMBER :\033[1;m"))
    print"\n" * 2
    print'\t\t\t\t\t\t\t\t\t\033[1;47mTHANKS...!!YOU ARE SUCCESSFULLY REGISTERED.. !!\033[1;m'
    Z = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")
    print"\n"*2

    clear()
    clear()
    clear()
    p1 = quiz_results()
    p1.create_table()
    p1.write_in_sql_table(name, phone_num)
    print"\t\t\t\t\t\t\t\t\t\t\033[1;46m==================================\033[1;m\n"
    print"\t\t\t\t\t\t\t\t\t\t\t\033[1;34m******WELCOME\033[1;m", name , "\033[1;34m*********\033[1;m"
    print"\n\t\t\t\t\t\t\t\t\t\t\033[1;46m===================================\033[1;m\n"
    Z = raw_input("\033[1;35m\n\n\t\t\t\t\tPRESS ANY KEY TO PROCEED :\033[1;m")
    print'\n' * 100
    print"\n" * 3
    print'\t\t\t\t\t\t\t\t\t\t********************************'
    print'\t\t\t\t\t\t\t\t\t\t\033[1;46mWELCOME TO THE PYTHON QUIZ.. !!\033[1;m'
    print'\t\t\t\t\t\t\t\t\t\t********************************\n'
    clear()
    clear()
    clear()
    menu(phone_num,name)
t = Turtle()
t.screen.bgcolor("black")
colors=["red","yellow","purple"]
t.screen.tracer(0,0)
for x in range(100):
    t.circle(x)
    t.color(colors[x%3])
    t.left(60)
t.color("cyan")
t.write("SUBMITTED BY :\nUMM E FARWA(CT-010)\nSYEDA MISBAH(CT-006)\nSUBMITTED TO:\nMISS SAMAN HINA\nDEPARTMEN OF COMPUTER SCIENCE AND INFORMATION TECHNOLOGY",move=True,align="center",font=("copper black",10,"normal"))
t.color("black")
t.goto(235,-150)
t.color("white")
t.write("Please close the current window to proceed",move=True,align="right",font=("copper black",10,"normal"))

#time.sleep(0.5)
mainloop()
t=Turtle()
t.screen.bgcolor("white")

t.hideturtle()
t.screen.bgpic("giphy.gif")
t.color("red")
t.hideturtle()
t.write("*QUIZ GAME*",move=True,align="center",font=("copper black",40,"normal"))
t.color("black")
t.goto(235,-130)
t.color("white")
t.write("Please close the current window to proceed",move=True,align="right",font=("copper black",10,"normal"))
mainloop()
clear()
user_input = raw_input("\033[1;34m\t\t\t\t\t\t\t\tPRESS ANY KEY TO CONTINUE.. !!\033[1;m ")
clear()
clear()
clear()
main()