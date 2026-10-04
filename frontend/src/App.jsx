import { useEffect, useState } from "react"

function App() {
  const [notes, setNotes] = useState([])
  const [title, setTitle] = useState("")
  const [content, setContent] = useState("")
  const [editingId, setEditingId] = useState(null)

  // Get notes from the backend when the page loads
  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/notes")
      .then((response) => response.json())
      .then((data) => {
        setNotes(data)
      })
      .catch((error) => {
        console.error("Error fetching notes:", error)
      })
  }, [])

  // Create a new note
  const createNote = async (event) => {
    event.preventDefault()

    const response = await fetch("http://127.0.0.1:8000/api/notes", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        title: title,
        content: content,
      }),
    })

    const newNote = await response.json()

    setNotes((currentNotes) => [...currentNotes, newNote])

    setTitle("")
    setContent("")
  }

  // Put a note into edit mode
  const startEditing = (note) => {
    setEditingId(note.id)
    setTitle(note.title)
    setContent(note.content)
  }

  // Update an existing note
  const updateNote = async (event) => {
    event.preventDefault()

    const response = await fetch(
      `http://127.0.0.1:8000/api/notes/${editingId}`,
      {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: title,
          content: content,
        }),
      }
    )

    const updatedNote = await response.json()

    setNotes((currentNotes) =>
      currentNotes.map((note) =>
        note.id === editingId ? updatedNote : note
      )
    )

    setEditingId(null)
    setTitle("")
    setContent("")
  }

  // Delete a note
  const deleteNote = async (noteId) => {
    await fetch(`http://127.0.0.1:8000/api/notes/${noteId}`, {
      method: "DELETE",
    })

    setNotes((currentNotes) =>
      currentNotes.filter((note) => note.id !== noteId)
    )
  }

  // Cancel editing
  const cancelEditing = () => {
    setEditingId(null)
    setTitle("")
    setContent("")
  }

  return (
    <div>
      <h1>Notes App</h1>

      <form onSubmit={editingId === null ? createNote : updateNote}>
        <input
          type="text"
          placeholder="Note title"
          value={title}
          onChange={(event) => setTitle(event.target.value)}
        />

        <textarea
          placeholder="Write your note..."
          value={content}
          onChange={(event) => setContent(event.target.value)}
        />

        <button type="submit">
          {editingId === null ? "Create Note" : "Update Note"}
        </button>

        {editingId !== null && (
          <button type="button" onClick={cancelEditing}>
            Cancel
          </button>
        )}
      </form>

      <hr />

      <h2>My Notes</h2>

      {notes.map((note) => (
        <div key={note.id}>
          <h3>{note.title}</h3>
          <p>{note.content}</p>

          <button onClick={() => startEditing(note)}>
            Edit
          </button>

          <button onClick={() => deleteNote(note.id)}>
            Delete
          </button>
        </div>
      ))}
    </div>
  )
}

export default App