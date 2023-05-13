<template>
    <div class="header">
        <nav>
            <div class="title-navbar">
                <h1>Star Wars Project</h1>
            </div>
            <div class="links-navbar">
                <router-link to="/">Home</router-link>
                <router-link to="/about">About</router-link>
            </div>
            <div class="button-navbar">
                <button>
                    <i class="bi bi-list"></i>
                </button>
            </div>
        </nav>
    </div>
</template>

<style lang="scss" scoped>
@import '@/assets/sass/variables';

@font-face {
    font-family: 'StarWars';
    src: url('@/../public/assets/font/Starjedi.ttf') format('truetype');
}

nav{
    width: 100%;
    padding: 10px;
    align-items: center;
    place-items: center;
    background-color: #111111;
    @include GridLayout-Columns(repeat(2, 1fr));

    div.title-navbar h1{
        margin-bottom: 0 !important;
        font-family: 'StarWars';
        text-shadow: 2px 0 #f7f307,
                    -2px 0 #f7f307,
                    0 2px #f7f307,
                    0 -2px #f7f307,
                    1px 1px #f7f307,
                    -1px -1px #f7f307,
                    1px -1px #f7f307,
                    -1px 1px #f7f307;
    }

    @include screenTablet{
        div.title-navbar{
            text-align: center;
        }
    }

    div.links-navbar{
        a{
            font-size: 1.5em;
            margin-left: 20px;
            text-decoration: none;
            color: #f0f8ff;

            &:first-child{
                margin-left: 0;
            }

            &:hover{
                font-weight: bold;
                color: #f7f307;
            }
        }

        @include screenTablet{
            display: none;
        }
    }

    div.button-navbar{
        display: none;

        @include screenTablet{
            display: block;

            button{
                font-size: 2em;
                padding: 4px 20px;
                border-radius: 15px;
                border: none;
                background-color: #a9a9a9;

                &:hover{
                    color: #f0f8ff;
                    background-color: #646464;
                }
            }
        }
    }
}
</style>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
    name: 'Navbar'
})
</script>
