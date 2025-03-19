const { GoogleGenerativeAI } = require("@google/generative-ai");
require("dotenv").config()

const genAI = new GoogleGenerativeAI(process.env.GOOGLE_GEN_AI_API_KEY);
const model = genAI.getGenerativeModel({ model: "gemini-2.0-flash" });

const generateContentService = async (prompt) => {
    const res = await model.generateContent(prompt);
    return res.response.text();
}

module.exports = generateContentService;