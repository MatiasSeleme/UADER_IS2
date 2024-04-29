from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Attach an observer to the subject.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Detach an observer from the subject.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers about an event.
        """
        pass


class ConcreteSubject(Subject):
    """
    The Subject owns some important state and notifies observers when the state
    changes.
    """
    SubjectID = None
    _state: int = None
    """
    For the sake of simplicity, the Subject's state, essential to all
    subscribers, is stored in this variable.
    """

    _observers: List[Observer] = []
    """
    List of subscribers. In real life, the list of subscribers can be stored
    more comprehensively (categorized by event type, etc.).
    """
    def SetID(self, id):
        self.SubjectID = id
        
    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    The subscription management methods.
    """

    def notify(self) -> None:
        """
        Trigger an update in each subscriber.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Usually, the subscription logic is only a fraction of what a Subject can
        really do. Subjects commonly hold some important business logic, that
        triggers a notification method whenever something important is about to
        happen (or after it).
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers react to the updates issued by the Subject they had been
attached to.
"""


class Observer1(Observer):
    ID = "0001"
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class Observer2(Observer):
    ID = "0002"
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")

class Observer3(Observer):
    ID = "0003"
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")

class Observer4(Observer):
    ID = "0004"
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")            

if __name__ == "__main__":
    # The client code.

    subject1 = ConcreteSubject()
    subject2 = ConcreteSubject()
    subject3 = ConcreteSubject()
    subject4 = ConcreteSubject()
    subject5 = ConcreteSubject()
    subject6 = ConcreteSubject()
    subject7 = ConcreteSubject()
    subject8 = ConcreteSubject()

    subject1.SetID("1845")
    subject2.SetID("0001")
    subject3.SetID("2004")
    subject4.SetID("0002")
    subject5.SetID("3000")
    subject6.SetID("4879")
    subject7.SetID("0003")
    subject8.SetID("0004")
    
    subject_List = [subject1, subject2, subject3, subject4, subject5, subject6, subject7, subject8]

    observer_1 = Observer1()
    observer_2 = Observer2()
    observer_3 = Observer3()
    observer_4 = Observer4()

    for i in subject_List:

        if i.SubjectID == observer_1.ID:
            print("\n\nel ID del sujeto: ")
            print(i.SubjectID)
            print("Es igual al del observer_1")
            i.attach(observer_1)
        elif i.SubjectID == observer_2.ID:
            print("\n\nel ID del sujeto: ")
            print(i.SubjectID)
            print("Es igual al del observer_2")
            i.attach(observer_2)
        elif i.SubjectID == observer_3.ID:
            print("\n\nel ID del sujeto: ")
            print(i.SubjectID)
            print("Es igual al del observer_3")
            i.attach(observer_3)
        elif i.SubjectID == observer_4.ID:
            print("\n\nel ID del sujeto: ")
            print(i.SubjectID)
            print("Es igual al del observer_4")
            i.attach(observer_4)
        else:
            print("\n\nel ID del sujeto: ")
            print(i.SubjectID)
            print("No es igual a el de ningun observer")
        