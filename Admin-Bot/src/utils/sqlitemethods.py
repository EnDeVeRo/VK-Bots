from sqlite3 import connect


class SqliteDataBaseAPI:

    def __init__(self, database_name):
        self.database = database_name

    def check_user_banlist(self, user_id):

        with connect(self.database) as connection:

            cursor = connection.cursor()
            cursor.execute("SELECT count(user_id) FROM banlist WHERE user_id = %d" % user_id)

            result = cursor.fetchone()[0]

            if result == 0:
                return False

            if result == 1:
                return True

        cursor.close()
        connection.close()

    def insert_user_banlist(self, user_id):

        with connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO banlist(user_id) VALUES (%d)" % user_id)

            connection.commit()

        cursor.close()
        connection.close()

    def delete_user_banlist(self, user_id):

        with connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM banlist WHERE user_id = %d" % user_id)

            connection.commit()

        cursor.close()
        connection.close()

    def check_user_warnlist(self, user_id):

        with connect(self.database) as connection:

            cursor = connection.cursor()
            cursor.execute("SELECT count(user_id) FROM warnlist WHERE user_id = %d" % user_id)

            result = cursor.fetchone()[0]

            if result == 0:
                return False

            if result == 1:
                cursor.execute("SELECT warns FROM warnlist WHERE user_id = %d" % user_id)
                count_warns = cursor.fetchone()

                return count_warns[0]

        cursor.close()
        connection.close()

    def insert_user_warnlist(self, user_id):

        with connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO warnlist(user_id, warns) VALUES (%d, 1)" % user_id)

            connection.commit()

        cursor.close()
        connection.close()

    def update_user_warnlist(self, user_id, count_warns):

        with connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE warnlist SET warns = %d WHERE user_id = %d" % (count_warns, user_id))

            connection.commit()

        cursor.close()
        connection.close()

    def delete_user_warnlist(self, user_id):

        with connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM warnlist WHERE user_id = %d" % user_id)

            connection.commit()

        cursor.close()
        connection.close()

    def get_settings(self):

        with connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM settings")
            result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    def get_admins(self):

        with connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM admins")
            result = cursor.fetchall()

        cursor.close()
        connection.close()

        return result

    def get_banwords(self):

        with connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM banwords")
            result = cursor.fetchall()

        cursor.close()
        connection.close()

        return result

    def add_admin(self, user_id):

        with connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO admins(user_id) VALUES (%d)" % user_id)

            connection.commit()

        cursor.close()
        connection.close()

    def del_admin(self, user_id):

        with connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM admins WHERE user_id = %d" % user_id)

            connection.commit()

        cursor.close()
        connection.close()

    def update_emoji_limit(self, emojis_limit):

        with connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("UPDATE settings SET emojis_limit = %d" % emojis_limit)

            connection.commit()

        cursor.close()
        connection.close()

    def check_ban_words(self, word):

        with connect(self.database) as connection:

            cursor = connection.cursor()
            cursor.execute("SELECT count(word) FROM banwords WHERE word = '%s'" % word)

            result = cursor.fetchone()[0]

            if result == 0:
                return False

            if result == 1:
                return True

    def insert_ban_words(self, word):

        with connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO banwords(word) VALUES ('%s')" % word)

            connection.commit()

        cursor.close()
        connection.close()

    def delete_ban_words(self, word):

        with connect(self.database) as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM banwords WHERE word = '%s'" % word)

            connection.commit()

        cursor.close()
        connection.close()
