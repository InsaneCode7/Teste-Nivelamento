// src/router.js
import Vue from 'vue';
import Router from 'vue-router';

// Importar componentes de página
import Home from './components/Home.vue';
import About from './components/About.vue';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      component: About
    }
  ]
});
