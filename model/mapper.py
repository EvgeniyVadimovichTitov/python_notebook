from model.note import Note


def mapString(line: str) -> Note:
    """string is converted to Note"""
    id, data, head, body = line.split(";")
    return Note(id, data, head, body)
    

def mapNote(note: Note) -> str:
    """Note is converted to string"""
    line = "{};{};{};{}"
    return line.format(note.id, note.data, note.head, note.body)
