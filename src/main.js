import Vue from 'vue';
import App from './App.vue';
import i18n from './i18n';

Vue.config.productionTip = false;

new Vue({
  i18n, // Adicione i18n aqui para integrar a internacionalização
  render: h => h(App),
}).$mount('#app');
