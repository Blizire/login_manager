# Author      : Trenton Stiles
# Name        : db.py
# Description : This module will hold all DB code to handle accordingly
#               and securely. Throughout the rest of the code base.

import sqlite3
import bcrypt
import config

class Db:
	def __init__(self):
		self.conn = sqlite3.connect('login_manager.db')
		self.init_db()

	# connect database session. If tables and default admin account
	# does not exist we create it based of config.py
	def init_db(self):
		# encrypting password for default admin account to database
		admin_pw = bytes(config.dbAdminPassword ,encoding = "utf-8")
		admin_pw = bcrypt.hashpw(admin_pw, bcrypt.gensalt())

		# CREATE DATABASE TABLE IF NOT EXISTS
		#-----------------------------------------|
		# username (text) | password_hash (BLOB)  |
		#-----------------|-----------------------|
		# admin           | [config file password]|
		#-----------------|-----------------------|
		cursor = self.conn.cursor()
		cursor.execute('''CREATE TABLE IF NOT EXISTS accounts
             (username text, password_hash BLOB)''')
		cursor.execute('''INSERT INTO accounts VALUES (?, ?)''', (config.dbAdminUsername,admin_pw))
		cursor.close()
	
	# checks if password matches up with hashed password in db accoring to username
	def compare_hash(self, username, password):
		sql_query = "SELECT password_hash FROM accounts WHERE username = ?;"
		result = ""
		cursor = self.conn.cursor()
		cursor.execute(sql_query, (username,))
		result = cursor.fetchone()[0]
		password = bytes(password , encoding = "utf-8")
		cursor.close()
		result = bcrypt.checkpw(password, result)
		return result

	# todo:
	# in progress, must use to add new accounts to the database. sensitive to flooding
	# if no captcha or verifying how accounts can be made at a certain IP in a certain
	# time period
	def register(self, username, password):
		# todo add captcha
		# check if username is unique
		sql_query = "SELECT username FROM accounts WHERE username = ?;"
		result = ""
		cursor = self.conn.cursor()
		cursor.execute(sql_query, (username,))
		result = len(cursor.fetchone())
		# if not return false
		if(result >= 1):
			return false

		# insert account
		sql_query = "INSERT INTO accounts(username, password_hash) VALUES (?,?);"
		cursor.execute(sql_query, (username, password))