import yaml
import psycopg2

def run_migrations():
    # Читаем файл changelog
    with open("migrations_log.yaml", "r") as file:
        migrations = yaml.safe_load(file)
    
    # Подключение к базе данных
    conn = psycopg2.connect("ваша_строка_подключения")
    cursor = conn.cursor()

    # Проверяем выполненные миграции
    cursor.execute("CREATE TABLE IF NOT EXISTS migrations_log (id SERIAL PRIMARY KEY, migration_id INTEGER, file_path TEXT)")
    applied_migrations = {row[1] for row in cursor.fetchall()}

    # Применяем новые миграции
    for migration in migrations:
        if migration['id'] not in applied_migrations:
            with open(migration['file_path'], "r") as sql_file:
                sql_script = sql_file.read()
            cursor.execute(sql_script)
            cursor.execute("INSERT INTO migrations_log (migration_id, file_path) VALUES (%s, %s)", (migration['id'], migration['file_path']))
            conn.commit()
    
    conn.close()
