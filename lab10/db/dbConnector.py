import psycopg2
from lab10.config.config import load_config
from lab10.db.PhoneBook import PhoneBook
from lab10.db.Users import Users


class DBConnector:
    def __init__(self):
        self.config = load_config()

    def createTable(self):
        sql = '''
            CREATE SEQUENCE IF NOT EXISTS s;
            CREATE TABLE IF NOT EXISTS phone_nums (
                id INTEGER DEFAULT nextval('s') PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                phone VARCHAR(11) NOT NULL
        );
        '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                conn.commit()
        except Exception as e:
            print("Error on creating new table ", e)

    def add_phone(self, p1: PhoneBook):
        sql = "INSERT INTO phone_nums (first_name, last_name, phone) VALUES (%s, %s, %s)"
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (p1.first_name, p1.last_name, p1.phone))
                conn.commit()
        except Exception as e:
            print("Error on inserting new user ", e)

    def update_phone_by_name(self, id, name):
        sql = '''
            UPDATE phone_nums 
            SET first_name=%s 
            WHERE id=%s 
        '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (name, id))
                conn.commit()
        except Exception as e:
            print("Error on updating new user ", e)

    def update_phone_by_phone(self, id, phone):
        sql = '''
                UPDATE phone_nums 
                SET phone=%s 
                WHERE id=%s 
                '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (phone, id))
                conn.commit()
        except Exception as e:
            print("Error on updating new user ", e)

    def delete_phone_by_id(self, id):
        sql = '''
            DELETE 
            FROM phone_nums 
            WHERE id=%s 
        '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (id))
                conn.commit()
        except Exception as e:
            print("Error on deleting user ", e)

    def get_all_users(self):
        sql = "SELECT * FROM phone_nums ORDER BY id ASC"
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    rows = cur.fetchall()
                    return rows
        except Exception as e:
            print("Error on listing all users ", e)

    # def createTableForRace(self):
    #     sql = '''
    #                 CREATE SEQUENCE IF NOT EXISTS s;
    #                 CREATE TABLE IF NOT EXISTS race_scores (
    #                     id INTEGER DEFAULT nextval('s') PRIMARY KEY,
    #                     username VARCHAR(255) NOT NULL,
    #                     level VARCHAR(11) NOT NULL
    #             );
    #             '''
    #     try:
    #         with psycopg2.connect(**self.config) as conn:
    #             with conn.cursor() as cur:
    #                 cur.execute(sql)
    #             conn.commit()
    #     except Exception as e:
    #         print("Error on creating new SCORE RACE table ", e)

    def createTableForGameUsers(self):
        sql = '''
                    CREATE SEQUENCE IF NOT EXISTS s;
                    CREATE TABLE IF NOT EXISTS t_users (
                        id INTEGER DEFAULT nextval('s') PRIMARY KEY,
                        username VARCHAR(255) NOT NULL, 
                        level INTEGER NOT NULL
                );
                '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql)
                conn.commit()
        except Exception as e:
            print("Error on creating new SCORE RACE table ", e)
    # def createTableForScores(self):
    #     sql = '''
    #                 CREATE SEQUENCE IF NOT EXISTS s;
    #                 CREATE TABLE IF NOT EXISTS t_scores (
    #                     id INTEGER DEFAULT nextval('s') PRIMARY KEY,
    #                     user_id INTEGER NOT NULL,
    #                     game_type INTEGER NOT NULL,
    #                     score INTEGER NOT NULL
    #             );
    #             '''
    #     try:
    #         with psycopg2.connect(**self.config) as conn:
    #             with conn.cursor() as cur:
    #                 cur.execute(sql)
    #             conn.commit()
    #     except Exception as e:
    #         print("Error on creating new SCORE RACE table ", e)

    def isUserExist(self, username):
        sql = '''
            SELECT * 
            FROM t_users 
            WHERE username=%s
        '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (username,))
                    row = cur.fetchone()  # Use fetchone for a single result
                    return True if row else False
        except Exception as e:
            print("Error on creating new SCORE RACE table ", e)
            return False
    def addNewUser(self, username):
        sql = '''
                   INSERT INTO t_users(username, level) 
                   VALUES(%s, 0)
                '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (username,))
                    conn.commit()
                    return True
        except Exception as e:
            print("Error on creating new SCORE RACE table ", e)
            return False
    def getCurrentUser(self, username):
        sql = '''
            SELECT * 
            FROM t_users 
            WHERE username=%s 
        '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (username,))
                    row = cur.fetchone()
                    if row:
                        return Users(*row)  # Unpack tuple into the User class
                    else:
                        return None  # No user found
        except Exception as e:
            print("Error on creating new SCORE RACE table ", e)
    def saveUser(self, username, point):
        sql = '''
            UPDATE t_users 
            SET level=%s 
            WHERE username=%s 
        '''
        try:
            with psycopg2.connect(**self.config) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, (point, username))
        except Exception as e:
            print("Error on creating new SCORE RACE table ", e)

    # def getUserIfExists(self, username):
    #     sql = "SELECT * FROM t_users WHERE username=%s LIMIT 1"
    #     try:
    #         with psycopg2.connect(**self.config) as conn:
    #             with conn.cursor() as cur:
    #                 cur.execute(sql, (username))
    #                 row = cur.fetchone()  # Use fetchone for a single result
    #                 return True if row else False
    #     except Exception as e:
    #         print("Error on listing all users ", e)
    # def getUserAndPoint(self, username):
    #     sql = '''SELECT * FROM t_users
    #                 INNER JOIN t_scores
    #                 ON t_users.id = t_scores.user_id
    #                 WHERE username =%s '''
    #     try:
    #         with psycopg2.connect(**self.config) as conn:
    #             with conn.cursor() as cur:
    #                 cur.execute(sql, (username))
    #                 rows = cur.fetchall()
    #                 return rows
    #     except Exception as e:
    #         print("Error on listing all users ", e)
    #
    # def saveUserAndPoint(self, user, point):
    #     sql = '''UPDATE  t_scores
    #             SET score=%s
    #             WHERE user_id=%s
    #     '''
    #     try:
    #         with psycopg2.connect(**self.config) as conn:
    #             with conn.cursor() as cur:
    #                 cur.execute(sql, (point, user.id))
    #     except Exception as e:
    #         print("Error on listing all users ", e)
    #
    # def saveUserAndPointIfNotExist(self, user, point):
    #     sql = '''
    #     INSERT INTO t_scores(user_id, game_type, score)
    #     VALUES (%s, 1, %s)
    #     '''
    #     try:
    #         with psycopg2.connect(**self.config) as conn:
    #             with conn.cursor() as cur:
    #                 cur.execute(sql, (user.id, point))
    #     except Exception as e:
    #         print("Error on listing all users ", e)
    # def addNewUser(self, username):
    #     sql = '''
    #     INSERT INTO t_users(username)
    #     VALUES(%s)
    #     '''
    #     try:
    #         with psycopg2.connect(**self.config) as conn:
    #             with conn.cursor() as cur:
    #                 cur.execute(sql, (username))
    #     except Exception as e:
    #         print("Error on listing all users ", e)