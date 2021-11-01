db.createCollection('usertext');
db.usertext.insertMany([
  {
    "user_id": "x1z21",
    "user_text": "Snicely is an immature applicatoin!",
    "toxicity_score": 0.5
  },
  {
    "user_id": "x1z21",
    "user_text": "I think Snicely are very Stupid",
    "toxicity_score": 0.76
  },
  {
    "user_id": "ab123",
    "user_text": "You guys are doing a great job",
    "toxicity_score": 0.05
  }
]);