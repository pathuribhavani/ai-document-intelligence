
import { useState } from "react";
import "./App.css";

function App() {
  const [sources, setSources] = useState([]);
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const uploadFile = async () => {
    if (!file) {
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/documents/upload",
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      console.log("Status:", response.status);
      console.log("Response:", data);

      if (response.ok) {
        setMessage("Upload successful: " + data.filename);
      } else {
        setMessage("Upload failed");
      }
    } catch (error) {
      console.error("Upload error:", error);
      setMessage("Upload failed: " + error.message);
    }
  };

  const askQuestion = async () => {
    if (!question) {
      return;
    }

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/documents/ask",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            question: question,
          }),
        }
      );

      const data = await response.json();

    if (response.ok) {
        setAnswer(data.answer);
          setSources(data.sources);
} else {
        setAnswer("Unable to get an answer.");
      }
    } catch (error) {
      console.error("Question error:", error);
      setAnswer("Unable to get an answer.");
    }
  };

  return (
  <div className="container">
    <div className="header">
      <div className="card">
      <h1>AI Document Intelligence</h1>
      <p>Upload documents and ask questions using AI.</p>
    </div>
    </div>

      <input
        type="file"
        accept=".pdf,.txt,.csv,.docx"
        onChange={(event) => setFile(event.target.files[0])}
      />

      {file && (
        <p>
          Selected file: <strong>{file.name}</strong>
        </p>
      )}

      <button onClick={uploadFile} disabled={!file}>
        Upload Document
      </button>

      {message && <p>{message}</p>}

      <hr />

      <h2>Ask a Question</h2>

      <input
        type="text"
        placeholder="Ask something about your document..."
        value={question}
        onChange={(event) => setQuestion(event.target.value)}
      />

      <button onClick={askQuestion} disabled={!question}>
        Ask AI
      </button>

      {answer && (
  <div>
    <h3>AI Answer</h3>
    <p>{answer}</p>
  </div>
)}

{sources.length > 0 && (
  <div>
    <h3>Sources</h3>

    {sources.map((source, index) => (
      <div key={index}>
        <p>
          <strong>Source {index + 1}</strong>
        </p>

        <p>{source.chunk}</p>

        <p>
          Score: {source.score.toFixed(4)}
        </p>

        <hr />
      </div>
    ))}
  </div>
)}
    </div>
  );
}

export default App;