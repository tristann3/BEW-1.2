const express = require("express");
const router = express.Router();

const Message = require("../models/message");
const User = require("../models/user");

/** Route to get all messages. */
router.get("/", (req, res) => {
  Message.find()
    .then((messages) => {
      return res.json({ messages });
    })
    .catch((err) => {
      throw err.message;
    });
});

/** Route to get one message by id. */
router.get("/:messageId", (req, res) => {
  console.log(`Message ID: ${req.params.messageId}`);
  Message.findbyId(req.params.messageId)
    .then((message) => {
      return res.json({ message });
    })
    .catch((err) => {
      throw err.message;
    });
});

/** Route to add a new message. */
router.post("/", (req, res) => {
  let message = new Message(req.body);
  messsage.save().then((messageResult) => {
    return res
      .send({
        message: "Create new message",
        data: req.body,
      })
      .catch((err) => {
        throw err.message;
      });
  });
});

/** Route to update an existing message. */
router.put("/:messageId", (req, res) => {
  Message.findByIdAndUpdate(req.params.messageId, req.body)
    .then((message) => {
      return res;
    })
    .send({
      message: `Update message with id ${req.params.messageId}`,
      data: req.body,
    })
    .catch((err) => {
      throw err.message;
    });
});

/** Route to delete a message. */
router.delete("/:messageId", (req, res) => {
  Message.findByIdAndDelete(req.params.messageId)
    .then(() => {
      return res.json({
        message: "Successfully deleted.",
        _id: req.params.userId,
      });
    })
    .catch((err) => {
      throw err.message;
    });
});

module.exports = router;
