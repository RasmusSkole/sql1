import sqlite3
import csv

# lager en tilkobling til databasen
def func_koble_til_database():
    conn = sqlite3.connect('randoms.db')
    conn.close()

# lager databasetabellen
def func_lag_table():
    conn = sqlite3.connect('randoms.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Randoms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fname TEXT,
        ename TEXT,
        email TEXT,
        phone TEXT,
        postal_code TEXT
    )
    ''')
    conn.commit()
    conn.close()

# leser av dataene fra csv-filen og importerer de til databasen
def func_importer_data_fra_csv(var_filename):
    conn = sqlite3.connect('randoms.db')
    cursor = conn.cursor()
    with open(var_filename, 'r') as var_file:
        var_reader = csv.reader(var_file)
        for row in var_reader:
            cursor.execute('''
            INSERT INTO Randoms (fname, ename, email, phone, postal_code)
            VALUES (?, ?, ?, ?, ?)
            ''', row)
    conn.commit()
    conn.close()

# sletter en rad (rad 1) fra databasen basert på id og gjør som 
# at databasen starter på id 2 istedenfor 1
def func_slett_idnummer(id):
    conn = sqlite3.connect('randoms.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Randoms WHERE id = ?', (id,))
    conn.commit()
    conn.close()

# main funksjonen
def main():
    func_koble_til_database()
    func_lag_table()
    func_importer_data_fra_csv('randoms.csv')
    func_slett_idnummer(1)

if __name__ == "__main__":
    main()
