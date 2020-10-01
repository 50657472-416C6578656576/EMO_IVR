var mongoose = require('mongoose');

var User = require('./users');

var messageSchema = new mongoose.Schema({
  content: { type: String, required: true },
    user: { type: mongoose.Schema.Types.ObjectId, ref: 'User' }
});

messageSchema.post('remove', function(message) {
  User.findById(message.user, function(err, user) {
    user.messages.pull(message);
    user.save();
  });
});

mongoose.model('Message', messageSchema);