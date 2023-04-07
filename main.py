from controller.controller import Controller
from model.db_operation import Operation
from model.repository import Repository
from view.view import View


if __name__ == "__main__":
    v = View(Controller(Repository(Operation("db.csv"))))
    v.ButtonClickRun()
