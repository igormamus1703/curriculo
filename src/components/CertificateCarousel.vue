<template>
    <section class="certificate-carousel">
      <h2>{{ $t('title') }}</h2>
      <vue-slick-carousel :settings="carouselSettings" ref="slick">
        <div v-for="(cert, index) in certificates" :key="index">
          <img :src="cert.image" alt="Certificado" class="carousel-image" />
        </div>
      </vue-slick-carousel>
  
      <!-- Botões de Navegação -->
      <button @click="prev" class="nav-button">{{ $t('previous') }}</button>
      <button @click="next" class="nav-button">{{ $t('next') }}</button>
    </section>
  </template>
  
  <script>
  import VueSlickCarousel from 'vue-slick-carousel';
  import 'vue-slick-carousel/dist/vue-slick-carousel.css';
  import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css';
  
  export default {
    name: "CertificateCarousel",
    components: {
      VueSlickCarousel,
    },
    data() {
      return {
        certificates: [
          {
            image: require('@/assets/certificados/certificado1.jpg'),
          },
          {
            image: require('@/assets/certificados/certificado2.jpg'),
          },
          {
            image: require('@/assets/certificados/certificado3.jpg'),
          },
          {
            image: require('@/assets/certificados/certificado4.jpg'),
          },
          {
            image: require('@/assets/certificados/certificado5.jpg'),
          },
          {
            image: require('@/assets/certificados/certificado6.jpg'),
          },
          {
            image: require('@/assets/certificados/certificado7.jpg'),
          },
          {
            image: require('@/assets/certificados/certificado8.jpg'),
          },
          {
            image: require('@/assets/certificados/certificado9.jpg'),
          },
          {
            image: require('@/assets/certificados/certificado10.jpg'),
          },
          {
            image: require('@/assets/certificados/certificado11.jpg'),
          },
          {
            image: require('@/assets/certificados/certificado12.jpg'),
          },
          {
            image: require('@/assets/certificados/certificado13.jpg'),
          },
          {
            image: require('@/assets/certificados/certificado14.jpg'),
          },
          {
            image: require('@/assets/certificados/certificado15.jpg'),
          },
        ],
    
        carouselSettings: {
          dots: true,
          infinite: true,
          slidesToShow: 1,
          slidesToScroll: 1,
          autoplay: true,
          autoplaySpeed: 3000,
          arrows: false,
        }
      };
    },
    methods: {
      prev() {
        this.$refs.slick.prev();
      },
      next() {
        this.$refs.slick.next();
      }
    }
  };
  </script>
  
  <style scoped>
  .certificate-carousel {
    padding: 20px;
    max-width: 800px;
    margin: auto;
  }
  
  .carousel-image {
    width: 580px;
    height: auto;
    display: block;
    margin: 0 auto;
  }
  
  .nav-button {
    background-color: #4f711c;
    color: white;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
    margin-top: 10px;
    margin-right: 10px;
  }
  
  .nav-button:hover {
    background-color: #4f711c;
  }
  </style>
  