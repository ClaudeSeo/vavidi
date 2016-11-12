# -*- coding: utf-8 -*-
import nose
from flask_script import Manager, Shell
from flask_migrate import MigrateCommand
from app.app import create_app


def main():
    manager = Manager(create_app)

    @manager.option('-p', '--path', dest='path', default='tests/')
    def test(path):
        nose.run_exit(argv=['nosetests', '-v', path])

    manager.add_option('-c', '--config', dest='config_name', required=False,
                       default='dev')
    manager.add_command('db', MigrateCommand)
    manager.add_command('shell', Shell())
    manager.run()


if __name__ == '__main__':
    main()
