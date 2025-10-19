import { useState } from "react";
import axios from "axios";

function App() {
  const [url, setUrl] = useState("");
  const [status, setStatus] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [videoTitle, setVideoTitle] = useState("");

  const handleDownload = async () => {
    if (!url) {
      alert("Please enter a YouTube URL");
      return;
    }

    setIsLoading(true);
    setStatus("🔄 Starting download...");

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/download/", { url });
      console.log(response.data);
      setVideoTitle(response.data.title || "Unknown Video");
      setStatus("✅ Download started! Please wait...");
    } catch (error) {
      console.error(error);
      setStatus("❌ Error starting download.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col justify-center items-center bg-gray-900 text-white">
      <h1 className="text-3xl font-bold mb-6">🎧 YouTube to MP3 Converter</h1>

      <input
        type="text"
        placeholder="Paste YouTube link here..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="px-4 py-2 w-96 rounded-lg text-black outline-none"
      />

      <button
        onClick={handleDownload}
        disabled={isLoading}
        className="mt-4 px-6 py-2 bg-blue-600 hover:bg-blue-700 rounded-lg disabled:opacity-50"
      >
        {isLoading ? "Processing..." : "Download MP3"}
      </button>

      {status && <p className="mt-6 text-lg">{status}</p>}

      {videoTitle && (
        <div className="mt-4 p-4 bg-gray-800 rounded-lg shadow-md">
          <p className="font-semibold">🎬 {videoTitle}</p>
        </div>
      )}
    </div>
  );
}

export default App;
