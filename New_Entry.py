﻿'''
Написать функцию для добавления новой записи в книгу, и сохранения в базу данных.
На входе минимум 4 переменных: Имя, Фамилия, номер и примечание.
'''
import os

os.chdir(os.path.dirname(__file__))

def new_entry_saver(first_name, last_name, tel_number, footnote):
	new_entry = f'\n{first_name}, {last_name}, {tel_number}, {footnote};\n'
	with open('PhoneBook.txt', 'a', encoding='utf-8') as phone_data:
		phone_data.write(new_entry)