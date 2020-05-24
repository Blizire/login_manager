import sqlite3
import bcrypt
class DB:
	def __init__(self):
		conn = sqlite3.connect('login_manager.db')
	
	def init_db(self):
		admin_default_pw = b"changeme"
		admin_default_pw = bcrypt.hashpw(admin_default_pw, bcrypt.gensalt())
		self.conn.execute('''CREATE TABLE IF NOT EXISTS accounts
             (username text, password_hash BLOB)''')
		self.conn.execute('''INSERT INTO accounts VALUES (admin, %s)''' % (admin_default_pw))
	
	def compare_hash(self, username, password):
		elf.conn.execute('''SELECT FROM accounts WHERE username=%s''' % (username , password.encode(password)))