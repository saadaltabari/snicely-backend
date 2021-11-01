db.createCollection('usertext');
db.usertext.insertMany([
  {
    "user_id": "x1z21",
    "user_text": "Snicely is an immature applicatoin!",
    "toxicity_score": 0.5,
    "date": "2021-10-25T07:33:04+00:00"
  },
  {
    "user_id": "x1z21",
    "user_text": "I think Snicely are very Stupid",
    "toxicity_score": 0.76,
    "date": "2021-10-14T17:29:24+00:00"
  },
  {
    "user_id": "ab123",
    "user_text": "You guys are doing a great job",
    "toxicity_score": 0.05,
    "date": "2021-10-12T16:53:43+00:00"
  }
]);
