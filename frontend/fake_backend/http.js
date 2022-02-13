export const openRequest = (path, method, body) => {
  const url = "http://localhost:4000/";

  const options = {
    method: method,
    headers: {
      "Content-Type": "application/json",
    },
    credentials: "include",
    body: JSON.stringify(body),
  };

  return fetch(url + path, options)
    .then(async (res) => {
      const result = {};
      result.status = res.status;
      result.data = await res.json();
      return result;
    })
    .catch((err) => console.log("Error:", err));
};
