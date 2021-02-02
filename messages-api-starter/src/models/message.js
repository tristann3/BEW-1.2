const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const MessageSchema = new Schema({
  title: { type: String, required: true },
  body: { type: String, select: true },
  author: { type: String, select: true },
});

const Message = mongoose.model("Message", MessageSchema);

module.exports = Message;
