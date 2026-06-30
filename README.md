<div align="center">
  <h1>🤖 J.A.R.V.I.S.</h1>
  <p><i>Just A Rather Very Intelligent System</i></p>
  <p>A highly capable, multimodal desktop assistant powered by LiveKit and Google's Gemini Multimodal Live API.</p>
</div>

---

## ⚡ What's New
- **Gemini Multimodal Live API:** Fully migrated to `gemini-3.1-flash-live-preview` for ultra-low latency, bidirectional native audio streams.
- **Visual Computer Control Loop:** Uses a discrete vision sub-loop powered by `gemini-2.5-flash` (`computer_use.py`). JARVIS now takes screen captures, analyzes UI elements, and autonomously determines the exact `x, y` pixel coordinates required to click, type, and verify multi-step computer tasks, entirely eliminating blind GUI coordinate hallucinations. 
- **Dynamic User Memory:** `Mem0` integration now dynamically isolates and persists memory based on the active user identity (`user_name`) rather than a hardcoded bucket.

---

## ⚙️ Core Directives (Capabilities)

J.A.R.V.I.S. operates as an autonomous desktop agent with deep system access, offering the following capabilities:

- **🧠 Smart Memory (Mem0):** Persistent context tracking across sessions. J.A.R.V.I.S. remembers you and retrieves prior context natively on boot.
- **👁️ Visually Grounded Computer Control:** Instead of guessing coordinates, JARVIS uses a vision-language model loop to visually analyze your desktop and drive UI interactions precisely.
- **💻 System Override:** Full command-line control over your Windows PC (execute commands, open apps like Spotify, control files).
- **🖱️ Motor Functions:** Precision mouse movement and clicking via `PyAutoGUI`, tethered strictly to confirmed visual coordinates.
- **⌨️ Keyboard Override:** Direct text input and complex keyboard shortcut execution.
- **🗣️ Vocal Interface:** High-speed, natural speech interaction (Voice: Charon).
- **🌐 Global Network Access:** Real-time web search (DuckDuckGo), weather data (`wttr.in`), and direct URL navigation.
- **📨 Communications Protocol:** Automated email dispatch via SMTP.
- **🔌 External Nodes (MCP):** Expandable via n8n MCP Server connections for automated workflows.

---

## 🚀 System Initialization Sequence (Setup)

To bring J.A.R.V.I.S. online, follow these exact initialization steps:

1. **Construct Environment:** Create a new Python virtual environment.
2. **Engage Environment:** Activate the virtual environment.
3. **Install Dependencies:** Execute `pip install -r requirements.txt`.
4. **Configure Core Constants:** 
   - Create a `.env` file and populate it with your `LIVEKIT_URL`, `LIVEKIT_API_KEY`, and `LIVEKIT_API_SECRET`.
   - Add your `GOOGLE_API_KEY` to authenticate the Gemini Multimodal Live API and the Vision GenAI Client.
   - For email capabilities, input your `GMAIL_USER` and `GMAIL_APP_PASSWORD`.
5. **Verify Services:** Ensure your LiveKit and Mem0 accounts are active and configured.
6. **Deploy:** Start the console mode by running `python agent.py console`.


---

## 👨‍💻 Author

Built and maintained by **Adi Pandey**.
