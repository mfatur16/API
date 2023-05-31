const fs = require('fs');
const path = require('path');

const usersFilePath = path.join(__dirname, './data/users.json');

const readUsersFile = () => {
  try {
    const data = fs.readFileSync(usersFilePath, 'utf8');
    return JSON.parse(data);
  } catch (error) {
    console.error('Error reading users file:', error);
    return [];
  }
};

const writeUsersFile = (users) => {
  try {
    fs.writeFileSync(usersFilePath, JSON.stringify(users, null, 2), 'utf8');
  } catch (error) {
    console.error('Error writing users file:', error);
  }
};

const getAllUsers = () => {
  return readUsersFile();
};

const getUserByUsername = (username) => {
  const users = readUsersFile();
  return users.find((user) => user.username === username);
};

const addUser = (username, password) => {
  const users = readUsersFile();
  users.push({ username, password });
  writeUsersFile(users);
};

module.exports = {
  getAllUsers,
  getUserByUsername,
  addUser,
};
