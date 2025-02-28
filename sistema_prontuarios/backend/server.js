const express = require('express');
const cors = require('cors');
const { Pool } = require('pg');
require('dotenv').config();

const app = express();
app.use(cors());
app.use(express.json());

const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_PORT,
});

app.get('/prontuario/:codigo', async (req, res) => {
  const { codigo } = req.params;
  try {
    const result = await pool.query('SELECT * FROM prontuarios WHERE codigo_barras = $1', [codigo]);
    res.json(result.rows[0] || { message: 'Prontuário não encontrado.' });
  } catch (error) {
    console.error(error);
    res.status(500).send('Erro no servidor');
  }
});

app.listen(3001, () => console.log('Servidor rodando na porta 3001'));
