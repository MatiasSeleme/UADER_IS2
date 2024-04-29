class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.history = []  

    def write(self, string):
        self.content += string

    def save(self):

        memento = Memento(self.file, self.content)
        self.history.append(memento)
        if len(self.history) > 4:
            self.history.pop(0)  
    def undo(self, num):

        if num < 0 or num > len(self.history) - 1:
            print("Número de estados a deshacer fuera de rango")
            return
        
        memento = self.history[-1 - num]
        self.file = memento.file
        self.content = memento.content

class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, num=0):
        writer.undo(num)

if __name__ == '__main__':
    caretaker = FileWriterCaretaker()

    writer = FileWriterUtility("GFG.txt")

    writer.write("Clase de IS2 en UADER\n")
    caretaker.save(writer)

    writer.write("Material adicional de la clase de patrones\n")
    caretaker.save(writer)

    writer.write("Material adicional de la clase de patrones II\n")
    caretaker.save(writer)

    caretaker.undo(writer, 0)  
    print("Se muestra el estado actual después de undo(0):")
    print(writer.content + "\n")

    caretaker.undo(writer, 2)  
    print("Se muestra el estado actual después de undo(2):")
    print(writer.content + "\n")
