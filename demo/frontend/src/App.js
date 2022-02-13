import React, { useState } from "react";
import "./App.css";
import { openRequest } from "./http.js";
import Button from '@mui/material/Button';

function App() {
  const areaName = "Haringey / Tottenham";
  const [topicsForMyArea, setTopicsForMyArea] = useState([]);
  const [topicUsers, setTopicUsers] = useState([]);
  const [fullContentMode, setFullContentMode] = useState(false);
  const [matchedTweets, setMatchedTweetsFull] = useState([]);

  const getTopics = async (e) => {
    e.preventDefault();
    const res = await openRequest("/topics/haringey-tottenham", "GET");
    setTopicsForMyArea(res.data.topics);
  };

  const getUsers = async (e) => {
    e.preventDefault();
    const res = await openRequest("/users/trees", "GET");
    setTopicUsers(res.data.users);
  };

  const viewAllTopicUserContent = async (e) => {
    e.preventDefault();
    const res = await openRequest("/matched-tweets/julie_witherow", "GET");
    setMatchedTweetsFull(res.data.matchedTweets);
    setFullContentMode(true);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Local Leads Finder</h1>
      </header>
      <main>
        {!fullContentMode ? (
          <div style={{
            paddingTop: 10
          }}>
            <Button onClick={getTopics} variant="contained">Topics available in {areaName}</Button>
            <div className="topics">
              {topicsForMyArea.map((topic) => (
                <Button onClick={getUsers}>{topic}</Button>
              ))}
            </div>
            <div
              style={{
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
              }}
              className="topic-users"
            >
              {topicUsers.map((user) => (
                <div
                  style={{
                    border: "solid 1px #282c34",
                    borderRadius: "2px",
                    margin: "10px",
                  }}
                >
                  <div
                    style={{
                      width: "50vw",
                      display: "flex",
                    }}
                  >
                    <div>
                      <h2>{user.username}</h2>
                      <p>{user.description}</p>
                    </div>
                    <div>
                      <img
                        src={user.profileImageUrl}
                        alt="The user's twitter"
                      ></img>
                    </div>
                  </div>
                  <div style={{ borderTop: "solid 1px #282c34" }}>
                    <Button onClick={viewAllTopicUserContent}>
                      View all relevant content
                    </Button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        ) : (
          <div
            style={{
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
            }}
          >
            <div>{topicUsers[0].username}</div>
            <div
              style={{
                width: "50vw",
              }}
            >
              {matchedTweets.map((tweet) => (
                <div
                  style={{
                    border: "solid 1px #282c34",
                    borderRadius: "2px",
                    margin: "5px",
                    textAlign: "left",
                  }}
                >
                  {tweet.renderedContent}
                </div>
              ))}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;
