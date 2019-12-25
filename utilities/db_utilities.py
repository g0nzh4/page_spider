import _sqlite3 as lite


def create_database(database_path: str):
    connection = lite.connect(database_path)
    with connection:
        cursor = connection.cursor()
        cursor.execute('drop table if exists words')
        ddl = 'create table words (word text not null constraint ' \
              'words_pk primary key, usage_count int default 1 not null); '
        cursor.execute(ddl)
        ddl = 'create unique index words_word_uindex on words (word);'
        cursor.execute(ddl)
    connection.close()


def save_words_to_database(database_path: str, words_list: list):
    connection = lite.connect(database_path)
    with connection:
        cursor = connection.cursor()
        for word in words_list:
            # check to see if th word is in there
            sql = "select count(word) from words where word='" + word + "'"
            cursor.execute(sql)
            count = cursor.fetchone()[0]
            if count > 0:
                sql = "update words set usage_count = usage_count + 1 where word ='" + word + "'"
            else:
                sql = "insert into words(word) values ('" + word + "')"
            cursor.execute(sql)
    print("Database save complete!")