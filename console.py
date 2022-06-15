import cmd
from core.dbtools import dbtools as db
import pandas as pd

class console(cmd.Cmd):
    intro = 'Welcome to the database console. Type help or ? to list commands.'
    prompt = ' }>  '
    file = None

    recentdf = pd.DataFrame()

    def do_dbq(self, line):
        'Send a SQL query to the PostgreSQL database and display first 10 rows.'
        self.recentdf = db.pg_query(line)
        print(self.recentdf.head(10))

    def do_sfq(self, line):
        'Send a SoQL query to the Salesforce database and display first 10 rows.'
        self.recentdf = db.sf_query(line)
        print(self.recentdf.head(10))

    def do_disp(self, line):
        'Display 50 rows from last query'
        if self.recentdf.empty == True:
            print("No recent file. Run a query first.")
        else:
            print(self.recentdf.head(50))

    def do_csv(self, line):
        'Enter a name to save last query'
        if self.recentdf.empty == True:
            print("No recent file. Run a query first.")
        else:
            db.df_to_csv(self.recentdf, line)
            print("Saved to "+ line + ".csv")

    def do_quit(self, line):
        'Close this session'
        return True

    def emptyline(self):
        print("Type help or ? for commands.")
    
    def default(self, line):
        print("Command" + line + " is not known.")
        self.onecmd('emptyline')


if __name__ == '__main__':
    print("___________________________________________________________________________________")
    console().cmdloop()