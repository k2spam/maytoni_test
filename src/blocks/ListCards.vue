<script setup>
import { storeToRefs } from 'pinia';
import { useLightsStore } from '../stores/lights';

import ListFilters from './ListFilters.vue';
import CardItem from '../components/CardItem.vue';
import MLoader from '../components/MLoader.vue';

const { filtered, loading, error } = storeToRefs(useLightsStore())
const { fetchLights } = useLightsStore()

fetchLights()
</script>

<template>
    <article>
        <ListFilters/>
        {{ error }}
        <MLoader v-if="loading"/>
        <CardItem 
            v-else
            v-for="item in filtered" 
            :key="item.key"
            :title="item.title"
            :subtitle="item.subtitle"
            :article="item.article"
            :image="item.image"
            :price="item.price"
            :status="item.status"
            :datetime="parseInt(item.datetime)"
            />
    </article>
</template>

<style lang="scss" scoped>
article {
    max-width: 1000px;
    min-width: 800px;
}
</style>