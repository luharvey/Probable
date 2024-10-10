# Who's backend? 
#Module import
import sqlite3

#Connecting to the locally stored word database
con = sqlite3.connect('./db/wordle.db')
cur = con.cursor()

#SQL query function
def sql(query):
    return cur.execute(query).fetchall()

#Solver class
class solver():
    def __init__(self):
        #List to the accumulated conditions
        self.further_conditions = []
    
    #Return top 20 responses by probability given stored previous conditions
    def return10(self, guess, response):
        query_condition = ''
        
        for i,l in enumerate(response):
            
            #Guess letter is grey
            if l == '?':
                query_condition += '_'
                
                self.further_conditions.append("AND word NOT LIKE '%" + guess[i] + "%'")
                
            else:
                #Guessed letter is green
                if l.isupper() == True:
                    query_condition += l.lower()
                #Guessed letter is yellow
                else:
                    self.further_conditions.append("AND word LIKE '%" + l + "%'")
                    
                    query_condition += '_'
                    
                    not_like = '_'*i + l
                    while len(not_like) < 5:
                        not_like += '_'
                    self.further_conditions.append("AND word NOT LIKE '" + not_like + "'")
                    
        #Compiling SQL query
        query = f"SELECT word FROM words WHERE word LIKE '{query_condition}'"
        for q in self.further_conditions:
            query += f' {q}'
        query += ' ORDER BY base_probability DESC LIMIT 10;'
        
        #Querying table
        return sql(query)
