<template>
    <div class="footer">
        <div class="container">
            <div class="row">
                <div class="col-12 footer-content-top">
                    <div class="col-12">
                        <h3>Star Wars Project</h3>
                        <span>&copy; 2023</span>
                    </div>
                    <div class="col-12">
                        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original-wordmark.svg" />
                    </div>
                </div>
                <hr class="mt-5 mb-5">
                <div class="col-12 footer-content-mid">
                    <div class="col-12 content-mid">
                        <h6 class="blue">Redes Sociais</h6>
                        <a href="https://twitter.com/Walleemc2" target="_blank">
                            <i class="bi bi-twitter"></i>
                        </a>
                        <a href="https://instagram.com/wallace_emc2" target="_blank">
                            <i class="bi bi-instagram"></i>
                        </a>
                        <a href="https://github.com/Baku-Stark" target="_blank">
                            <i class="bi bi-github"></i>
                        </a>
                        <a href="https://www.linkedin.com/in/wallace-freitas-92a2061b6/" target="_blank">
                            <i class="bi bi-linkedin"></i>
                        </a>
                    </div>
                    <div class="col-12 content-mid">
                        <h6 class="red">Projetos</h6>
                        <a href="https://baku-stark.github.io/Portfolio-Wallace/indexBaku.htm" target="_blank">
                            <span>
                                Portfólio
                            </span>
                        </a>
                        <a href="https://github.com/Baku-Stark/Portfolio-Projects" target="_blank">
                            <span>
                                Projetos (Repositório Full-Stack)
                            </span>
                        </a>
                    </div>
                </div>
                <hr class="mt-5 mb-5">
                <div class="col-12 footer-content-bot">
                    <p>
                        Star Wars é uma franquia do tipo space opera estadunidense criada pelo cineasta George Lucas, que conta com uma série de nove filmes de fantasia científica e dois spin-offs.
                    </p>
                </div>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
@import '@/assets/sass/variables';

@font-face {
    font-family: 'StarWars';
    src: url('@/../public/assets/font/Starjedi.ttf') format('truetype');
}

div.footer{
    width: 100%;
    padding: 25px;
    background-color: #111111;

    div.footer-content-top{
        .col-12{
            margin-bottom: 5vh;
            @include FlexBox-Pattern(center, center);

            &:last-child{
                margin-bottom: 0;
            }

            h3, span{
                color: #f0f8ff;
            }
    
            h3{
                font-family: 'StarWars';
            }

            span{
                opacity: .6;
                margin-left: 2vw;
                font-weight: bold;
            }
    
            img{
                height: 20vh;
            }
        }
    }

    div.footer-content-mid{
        @include GridLayout-Columns(repeat(2, 1fr));

        @include screenPhone{
            @include GridLayout-Columns(repeat(1, 1fr));
        }

        .content-mid{
            margin-bottom: 5vh;
            text-align: center;
            @include FlexBox-Custom(column, space-between);

            &:last-child{
                margin-bottom: 0;
            }

            h6{
                font-size: 2rem;
                margin-bottom: 3.5vh !important;
                color: #f0f8ff;
                font-family: 'StarWars';
            }

            .blue{
                text-shadow: 1px 1px 10px #00ffff;
            }

            .red{
                text-shadow: 1px 1px 10px crimson;
            }

            a{
                margin-bottom: 15px;
                text-decoration: none;

                &:last-child{
                    margin-bottom: 0;
                }

                span, i.bi{
                    color: #f0f8ff;

                    &:hover{
                        color: #a9aaaa;
                    }
                }

                span{
                    font-size: 1rem;
                }

                i.bi{
                    font-size: 2rem;
                }
            }
        }
    }

    div.footer-content-bot{
        text-align: center;

        p{
            opacity: .6;
            color: #f0f8ff;
        }
    }
}
</style>

<script lang="ts">
import {defineComponent} from 'vue'

export default defineComponent({
    name: 'Footer',
})
</script>