import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import { motion } from "framer-motion";
import { SendHorizonal } from "lucide-react";

const ChatBubble = ({ isUser, text }) => (
  <motion.div
    initial={{ opacity: 0, y: 10 }}
    animate={{ opacity: 1, y: 0 }}
    transition={{ duration: 0.3 }}
    className={`max-w-[70%] p-3 my-2 rounded-2xl shadow-md text-sm break-words ${
      isUser
        ? "bg-gradient-to-br from-blue-400 to-blue-600 text-white self-end"
        : "bg-gradient-to-br from-pink-300 to-pink-500 text-white self-start"
    }`}
  >
    {text}
  </motion.div>
);

function PlayfulChatBot() {
  const [messages, setMessages] = useState([
    { from: "bot", text: "Hey there! 🌟 Ask me anything!" },
  ]);
  const [input, setInput] = useState("");
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const newMessages = [...messages, { from: "user", text: input }];
    setMessages(newMessages);
    setInput("");

    try {
      const res = await axios.post("http://localhost:8000/chat/chat", {
        prompt: input, // 🧠 Must match your FastAPI input schema
      });

      const aiReply = res.data?.reply || "🤖 Oops, no reply received.";
      setMessages([...newMessages, { from: "bot", text: aiReply }]);
    } catch (err) {
      console.error("Error sending message:", err);
      setMessages([
        ...newMessages,
        { from: "bot", text: "❌ Oops! Something went wrong with the server." },
      ]);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-yellow-100 to-pink-100 flex flex-col items-center justify-center p-4">
      <div className="w-full max-w-md bg-white rounded-3xl shadow-xl flex flex-col overflow-hidden">
        <div className="bg-gradient-to-br from-pink-400 to-pink-600 text-white text-center py-4 text-xl font-bold">
          🌈 chatBot
        </div>
        <div className="flex-1 overflow-y-auto p-4 flex flex-col">
          {messages.map((msg, i) => (
            <ChatBubble key={i} isUser={msg.from === "user"} text={msg.text} />
          ))}
          <div ref={chatEndRef} />
        </div>
        <div className="flex items-center border-t border-gray-200 p-3">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="Type something fun... 🎈"
            className="flex-1 p-2 rounded-xl border focus:outline-none focus:ring-2 focus:ring-pink-400"
          />
          <button
            onClick={sendMessage}
            className="ml-2 p-2 bg-pink-500 hover:bg-pink-600 text-white rounded-full"
          >
            <SendHorizonal size={20} />
          </button>
        </div>
      </div>
    </div>
  );
}

export default PlayfulChatBot;
