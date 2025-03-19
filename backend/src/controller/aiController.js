const generateContentService = require("../services/aiService");

const ResponseByAI = async(req, res) => {
    const prompt = req.body.prompt;

    if(!prompt) {
        return res.status(400).json({
            success: false,
            message: "Please provide the prompt"
        });
    }

    const result = await generateContentService(prompt);
    return res.status(200).json({
        sucess: true,
        message: "successfully generate the response",
        response: result
    });
}

module.exports = ResponseByAI;