const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const fs = require('fs');
const path = require('path');
const User = require('./handler');

exports.registerUser = (req, res) => {
  const { username, password } = req.body;

  // Validasi panjang nama pengguna
  if (username.length < 6 || username.length > 10) {
    res.status(400).json({ error: 'Username length should be between 6 and 10 characters' });
    return;
  }

  // Validasi karakter nama pengguna
  const usernameRegex = /^[a-zA-Z0-9_-]+$/;
  if (!usernameRegex.test(username)) {
    res.status(400).json({ error: 'Username should only contain alphanumeric characters, hyphen, or underscore' });
    return;
  }

  const existingUser = User.getUserByUsername(username);
  if (existingUser) {
    res.status(409).json({ status: 'error', message: 'User already exists' });
    return;
  } else {
    // Menghasilkan hash password
    const saltRounds = 10;
    bcrypt.hash(password, saltRounds, (err, hash) => {
      if (err) {
        return res.status(500).json({ status: 'error', message: 'Internal server error' });
      }

      // Simpan pengguna ke file users.json
      User.addUser(username, hash);

      res.json({ status: 'success', message: 'Registration successful' });
    });
  };
};

exports.loginUser = (req, res) => {
  const { username, password } = req.body;

  // Mencari pengguna berdasarkan username
  const user = User.getUserByUsername(username);

  if (!user) {
    return res.status(404).json({ status: 'error', message: 'User not found' });
  }

  // Memverifikasi password
  bcrypt.compare(password, user.password, (err, result) => {
    if (err || !result) {
      return res.status(401).json({ status: 'error', message: 'Invalid credentials' });
    }

    // Membuat token JWT
    const token = jwt.sign({ username: user.username }, 'your_secret_key');

    res.json({ status: 'success', message: 'Login successful', token });
  });
};

exports.listUsers = (req, res) => {
  const filePath = path.join(__dirname, './data/users.json');

  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
      res.status(500).json({ status: 'error', message: 'Internal server error' });
      return;
    }

    try {
      const users = JSON.parse(data);
      res.json({ status: 'success', data: users });
    } catch (error) {
      console.error(error);
      res.status(500).json({ status: 'error', message: 'Internal server error' });
    }
  });
};