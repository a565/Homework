'''
1. Создать скрипт, который через параметр запуска получает имя исполняемого файла.
И запускает этот файл через библиотеку subprocess. Обработку ошибок (файл не существует, или не
может быть запущен и т.д.) сделать через исключения.
'''
import click

@click.command()
@click.argument('name')
def run(name):
    print(name)
    import subprocess

    subprocess.run([name])

if __name__ == '__main__':
    try:
        run()

    except FileNotFoundError as err:
        print('file not found')


