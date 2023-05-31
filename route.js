const express = require('express');
const router = express.Router();
const controller = require('./controller');

router.post('/auth/login', controller.loginUser);
router.post('/auth/register', controller.registerUser);
router.get('/users', controller.listUsers);

module.exports = router;