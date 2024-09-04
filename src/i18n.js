import Vue from 'vue';
import VueI18n from 'vue-i18n';

// Registrar o plugin vue-i18n
Vue.use(VueI18n);

const messages = {
  en: {
    title: 'Certificates',
    experience: 'Experience',
    projects: 'Projects',
    previous: 'Previous',
    next: 'Next',
    selectLanguage: 'Select Language',
    // Adicione mais chaves conforme necessário
  },
  pt: {
    title: 'Certificados',
    experience: 'Experiência',
    projects: 'Projetos',
    previous: 'Anterior',
    next: 'Próximo',
    selectLanguage: 'Selecione o Idioma',
    // Adicione mais chaves conforme necessário
  },
};

const i18n = new VueI18n({
  locale: 'pt', // Idioma padrão
  fallbackLocale: 'en', // Idioma de fallback
  messages,
});

export default i18n;
