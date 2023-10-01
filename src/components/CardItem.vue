<script setup>
import { ref } from 'vue'

import MButton from './MButton.vue';
import MStatus from './MStatus.vue';


defineProps({
    title: String,
    subtitle: String,
    article: String,
    image: String,
    price: String,
    status: String,
    datetime: Number,
})

let isSelected = ref(false)

const getImage = (el, url) => {
    const img = new Image()
    img.onload = () => el.src = url
    img.onerror = () => el.src = '/empty.png'
    img.src = url
}

const toggleSelected = () => {
    isSelected.value = !isSelected.value
}

const zero = (num) => {
    return `${num}`.length == 1 ? `0${num}` : num
}

const dateFormat = (dt)=>{
    const date = new Date(dt)
    return `${zero(date.getDate())}.${zero(date.getMonth()+1)}.${date.getFullYear()}`
}
</script>

<template>
    <section :data-selected="isSelected">
        <div>
            <img :ref="el => getImage(el, image)">
        </div>
        <div>
            <h4>{{ title }}</h4>
            <h3>{{ subtitle }}</h3>
            <i>{{ article }}</i>
        </div>
        <p>{{ price }}</p>
        <MStatus>{{ status }}</MStatus>
        <time>{{ dateFormat(datetime) }}</time>
        <MButton @click="toggleSelected">Добавить</MButton>
    </section>
</template>

<style lang="scss" scoped>
section {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0;
    padding: 10px 30px;
    border-bottom: 1px solid var(--m-border-color);

    &[data-selected="true"] {
        background: var(--m-border-color-green);

        button {
            background: var(--m-bg-color);
        }
    }

    div {
        &:nth-child(1) {
            width: 80px;
            height: 80px;
        }

        &:nth-child(2) {
            width: 30%;
        }

        img {
            width: 100%;
            min-width: 100%;
            min-height: 100%;
        }
    }

    h3 {
        font-weight: bold;
        margin: 0;
        padding: 0;
    }
    h4 {
        font-size: 12px;
    }
    i {
        font-size: 10px;
    }
}
</style>