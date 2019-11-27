from .models import Manager


class onlineManager:
    managers = []

    @staticmethod
    def add(manager: Manager):
        if onlineManager.managers != "":
            onlineManager.managers.append(manager)
        else:
            onlineManager.managers.clear()
            onlineManager.managers.append(manager)

    @staticmethod
    def remove(manager: Manager):
        if onlineManager.has(manager):
            onlineManager.managers.remove(manager)

    @staticmethod
    def has(manager):
        return manager in onlineManager.managers

    @staticmethod
    def get():
        return onlineManager.managers

    @staticmethod
    def get():
        return onlineManager.managers
