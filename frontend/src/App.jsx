// JSX similar to HTML but it is being used inside JavaScript

import { useEffect, useState } from "react"

function App() {
  const [notes, setNotes] = useState([])
  const [title, setTitle] = useState("")
  const [content, setContent] = useState("")

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

  // Send a new note to the backend
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

    // Add the newly created note to the page
    setNotes([...notes, newNote])

    // Clear the form
    setTitle("")
    setContent("")
  }

  return (
    <div>
      <h1>Notes App</h1>

      <form onSubmit={createNote}>
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

        <button type="submit">Create Note</button>
      </form>

      <hr />

      <h2>My Notes</h2>

      {notes.map((note) => (
        <div key={note.id}>
          <h3>{note.title}</h3>
          <p>{note.content}</p>
        </div>
      ))}
    </div>
  )
}

export default App