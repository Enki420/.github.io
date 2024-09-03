const OpenAI = require('openai');

const openai = new OpenAI();

const completion = await openai.chat.completions.create({
  model: "gpt-4o",
  messages: [
    { role: "user", content: "Write a haiku about AI" }
  ]
]};

console.log(completion);
