<template>
  <div id="app">
    <h1>Busca de Operadoras</h1>
    <input 
      type="text" 
      v-model="termoBusca" 
      @input="buscarOperadoras" 
      placeholder="Digite o termo para buscar"
    />
    <ul v-if="resultados.length > 0">
      <li v-for="(registro, index) in resultados" :key="index">
        <strong>{{ registro.Registro_ANS }}</strong>
        <p>{{ registro.CNPJ }}</p>
      </li>
    </ul>
    <p v-else-if="erro">{{ erro }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      termoBusca: '',
      resultados: [],
      erro: ''
    };
  },
  methods: {
    async buscarOperadoras() {
      if (this.termoBusca.trim() === '') {
        this.resultados = [];
        this.erro = '';
        return;
      }
      
      try {
        const response = await fetch(`http://127.0.0.1:5000/buscar?termo=${this.termoBusca}`);
        
        // Verifique se a resposta foi bem-sucedida
        if (!response.ok) {
          const errorText = await response.text();  // Captura o erro como texto
          throw new Error(`Erro ao buscar dados: ${response.status} - ${errorText}`);
        }
        
        // Tente transformar a resposta em JSON
        const data = await response.json();

        // Verifique a resposta no console
        console.log('Dados recebidos da API:', data);


        // Se os dados não estiverem no formato esperado, avise o usuário
        if (Array.isArray(data)) {
          this.resultados = data;
          this.erro = '';
        } else {
          this.erro = 'Formato de resposta inesperado';
          this.resultados = [];
        }

      } catch (err) {
        // Em caso de erro, mostre o erro ao usuário
        this.erro = `Erro ao buscar operadoras. Detalhes: ${err.message}`;
        this.resultados = [];
      }
    }
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  margin-top: 50px;
}

input {
  padding: 10px;
  font-size: 16px;
  width: 300px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 20px;
}

strong {
  font-size: 18px;
  color: #333;
}
</style>
