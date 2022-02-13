var express = require("express");
var router = express.Router();
var tree_tweets = require("../tree_tweets.json");
var julie_witherow = require("../julie_witherow.json");

router.get("/topics/haringey-tottenham", function (req, res, next) {
  res.status(200).json({
    topics: ["trees", "climate change", "rubbish", "football", "tennis"],
  });
});

router.get("/users/trees", function (req, res, next) {
  users = tree_tweets.map((tweet) => tweet.user);
  res.status(200).json({
    users: users,
  });
});

router.get("/matched-tweets/julie_witherow", function (req, res, next) {
  users = tree_tweets.map((tweet) => tweet.user);
  const matchedTweets = [];
  julie_witherow.forEach((tweet) => {
    if (
      tweet.renderedContent.includes(" trees ") ||
      tweet.renderedContent.includes(" field ") ||
      tweet.renderedContent.includes(" nature ")
    ) {
      matchedTweets.push(tweet);
    }
  });
  res.status(200).json({
    matchedTweets: matchedTweets,
  });
});

module.exports = router;
