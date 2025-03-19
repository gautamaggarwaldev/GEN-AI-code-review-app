const generateContentService = require("../services/aiService");

const ReviewByAI = async(req, res) => {
    try {
        const code = req.body.code;

        if(!code) {
            return res.status(400).json({
                success: false,
                message: "Please provide the code"
            });
        }

        const result = await generateContentService(code);
        return res.status(200).json({
            sucess: true,
            message: "successfully generate the response",
            response: result
        });
    }
    catch(error) {
        return res.status(500).json({
            sucess: false,
            message: "something went wrong. Please try again later",
            error: error
        })
    }
}

module.exports = ReviewByAI;