# main import
import main as m

# db 연동


<<<<<<< HEAD
def db():
=======
# db 연동
def db_insert_data():
>>>>>>> 043a0ad73abd6699efde7f0afc89ea34e4283450

    sql = 'INSERT INTO chatbot(username, jointime, location, gamescore, newskeyword) VALUES (:name, :time, :loca, :score, :search_word)'
    m.cursor.execute(sql, name=m.name, time=m.now,
                     loca=m.wt.location, score=m.mg.score, search_word=m.n.search_word)

    sql2 = 'INSERT INTO foodlist(username, foodtype, foodname) VALUES (:name, :type, :fname)'
    m.cursor.execute(sql2, name=m.name, type=m.ms.inputed_type,
                     fname=m.ms.inputed_name)

    m.connection.commit()
    m.cursor.close()
    m.connection.close()
