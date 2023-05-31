const express = require('express');
const app = express();
const route = require('./route');

// Middleware untuk mengizinkan body dengan format JSON
app.use(express.json());

// Menggunakan rute
app.use('/api/v1/', route);

// Middleware untuk menangani kesalahan path atau metode yang tidak valid
app.use((req, res, next) => {
  res.status(404).json({ status: 'error', message: 'Path atau Metode tidak valid' });
});

// Middleware untuk menangani kesalahan metode yang tidak valid
// app.use((err, req, res, next) => {
//   res.status(405).json({ error: 'Method not allowed' });
// });

// Middleware untuk menampilkan pesan saat mengakses http://localhost:3000
app.use('/', (req, res) => {
  res.json({ status: 'success', message: 'Akses berhasil ke http://localhost:3000' });
});

// Menjalankan server pada port 3000
app.listen(3000, () => {
  console.log('Server berjalan di http://localhost:3000');
});
